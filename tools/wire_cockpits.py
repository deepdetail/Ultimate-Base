#!/usr/bin/env python3
"""Wire the painted wide cockpits and controls (art/CHROME_COCKPIT_WIDE_RUN.md) into the game.

    python3 tools/wire_cockpits.py FOLDER            # every cpw_*.png and ctl_*.png in FOLDER
    python3 tools/wire_cockpits.py FOLDER --dry-run  # report only, change nothing

Cockpits (cpw_<vehicle id>.png, 1536 x 1024): the flat magenta windows are keyed to clear, then each is saved
about 1280 px wide as WebP. Controls (ctl_<name>.png, square): the flat green is keyed, the picture is trimmed to the
control, and the trim box is recorded in the square it was painted in, so its pivot (the center for wheels, yokes,
helms and handlebars; the bottom center for sticks and levers) stays exactly where the game expects it.

The results go into prototype/based.html between the /*CKART*/ and /*CTLART*/ markers. The game uses a painted
picture wherever one exists and its own drawing everywhere else, so pictures can arrive a few at a time.
After wiring, check each cockpit in a mission and adjust its row in CKW (mx, my, ms, cy, gl) if the painted
control mount or eye level sits somewhere other than the drawn one. Then run tools/build_exports.py.
"""
import base64, io, json, os, re, sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, 'prototype', 'based.html')
CONTROLS = {'ctl_yoke', 'ctl_stick_center', 'ctl_stick_side', 'ctl_stick_future', 'ctl_wheel_ship',
            'ctl_wheel_classic', 'ctl_wheel_truck', 'ctl_wheel_sport', 'ctl_wheel_offroad', 'ctl_lever_tank',
            'ctl_stick_mech', 'ctl_handlebars', 'ctl_helm', 'ctl_yoke_sub'}
VEHICLES = {'cessna', 'l39', 'f16', 'mig', 'f18', 'f22', 'hover', 'rocket', 'airship', 'mustang', 'cyber',
            'ferrari', 'rezvani', 'lambo', 'revuelto', 'tank', 'mech', 'rbuggy', 'dirtbike', 'speedboat', 'sub'}


def key(img, target, hard=70, soft=150):
    """Clear every pixel near the key color. Edges fade out and lose the key color's tint (no pink or green fringe)."""
    img = img.convert('RGBA')
    px = img.load()
    tr, tg, tb = target
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            d = ((r - tr) ** 2 + (g - tg) ** 2 + (b - tb) ** 2) ** .5
            if d < hard:
                px[x, y] = (0, 0, 0, 0)
            elif d < soft:
                k = (d - hard) / (soft - hard)
                if target == (255, 0, 255):
                    r = g + (r - g) * k if r > g else r
                    b = g + (b - g) * k if b > g else b
                else:
                    g = max(r, b) + (g - max(r, b)) * k if g > max(r, b) else g
                px[x, y] = (int(r), int(g), int(b), int(a * k))
    return img


def webp(img, quality=82):
    buf = io.BytesIO()
    img.save(buf, 'WEBP', quality=quality, method=6)
    return buf.getvalue()


def cockpit(path):
    img = key(Image.open(path), (255, 0, 255))
    if abs(img.width / img.height - 1.5) > .03:
        print(f'  warning: {os.path.basename(path)} is {img.width} x {img.height}, not 3:2. It will be stretched to fit.')
    img = img.resize((1280, 853), Image.LANCZOS)
    return {'src': 'data:image/webp;base64,' + base64.b64encode(webp(img)).decode()}


def control(path):
    img = key(Image.open(path), (0, 255, 0))
    sz = img.width
    if img.height != sz:
        print(f'  warning: {os.path.basename(path)} is not square; the pivot math assumes it is.')
    box = img.getbbox()
    if not box:
        raise SystemExit(f'{path}: nothing left after keying the green')
    pad = 4
    box = (max(0, box[0] - pad), max(0, box[1] - pad), min(img.width, box[2] + pad), min(img.height, box[3] + pad))
    img = img.crop(box)
    # the game never shows a control wider than about 512 screen pixels, so keep files small
    scale = min(1, 640 / max(img.size))
    if scale < 1:
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    return {'src': 'data:image/webp;base64,' + base64.b64encode(webp(img, 85)).decode(),
            'sz': sz, 'ox': box[0], 'oy': box[1], 'w': box[2] - box[0], 'h': box[3] - box[1]}


def put(html, name, table):
    body = ','.join(f'{json.dumps(k)}:{json.dumps(v, separators=(",", ":"))}' for k, v in sorted(table.items()))
    pat = re.compile(r'/\*%s\*/const %s=\{.*?\};/\*/%s\*/' % (name, name, name), re.S)
    if len(pat.findall(html)) != 1:
        raise SystemExit(f'could not find the /*{name}*/ markers in prototype/based.html')
    return pat.sub(lambda m: '/*%s*/const %s={%s};/*/%s*/' % (name, name, body, name), html)


def existing(html, name):
    m = re.search(r'/\*%s\*/const %s=(\{.*?\});/\*/%s\*/' % (name, name, name), html, re.S)
    return json.loads(m.group(1)) if m and m.group(1) != '{}' else {}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1 or not os.path.isdir(args[0]):
        raise SystemExit(__doc__)
    folder, dry = args[0], '--dry-run' in sys.argv
    html = open(GAME, encoding='utf-8').read()
    ck, ctl = existing(html, 'CKART'), existing(html, 'CTLART')
    for f in sorted(os.listdir(folder)):
        stem, ext = os.path.splitext(f)
        if ext.lower() not in ('.png', '.webp', '.jpg', '.jpeg'):
            continue
        path = os.path.join(folder, f)
        if stem.startswith('cpw_') and stem[4:] in VEHICLES:
            ck[stem] = cockpit(path)
            print(f'cockpit {stem}: {len(ck[stem]["src"]) * 3 // 4 // 1024} KB')
        elif stem in CONTROLS:
            ctl[stem] = control(path)
            c = ctl[stem]
            print(f'control {stem}: {len(c["src"]) * 3 // 4 // 1024} KB, trimmed to {c["w"]} x {c["h"]} at {c["ox"]},{c["oy"]} of {c["sz"]}')
        else:
            print(f'skipped {f} (not a cockpit or control name from the run)')
    missing = sorted({'cpw_' + v for v in VEHICLES} - set(ck)) + sorted(CONTROLS - set(ctl))
    if missing:
        print('still drawn in code:', ', '.join(missing))
    if dry:
        return
    html = put(put(html, 'CKART', ck), 'CTLART', ctl)
    open(GAME, 'w', encoding='utf-8').write(html)
    print('wired into prototype/based.html. Next: check the missions, then python3 tools/build_exports.py')


if __name__ == '__main__':
    main()
