# BASED: Next Steps (21 October 2026)

## Shipped today
- **Cloud save.** Each Commander name is its own save slot, stored privately under the signed-in claude.ai account (`data/users/<id>/<commander-slug>`).
  - It saves every 30 seconds and whenever the tab is hidden.
  - A new device, or a cleared browser, shows "Continue a saved base" on the start screen.
  - If the cloud copy is newer than the copy on this device, the game offers to load it.
  - Founding a base under a name that already has one is blocked, so a base cannot be overwritten by accident.
- **Save code backup.** Settings has SAVE CODE and LOAD CODE, for when cloud save is off (a signed-out or view-only visitor).
- **Simpler setup.** It now has the name, four look cards with faces (Dark hair, Blond, Ponytail, Classic) and the faction choice. The skin, hair and trim pickers only appear for the Classic look.
- **"Start a new base"** now keeps the old Commander in the cloud list instead of erasing it.

**Limits:**
- Names are unique per claude.ai account, not across every player. This is deliberate: saves are private to each account.
- People viewing the shared link as Viewers cannot write data, so they get device-only saves plus the save code.
- The base lost before this update cannot be recovered. It only lived in that browser's storage.

## Small updates, one session each (ready to build)
1. **Academy plus trivia and lessons (v1).**
   - A new Academy room.
   - To level a room up past L2, the crew must pass a 3-question quiz tied to that room: the Hangar asks aviation questions, Power asks energy questions, Food asks nutrition questions, and the Map and Recon rooms ask geography questions (Tahoe, Moab).
   - Right answers give a discount and bonus XP. Wrong answers explain the answer, and the quiz can be retried later.
   - Questions live in a data table, with three difficulty bands.
   - Lesson cards are short illustrated explainers, unlocked by levelling the Academy.
2. **Explorer mode (no combat).**
   - A profile setting, with an optional parent PIN.
   - Raids become scouting trips, battles become storms or supply runs, and turrets become sensors.
   - Rewards stay comparable, so no progression requires fighting.
3. **Painted art as it arrives.** Rooms, lobby eras, turrets, vehicles and icons. The code paths already exist for crew, enemies and vehicles (`SPRITES`, `ESPR`, `VSPR`). Rooms and lobbies need a new raster layer.
4. **Cybertruck wrap shop.** Wrap designs painted over the side view, bought in the Store.
5. **Bigger enemies in battle.** Raise the regular and big sprite sizes now that the art is painted.

## The flight, driving and recon spec (from the ChatGPT handoff, v1.0, 20 October 2026)
This is a long-term direction, not a rewrite. The order it recommends, which I agree with:
- **Phase 0, baseline.** Record FPS, startup time and memory. Put a feature flag on the new physics and terrain, so the current missions keep working.
- **Phase 1, Tahoe terrain proof.** One small high-quality area: lake, an airport (probably Truckee Tahoe KTRK), haze, materials, better cameras, and quality settings.
- **Phase 2, Cessna 182 Flight 2.0.**
  - A FlightPhysicsProvider interface: the current flight model as the fallback, plus an experimental force-based 6DOF model.
  - Taxi, takeoff, flaps, trim, coordinated turns, stall, landing, and a basic cockpit.
  - Three assist profiles: Casual, Assisted and Advanced.
  - JSBSim compiled to WebAssembly is only to be evaluated in an isolated harness, not assumed to work.
- **Phase 3, Driving 2.0.** A GroundPhysicsProvider: raycast wheels, suspension, and grip that changes with the surface (pavement, gravel, sand, snow). The Cybertruck is the first vehicle.
- **Phase 4, recon and discovery.**
  - The PHOTO button grows into a SurveyMission framework: scoring on framing, range and angle, a photo album, and discoveries on the map that feed base upgrades.
  - Five noncombat missions, one of them a fly-then-drive mission.
- **Phase 5, regions.** Tahoe, then Moab, then Sky Vegas, then the Bahamas and Atlantis.
- **Phase 6, more aircraft, then optional combat.** Combat stays behind a mode setting.

**Architecture rule:** extract modules from the single HTML file in small steps (state, world, render, vehicles, missions, base, ui), test after each one, and keep old saves loading.

