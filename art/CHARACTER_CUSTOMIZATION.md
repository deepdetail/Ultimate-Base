# BASED: Character Customization with 2D Raster Sprites

Decision: v1 uses painted PNG sprites, not 3D models. The player's Commander gets skin tone, hair color and hair style choices through tint masks and baked hair variants. Named crew and clones keep fixed, hand-approved looks.

## Why 2D raster for v1
- The approved style (realistic anime, detailed cel shading) comes straight out of the image generator. Matching it in 3D needs custom modeling, rigging and a toon shader, which is months of work.
- The prototype already stores `skin`, `hair` and `hs` (hair style) for every person (`prototype/based.html`, `SKINS`, `HAIRS`, `personSVG`). Raster sprites plug into the same fields, so the save format barely changes.
- Limits we accept: one facing direction (three quarters right, mirrored for left), and motion is limited to simple transforms (idle bob, squash on landing, flip). Real limb animation would need a cut-out rig (for example Spine) later.

## The two mechanisms

### 1. Hair style: baked whole-sprite variants
AI images cannot produce pixel-aligned layers, so a hair overlay on a shared body would never line up. Instead, each hair style is its own full sprite of the same Commander.

| Style | Male | Female |
|---|---|---|
| Buzz | `char_commander_m_buzz_01.png` | `char_commander_f_buzz_01.png` |
| Messy / Natural | `char_commander_m_01.png` (messy, slightly in the face, from sheet 1) | `char_commander_f_natural_01.png` (natural, down to the shoulders) |
| Ponytail | `char_commander_m_ponytail_01.png` (short) | `char_commander_f_01.png` (long, from sheet 2) |

Each one also gets a `portrait_...` version. That's 6 sprites and 6 portraits, all listed in `art/CHROME_RUN.md`.

`hs` changes from four values to three: `0 = Buzz`, `1 = Messy/Natural`, `2 = Ponytail`. The Commander's existing `c.art` field (`m` or `f`, see `CMD_ART` in `prototype/based.html`) picks the right column, so no separate field is needed.

### 2. Skin tone and hair color: runtime tint masks
Every Commander sprite and portrait ships with a mask PNG of the same size:
- Red channel: skin (face, neck, ears, hands, any bare arm)
- Green channel: hair, including eyebrows
- Blue channel: unused (reserved for outfit trim later)
- Soft edges, 8-bit, so the tint fades into the line art

At runtime (canvas, once per combination, then cached):
1. Take each masked pixel's luminance L.
2. Hair only: stretch L to the full 0 to 1 range within the hair mask first. The source hair is near-black, and without this step light colors (blonde, white) look flat.
3. Map L through a 3-stop ramp (shadow, mid, highlight) for the chosen tone. Keep the cel bands by using hard stops, not a smooth gradient.
4. Leave pixels with L below about 0.12 untouched so line art stays crisp.
5. Blend by the mask value.

Ramps come from the existing palettes, so the chibi and raster versions agree:
- Skin: the 5 tones in `SKINS`
- Hair: the 7 colors in `HAIRS` (dark, brown, blonde, red, white, blue, teal)

Presets only, no free color sliders. Presets keep every result on-model and kid-safe, and they are cheap to QA (5 x 7 x 6 = 210 combinations, all testable).

## Pipeline (per accepted image)
1. Chroma-key the #00FF00 background to alpha, with despill on the edge pixels.
2. Generate the skin and hair masks (Adobe select-subject with Face, Neck, Arms and Hands for skin and Hair for hair, then a hand touch-up), saved as `mask_<same name>.png`.
3. Export at 512 px tall plus a 1024 px @2x version.

## What stays fixed
- Named crew (section 2 of the prompt pack) and clones: no customization. Each is a unique character with baked colors. A hair-only tint could be added later with the same masks.
- Physique: the Commander uses the Intermediate build in v1. A full physique ladder per hair style would be 2 x 3 x 3 = 18 sprites, so the ladder images (`char_commander_m_novice`, `char_commander_m_advanced`) are for training-progress screens only until that is decided.

## Risks
- Face drift between hair variants. Mitigation: generate each variant as an edit of the approved sheet, and redo any variant that drifts.
- Dark target skin tones on light source skin can look muddy. Mitigation: tune each skin ramp by eye on the first real sprite before locking the palette.
- Mirroring flips the light from upper left to upper right. It's acceptable at game scale. Ship pre-mirrored files only if it bothers playtesters.
