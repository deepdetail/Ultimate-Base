# Exports: web hosting zip and iPhone app

`python3 tools/build_exports.py` turns `prototype/based.html` into:

- `dist/BASED-Commander-web.zip`: a folder any static host can serve (instructions in `export/web/README.md`, copied into the zip).
- `ios/BASEDCommander/Web/` and `dist/BASED-Commander-iOS.zip`: the Xcode project with the game inside (instructions in `ios/README.md`).

What is in this folder:

| Path | Used for |
|---|---|
| `vendor/three/` | three.js r128 plus OrbitControls and Reflector, so the map and showroom work offline (MIT) |
| `vendor/fonts/` | Orbitron and Chakra Petch, latin and latin-ext, with their OFL licenses |
| `icons/` | App and home screen icons (the Crimson Dragon over the raid sunset), made by `tools/make_icons.py` |
| `web/README.md` | The hosting guide that ships inside the web zip |

The build script swaps the game's CDN links for these bundled files and stops with an error if any of the expected lines in the game ever change, so an export can't quietly break. Run it after game changes so the Xcode project gets the newest game. `dist/` is not committed.
