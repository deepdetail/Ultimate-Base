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
| 2 | Auto-targeting: point roughly at a target, it locks in about half a second, aim drifts toward it and shots curve in. Photo missions snap automatically when the camp is close and roughly in view | About a quarter session | **Shipped** (lock-on brackets, curving shots, laser auto-aim, auto photo) |
| 3 | Courses: a real road ribbon on the terrain with soft edges and checkpoint arches; sky lanes of rings with chevrons; obstacles and bad guys along the way (rocks, roadblocks, raider trucks, drones crossing, cliff turrets) | About a full session | **Shipped** (see below; cliff turrets and rock obstacles still to come) |
| 4 | Course layouts for each region, tuned from Phoenix's play | About half a session | Planned |

### Phase 1, as shipped
- **Starfighter flying:**
  - Stick sideways turns, gently at first (see the controls update of November 9): at the full rate about 35 degrees a second for the Cessna, about 55 for fighters.
  - Pull the stick back (down on the screen) to climb and push it forward to dive, and the plane levels itself when you let go.
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

## Arcade missions (November 8 and 9), Phoenix's second round
Asked for: shorter trips, obvious targets, Star Fox barrel rolls, easy enemies early, celebrations, the outside view, faster planes, and waypoint boxes like Flight Simulator 2024.
- **Short hops:** three checkpoints about 30 seconds apart (measured 29 to 33 seconds for every vehicle in a headless simulation), heading out toward the region's landmarks. Fast planes on small maps fly a loop around the landmarks so hops stay about 30 seconds.
- **Planes:** about 1.75 times faster in Starfighter mode (capped near F-22 speed), BOOST about 1.5 times on top with speed streaks and a wider view.
- **Waypoint boxes:** a tunnel of floating boxes about 1.3 seconds apart; the next three glow pink. With the stick level the plane eases to the boxes' height. The final target sits right on the path and the boxes dive at it: the simulated approach comes in about 5 degrees off the target.
- **Barrel roll (Starfighter mode only):** double tap the left or right side of the screen (a mouse double click works too). The stick flick was taken out on November 9 because quick steering kept setting it off. One spin with a slide; an orb that reaches you mid-roll bounces back. Normal flying never banks past about 30 degrees.
- **Roads:** a road cut into the terrain between landmarks. Let go of the stick and the car follows the road back to the middle; the edges are soft bumpers. Gems along the road.
- **Challenge picker on the mission sheet:** ROOKIE (drones only from the front, one hit, fade once passed, barely hurt), PILOT (slow orbs, some two-hit drones, oncoming trucks), ACE (enemy jets that turn and chase, trucks from behind). The default follows mission wins; any can be picked for testing.
- **Every vehicle can shoot on a mission:** with no weapon upgrade it gets a basic stun blaster. Weapon upgrades hit harder. (Decision for the owner to confirm.)
- **Celebrations:** comic fireballs that stay visible at a distance, BOOM and POW words, points with combos up to x4, lock-on brackets, CHECKPOINT and PERFECT LINE banners, a little repair at each checkpoint, screen shake, a red flash when hit, stars on the results. Synthesized sound effects (no sound files) with a SOUND button.
- **Outside view by default:** each mission opens with about three seconds in the cockpit and a line from the tower, then the camera swoops outside. Tap to skip.
- **The helicopter is out of the game for now:** owners get its full price back ($1,200,000). The prize at 12 wins is now the L-39, and the armored SUV is the prize at 16.
- **3D roster:** `art/MISSION_3D_ROSTER.md` lists the bad guys, targets, obstacles and bosses to build in 3D, with a handover spec so models drop in.

### Controls update (November 9)
Asked for: turns that bank only 10 to 15 degrees at first, pull back to climb like Star Fox and Metal Storm, and no rolling unless you double tap.
- **Gentle turns (Starfighter mode):**
  - The stick all the way over banks about 12 degrees and turns at three quarters of the plane's best rate.
  - Held all the way over for more than about a second, the turn tightens to the full rate and the bank deepens to about 30 degrees.
  - Quick back and forth steering stays under about 11 degrees.
  - Assisted and Real pilot still roll to turn, like a real plane: if the MODE button reads ASSISTED or REAL PILOT, sideways rolls on purpose.
- **Pull back to climb, in every flying mode:**
  - Drag the stick down (or press the down key) to climb, and push it up to dive.
  - The drawn cockpit yoke moves toward the pilot when you pull.
  - The hover's Assisted and Real pilot modes keep a helicopter stick, where pushing forward flies forward.
- **Up and down blend with the boxes:** let go and the plane follows the boxes' height. A small nudge now adds to that height instead of replacing it, so the nose always moves the way you pushed. Before, a small push could pull the plane out of a dive.
- **Rolls only on a double tap:** double tap the left or right side of the screen, or double tap a turn key on a keyboard. Wiggling the stick never rolls.
- **Measured in the headless simulation:**
  - Every plane still finished with full health and no missed targets, with the same 30 second hops.
  - The fast jets flew through more boxes: the F-16 got 63 of 70 on Tahoe, up from 56.

### Still to come
- Story missions per location (a short story, a cutscene, a boss), an automated takeoff in the intro, and a look-around in the cockpit during the briefing.
- Recorded voice lines and music (the sound effects are code-made for now).
- Bonus targets and obstacles from the roster (comms towers, turrets, rock arches, cables) placed along the courses.
