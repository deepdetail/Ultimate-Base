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
  - Stick sideways turns (see the flying update of November 10): all the way over, about 44 degrees a second for the Cessna and about 70 for fighters right away, and about a third more when held over.
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
- **Barrel roll (Starfighter mode only):** double tap the left or right side of the screen (a mouse double click works too). The stick flick was taken out on November 9 because quick steering kept setting it off. A deliberate double flick, lifting the thumb in between, came back on November 10. One spin with a slide; an orb that reaches you mid-roll bounces back. Normal flying never banks past about 30 degrees.
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
  - The stick all the way over banks about 12 degrees and turns at three quarters of the plane's best rate. (On November 10 the turn became strong from the start, while the bank stays gentle.)
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

### Flying update (November 10)
Asked for: an autopilot you can switch on and off, a BOOST button, better turning, and an instant barrel roll from a double tap on either side or on the stick that dodges and attacks.
- **Why BOOST seemed to be missing:**
  - BOOST, barrel rolls and the new autopilot are Starfighter features.
  - The MODE button in a mission used to switch modes on every tap. A stray tap could leave a pilot in Assisted, where a throttle replaces BOOST, sideways rolls the plane, and double taps do nothing.
  - Every save is switched back to Starfighter once, with a message.
  - MODE now opens a picker that pauses the mission and explains each mode. Picking a mode there is never undone.
- **AUTOPILOT button:**
  - It sits on the left above the stick (the P key does the same).
  - When it's on, let go of the stick and the plane steers itself along the boxes and holds their height.
  - A thumb on the stick hands control back, and the autopilot takes over again a third of a second after you let go.
  - It stays on between missions until you turn it off. Starfighter only.
- **BOOST:** hold it as long as you like, or tap it for three seconds of boost so your thumb can go back to FIRE. The button glows while you boost.
- **Turning:**
  - The stick all the way over now turns 1.25 times as fast as before, right away: about 44 degrees a second for the Cessna, about 70 for fighters.
  - Held over for about a second, it turns about 1.7 times as fast as before.
  - The first second still banks only about 12 degrees, then deepens to 30.
  - The middle of the stick is gentler, for lining up on the boxes.
- **Instant barrel roll:**
  - Double tap either side of the screen, or double flick the stick: two quick flicks the same way, lifting the thumb in between.
  - It starts the moment the second touch lands and spins at full speed from the start, taking 0.45 seconds instead of 0.6.
  - It slides farther: 34 instead of 26.
  - Holding the stick and wiggling it never rolls.
- **Roll attack and dodge:**
  - The spin smashes any drone, jet or balloon within 30 for full points (SPIN SMASH!, WHIRLWIND!, ROLL ATTACK!), both when it starts and while it spins.
  - It bounces back orbs within 15 instead of 6.5.
- **Measured in the headless simulation:**
  - With the autopilot flying hands-free, every plane finished with full health and no missed targets, and the legs stayed about 30 seconds.
  - It flew through 56 to 70 boxes per run. The F-16 got 66 of 70 on Tahoe and 70 of 71 on Moab.
  - From 70 degrees off course, it was back on the line within 8 seconds.
  - Double taps and double flicks rolled on the second touch. Holding and wiggling the stick, slow double flicks, and flicks in opposite directions never rolled.
  - A roll smashed a drone 25 to one side and one 15 behind on the other side, and left one 45 away alone.

## Low-level runs (November 16), Phoenix's third round
Asked for:
- Missions as one short, fairly straight trip (like Donner Lake to Emerald Bay) instead of a circle around the lake.
- Flying low, under the gang's radar, which is why the boxes are low.
- The terrain shaping the course: gaps between trees, and canyons.
- The same for Utah, with a flight under an arch.
- Slightly smaller planes, without overcorrecting.

- **One run, one trip:**
  - Every plane mission is now a run from one real place to another. Missions no longer start at the base, and fast planes no longer loop around the lake to fill time.
  - The game picks a run that takes this plane roughly 40 to 100 seconds, so slow planes get the short runs and jets the long ones.
  - Each run keeps three stops: two checkpoints on the way and the gang outpost at the end.
