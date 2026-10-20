# Ultimate Base: Preliminary Game Plan

Working title: **Ultimate Base** (placeholder, open to a better name).

## 1. The one sentence pitch

A side view, tower style base builder for phones (think SimTower and Fallout Shelter) set in a bright, high tech near future, where you dig down and build up, defend the outside with turrets you place yourself, train a named crew, and fill a giant hangar with every kind of vehicle you can collect.

## 2. Core pillars (what makes it ours)

| Pillar | What it means in play | Different from Fallout Shelter because |
|---|---|---|
| Build down AND up | Cutaway grid that grows underground and as a tower above ground | Fallout Shelter only digs down |
| Defend the outside | Place auto turrets, walls, shield pylons on the surface around the base | Fallout Shelter has no exterior defenses |
| The Hangar | A huge room where collected planes, cars, boats, mechs, and drones are parked and shown off | Inspired by the Metal Storm hangar, minus the PvP |
| Named crew | Recruit, name, train, and assign crew to rooms | Same spirit, with clearer jobs and training paths |
| Shapeshifter aliens | Infiltrators flash a trench coat for half a second on arrival, then look human except for one tell (alien feet) | A spot the imposter mini game that is unique to us |

## 3. Rooms (first pass)

| Room | Job | Produces / Unlocks |
|---|---|---|
| Headquarters (Commander's Office) | The player's office, base level, unlocks new rooms | Base level, missions |
| Sleeping Quarters | Crew housing, raises max crew | Crew capacity, morale |
| Food Hall | Feeds the crew | Food |
| Power Core | Runs everything | Power |
| Fitness Center | Trains strength and stamina | Crew HP, carry capacity |
| Barracks | Trains defenders | Combat skill, guards |
| Tech Center | Research and upgrades | Tech points, turret upgrades |
| Hangar | Stores and repairs vehicles | Vehicle slots, expeditions |
| Elevator / Stairwell | Connects floors | Movement |

Exterior (surface layer): auto turrets, laser turrets, walls, shield pylon, radar dish, landing pad.

## 4. Threats

1. **Roaming factions**: raider crews in dune buggies that attack the surface defenses.
2. **Monsters**: big creatures that roam in from the wilds, slow but tanky.
3. **Shapeshifter aliens**: arrive as a "new recruit." Trench coat flash for about 0.5 seconds, then a normal looking person with one wrong detail (alien feet first, later other tells like glowing eyes or an extra finger). Tap to unmask and you get a reward. Miss them and they quietly sabotage a room.

## 5. Core game loop

1. Rooms produce resources over time (food, power, tech, credits).
2. Spend resources to build and upgrade rooms and turrets.
3. Assign crew to rooms that match their best stat.
4. Threat waves arrive. Turrets and guards fight. Damaged rooms need repairs.
5. Send vehicles on expeditions to find parts, new vehicles, and new crew.
6. Base level goes up, unlocking bigger rooms and better vehicles.

## 6. Visual direction

| Token | Color | Use |
|---|---|---|
| Gunmetal base | `#2B3036` to `#4A525C` gradient | Room walls, panels, UI frames |
| Metal highlight | `#8A939E` to `#C9D1D9` thin diagonal gradient | Brushed metal sheen on panels |
| Turquoise accent | `#2EC4C9` | Buttons, selection glow, holograms |
| Text | `#F4F7FA` | All text |
| Support blue | `#3A8DDE` | Secondary UI, water, info |
| Support green | `#3DDC97` | Healthy, ready, success |
| Cue yellow | `#FFC845` | Warning, low resource |
| Cue red | `#FF4D5E` | Danger, damage, enemy |

Rule: red, yellow, and green are reserved for status meaning (HP, alerts), never decoration.

Style: clean sci fi, rounded panels, soft glow on accents, friendly chunky characters (kid readable, not gritty).

## 7. Storyboard: first screens to mock

1. **Title screen**: base silhouette at dusk, turquoise logo, PLAY button.
2. **Main base view**: cutaway of the base, surface with turrets on top, floors above and below, resource bar along the top.
3. **Build menu**: bottom sheet with room cards (cost, size, what it does).
4. **Crew card**: name, portrait, stats (Strength, Smarts, Speed, Aim), assign button, rename.
5. **Hangar view**: big wide room, vehicles parked on pads, collection counter ("12 of 40").
6. **Defense mode**: zoom out to the surface, raiders approaching, turret range circles.
7. **Alien arrival moment**: new recruit at the door, trench coat flash, then the "something is off" close up on the feet.
8. **Expedition map**: send a vehicle out, timer, loot result.

## 8. Technology recommendation

**Prototype (today to one week):** a mobile web game (HTML5, using the Phaser game library or plain canvas). It runs in any phone browser, can be added to the home screen like an app, needs no app store approval, and can be shared with a link.

**About Glide:** from memory (not verified in this session), Glide is a no code builder for data driven apps backed by spreadsheets or tables. It is excellent for lists, forms, and catalogs, but it is not a game engine and is not built for animated, real time, side view gameplay. Good uses for it here: a companion "Vehicle Collection Encyclopedia" or "Crew Roster" app, or a design notebook where your son logs ideas. The core game should live in a game tool.

**Real release (later):** Unity or Godot for proper iOS and Android store builds. The prototype's design and art carry straight over.

## 9. Main considerations

1. **Scope control.** The fastest way to kill a fun game is to build everything at once. Prototype one floor of rooms, one turret type, one enemy, one alien, three vehicles.
2. **Original IP.** Fallout Shelter, Vault Boy, and Metal Storm are owned by other companies. The trench coat wink is fine as an homage, but all names, characters, and art must be our own.
3. **Kid safety if it ever ships publicly.** No chat, no ads, no data collection by default. Apps aimed at children under 13 fall under rules like COPPA in the US (verify specifics before any public launch).
4. **Monetization.** Not needed for a family project. If it ever matters, avoid loot box style mechanics in a kids' game.
5. **Art pipeline.** Start with simple shapes and emoji style placeholders. Later: AI assisted concept art, then a consistent sprite set.
6. **Save system.** The prototype saves to the phone's browser storage. Cloud saves come much later.

## 10. Time frame

| Phase | When | Result |
|---|---|---|
| 0. Questions and plan | Today | This document plus answers to the questions below |
| 1. Silly playable prototype | Today | Tap to build rooms, named crew, resources ticking, one turret, one raider wave, one alien with the trench coat flash, a hangar with 3 vehicles |
| 2. Fun pass | This week | Better art, sounds, saving, 6 to 8 rooms, 2 to 3 enemy types, expeditions, 10 vehicles |
| 3. Vertical slice | 1 to 2 months | Real art style, tutorial, progression, balanced economy |
| 4. Store release | 3 to 6+ months | Native build in Unity or Godot, testing, App Store and Google Play |

## 11. Ideation questions for you and your son

**Story**
1. Where is the base? (Desert, ocean floor, a mountain, the Moon, a floating city?)
2. Who is the Commander, and why are they building this base?
3. What do the aliens actually want? Are any of them friendly?
4. Who are the roaming factions, and do they have a name and a look?

**Gameplay**
5. Should the player ever leave the base, like driving a vehicle on a mission, or is it all base view?
6. What is the coolest vehicle in the hangar, the one you would save for?
7. What happens when an alien is caught? Jail cell, kicked out, or can they be turned into a crew member?
8. Should crew level up into classes (Pilot, Engineer, Soldier, Scientist)?

**Visual and fun**
9. What are three other alien tells besides the feet? (Tail, glowing eyes, antenna under a hat?)
10. Should crew have funny animations, like dancing in the fitness center?
11. Day and night cycle, with attacks mostly at night?
12. What is the game called?
