# BASED Commander: Character System (archetypes, base bodies, outfits, armor)

Status: DECIDED with Phoenix (31 October 2026). Answers are recorded in `art/PHOENIX_QUESTIONS.md`. Copy-paste prompts for all 40 characters: `art/CREW_SHEET_RUN.md` (built by `art/tools/crew_prompts.py`).

## 1. The idea in one paragraph
Every crew member is built from a small set of fixed **archetypes** (8 to start). Each archetype is drawn once in a plain **base layer** (a fitted future singlet), as a turnaround sheet with five views. Every uniform, class outfit and armor is then drawn **on that same body**, as the same five views, so clothes always fit that archetype's size and shape. New recruits are randomized from the archetypes (skin tone, hair color, name, small stat spread), so no two feel identical even though the art set stays manageable.

## 2. Why full outfit sheets, not clothing layers
AI image tools cannot draw a jacket on its own that lines up pixel-perfectly with a separately drawn body, so "body plus clothing overlay" would slip at the shoulders and hands. Instead, each outfit is drawn as a full image of that archetype wearing it, made by editing the base sheet ("same person, same five poses, now wearing X"). The base sheet is the anchor that keeps proportions identical. This is the same method `art/WARDROBE_RUN.md` already uses with the two Commanders.

## 3. Characters (decided)

### Natural abilities (Phoenix's list)
| Ability | Role | What it does in the game |
|---|---|---|
| Strength | Athlete | More health (HP) in battles |
| Battle | Soldier | Hits harder (AP, read here as attack power) |
| Charisma | Leader | Keeps roommates happy and working faster |
| IQ | Genius | Smarter, earns more in HQ |
| Med | Healer | Knocked out crew heal faster |
| Tech | Nerd | More power and faster repairs |
| Scientist | Research | More tech points, better at spotting clones |
| Driving and Pilot | Adventurer | Faster, safer missions |

### 16 recruit kinds, each as a boy and a girl (32 characters)
Two kinds per ability. Recruits are drawn with plain medium-brown hair and medium skin so the game can recolor every new recruit.

| Ability | Kind 1 | Kind 2 |
|---|---|---|
| Strength | Bruiser (big, heavy) | Sprinter (lean runner) |
| Battle | Trooper (square stance) | Ranger (wiry, steady) |
| Charisma | Captain (tall, confident) | Diplomat (relaxed, friendly) |
| IQ | Prodigy (small, round glasses) | Strategist (tall, calm, rectangular glasses) |
| Med | Paramedic (sturdy, kind) | Caretaker (warm, curly hair) |
| Tech | Hacker (slim, headphones) | Mechanic (stocky, goggles) |
| Scientist | Chemist (lab goggles) | Explorer (outdoorsy, compass) |
| Driving and Pilot | Pilot (aviator glasses) | Racer (compact, gloves) |

### 8 Legendary characters (bonus, half boys and half girls)
The first draft archetypes became the Legendary set. Each has a special name that can never be changed, fixed colors (never recolored) and a gold-seam base layer. A player can recruit one of each, at most. Names are proposals until Phoenix okays them.

| Legendary | Name | Boy or girl | Ability | Look |
|---|---|---|---|---|
| Titan | Ironclad Rex | boy | Strength | Towering, black buzz cut, deep brown skin |
| Sharpshooter | Nova Vex | girl | Battle | Silver-white low bun, violet eyes |
| Heart | Sunny Valor | girl | Charisma | Bright red curls, freckles, big smile |
| Brain | Quill Quantum | boy | IQ | Round gold glasses, blue-black hair |
| Medic | Mercy Bloom | girl | Med | Long dark braid, calm |
| Gearhead | Bolt Ryder | boy | Tech | Copper-red hair, goggles, grease smudge |
| Shadow | Echo Nightshade | girl | Scientist | Black pixie cut with a teal streak, green eyes |
| Ace | Skye Maverick | boy | Driving and Pilot | Swept blond hair, aviator glasses |

The Commander stays separate (the player's own character, already in `art/commander/`).

## 4. Randomizing new recruits
When a new person joins:
1. Pick one of the 16 recruit kinds (weighted toward what the base needs, or random). Rarely, offer a Legendary the player does not have yet.
2. Pick boy or girl.
3. Pick a skin tone and hair color from the presets, applied at runtime with the tint masks in `art/CHARACTER_CUSTOMIZATION.md` (5 skin tones x 7 hair colors).
4. Give a random name and a small stat spread around the archetype's boost.
5. The outfit comes from their job and faction, so the same archetype looks different by role.

That gives 32 recruit bodies x 35 color combos = 1,120 looks before outfits. Legendary characters are never recolored or renamed, and each can be recruited once per player.

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

## 7. How many images, in phases (40 characters)
| Phase | What | Images |
|---|---|---|
| 1 and 2 | Master sheets (turnaround plus action poses) | 40 |
| 3 | 4 faction uniforms | 160 |
| 4 | 10 class outfits | 400 |
| 5 | 3 armor tiers | 120 |
| | Total | 720 |

Phase 1 and 2 first (40 chats, `art/CREW_SHEET_RUN.md`), check them in the game, then decide how many outfits each character really needs before Phase 3.

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