- **The runs:**
  - Tahoe, short: Truckee River Canyon (Truckee to Tahoe City) and West Shore (Tahoe City to Emerald Bay).
  - Tahoe, long: Donner Lake to Emerald Bay (down the Truckee River canyon, then along the west shore) and East Shore (Incline Village to South Lake Tahoe).
  - Moab: Arches Run (Moab to Delicate Arch), River to Balanced Rock, and Colorado River Gorge (River Bend to the Fiery Furnace).
  - Donner Lake was missing from the map data, so the flat ground at its level is now filled in as water.
- **How a run is found:**
  - The game searches the real height map for the cheapest path between the two places, where high ground costs more. That makes runs follow valleys, river canyons and shorelines.
  - A gentle pull keeps runs from wandering far from the straight line.
  - Over Lake Tahoe, water far from shore costs more, so runs hug the shoreline with trees on one side.
  - Bends are smoothed only as much as each plane's turning allows.
- **Flying low:**
  - The boxes sit about 17 units above the ground for the Cessna and 24 for fast jets, above the trees on the corridor's edges.
  - They climb early for hills, no steeper than about 19 degrees, and come down gently, at about 13 degrees.
  - The plane holds the boxes' height a short way ahead, so it follows the ground.
  - Ground avoidance steps in only very close to the ground. A bump costs a little health instead of a big hit.
  - There's no TOO LOW warning on these runs.
- **The radar line:**
  - It sits about 60 to 76 units above the boxes.
  - Climb above it and you get a red glow around the screen, RADAR HIGH! in the HUD, a beeping warning and a red laser grid at the line. A meter starts to fill.
  - If the meter fills you're SPOTTED: a squad of drones scrambles from the ground ahead. There are five seconds before it can happen again.
  - Finish without being spotted for a GHOST RUN bonus (+1000).
- **Trees and canyons:**
  - In the Sierra, the run cuts a gap through the forest, lined with two ragged rows of tall pines.
  - In Moab, the canyon walls are the real terrain, and sandstone pillars stand along the run's edges.
  - Clipping a tree or pillar costs a little health and bumps you up, with a "stay in the gap" warning.
- **The arch:** every Moab run passes under a giant red rock arch, built by the game until the GLB model arrives. Flying under it pays +500 (UNDER THE ARCH!).
- **Smaller planes:** planes are drawn 15% smaller, and the chase camera sits a little closer.
- **Measured in the headless simulation (autopilot, hands off):**
  - Every run finished with full health. No radar spots, no tree or pillar hits, no ground bumps.
  - It flew through 78 to 95 percent of the boxes, and went under the arch on every Moab run.
  - Times:
    - Cessna: Truckee River Canyon 65 s, West Shore 76 s, Arches Run 80 s.
    - F-16: Donner Lake to Emerald Bay 52 s, Colorado River Gorge 38 s.
    - L-39: East Shore 64 s, Arches Run 49 s.
    - Rocket: Donner Lake to Emerald Bay 46 s.
  - A 4 second pull-up got spotted, and a swerving test hit the trees, so both checks work.

### Next for low-level runs
- More runs per region from your ideas. (Obstacles inside the corridor shipped in round 5, below.)
- The arch and pillars as real GLB models (see `art/MISSION_3D_ROSTER.md`).
- Moab's runs are short for jets (about 40 to 50 seconds since the November 17 slowdown), because the map is only 32 km across.

## Guns, missiles and a slower pace (November 17), Phoenix's fourth round
Asked for:
- Cannons with rapid-firing bullets that come from each wing and overheat after 10 seconds.
- A total of 4 to 8 heat-seeking rockets or missiles.
- Slower gameplay: it felt a little too fast.

