# BASED Commander: rooms, hangar, vehicles and battles, the plan

The design for the next round of updates, from the November 2 brief. The art for it comes from `CHROME_ROOMS_V2_RUN.md`.

## 1. Room sizes

Rooms are a grid of cells, written height x width.

| Size | Rule |
|---|---|
| 1x1, 1x2, 1x3, 1x4 | one floor tall; 4 wide is the maximum |
| 2x2, 2x3, 2x4 | two floors tall; needs at least 2 wide |
| 3x4 | three floors tall; needs the full 4 wide |
| Hangar 2x4, 2x6, 2x8 | special: lives beside the base, see section 4 |

Each room's picture changes with its size (by shape) and with its Level (1, 3, 5):

| Room | Sizes it can grow to | Shapes painted |
|---|---|---|
| Headquarters | 1x1 to 3x4 | square, long, tall, grand |
| Sleeping Quarters | 1x1 to 2x4 | square, long, tall |
| Food Hall | 1x1 to 2x4 | square, long, tall |
| Power Core | 1x1 to 3x4 | square, long, tall, grand |
| Tech Center | 1x1 to 3x4 | square, long, tall, grand |
| Fitness Dojo | 1x1 to 2x4 | square, long, tall |
| Armory | 1x1 to 2x4 | square, long, tall |
| Barracks | 1x1 to 2x4 | square, long, tall |
| Med Bay | 1x1 to 2x4 | square, long, tall |
| Holding Cell | 1x1 to 1x4 | square, long |
| Clone Lab | 1x1 to 2x4 | square, long, tall |
| Hangar | 2x4, 2x6, 2x8 | one wide picture per size |
| Stairs, Elevator | one cell per floor | stacked sections |

## 2. What upgrades in each room (Level 1, then 3, then 5)

| Room | Level 1 | Level 3 | Level 5 |
|---|---|---|---|
| Headquarters | folding desk, one screen, paper map, desk lamp | steel command desk, three monitors, lit map with pins | holographic war table, curved screen wall, leather chair, bronze Commander statue |
| Sleeping Quarters | metal bunks, gray blankets, dented lockers, bare bulb | neat bunks, reading lights, footlockers, rug, framed photos | sleep pods, plants, big painting, marble statue, Lake Tahoe window screen |
| Food Hall | camp stove, crates of cans, metal table and benches | kitchen counter, big fridge, hanging pots, serving window | food printers, vegetable wall garden, booths, chef robot |
| Power Core | generator, fuel drums, tangled cables | battery cabinets, caged energy cell, cable trays | giant fusion core with spinning energy rings |
| Tech Center | workbench, old computers, soldering station | lab benches, microscopes, 3D printer, server rack, half-built drone | holo screens, robot arms, quantum computer, energy rifle and small mech suit on display |
| Fitness Dojo | punching bag, weight bench, worn mats | dojo mats, wooden dummy, pull-up bars, mirror wall | holographic sparring targets, smart weights, climbing wall |
| Armory | practice rack, simple workbench, crate of vests | stun blaster racks, armor stands, forge and vise bench | weapon and armor display cases, robotic assembly arm, holo blueprints |
| Barracks | sandbag wall, practice target, cots, supply crates | practice lane, pop-up targets, gear lockers | holographic range, armor lockers, tactical map table |
| Med Bay | cot, first aid kits, curtain | two clean beds, monitors, supply cabinet | healing pods, robotic helper arm, floating readouts |
| Holding Cell | chain-link cage, bench, lamp | steel cell, two cots, guard desk | force-field bars, comfy cots, wall screen |
| Clone Lab | two bubbling tanks, cables, bench | row of clone pods, DNA scanner, console | tall glowing pods, holographic DNA helix, robot arms |
| Hangar | bare concrete, simple tools | lift, fuel pump, clean bays | landing lights, robotic gantry arms, polished floor |

## 3. Room production (new)