## Decisions needed from you (from the spec, with my recommendation)
1. **Which Cessna 182:** a classic analog-panel C182 (recommended for a first build), or a glass-cockpit G1000 model.
2. **"G2":** a Gulfstream II, or a Cirrus Vision Jet G2?
3. **Target device:** desktop-first with an iPhone that works (recommended), or iPhone-first.
4. **Controls:** touch plus keyboard first, then a gamepad. HOTAS (a flight stick) later.
5. **First airport:** Truckee Tahoe (KTRK) is recommended, with the core map covering Truckee to Emerald Bay.
6. **Driving feel:** open exploration plus believable off-road handling (recommended).
7. **Explorer mode for your son:** permanent, with a PIN to change it?
8. **Visuals:** semi-realistic 3D missions with the anime base kept (recommended).
9. **Goal:** a family project, or a future public release? This changes the rules for licensing real aircraft and brands.

## Rough cost (session time)
- **Small updates 1 to 5:** about one session each.
- **Spec Phases 0 to 1:** one or two sessions.
- **Phase 2 (flight):** two or three sessions.
- **Phase 3 (driving):** two sessions.
- **Phase 4 (recon):** one or two sessions.
- **Regions and the aircraft roster:** ongoing.

## Future UI idea (Phoenix): start outside, tap in
**The idea.** The game opens on the base EXTERIOR only: the building front, the grounds, the runway and the sky. You tap a part of the outside to go into that view:
- **The building** opens the full cutaway base view we have now.
- **The hangar** opens the hangar and showroom.
- **The radar tower or map table** opens the world map and mission list.
- Possible later hotspots: the Barracks yard (battles and defense), the Store (a shop front), and the Academy.

**Why it works.**
- The first screen reads as one place, not a menu.
- It gives the painted lobby and exterior art (ROOM_LEVEL_RUN images 23 to 36) a home.
- Upgrades become visible from the outside: a bigger hangar door, a taller tower.

**How I would build it.**
- A new `view` state: exterior, base, hangar or map.
- The exterior is a wide 2D painted scene with tappable hotspots, plus a Back button in each view.
- The base cutaway becomes one view instead of the home screen.
- Saves don't change.
- Cost: one session for the shell and hotspots with the current drawn art, then swapping in painted art as it arrives.

