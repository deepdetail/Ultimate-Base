# Mission 3D roster: bad guys, targets and structures

The game already has stand-in versions of most of these, built in code from simple shapes. Each 3D model you make replaces one stand-in, or adds something new. Everything stays kid-friendly: toy-safe stun tech, robots and drones instead of people, and things that pop, fizzle or fall apart instead of anything gory. No real brand names or logos.

## How to hand a model over (so it drops straight in)
- **File:** one GLB per model, named like the "file" column below (for example `enemy_drone_scout.glb`). Put them in Drive, in BASED Art/3D/Enemies.
- **Scale and direction:** real size in meters, Y up, the front facing -Z (forward), and the origin on the ground under the model (for things that stand) or at its middle (for things that fly).
- **Moving parts:** separate, named pieces, with their pivot where they turn: `rotor_1` to `rotor_4`, `leg_L` and `leg_R`, `arm_L` and `arm_R`, `turret`, `barrel`, `wheel_*`, `dish`. The game spins and swings them.
- **Size budget (triangles):** small bad guys 2,000 to 6,000; trucks, jets and big targets 6,000 to 15,000; bosses up to 40,000; small props under 1,500. Textures 1024 x 1024 (2048 for bosses), as PBR (color, roughness, metal) or flat colors that the game's cartoon shading can use.
- **Style:** the game's comic style, but realistic: believable shapes and materials, clean panel lines, chunky readable silhouettes. Badlands Gang colors are rust orange, gunmetal and red lights; Sky Vegas is gold, white and neon teal.

## Air bad guys (by challenge)
| Name | File | What it does | Hits | Size | Moving parts | Challenge |
|---|---|---|---|---|---|---|
| Scout drone | `enemy_drone_scout.glb` | Pops up from the trees ahead, drifts toward your path, never chases. In the game now (stand-in). | 1 | 4 m across | rotor_1 to rotor_4, a red camera eye | Rookie |
| Armored drone | `enemy_drone_armored.glb` | Like the scout, with red armor; shoots slow orange orbs. In the game now (stand-in). | 2 | 4.5 m | rotors, a small gun pod | Pilot |
| Balloon carrier | `enemy_balloon.glb` | A striped supply balloon floating on your path. Pop it by shooting or flying through. In the game now (stand-in). | 1 | 10 m tall | basket swings | All |
| Raider jet | `enemy_jet_raider.glb` | Comes at you head-on in pairs, then turns around and chases. In the game now (it borrows the MiG model). | 2 | 15 m | flaps, a glowing engine | Ace |
| Drone carrier | `enemy_carrier.glb` | A slow flying wing that drops scout drones every few seconds. Knock out its two engine pods to bring it down. | 3 per pod | 30 m wingspan | engine pods, drop doors | Ace |
| Kite gliders | `enemy_kite.glb` | Cheap paper and stick gliders the gang launches in swarms of five. Fragile, fun to sweep up. | 1 | 3 m | none | Pilot |

## Ground bad guys (along the road)
| Name | File | What it does | Hits | Size | Moving parts | Challenge |
|---|---|---|---|---|---|---|
| Road bot | `enemy_bot_road.glb` | Small two-legged robot that walks into the road and waves. Bonk it with your car or shoot it. In the game now (stand-in). | 1 to 2 | 2 m tall | leg_L, leg_R, arm_L, arm_R, head | Rookie |
| Hover drone (low) | uses the scout drone | Hovers over the road ahead. In the game now. | 1 | 4 m | rotors | Rookie |
| Robo coyote | `enemy_robo_coyote.glb` | A four-legged robot coyote that runs along the shoulder, then darts across. | 1 | 1.5 m long | four legs, tail, jaw | Pilot |
| Raider truck | `enemy_truck_raider.glb` | Rusty armored pickup. Drives at you in the other lane (Pilot), chases from behind (Ace). In the game now (it borrows the Cybertruck model). | 3 | 6 m | wheel_* | Pilot, Ace |
| Spike roller | `enemy_roller.glb` | A rolling barrel bot with stubby spikes that rolls down hills onto the road. | 2 | 2 m | the whole body spins | Ace |
| Titan walker | `enemy_titan.glb` | The gang's own walker guarding the outpost gate (Phoenix's Titan Mech idea, an original design). Steps slowly, stomps, shoots orb volleys. Knock out its knee joints, then its head. | 4 per knee | 12 m tall | leg_L, leg_R, knee joints, torso turret, head | Boss (ground) |