- **Twin wing cannons (planes):**
  - Every plane has a cannon in each wing. The hover saucer has one on each side of its rim.
  - They take turns, left then right, aimed so the two streams cross about 300 units ahead.
  - Each wing fires at the installed weapon's own rate, so together they shoot twice as fast:
    - Bullets fire at least about 14 rounds a second and at most about 28.
    - Rockets and railgun slugs keep their own slower pace.
    - The laser pod fires a beam from each wing.
  - Weapon upgrades in the Hangar still decide the damage, color and muzzle speed.
  - Cars, boats and the tank keep one gun up front, with no heat.
- **Gun heat:**
  - Heat builds while FIRE is held, and 10 seconds straight overheats the guns. When that happens:
    - An OVERHEATED warning shows and a sizzle plays.
    - The FIRE button turns grey and reads HOT!.
    - GUNS HOT shows under the crosshair.
  - Overheated guns cool for 3 seconds, then fire again.
  - Letting go cools them at the same rate, so short bursts never overheat. One second on and one second off peaked at 10 percent heat.
  - Heat shows in two places: a ring around FIRE, and a curved gauge to the left of the crosshair. The gauge stays visible while a thumb covers FIRE.
- **Heat-seeking missiles:**
  - **Load per mission:**
    - Cessna: 4.
    - L-39 and hover saucer: 6.
    - F-16, MiG-29, F/A-18, F-22 and Star Hopper: 8.
  - They hang on the model, on wingtip rails and pylons, and disappear one by one as they fire, left then right.
  - **The MISSILE button:**
    - It sits above FIRE. On a keyboard, M or X fires one.
    - It shows how many are left and pulses red while you're locked on.
    - A lock tone beeps when the lock comes on.
  - **Flight:**
    - The missile drops off its pylon, lights its motor, and chases the target you're locked on to. With no lock, it chases the closest one in front of you.
    - If its target is knocked out first, it looks for another.
    - After 5 seconds it blows up on its own.
  - Heat seekers look for engines, so they skip the supply balloons.
  - On low runs the missile skims over the ground instead of flying into it. It stops skimming right at the end, so it can still hit targets on the ground.
  - A hit knocks out the target and anything else within about 22 units, with DIRECT HIT, KABOOM or SPLASH ONE.
  - The results screen lists missile hits.
- **Slower pace:**
  - Every plane flies at 80 percent of its November 10 speed, in every flying mode. Starfighter mode is still about 1.4 times the speed from before November 10.
  - Drones and enemy jets slow down with it.
  - Runs take about a quarter longer. The picker still gives slow planes the shorter runs.
  - Cruise in Starfighter mode: Cessna 64, L-39 105 and F-16 177 units a second.
- **Measured in the headless simulation (autopilot):**
  - **Overheat:** 10.0 seconds after FIRE starts, every time, then 3.0 seconds to cool. Rounds split evenly between the wings (F-16: 397 left, 396 right).
  - **Missile hits:**
    - F-16, Colorado River Gorge: 7 of 8.
    - Hover, River to Balanced Rock: 6 of 6.
    - L-39, West Shore: 6 of 6.
    - Cessna, Arches Run: 3 of 4.
    - With FIRE held at the same time, the guns often knock out a missile's target first. The missile then looks wider for another one, and blows up after 5 seconds if nothing is left. The F-16 on Colorado River Gorge still hit with 6 of 8.
  - **Low runs, hands off with FIRE held:** every run finished with full health, no radar spots and no tree hits. It flew through 90 to 100 percent of the boxes, and went under the arch on every Moab run.
  - **Times:**
    - Cessna: Truckee River Canyon 82 s, West Shore 95 s, Arches Run 101 s.
    - L-39: East Shore 82 s, Arches Run 61 s.
    - F-16: Donner Lake to Emerald Bay 71 s, Colorado River Gorge 49 s.
    - Star Hopper: Donner Lake to Emerald Bay 58 s.
  - **Earlier controls:** turns, rolls, flicks, the roll attack, BOOST, autopilot and the mode picker all pass.

### Next for weapons
- A feel test on a phone:
  - Is 10 seconds of heat right, and are 3 seconds of cooling too long?
  - Should missiles reload at checkpoints?
- A missile camera. (A lock tone that speeds up while the lock builds shipped in round 5, below.)
- Shorter runs for the Cessna: its Tahoe run is now about 80 seconds.