**Hangar levels (also Phoenix's idea).**
- **L1:** a ground-floor hangar beside the building.
- **L10:** upgraded to a SUBTERRANEAN hangar. The ground opens through a ceiling port door, and vehicles rise on a lift platform to launch.

The animation would be: the doors slide apart, the lift rises, and the vehicle rolls out or takes off.

Rooms are capped at Level 5 today, so this needs the Hangar to get its own 10-level ladder. Suggested ladder:

| Hangar level | What it adds |
|---|---|
| L1 | 4 vehicle slots |
| Every 2 levels | +1 slot |
| L5 | Fighter jets |
| L7 | A second bay |
| L10 | Underground hangar with the port door, 10 slots, and launch time cut in half |

**Art needed:**
- A ground hangar exterior.
- A closed and an open port door.
- The underground bay interior.
- The lift platform.

These would be added to the room and level run sheet when we build it.

**Open questions for you:**
- Should the exterior also show crew walking around outside?
- Should raids happen on the exterior view, with turrets visible on the walls?

## Flight 2.0 progress (path to legendary flight)
- **F1, shipped.** The new flight model:
  - The plane's attitude is tracked as a quaternion, so loops, rolls and inverted flight all work.
  - Energy: climbing costs speed, diving gains it, gravity applies, and hard turns bleed speed.
  - Pro mode adds stalls and sink, G-load, over-G and the tunnel-vision blackout.
  - The afterburner is the top 10% of the throttle.
  - Every aircraft flies from its own spec row (`VSPEC`): top speed, stall speed, thrust to weight, roll rate and G limit.
  - The Huey and the Hover Saucer fly like helicopters: they can hover, and the throttle works as the collective.
  - Three assist levels: Casual, Assisted and Pro.
  - The HUD has a pitch ladder, KT, FT, Mach and G readouts, an afterburner cue, and a PULL UP warning.
  - The game runs on real speeds in m/s and squeezes them into map units with a square root, so the map still fits. The HUD shows real knots.
- **Hangar realism, shipped.**
  - Real engines, top speed, stall speed, climb rate, ceiling, G limit, 0 to 60 times and weights replace the old 1 to 5 ratings.
  - Upgrades are named stages, for example: Factory engine, Hot section overhaul, FADEC, Thrust uprate, Enhanced-performance engine.
  - The specs are rounded public figures written from memory. Spot-check them before any public release.
- **Ballistics, shipped.**
  - Weapons carry their real names, muzzle velocities and fire rates: M2 Browning .50 cal, M61A1 Vulcan, Hydra 70 rockets, a laser pod, and a railgun.
  - Tracers inherit the shooter's speed and drop under gravity.
  - Hit tests check the whole path a round travels each frame, so fast rounds can't skip through a target.
  - Rockets leave smoke trails and splash damage; the laser is a continuous beam; the railgun pierces through targets.
  - Assisted and Pro show a lead marker; Casual keeps light aim help.
- **Next:** F2 (cockpit images with live gauges), F3 (takeoff and landing at Truckee), F4 (enemy jets, radar, missile lock tones and flares), F5 (clouds, contrails, afterburner glow and sound).
- **Not done yet:** realistic names for the base-defense turrets, and real flight physics for ground vehicles.

## Battles and raids (shipped 22 October)
- **Approved art only.** Every enemy uses painted art. Any old drawn key falls back to an approved enemy, and the raven, coyote, rogue thief and black bear were added from Drive.
- **Waves grow with base level, a few enemies at a time:**

| Base level | New enemies |
|---|---|
| 1 | Critters: coyote, raven, skunk |
| 3 | Phoenix's pairs: girl thief with raven, boy thief with coyote |
| 5 | Raider soldier with coyote, boars |
| 8 | Mercs and the black bear |
| 12 | Glow gator and clone bear |
| 18 | Giant grizzly |

  Boss fights bring the grizzly first, then the dragon at level 25 and the T. rex at level 35.
- **Crew on the battlefield.** Barracks defenders stand at the turret posts and lobby crew step out front. Each fires their own equipped weapon, with tracers and muzzle flashes, and the win-chance math uses the same positions.
- **Raid you can watch.** The enemy fort is generated from the base's power (walls, towers, number of defenders) and stocked with that faction's roster. Your squad drives up and fights, and the outcome matches the real result. It can be skipped.
- **Flight and drive missions.** Quadcopter drones replace the orange blobs. On ground missions, raider Cybertrucks chase you; shooting the engine and tires disables them (smoke, then a pop), and the driver runs off safe.

## Metal Storm options for flight (pick the order)
1. **Enemy jets and dogfights.** Raider fighter jets with simple chase and evade AI, a radar ring, a missile lock tone, flares to break locks, and pilots who eject and parachute when hit.
2. **Missiles and countermeasures.** Heat seekers (an AIM-9 style missile) and radar missiles with real lock time, range, and lead.
3. **Ground attack runs.** Raider convoys, truck camps and anti-air sites, with strafing passes, rockets and bombs.
4. **Squad wingman.** A crew member flies a second jet and calls out targets.
5. **Mission chains and an XP ladder.** Patrol, then intercept, then escort, then a boss. Pilot ranks unlock new aircraft and loadouts.
6. **PvP-like ghost battles.** Fight a recorded version of your own best run, or a friend's, saved in cloud storage.
7. **Spectacle.** Clouds, contrails, afterburner glow, camera shake, engine sound, and a slow-motion replay of each takedown.
8. **Cockpit gauges.** Live needles drawn over the photo cockpits.

## Later stage (parked)
- **Rooftops as their own stage levels.** The 7 painted rooftops are in the game (`CSPR`). Outside they're not shown, and inside they still cap the top floor. They'll be redesigned as separate rooftop stages later.
- **Still open:** growth rates for base height, depth and width; renaming the Hover Saucer to Hover Bike; painted tower facades.

## Gameplay roadmap from J and Phoenix (22 October)
Shipped now: the level roster waves, enemy weapons, the Clone Lab timer and Holding Cell escapes (see art/LEVEL_ROSTER.md).

Still to build, in a sensible order:
1. **Hangar missions with a story flow.** Start with a Cessna recon flight to spot things, then unlock base growth and harder missions from what you found.
2. **Top-down map of the home region.** (First version shipped 22 October: Sierras map with recon and outposts on the road to Las Vegas.) The real Tahoe or Utah area seen from above, with your base on it. Recon flights reveal enemy bases on the map, and you pick raid targets from there.
3. **Satellite (an exterior upgrade).** Once built, it shows roaming gangs on the map and how far away they are, so you get a warning before a raid and more time to prepare.
4. **New rooms: Weapon Foundry and Armory.** The Foundry builds weapons (cheaper or better than the store over time). The Armory stores and upgrades gear and could arm exterior guards. Both need room art in the next ChatGPT room run.
5. **Clone Lab and Holding Cell tuning.** Converting takes 10 minutes at room level 1 (each level makes it faster). Prisoners sneak out after 10 minutes at level 1 (each cell level adds 50 percent) and come back as a disguised clone worth a big bonus. Tune these once Phoenix has played them.

## Mission map (shipped 22 October)
- MAP button above BASE. Real shaded relief of Lake Tahoe to Las Vegas, built from AWS Terrain Tiles elevation (USGS and SRTM), Natural Earth lakes and US Census state lines.
- Towns on the road east: Carson City, Yerington, Hawthorne, Tonopah, Beatty, Las Vegas. Recon with the Cessna (or any plane) to find each enemy base, then capture it with a squad raid. Each outpost reaches another 110 miles, so the chain is Tahoe, Hawthorne, Tonopah, Beatty, Las Vegas.
- Next: Las Vegas opens Sky Vegas (airship), then the road to Moab. A Moab map and the Bahamas by sea come later. Ideas: faster planes recon farther, outposts pay a small income, enemies try to take outposts back, and the satellite shows raiders moving on this map.

## Building scale (note from J, 23 October)
- Bigger bases should look much taller and larger outside, scaling one to one with the base: more floors up means a taller front, more width means a wider front. Keep checking crew to door proportions on each painted front as the art lands.
- Inside view: the rooms sit inside the outline of the current approved front, stretched to fit the whole base, with a soft blurred wash of the building's colors between the rooms and the outline. No rooftop piece on top.

## Exterior defenses module (draft, 23 October)
Shipped now: a DEFENSES button outside with three upgrades that already change raids. No wall art yet.
- Reinforced Walls: each level adds 20 percent base core health.
- Turret Armor Plating: each level, turrets take 10 percent less damage (up to 50 percent).
- Blast Door: each level, raiders at the door hit 8 percent softer (up to 64 percent).
- Upgrade levels unlock with the base: one level per 4 base levels, up to 10. Costs grow 1.7x per level.
- Base core health now also grows with every turret's level, on top of base level and Barracks armor.

Next for this module (art and features to add later):
1. Wall art layers on the outside view that change look at levels 1, 4 and 8 (sandbags, concrete, energy fence), sized to each painted front.
2. Gate and moat style upgrades that slow raiders near the door, and spike strips that hurt walkers but not flyers.
3. Repair crew: turrets heal slowly during a raid; Engineers in the Power Core make it faster.
4. Shield generator (needs tech): a separate energy bar that soaks hits before the core, recharging between raids.
5. Paid repairs after a raid for turrets knocked offline, so damage carries a cost.
6. Exterior guard posts: towers or bunkers that raise the guard limit and protect guards.

## Backdrop, crew ranks and pets (shipped 25 October)
- Sierras backdrop from Drive (Exteriors, 31AB2791...): full painting behind the outside view, a cropped and softened mountain band behind the inside view. Saved as art/backdrops/sierra_sunset.webp.
- Crew ranks: Common, Rare (+1 every stat) after 300 XP, Legendary (+2 every stat) after 1800 XP and 3 raids fought. Barracks gives 1 XP a second, other jobs 0.5, so Rare is about 5 Barracks minutes and Legendary about 30 plus three raids. Tune after Phoenix plays.
- Pets with placeholder emoji: Guard Dog, Base Cat, Clever Fox, Scout Hawk, Dire Wolf, Baby Dragon. One per crew member, bought from the crew card PET button. Bonuses to stats, mood, and raid damage. Swap in painted pet art from Drive when it lands.
- Still pending: painted art for each room, the Moab backdrop, pet art.