- **Armory makes weapons.** Every cycle (about 40 minutes at Level 1, down to 15 at Level 5) it adds one weapon to the Arsenal, picked from the tiers its Level allows. It stops when storage is full. Armorers working there speed it up.
- **Tech Center makes advanced gear.** From Level 3, a research cycle (about 2 hours, faster with scientists) awards an energy weapon: laser, plasma or rail. At Level 5 it can also finish a small mech or a turret upgrade.
- **Small vehicles.** At Level 3 or higher, the Armory and the Hangar together slowly build small vehicles (a dirt bike, a buggy, a drone) when a bay is free.

## 4. The hangar and vehicles

- **Where it lives:** on the ground floor at the far right of the base, outside the main tower, so it never splits the rooms. Later it can move underground, next to the base center on the right, with a vault hatch on the surface.
- **Sizes and capacity:**
  - 2x4 holds 1 plane and 2 cars (the starting size).
  - 2x6 holds 2 planes and 3 cars.
  - 2x8 holds 4 planes and 4 cars (the maximum).
- **True scale:** every parked vehicle shows in its bay. A plane is about 3 cells long, a car about 1.5.
- **Condition:** each vehicle has a condition from Wrecked to Mint:
  - Vehicles captured from raiders arrive Wrecked to Worn.
  - Parked in the hangar, they repair over time, faster at higher hangar Levels and with pilots or engineers assigned.
  - Condition affects mission speed and armor.
  - Repair unlocks at Hangar Level 2. Upgrades for speed, armor and weapons unlock at Level 4, using the existing upgrade system.
- **Departure:** when a mission launches, the selected plane taxis out of the hangar door and climbs away, or the car drives out and off screen, then the mission starts.
- **Vehicle art:** all 20 vehicles get one new side view in the house style, because 9 have no picture yet:
  - airship, cybertruck, armored SUV, two Lamborghinis, tank, mech, speedboat, submarine
- **Brand names:** the run asks for original designs with no badges. Real brand names and likenesses (Ferrari, Lamborghini, Ford, F-16) are worth replacing with made-up names before the App Store, since some brands enforce trademarks against games. I'm reasoning from general knowledge here, not legal advice.

## 5. Moving around the base (new)

- **Stairs:** every floor gets free stairs at the far right inside the base.
- **Elevator:** a buildable shaft. The basic one is cheap. Upgrades make it faster (Level 3) and wider, with two cars (Level 5).
- **Travel time:** crew moving between floors take time based on floors climbed, divided by stairs or elevator speed.

## 6. Battles

**How it works today (from the code):**
- **Barracks crew** are defenders. They shoot from the turret posts on the roofline in every battle, with damage from Aim and their weapon.
- **Guards** (crew stationed outside) fight at the front door.
- **Lobby crew** also shoot, from inside the lobby.

**The change:**
- **Guards** stationed outside fight from the first round.
- **Barracks crew** join after a travel time: the distance from the Barracks to the ground floor, at stairs or elevator speed. A Barracks near the ground floor, or a fast elevator, gets them into the fight sooner.

**Breaching (new, both directions, room by room like Fallout Shelter):**
- **Defending:** if raiders or monsters beat the outside defenses, they break in on the ground floor and fight the crew room by room. Crew in each room defend it.
- **Attacking:** after your squad beats an enemy base's outside, they can choose to go in. Each room is a fight, then a treasure find (cash, gear, tech, a rare recruit), and they can keep pushing deeper or pull out.

## 7. Big updates after this

- **Flight missions:** turn the phone sideways, with arcade flying in the spirit of Metal Storm.
- **Driving missions:** Forza-style chase-camera driving.
- **Excursions:** also in landscape.

## Suggested order

1. Art: the room, hangar and vehicle run (`CHROME_ROOMS_V2_RUN.md`, 140 images over several days). Code can start before the art lands.
2. Code, part 1: room sizes up to 4 wide and 3 high, stairs and elevator, hangar outside the base, vehicle condition and repair. Wire the room art as it arrives.
3. Code, part 2: Armory, Tech Center and Hangar production; barracks travel time in battles.
4. Code, part 3: breaching (defending, then raiding enemy bases).
5. Code, part 4: the landscape flight and driving missions.

Each code part is about one working session.
