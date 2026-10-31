# BASED Commander: web version

This folder is the whole game. Nothing to install, and it plays with no internet.

## Try it now
Double-click `index.html`. It opens in your browser and plays offline. Saves stay in that browser on that computer.

## Put it online for free
It is just files, so any static web host works. Upload the contents of this folder, with `index.html` at the top level.

1. **Netlify Drop:** open app.netlify.com/drop, sign in, and drag this whole folder onto the page. You get an https link in a few seconds.
2. **GitHub Pages:** make a public repository, upload these files, then Settings > Pages > Deploy from a branch > main, root folder. The link looks like `https://yourname.github.io/repo-name/`.
3. **Cloudflare Pages:** Workers & Pages > Create > Pages > Upload assets, then drop the folder.

## Play it like an app on iPhone or iPad
Open the https link in Safari, tap Share, then Add to Home Screen. It opens full screen with its own dragon icon, and after the first visit it keeps working offline.

## Moving a base between devices
Saves live on each device (and in each browser). To move a base, open Settings (the gear) > SAVE CODE on the old device, copy the code, then Settings > LOAD CODE on the new one. The same code also moves a base into the iPhone app.

## What is inside
| File | What it is |
|---|---|
| `index.html` | The game |
| `terrain.js` | Map terrain for the mission map |
| `vendor/three/` | three.js r128 and two add-ons (MIT license, see `LICENSE`) |
| `vendor/fonts/` | Orbitron and Chakra Petch (SIL Open Font License, see `OFL-*.txt`) |
| `icons/`, `manifest.webmanifest`, `sw.js` | Home screen icon and offline play |

Built from `prototype/based.html` by `tools/build_exports.py`.
