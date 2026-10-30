# BASED Commander: Character System (archetypes, base bodies, outfits, armor)

Status: DRAFT for Phoenix to review. The archetype table below is a starting proposal, not a decision. Questions are in `art/PHOENIX_QUESTIONS.md`.

## 1. The idea in one paragraph
Every crew member is built from a small set of fixed **archetypes** (8 to start). Each archetype is drawn once in a plain **base layer** (a fitted future singlet), as a turnaround sheet with five views. Every uniform, class outfit and armor is then drawn **on that same body**, as the same five views, so clothes always fit that archetype's size and shape. New recruits are randomized from the archetypes (skin tone, hair color, name, small stat spread), so no two feel identical even though the art set stays manageable.

## 2. Why full outfit sheets, not clothing layers
AI image tools cannot draw a jacket on its own that lines up pixel-perfectly with a separately drawn body, so "body plus clothing overlay" would slip at the shoulders and hands. Instead, each outfit is drawn as a full image of that archetype wearing it, made by editing the base sheet ("same person, same five poses, now wearing X"). The base sheet is the anchor that keeps proportions identical. This is the same method `art/WARDROBE_RUN.md` already uses with the two Commanders.

## 3. Archetypes (draft, 8)
Each one has a fixed build, a signature look and one natural boost that fits the game's existing stats (`str`, `aim`, `smarts`, mood) and room classes.

| # | Archetype | Build | Signature look | Natural boost | Fits class |
|---|---|---|---|---|---|
| 1 | Titan | Tall, broad, heavy muscle | Buzz cut, strong jaw | +Strength | Athlete, Defender |
| 2 | Sharpshooter | Lean athletic, very steady stance | Short neat hair, focused eyes | +Aim | Defender |
| 3 | Brain | Slim, slightly shorter | Glasses, messy hair | +Smarts (research) | Scientist |
| 4 | Gearhead | Stocky, thick forearms | Bandana or goggles, grease smudge | +Repair and power output | Engineer |
| 5 | Medic | Average build, calm posture | Neat hair, gentle face | +Healing speed in Med Bay | Medic |
| 6 | Ace | Wiry, quick | Swept hair, aviator look | +Vehicle speed and handling | Pilot |
| 7 | Shadow | Small, very agile | Hood-friendly short hair, sharp eyes | +Speed, better at spotting clones | Athlete, Scout |
| 8 | Heart | Sturdy, warm | Curly hair, big smile | +Mood for roommates, +food output | Cook |