## Playtest round 5 (November 17), J and Phoenix
Asked for, after playing the sideways missions:
1. Obstacles along the path between waypoints, like a large tree, so you can't just fly straight on autopilot. Avoidable, never impossible.
2. Fly-through checkpoints about 15 to 20 percent further apart.
3. A throttle on the right, thinner than BOOST, resting at full, with BOOST as a button above it.
4. Cannons that feel more realistic and less electric: gray metallic tracers with the yellow streaks, more staccato, in bursts of 3 to 5 seconds.
5. A missile lock from far out (about 1 to 1.5 miles), with a reticle that appears at the initial lock and builds to a full lock over about 3 seconds. Missiles fire with or without a lock, and upgrades can shrink the lock time later.
6. More and better targets: drones now and then, ground targets like trucks, and an enemy outpost near the end that's targetable from far out and takes more than one missile or 5 to 7+ seconds of cannon fire.

Tabled for later: an end boss, importing 3D assets (the Cessna 182 model), and deeper weapon and plane upgrades.

- **Giant obstacles:**
  - A huge pine in the Sierra, a granite rock stack where a run crosses the lake, and a sandstone tower in Moab. Each stands right on the flight line and rises about 20 to 28 units above the flight path.
  - About one every 14 seconds of flying: 3 to 6 on every run a plane can draw. They're spread evenly, at least 4 seconds apart, and never near the start, a checkpoint, the Moab arch or the final run-in.
  - Each leaves a wide gap on both sides (the corridor runs about 48 to 74 units each way from the middle), or you can hop over it just under the radar line.
  - The boxes stop about 2.6 seconds before an obstacle and pick up about 1.8 seconds after it, so a dodge never costs a box.
  - While you're lined up to hit one, a warning (GIANT TREE AHEAD! or ROCK TOWER AHEAD!) and a beep come up about 2.5 seconds ahead.
  - Clipping one hurts once, as much as a drone crash (6 on ROOKIE, 7 on PILOT, 9 on ACE), shoves you clear and breaks the box streak. Slipping past is a NICE DODGE, +50.
  - AUTOPILOT does not steer around them, on purpose. It tells you to take the stick, and once you do near an obstacle it waits until you're past before taking over again.
- **Boxes 18 percent further apart:** about every 1.5 seconds instead of 1.3, and at least 82 units apart instead of 70.
- **Throttle (Starfighter):**
  - A thin throttle on the right edge (30 pixels wide; BOOST is 54) that rests at full, the normal cruise speed. Slide it down to slow to as little as half speed. It stays where you put it.
  - BOOST is now a button right above it, and still goes faster than full, whatever the throttle says.
  - On a keyboard, Q or Ctrl slows down and R speeds back up.
  - ASSISTED and REAL PILOT keep the big throttle.
- **Bursty guns:**
  - Tap FIRE for a 4 second burst, so your thumb is free while it fires. Hold FIRE and the guns fire burst after burst, with about half a second between them.
  - A steady clip you can count: about 9 to 11 rounds a second from both wings for most guns, and about 17 for the Vulcan. These replace the round 4 rates of 14 to 28 a second.
  - Real guns fire plain gray metal rounds with a glowing tracer every third round. They puff gun smoke at the muzzle and make a sharp crack and thump instead of a zap.
  - Planes without a weapon upgrade now have plain Wing Guns with yellow tracers instead of the electric Stun Blaster. Cars and boats keep the Stun Blaster.
  - About 10 seconds of firing still overheats the guns: 11.2 seconds of holding FIRE, counting the pauses.
- **Missile lock:**
  - Keep the nose on a target (within about 16 degrees) and the reticle pops up on it: yellow corners, a ring that fills up over 3 seconds, LOCKING and the range in miles. The seeker beeps speed up as it builds.
  - Range: 1 mile for slow planes up to 1.5 miles for fast jets (Cessna 1, L-39 about 1.2, F-16 1.5).
  - At full lock it snaps tight and turns red with a diamond: LOCKED, a double beep, and the MISSILE button pulses.
  - The lock stays on its target while the nose stays roughly on it, and lets go after half a second pointed away.
  - Missiles fire with or without a lock:
    - Locked: FOX TWO!, and it chases that target hard.
    - Unlocked: it flies straight, only grabs what comes right in front of it (within about a mile), and turns less sharply.
  - The lock time is one setting in the code (`lockTime`), ready for an upgrade that shrinks it.
