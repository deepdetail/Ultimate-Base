#!/usr/bin/env python3
"""Resolve Wikimedia Commons links, check the license, and download the
originals with numbered, space-separated file names.

Usage:
  python3 -I fetch_commons.py --titles titles.txt --prefix "Tchaikovsky 11.14.26" --out OUTDIR

titles.txt holds one Commons file per line, in script order. Each line may be
"File:Name.jpg" or a full https://commons.wikimedia.org/wiki/File:... URL,
optionally followed by " | <script beat>" (copied into the manifest).
Lines starting with # are skipped.

Writes OUTDIR/"<prefix> Image <n>.<ext>" for each file plus OUTDIR/manifest.csv
(number, file name, beat, Commons title, license, source page, pixel size).
Files whose license is not public domain or CC0 are skipped and listed in the
manifest with status "skipped: license".

Wikimedia throttles shared cloud IPs. The script backs off on HTTP 429 using
the Retry-After header, so a full run can take several minutes.
"""
import argparse
import csv
import json
import os
import subprocess
import sys
import time
import urllib.parse

UA = "ContentImageFetcher/1.0 (https://www.instagram.com/deepdetail)"
API = "https://commons.wikimedia.org/w/api.php"
EXT = {"image/jpeg": "jpg", "image/gif": "gif", "image/png": "png",
       "image/tiff": "tif", "image/webp": "webp"}
OK_LICENSES = ("public domain", "pd", "cc0", "no restrictions")


def curl(args, retries=8):
    """Run curl, backing off on 429. Returns (status_code, stdout)."""
    for attempt in range(retries):
        p = subprocess.run(["curl", "-sS", "-A", UA, "-w", "\n%{http_code}",
                            "-D", "/dev/stderr"] + args,
                           capture_output=True, text=True)
        body, _, code = p.stdout.rpartition("\n")
        code = int(code or 0)
        if code == 429 or code >= 500 or code == 0:
            wait = 30 * (attempt + 1)
            for line in p.stderr.splitlines():
                if line.lower().startswith("retry-after:"):
                    try:
                        wait = min(int(line.split(":", 1)[1]), 900)
                    except ValueError:
                        pass
            print(f"  HTTP {code}, waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
            continue
        return code, body
    return code, body


def norm_title(line):
    line = line.strip()
    if "commons.wikimedia.org/wiki/" in line:
        line = urllib.parse.unquote(line.split("/wiki/", 1)[1])
    line = line.replace("_", " ")
    if not line.startswith("File:"):
        line = "File:" + line
    return line


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--titles", required=True)
    ap.add_argument("--prefix", required=True, help='e.g. "Tchaikovsky 11.14.26"')
    ap.add_argument("--out", required=True)
    ap.add_argument("--start", type=int, default=1, help="first image number")
    a = ap.parse_args()

    lines = [l for l in open(a.titles, encoding="utf-8")
             if l.strip() and not l.lstrip().startswith("#")]
    beats = {}
    titles = []
    for l in lines:
        t, _, beat = l.partition(" | ")
        t = norm_title(t)
        titles.append(t)
        beats[t] = beat.strip()
    os.makedirs(a.out, exist_ok=True)

    # One batched metadata request (up to 50 titles) keeps us under the throttle.
    info = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        params = {"action": "query", "titles": "|".join(chunk), "prop": "imageinfo",
                  "iiprop": "url|size|mime|extmetadata", "format": "json",
                  "formatversion": 2}
        code, body = curl([API, "--data", urllib.parse.urlencode(params)])
        d = json.loads(body)
        back = {n["to"]: n["from"] for n in d["query"].get("normalized", [])}
        for p in d["query"]["pages"]:
            info[back.get(p["title"], p["title"])] = p

    rows, n = [], a.start
    for t in titles:
        p = info.get(t, {})
        if "imageinfo" not in p:
            rows.append([None, "", beats[t], t, "", "", "", "skipped: not found"])
            continue
        ii = p["imageinfo"][0]
        lic = ii.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "")
        size = f'{ii["width"]}x{ii["height"]}'
        if not any(k in lic.lower() for k in OK_LICENSES):
            rows.append([None, "", beats[t], t, lic, ii["descriptionurl"], size, "skipped: license"])
            continue
        name = f"{a.prefix} Image {n}.{EXT.get(ii['mime'], 'jpg')}"
        dest = os.path.join(a.out, name)
        if not (os.path.exists(dest) and os.path.getsize(dest) == ii["size"]):
            code, _ = curl(["-f", "-o", dest, ii["url"]])
        ok = os.path.exists(dest) and os.path.getsize(dest) == ii["size"]
        rows.append([n, name, beats[t], t, lic, ii["descriptionurl"], size,
                     "downloaded" if ok else "failed"])
        print(f"{n:>3} {'ok ' if ok else 'ERR'} {name}  <-  {t}")
        n += 1
        time.sleep(3)  # be polite to upload.wikimedia.org

    with open(os.path.join(a.out, "manifest.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["number", "file", "beat", "commons_title", "license", "source_page", "pixels", "status"])
        w.writerows(rows)
    failed = [r for r in rows if r[7] != "downloaded"]
    print(f"\n{len(rows) - len(failed)} downloaded, {len(failed)} not downloaded. Manifest: "
          + os.path.join(a.out, "manifest.csv"))
    sys.exit(1 if any(r[7] == "failed" for r in rows) else 0)


if __name__ == "__main__":
    main()
