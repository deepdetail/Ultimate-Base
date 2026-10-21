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