- **More targets:**
  - Drones now and then: one flight per hop on ROOKIE and two on PILOT and ACE, down from two or three swarms per hop.
  - **A gang convoy every hop:**
    - 2 trucks, or 3 on the last hop, drive up the valley toward you on the ground beside the flight line, never on water.
    - They take 3 hits (4 on PILOT and ACE). On PILOT and ACE they lob orbs.
  - Supply balloons, and enemy jets on ACE, as before.
  - **The enemy outpost (strike runs):**
    - A walled yard about 200 m across with a command hut, a barracks, a hangar, fuel tanks, a radar dish, an anti-air gun and a flag. It stands beside the flight line at the end of the run, and replaces the old radar and road block for planes.
    - Lockable from up to 1.5 miles, with an armor bar floating over it.
    - Armor: about 5.5 seconds of steady fire from your plane's guns on ROOKIE, 6.5 on PILOT and 7.5 on ACE, or 3 missiles (each knocks off 40 percent).
    - It smokes, then burns, as it takes damage. Its gun lobs orbs at you on PILOT and ACE. It goes up in a chain of blasts.
    - Fly past it while it's still standing and you come around for another pass, like a real strafing run. The plane keeps straight for about 2.6 seconds, then swings back around (by itself in Starfighter mode and on AUTOPILOT). You get 35 seconds near it, then the mission ends without it: fewer points, never a loss.
  - Recon flights (planes without a weapon upgrade) still end with the camp photo.
- **Measured in the headless simulation:**
  - **Obstacles:**
    - A scripted pilot that steers around them dodged every one: L-39 on East Shore 6 of 6 (with 36 of 36 boxes), F-16 4 of 4, Cessna in Moab 3 of 3.
    - Hands-off AUTOPILOT hits every one (5 of 5 on the L-39's East Shore run), as designed.
  - **Guns:** a tap gave one 4.05 second burst of 41 rounds. Holding FIRE gave 3 bursts with 2 pauses and overheated at 11.2 seconds.
  - **Throttle:** the L-39 flies 105 units a second at full, 79 at half, 53 at zero and 166 with BOOST.
  - **Lock:** the initial lock came at 474 units (1.18 miles) for the L-39 and 601 units (1.5 miles) for the F-16, and the full lock 3.05 seconds later.
  - **Outpost:** guns only (M2 .50 cal) took 5.9 seconds of firing on ROOKIE, 6.8 on PILOT and 7.8 on ACE. Missiles only took 3 hits on every tier.
  - **The kids' saves:**
    - Phoenix (F/A-18 with the Vulcan): the outpost went down on all three test runs, after 0, 2 and 3 come-around passes.
    - Dude (Cessna with the M2): it went down on the first pass.
    - Both summaries list the dodged obstacles.
  - **Other vehicles:** cars, the tank, the boat, the hover saucer, ASSISTED and REAL PILOT run with no errors.

### Next for round 5
- **A feel test on a phone:**
  - Do the obstacles look big enough from far away?
  - Is a 4 second burst right?
  - Does the 3 second lock feel fair in fast jets? An F-16 at full throttle only gets its full lock about 70 units out, so pulling the throttle back, or a second pass, matters.
- Lock time upgrades in the Hangar.
- Tabled by J and Phoenix: an end boss, the Cessna 182 3D model, and deeper weapon and plane upgrades.

### Still to come
- Story missions per location (a short story, a cutscene, a boss), an automated takeoff in the intro, and a look-around in the cockpit during the briefing.
- Recorded voice lines and music (the sound effects are code-made for now).
- Bonus targets and obstacles from the roster (comms towers, turrets, rock arches, cables) placed along the courses.