The Commander stays separate (the player's own character, already in `art/commander/`).

Recommended: each archetype has a boy and a girl version, so 16 base bodies. That lands inside the 8 to 16 range and lets the crew look mixed without extra archetypes.

## 4. Randomizing new recruits
When a new person joins:
1. Pick an archetype (weighted toward what the base needs, or random).
2. Pick boy or girl.
3. Pick a skin tone and hair color from the presets, applied at runtime with the tint masks in `art/CHARACTER_CUSTOMIZATION.md` (5 skin tones x 7 hair colors).
4. Give a random name and a small stat spread around the archetype's boost.
5. The outfit comes from their job and faction, so the same archetype looks different by role.

That gives 16 bodies x 35 color combos = 560 looks before outfits, from 16 base drawings.

## 5. Image types

### A. Base turnaround sheet (one image per archetype and sex)
Five equal panels side by side, left to right:
1. Front
2. Front 3/4, turned toward the right (this is the in-game sprite view)
3. Side, facing right
4. Back 3/4
5. Back

Rules: same character in all five panels, same height and scale, feet on the same baseline, relaxed standing pose, arms slightly away from the body, empty hands, solid green #00FF00 background, no text.

Base layer: a fitted, modest future base-layer singlet in charcoal gray with thin teal seams, covering from the neck to mid-thigh with short sleeves, plain gray slip-on socks. It reads as an athletic base layer, kid-appropriate.

### B. Outfit and armor sheets (one per archetype, sex and outfit)
The same five panels, made by editing the base sheet: same person, same five poses, only the clothes change.

### C. Action sheet (one per archetype and sex, in the base layer)
Six panels, all facing right: walk A (contact, left foot forward), walk B (passing, legs together), jump (knees tucked), crouch, hold pose (both hands forward at chest height, gripping nothing, so the game can attach any weapon), knocked out (sitting, dizzy, no injuries).

Two-frame walking (A and B) fixes the "bobbling" look and tolerates small differences between AI frames better than a four-frame cycle.

### D. Weapons
Weapons stay universal: one image per weapon (already in `art/WEAPON_SHEET_RUN.md`), attached to the hold pose's hand point by the game.

## 6. File names
`char_<archetype>_<m|f>_<outfit>_sheet.png`

- outfit = `base`, `action`, a faction (`fac_icr`, `fac_nus`, `fac_atlantis`, `fac_skyvegas`), a class (`cls_soldier`, `cls_medic`, `cls_pilot`, `cls_scientist`, `cls_engineer`, `cls_cook`, `cls_athlete`, `cls_scout`, `cls_executive`, `cls_teacher`) or armor (`elite_t1`, `elite_t2`, `elite_t3`), matching `art/WARDROBE_RUN.md`.
- Example: `char_titan_f_fac_icr_sheet.png`.
- Drive folder: BASED Art/Characters/<archetype>.

## 7. How many images, in phases
| Phase | What | Images (16 bodies) | Images (8 bodies) |
|---|---|---|---|
| 1 | Base sheets | 16 | 8 |
| 2 | Action sheets | 16 | 8 |
| 3 | 4 faction uniforms | 64 | 32 |
| 4 | 10 class outfits | 160 | 80 |
| 5 | 3 armor tiers | 48 | 24 |
| | Total | 304 | 152 |

At a few dozen ChatGPT images a day, Phase 1 and 2 take a day or two. The full set is several weeks, so do Phases 1 to 3 first and check them in the game before committing to Phase 4.

## 8. Prompt templates

### Style lock (first message of every chat, with the two Commander sheets attached)
```
These two character sheets are the approved art style for my kids' mobile game BASED Commander (year 2526, age 9+): realistic anime, adult proportions, detailed cel shading, clean dark line art, light from the upper left. I'm building the crew as character turnaround sheets. Rules for every image: one character only, shown in the panels I ask for, side by side in equal panels separated by thin dark lines, same height and scale in every panel, feet on the same baseline, empty hands, solid pure green #00FF00 background, no shadow, no checkerboard, no text, no logos. Kid-friendly. I'll send one request per message. Reply with just the image.
```

### Base sheet (fill in the {braces})
```
New character: {ARCHETYPE NAME}, a {boy or girl} crew member. Build: {BUILD}. Look: {SIGNATURE LOOK}, {AGE: young adult}. Wearing only the base layer: a fitted, modest future singlet in charcoal gray with thin teal seams, neck to mid-thigh, short sleeves, plain gray slip-on socks. Make a five panel turnaround sheet, left to right: front; front three quarter turned toward the right; side facing right; back three quarter; back. Relaxed standing pose, arms slightly away from the body, empty hands.
```

### Outfit or armor sheet (send in the same chat, right after that character's base sheet, or attach the base sheet)
```
Same character, same five panels and same poses as the base sheet, same face, hair and body. Only the clothes change: now wearing {OUTFIT DESCRIPTION from art/WARDROBE_RUN.md}. Keep the base proportions exactly.
```

### Action sheet
```
Same character in the base layer, six panels all facing right: walk A (left foot forward, heel down); walk B (passing, legs together); jump (knees tucked); crouch; hold pose (both hands forward at chest height gripping nothing, ready to hold a tool or weapon); knocked out (sitting, dizzy stars, no injuries). Same scale and baseline in every panel.
```

### Fix lines
```
Keep the face, hair and body exactly like the base sheet. Only the clothes change.
Keep all five panels the same height and scale, feet on one baseline.
Redo it on a solid pure green #00FF00 background with no shadow.
Same image with no text, letters or logos anywhere.
```

### Chrome driver wrapper
Paste into the Claude side panel in Chrome, with the prompts for one phase listed underneath:
```
Drive ChatGPT (chatgpt.com) in a NEW tab to make character art for my kids' mobile game BASED Commander. Don't touch my other tabs. If ChatGPT isn't signed in, stop and ask me. Ask me before anything that spends money or changes account settings. Never type passwords. Keep everything kid-friendly.
SETUP (start of each chat): start a new ChatGPT chat, ask me to attach the two Commander sheets and wait until I say they're attached, then send the STYLE LOCK with them.
RUN: one character per chat. Send that character's base sheet first, then its other sheets in order, one per message. Start a fresh chat for each new character.
CHECK each image against the rules (five equal panels, same scale and baseline, same face and body as the base sheet, green background, no text). If it fails, send the matching fix line ONCE, then move on and note it.
SAVE: download each accepted image and tell me the downloaded file name next to the target name.
STOP when the list is done or ChatGPT hits a usage limit, and finish with a table: target name, downloaded name, PASS or FAIL, what to redo.
```

## 9. Later (noted, not now)
- **Clones for hide and seek:** each archetype gets a clone version of its base sheet with the tells (bare green feet, a slightly too-perfect smile) plus the trench coat. A hidden clone sometimes carries a rare item (for example a legendary weapon), so catching one is a reward.
- **Legendary outfits:** a short list of rare outfits, some only available to brand-new recruits, so a new arrival can be special.
- **Animation upgrade:** if two-frame walking isn't smooth enough, the next step is a cut-out rig (separate head, torso, arms and legs per archetype).
