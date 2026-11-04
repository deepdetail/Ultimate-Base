# Missions plan: courses, starfighter flying, and real-looking vehicles

Phoenix's ideas, approved November 3: missions become arcade courses instead of an open-world sim. A plane flies a lane of rings and a car drives a road with checkpoints. Steering and aiming get help.

## How every update ships
- **GitHub:** a push to the `claude/base-building-game-design-qpewo0` branch.
- **Game link for quick play-testing**, with no upload: https://claude.ai/artifact/2NEphQxGX7mwigZw9zMLPN
- **Website zip** (`dist/basedcommander.com.zip`) for cPanel, whenever the main domain should update.
  - Optional upgrade: cPanel's Git Version Control pulls the site straight from GitHub, so the domain updates in a couple of clicks instead of a zip upload. It needs the owner's GitHub and cPanel logins.

## Decisions (approved)
1. **Starfighter controls for everyone,** with today's realistic flying kept as an option. The mode button cycles STARFIGHTER (the default), ASSISTED and REAL PILOT.
2. **Speed:** automatic, with a BOOST button, in Starfighter mode. Assisted and Real pilot keep the throttle.
3. **Checkpoint size:**
   - A plane counts within about a quarter mile, and within a tenth of a mile is a bullseye worth $1,000.
   - A car counts within about 0.15 mile.
4. **A missed checkpoint:** keep going with fewer points, never get turned around.
5. **Road edges:** soft bumpers that slow you down, not walls (Phase 3).
6. **Auto-lock:** strong in Starfighter, lighter in Assisted, off in Real pilot (Phase 2).
7. **Roads:** smooth made-up roads between real landmarks first; real highways later (Phase 3).

## Phases
| Phase | What | Size | Status |
|---|---|---|---|
| 1 | Starfighter flying, BOOST, forgiving checkpoints, missed checkpoints that hand over to the next, off-course help, cars steered on the stick with GAS and BRAKE | About half a session | **Shipped** (see below) |
| 2 | Auto-targeting: point roughly at a target, it locks in about half a second, aim drifts toward it and shots curve in. Photo missions snap automatically when the camp is close and roughly in view | About a quarter session | Next |
| 3 | Courses: a real road ribbon on the terrain with soft edges and checkpoint arches; sky lanes of rings with chevrons; obstacles and bad guys along the way (rocks, roadblocks, raider trucks, drones crossing, cliff turrets) | About a full session | Planned |
| 4 | Course layouts for each region, tuned from Phoenix's play | About half a session | Planned |

### Phase 1, as shipped
- **Starfighter flying:**
  - Stick sideways turns right away: about 35 degrees a second for the Cessna, about 55 for fighters.
  - Up and down climbs or dives, and the plane levels itself when you let go.
  - It can't stall, looks ahead and pulls up near the ground, and BOOST goes faster.
- **Checkpoints:**
  - A ring counts within about a quarter mile, and a bullseye (a tenth of a mile) adds $1,000.
  - Flying well past a checkpoint counts it as missed and the next one takes over. Missed rings don't pay.
- **Off-course help:** more than about half a mile off the line, the plane eases back toward the next checkpoint in Starfighter mode. Cars are told to head for the arrow.
- **Cars and boats:**
  - The stick only steers.
  - GAS (tall, green) and BRAKE (red) sit on the right. BRAKE stops, then backs up.
  - The up and down keys still work on a keyboard.
  - FIRE sits above GAS for armed vehicles.
- **Known gap:** cars still drive the open map, so a straight line to a checkpoint can run into a lake. Phase 3's roads fix that.

## Later, noted
- **Hover saucer:** a fast jet-like craft that can stop and hover in place without losing height at zero throttle, and zip around very fast without crashing.

## Real-looking 3D vehicles: what it takes
- **What makes a model look premium on a phone:**
  - An accurate shape, within about one percent.
  - Panel lines and decals baked into textures.
  - Real metal and glass materials, plus soft shadowing and good lighting.
  - Millimeter accuracy is invisible on a phone: a 15 meter jet is drawn about 300 pixels wide.
- **Can Claude or ChatGPT make it from photos? Not at that level yet:**
  - ChatGPT makes flat pictures.
  - Claude builds models from code shapes, which is today's toy look.
  - AI photo-to-3D tools (Meshy, Tripo, Rodin, Hunyuan3D and others) soften panel lines, wobble proportions and make messy geometry on vehicles. That's from memory, and these tools improve fast, so one free test is worth running.
- **What does look exact:** a model a 3D artist built from real drawings, either bought game-ready with a commercial license or commissioned.
- **Trademarks:**
  - There's no known public-domain carve-out for real aircraft or car designs, and makers have gone after games before. That's recalled from memory: a helicopter maker versus a shooter game around 2012, and a Humvee case a game company won in 2020. Neither is verified.
  - The safe pattern: get the exact look, then fictionalize it with new names, no maker logos, and small shape and paint changes. Check with a lawyer before the App Store.
  - A sourced research pass is available on request (High or Max mode).
- **Homework for the owner:**
  1. Pick two test vehicles. Suggested: the Cessna and the Mustang.
  2. Find a game-ready model of each on Sketchfab's store, Fab or CGTrader: PBR textures, a glTF or GLB download, under about 100,000 triangles. Skip "editorial use only" licenses, which forbid games.
  3. Check the license allows commercial app use and changes. A rough budget, from memory: about $20 to $150 for a stock model, and about $300 to $1,500 for a commissioned one.
  4. Put the GLB files in Drive, in BASED Art/3D. Claude then strips logos, renames them, and loads them into the hangar showroom and a mission for a phone test.
  5. Optional: one free AI photo-to-3D test of the same plane, for comparison.
- **The engine question:**
  - The game runs three.js r128 in a web view. That can show a few high-quality models well.
  - A full Metal Storm-style dogfight may eventually need a native engine.
  - Prove it with one licensed model in the hangar first.