## Sea bad guys
| Name | File | What it does | Hits | Size | Moving parts | Challenge |
|---|---|---|---|---|---|---|
| Floating mine | `enemy_mine.glb` | Bobbing spiky ball with a red light, in rows across the lane. In the game now (stand-in). | 1 | 2 m | bob, light blinks | Rookie |
| Jet ski bot | `enemy_jetski.glb` | A robot on a jet ski that zigzags across your bow. | 2 | 3 m | rider arms, spray | Pilot |
| Harbor turret buoy | `enemy_buoy_turret.glb` | A buoy with a small orb turret that turns to track you. | 3 | 4 m | turret, barrel | Ace |

## Targets and structures (outposts and checkpoints)
| Name | File | What it is | Hits | Size | Moving parts |
|---|---|---|---|---|---|
| Gang radar | `target_radar.glb` | The outpost radar dish the strike missions knock out. The waypoint boxes dive right at it. In the game now (stand-in). | 4 | 12 m tall | dish turns |
| Road block | `target_roadblock.glb` | Striped barrier with crates and tires. Shoot it or smash through. In the game now (stand-in). | 3 | 6 m wide | none |
| Gang camp | `target_camp.glb` | Three tents, a flag and a fire pit: what recon missions photograph. In the game now (stand-in). | (photo) | 25 m across | flag waves |
| Outpost buildings | `outpost_set.glb` | Scrap metal huts, a watchtower and a fuel tank, as one set placed at the end of each course. In the game now as plain boxes. | none | 50 m across | watchtower light |
| Comms tower | `target_comms.glb` | A tall lattice tower with blinking lights on a hilltop. Bonus target. | 4 | 30 m tall | lights blink |
| Orb turret | `target_turret.glb` | A ground turret that lobs slow orbs at planes. Bonus target. | 3 | 4 m | turret, barrel |
| Fuel depot | `target_fuel.glb` | Two round tanks and pipes; makes a big blast. Bonus target. | 3 | 15 m | none |
| Drone hive | `target_hive.glb` | A boxy launcher that sends up scout drones until it's knocked out. | 5 | 8 m | hatch doors |
| Checkpoint gate | `gate_checkpoint.glb` | A friendly arch for road checkpoints (teal lights, a scoreboard with no words). | none | 22 m wide | lights chase |

## Obstacles and scenery that make courses fun
| Name | File | What it is |
|---|---|---|
| Rock arch | `prop_rock_arch.glb` | A natural red-rock arch in Moab that the waypoint boxes fly you through. |
| Cable line | `prop_cable.glb` | Power cables strung across a canyon; fly under them for bonus points. |
| Wind turbine | `prop_turbine.glb` | Sierras hilltop turbines with turning blades to weave between. |
| Billboard | `prop_billboard.glb` | Sky Vegas neon billboards (pictures only, no words) along the Vegas run. |
| Floating platform | `prop_platform.glb` | Sky Vegas sky platforms the lane weaves between. |
| Pine and rock sets | `prop_sierras_set.glb` | A few pine and boulder shapes to swap for the game's simple trees near the course. |

## One boss per region (for the last mission of each region)
| Region | Boss | File | The fight |
|---|---|---|---|
| Sierras and Lake Tahoe | Thunder Barge | `boss_barge.glb` | A huge hovering barge over the lake with four orb turrets and a drone hive. Knock out the turrets, then the core. |
| Moab | Dust Crawler | `boss_crawler.glb` | A giant tracked mining crawler in the canyon (an original design). Its scoops dig up rocks it throws. Hit the glowing vents. |
| Las Vegas and Sky Vegas | Neon Ringmaster | `boss_ringmaster.glb` | A flying casino-blimp robot that spins rings of orbs. Fly through the gaps, hit its eyes. |
| Atlantis | Iron Squid | `boss_squid.glb` | A robot squid under the waves with tentacle turrets. Mines and bubbles as hazards. |

## What to make first (biggest win for the least work)
1. Scout drone and armored drone (they're in every flight).
2. Gang radar and outpost buildings (every strike mission ends there).
3. Raider truck and road bot (every drive).
4. Floating mine (every boat run).
5. Titan walker (Phoenix's mech, and it fits the enemy bases).

When models land in Drive, ask Claude to wire them in: it swaps each stand-in for the GLB, hooks up the moving parts, and checks it in a mission on a phone-sized screen.
