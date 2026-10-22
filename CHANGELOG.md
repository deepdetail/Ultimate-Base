# BASED Commander changelog

Every commit on GitHub, oldest first, grouped into versions. The playable game is `prototype/based.html`.

## Version 2.0 (current, 2026-10-22)

The painted art version. Still a little glitchy, with plenty left to work out (see NEXT_STEPS.md), but most of the game now runs on approved art from Drive.

**Highlights**
- Painted Commanders and crew, painted enemies in level-tiered waves (including the girl thief with raven and the boy soldier with coyote), painted vehicles, turrets, building fronts and gear icons.
- Outside and inside views with a big BASE / OUTSIDE button. The outside shows only the approved front, which grows with the base; tap the building or the top bar Recruit button to recruit.
- Bases grow taller, deeper and wider with level; room width is capped by room level; rooms can be destroyed.
- Crew hold their equipped weapons, and wear the approved armor and outfit art, with the gun always on top.
- Defense battles: turrets turn and aim at targets, Barracks defenders, exterior guards and lobby crew fire their own weapons. Raids against generated enemy bases you can watch.
- Jobs: Auto Assign Jobs, Auto Pick Best Job, the Exterior Guard job (one spot per turret plus level bonus), Deny Access for recruits and Exile for crew.
- Clone game v2 with tells and quirks, and name-as-password Continue Game with cloud saves.
- Flight 2.0 with real vehicle specs, photoreal Cessna and L-39 cockpits, 3D missions over real terrain, drones and raider Cybertrucks that get disabled, never killed.
- Run sheets for ChatGPT art batches (crew, enemies, vehicles, rooms, icons, cockpits, wardrobe, weapon side views).

### Art pipeline and painted characters

- `25da561` 2026-10-20: Add art brief for generating realistic anime assets
- `6f3ced6` 2026-10-20: Add approved character style sheets and ChatGPT prompt pack for crew art
- `39097aa` 2026-10-20: Add paste-ready Claude in Chrome run sheet for crew art batch 1
- `e4684b8` 2026-10-20: Make the teal M and orange F sheets the Commander; rename section 1 and ladder outputs
- `70047bf` 2026-10-20: Add Commander hair variants to run sheet and 2D raster customization design
- `c2b3f83` 2026-10-20: Add level 1 to 4 enemy run sheet; key green subjects (clones, alligators, clone bear) on magenta
- `d8bc462` 2026-10-20: Deploy painted Commander sprites (male and female) cut from the approved style sheets
- `10a2903` 2026-10-20: Run sheet: skip Commander items already cut from sheets; match variants to the sheet's standing pose
- `706c702` 2026-10-20: Tighten Commander sprite edges to remove soft halo at the boots
- `f135adc` 2026-10-20: Customization doc: use existing c.art field instead of a new sex field
- `2d36a18` 2026-10-20: Deploy first painted crew: five crew sprites, blond male Commander, cleaner female Commander

### Painted vehicles, enemies and cloud saves

- `11cdf1d` 2026-10-20: Add crew variety lineup prompts per role; skip clone prompts (game builds clones from crew sprites)
- `3806922` 2026-10-20: Match in-game BASED rooftop sign and Huey livery to the setup logo; add utf-8 charset
- `987d153` 2026-10-20: Add painted vehicle art prompts (17 vehicles, side view, magenta key)
- `486b746` 2026-10-20: Prepare vehArt for painted vehicle sprites (VSPR, falls back to drawn art)
- `ef5e891` 2026-10-20: Vehicle prompts: keep wheels or gear level at the bottom so sprites sit in the 120x44 box
- `43d3110` 2026-10-20: Add painted enemies (raider, thief, feral boar, glow gator, clone bear) and painted Cybertruck
- `146ef69` 2026-10-21: Add painted skunk, mercenary, giant grizzly and dragon boss; bosses render larger
- `3cf15f5` 2026-10-21: Cloud save per Commander name, save code backup, simpler setup; next art list and roadmap
- `3f85600` 2026-10-21: Commander looks: keep only M (blond) and F; drop dark-hair and Classic; female sprites at 94 percent height
- `1af65fb` 2026-10-21: Add paste-ready Chrome run sheet for rooms, building fronts and turrets (35 images)
- `7109776` 2026-10-21: Add painted T. rex boss (level 40, both regions)
- `62cf8ce` 2026-10-21: Rename the Tahoe home to Sierras, California
- `f9f3aa5` 2026-10-21: Add rooms, building fronts and turrets run sheet: one-at-a-time ChatGPT prompts plus Chrome driver version
- `6a3af7a` 2026-10-21: Level art prompts: use the new Sierras, California home name

### Logo, HD vehicles, icons and prize ladders

