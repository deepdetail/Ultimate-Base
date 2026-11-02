# Missing assets (November 2)

Every picture the game still draws in code, borrows from something else, or does not have yet, and what makes it. Checked against the game code (build ebd3438) and a Drive search on November 2.

## 1. Fixed November 2: enemies that showed as the Raider

Five enemies had no picture of their own, so battles showed the Raider instead (Raid Level 1, Phoenix's 4 Girl Thieves and 4 crows, showed as 8 Raiders). Their paintings were already in Drive (the October 20 monster art) and are now in the game.

| Enemy | Now uses | From Drive |
|---|---|---|
| Girl Thief | Her own painting | "Stealthy Purple-Hooded Rogue Operative.png" |
| Coyote | Its own painting | "Stalking Coyote on Green Screen.png" |
| Raven, and the Crow | The raven painting | "Iridescent Raven in Flight.png" |
| Black Bear, and the Mutant Bear, Bear Rider and Yeti | The black bear painting | "Grumpy Black Bear on Green Background.png" |
| Soldier | The Merc painting, recolored olive | The Merc already uses "enemy_l3_merc_ops_01.png", so a soldier of its own is still worth painting |
| Female Raider (new) | Every other Raider in a group | "Post-Apocalyptic Desert Mercenary.png" (the enemy_l1_raider_f_01 picture from `MONSTER_RUN.md`) |

These borrow another enemy's picture, tinted:

| Enemy | Borrows | Status |
|---|---|---|
| Superbear | Giant Grizzly, gold glow | Low priority |
| Radioactive Crocodile | Glow Gator, green glow | Low priority |
| Dinosaur | T. rex | Low priority |
| Dragon Rider | Dragon, with the Merc as rider | Low priority |

Still worth painting: a Soldier of its own (it borrows the Merc, recolored).

## 2. Paintings waiting on a Chrome run

| Run | What it makes | Pictures | Saves to (Drive) | Status |
|---|---|---|---|---|
| `CHROME_WORLD_RUN.md` | Moab base backdrop, Sierras raid backdrop, mission skies, mission cards, the underground, Raider Buggy and Dirt Bike | 15 | BASED Art/World, BASED Art/Vehicles2 | Not run |
| `CHROME_ROOMS_LAYERED_RUN.md` | Every room built from layers: shells, era furniture, level items, hangar, stairs, elevator | 263 | BASED Art/Rooms2 | Not run |
| `CHROME_EXTERIOR_RUN.md` | One base front per Level, 1 to 60 | 60 | BASED Art/Exteriors2 | Not run |
| `CHROME_ROOMS_V2_RUN.md`, vehicles section only | Side views of 20 vehicles (only the Cybertruck has a painting now) | 20 | BASED Art/Vehicles2 | Not run |
| Recruit sheets | The Sprinter girl in the merc outfit (every other recruit outfit is in) | 1 | BASED Art 2.0 | Missing |

## 3. Not in any run yet (needs a request written)

| Asset | Why | Shows now |
|---|---|---|
| Rail Gun and Plasma Cannon turrets | 6 of the 8 turrets are painted | Drawn turret shapes |
| Lab Coat and Suit outfit icons | 4 of the 6 outfits have icons | Drawn icon |
| Base fronts for Levels 61 to 100 | The exterior run covers Levels 1 to 60 | The era painting |
| Distinct art for the tinted enemies above | They borrow another enemy | Tinted stand-in |

## 4. Made earlier, but not in the game yet (find in Drive, then wire)

| Asset | Where it is | Shows now |
|---|---|---|
| Ninja Stars shop icon | Downloaded with the October 31 weapon art (shop_shuriken.png) | Drawn icon |
| Pets: dog, cat, fox, hawk, wolf, crow, dragon | `PET_RUN.md`; Drive not checked | Emoji |
| Cockpits for the other aircraft and the cars | `COCKPIT_RUN.md`; Drive not checked | Drawn cockpit frame (only the Cessna and L-39 are painted) |
| Icons and home emblems | `ICON_RUN_CHROME.md` (88 icons); Drive not checked | Drawn vector icons |
| Great White Shark, two neon bears | Drive, October 20 monster art | Not used yet: the shark suits Bahamas ocean raids |

## 5. Maps for missions: traveling from Moab

| Map | Covers | Made from | Status |
|---|---|---|---|
| Moab to Las Vegas | 8 towns: Green River to Las Vegas | Real elevation, lakes and state lines | Done (ebd3438) |
| Lake Tahoe to Las Vegas | 6 towns across Nevada | Same | Done, used by Sierras bases |
| Las Vegas to the Sierras, for Moab bases | The Nevada towns in reverse, ending at Lake Tahoe | Reuses the Tahoe map | To build |
| Moab to the Bahamas | Long-range hops across the southern states to Nassau | A new relief map from the same real data | To build |
| Sky Vegas | The floating city above Las Vegas | Needs a design and painted art | Later |
| 3D mission terrain | The Sierras and Moab exist; the Bahamas and Las Vegas do not | Real elevation data | Later |

## 6. Known art bugs

- Moab missions show a big teal lake around town where the Colorado River should be a thin ribbon. This comes from the mission terrain data.
- The Fortress Tech and Sky Citadel fronts are cut off at the top. They fade there as a patch until the exterior run lands.
- Some recruits are stand-ins that reuse Legendary faces.
- The clone sheets are in, but the game does not use them yet.
