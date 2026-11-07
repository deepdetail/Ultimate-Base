---
name: content-image-drop
description: Turn the image-source list in a deepdetail script doc into saved, numbered image files (JPG, PNG, GIF) and file them in Google Drive under "Content and Creative Ideas / <Theme> / <Topic>". Use when the user says "drop the images", "save these links to Drive", "pull the public domain images for <script>", or hands over a script doc or a list of Wikimedia Commons links for an Instagram post.
---

# Content image drop

Final-stage helper for the Content and Creative Ideas project (Instagram: deepdetail).
Input is a script doc with an "Image sources" section, or a list of links.
Output is a Drive folder of numbered public domain images plus a sources sheet for credits.

## Naming rules (from the user, do not change without asking)

- Drive tree: `Content and Creative Ideas / <Theme> / <Topic>`.
  Themes so far: San Diego Symphony, SD Maritime Museum, Concerts, Events Industry, Event Economics.
  Add new themes as new genres come up. Reuse existing folders: search Drive before creating.
- File name: `<Topic> <MM.DD.YY> Image <n>.<ext>`, spaces not underscores.
  The date is the event or post date tied to the script (Tchaikovsky = 11.14.26, the concert date).
  Numbers start at 1 and follow script order (hook first, closer last).
- Keep the original format (jpg, png, gif). Do not re-encode.

## Steps

1. **Find the source doc.** A claude.ai share link cannot be fetched (it renders in the browser).
   Look for the doc in the user's artifacts instead (list artifacts, query the topic name, take the
   most recently updated), then read it with the Claude Docs tools. Otherwise ask the user to paste the list.
2. **Pick the downloadable items, in script order.**
   - Take direct Commons `File:` links.
   - For Commons category links, take the specific file the doc names inside that category.
   - Skip: copyrighted meme or film references, museum or archive pages marked "ask before using",
     anything marked "no reproduction", IMSLP and Internet Archive scans (not reachable from the
     cloud sandbox and usually PDFs), and text-only pages.
   - List every skipped item and why in the final report.
3. **Write a titles file** at `content/<theme-slug>/<topic-slug>/titles.txt`, one `File:` per line.
4. **Download and license-check**:
   ```
   python3 -I .claude/skills/content-image-drop/scripts/fetch_commons.py \
     --titles content/<theme>/<topic>/titles.txt --prefix "<Topic> <MM.DD.YY>" \
     --out content/<theme>/<topic>/images
   ```
   The script keeps only files Commons tags public domain or CC0 and writes `manifest.csv`.
   Run it in the background. Known issue (November 7, 2026): from the Claude Code cloud sandbox,
   `upload.wikimedia.org` answered HTTP 429 to every file request for over 40 minutes, while the
   Commons metadata API worked. The shared cloud IP is throttled. So run this step on the user's own
   computer (Claude Code desktop or terminal), or use the Make.com route in step 7, which skips it.
5. **Create the Drive folders** with the Google Drive connector (`create_file`,
   mimeType `application/vnd.google-apps.folder`), searching first so nothing is duplicated.
6. **Create a sources sheet in the topic folder** named `<Topic> <MM.DD.YY> Image Sources`
   from `manifest.csv` (number, file, license, Commons page). This is the credit list for captions.
7. **Put the image files in the folder.** The Drive connector only accepts file bytes as base64
   inside the tool call, so binary uploads cost too much to do that way. Use, in order of preference:
   - **Make.com** (best for automation): once the user has a Google Drive connection in Make, build a
     scenario: HTTP "Get a file" (the Commons URL) then Google Drive "Upload a file" (folder ID, file name).
     Make runs it on its own servers, so no sandbox network limits and no base64.
   - **GitHub**: commit the images on the working branch; the user downloads the folder from GitHub
     and drags it into the Drive folder.
   - **Connector base64**: only for one or two files under about 50 KB.
8. **Report**: Drive folder link, count saved, the skipped list with reasons, and anything to verify.

## Sandbox network

Hosts the cloud environment must allow: `commons.wikimedia.org`, `upload.wikimedia.org`.
Add more (for example `imslp.org`, `archive.org`, `tile.loc.gov`) only when a run needs them.

## Quality bar

- Never call an image public domain unless Commons tags it that way; the script enforces this.
- The Commons tag reflects US public domain. For "PD in Russia" files, note it in the sources sheet.
- Before posting, spot-check that each image matches its script beat (the manifest lists the beat order).