- `c6b3195` 2026-10-21: Title logo: BASED over COMMANDER, same width, one steel gradient; page title BASED Commander
- `214f6df` 2026-10-21: HD vehicles: PBR paint, metal and glass with studio reflections in the Hangar and missions
- `841cc4e` 2026-10-21: Add ChatGPT icon run: 88 icons for weapons, armor, outfits, vehicle weapons, turrets, resources, rooms, UI, badges, factions, eras
- `7d6e4bf` 2026-10-21: Split the 88-icon run into one-at-a-time prompts and three Chrome driver runs
- `06fc08c` 2026-10-21: Mission scale: stretch the real map 2.5x, smaller trees, smaller vehicles
- `e68cfa8` 2026-10-21: Base crew walk side to side only and face their direction; denser Tahoe forests
- `e19091f` 2026-10-21: Prepare gearArt for painted weapon and armor icons (GSPR, falls back to drawn art)
- `05066a9` 2026-10-21: Sell vehicles and a mission prize ladder
- `3c280e3` 2026-10-21: Prize ladders: Ferrari at mission win 3; battle ladder with Rezvani (3), Lamborghini Huracan (7), Revuelto (21)
- `69cc1b7` 2026-10-21: Phase A: Hangar showroom renderer upgrade
- `b37b305` 2026-10-21: Remove the vintage rooftop water tower and center the sign; prepare painted rooms, rooftops and building fronts
- `4c7c633` 2026-10-21: Add room, building front and rooftop run sheet matched to the character art style
- `5b52de4` 2026-10-21: Split the main session's room, front and rooftop run into one-at-a-time prompts and a Chrome driver; mark LEVEL_ART_RUN rooms superseded
- `ee9fc1a` 2026-10-21: Tidy room run prompt punctuation
- `8ee9ee2` 2026-10-21: Tidy remaining double periods in room run prompts

### Clone game v2, flight 2.0 and cockpits

- `fcc099a` 2026-10-21: Clone game v2 and name-as-password Continue Game
- `f136e1f` 2026-10-21: Add cockpit and wardrobe run sheets for Claude in Chrome
- `4d9a4fb` 2026-10-21: Roadmap: exterior-first UI and the 10-level underground hangar
- `9588e8c` 2026-10-21: Flight 2.0 core, real vehicle specs, named upgrades, real weapons and ballistics
- `3627161` 2026-10-21: Photoreal Cessna 182 and L-39 cockpits from Drive
- `892b8f7` 2026-10-21: Use the wide-windshield Cessna cockpit; per-image cockpit framing
- `d8c00f2` 2026-10-21: Show weapon, armor and outfit icons in crew lists, crew cards and raid squads

### Battles, raids and the painted base

- `e6e3f21` 2026-10-22: Approved-art enemy waves by level, crew fire from their posts, watchable raids, real drones and raider trucks
- `46cee33` 2026-10-22: Painted gear, turrets, building fronts and rooftops from Drive
- `6f221fd` 2026-10-22: Outside and inside views, base size that scales with level, painted vehicles
- `5f6b0f8` 2026-10-22: Fix the BASE / OUTSIDE button
- `586328d` 2026-10-22: Outside view is one compact exterior shot
- `e1b097f` 2026-10-22: Exterior shows the full building height and width; destroy room
- `c8bd3d6` 2026-10-22: Exterior is only the approved painted front; tapping the building recruits
- `301fcb3` 2026-10-22: Roadmap: park rooftop stage levels for later
- `d886414` 2026-10-22: Restore tapping people to open their card; simplify the inside view
- `30b6058` 2026-10-22: Bigger tap area for crew at the door
- `eeec45e` 2026-10-22: Crew hold their equipped weapons
- `b763b1c` 2026-10-22: Bigger exterior that grows with the base; no waiting crew inside
- `3b6b930` 2026-10-22: Front scales with floors above ground; Deny Access and Exile for crew
- `d8845b5` 2026-10-22: Bigger first building fronts, about two crew tall
- `de53606` 2026-10-22: Turrets aim at targets, Recruit button in the top bar, auto assign jobs, exterior guards who fight in raids
- `01fa7e1` 2026-10-22: Armor shows on painted crew, under the held weapon
- `eca2cc2` 2026-10-22: Use the approved gear art for armor and outfits on painted crew

## Version 1.0 (2026-10-20)

The one-shot build: the game plan and playable prototypes v0.1 to v0.6 with code-drawn art and no painted graphics.

- `eb92ca3` 2026-10-20: Add preliminary game plan for Ultimate Base
- `aab5604` 2026-10-20: Update game plan with world, factions, clones, classes, vehicles
- `68897d9` 2026-10-20: Add playable BASED prototype v0.1 and round 2 decisions
- `bd855b7` 2026-10-20: Prototype v0.2: anime art pass, hangar categories, 3D missions over real terrain
- `e1bf5ce` 2026-10-20: Prototype v0.3: anime ninja crew, gear, themed rooms, real prices, strike and recon missions, 3D vehicle models
- `76442f1` 2026-10-20: Prototype v0.4: 3D turrets, 100 base levels with seven styles, wide rooms, tall floors, room levels
- `b78dbb6` 2026-10-20: Prototype v0.5: growing lobby, 16 turret slots, boxy 3D turrets, store and gear, vehicle upgrades, original art
- `a8df125` 2026-10-20: Add sandbox test mode: cheat code, separate save, unlimited resources and test tools
- `8fdb5e2` 2026-10-20: v0.6: realistic anime art refresh, lobby defenders, difficulty picker with simulated win chance, raids on enemy bases
