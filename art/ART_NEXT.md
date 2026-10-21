# BASED: Next Art Assets (batch 3)

Hand this to ChatGPT with the two approved style sheets attached (art/reference). Same rules as before. Paste the STYLE LOCK once per chat, then one prompt per message, and start a fresh chat every 8 images.

## STYLE LOCK (paste first)
> These two character sheets are the approved art style for my kids' mobile game BASED (age 9+, year 2526, real places: Lake Tahoe and Moab). Keep this exact style: realistic anime, detailed cel shading, light from the upper left, gunmetal gray, white and teal (#2FD4D9) accents. Rules: no text, no logos, no watermarks, no borders, no panels, one subject per image. Use the background I name in each prompt: SOLID GREEN #00FF00, SOLID MAGENTA #FF00FF, or FULL SCENE (painted all the way to the edges). Kid-friendly: nothing gory or scary-scary.

## Background key
- **GREEN** = cut-out objects that have no green in them.
- **MAGENTA** = cut-out objects that are green, or have green parts (plants, clone tech, green glow).
- **FULL SCENE** = backdrops that fill the whole frame (room interiors, skies).

---

## 1. Room interiors (highest priority, FULL SCENE, 1536 x 1024)
A straight-on cutaway of the room like a dollhouse: back wall, side walls angled in slightly, floor and ceiling visible. Keep the bottom third mostly clear floor so characters can stand there. No people.

Make each room in two looks first: **L1 (basic, just built)** and **L5 (fully upgraded, luxury future tech)**. Add L3 later if it looks good.

| File | Room | L1 idea | L5 idea |
|---|---|---|---|
| room_hq_l1 / _l5 | Headquarters | Folding desk, one screen, map pinned to concrete | Holo war table, wall of screens, leather chair |
| room_quarters_l1 / _l5 | Sleeping Quarters | Metal bunk beds, lockers | Pod beds with soft light, plants, a window screen of Lake Tahoe |
| room_food_l1 / _l5 | Food Hall | Camp stove, crates of cans, one table | Chef's kitchen, hydroponic herb wall, long table |
| room_power_l1 / _l5 | Power Core | Generator with cables, fuel drums | Glowing teal fusion core in a glass column |
| room_fitness_l1 / _l5 | Dojo / Fitness | Punching bag, mats, rope | Wooden dojo floor, weapon racks, training droids |
| room_barracks_l1 / _l5 | Barracks | Sandbags, gear lockers, a sign-in board | Armory wall, armor stands, briefing screen |
| room_tech_l1 / _l5 | Tech Lab | Workbench, spare parts, soldering station | Clean lab, robot arm, holographic schematics |
| room_hangar_l1 / _l5 | Hangar | Concrete bay, tool cart, painted lines | Polished floor, light rig, vehicle lift |
| room_school_l1 / _l5 | **NEW** Academy (for trivia and lessons) | Chalkboard, a few desks, a globe | Holo classroom, flight simulator seat, star map |
| room_jail_l1 / _l5 | **NEW** Clone Lockup | Simple bars, a cot | Glowing force-field cells, cure lab station |

## 2. Building exterior by era (MAGENTA, 2048 x 1024)
The ground-floor front of the base, centered, with a big entrance door in the middle, standing on a strip of ground. The sky must be MAGENTA so the game's sky shows through.

| File | Era (unlock level) |
|---|---|
| lobby_brutal | Minimalist Brutalist (1): concrete bunker dome, one door |
| lobby_futur | Standard Futuristic (10): white panels, teal light strips |
| lobby_vintage | Vintage Mid-Century (20): neon sign frame, chrome, pastel paint |
| lobby_antique | Antique Grand (35): stone columns, brass, arched windows |
| lobby_modern | Ultra Modern (50): glass tower base, steel fins |
| lobby_luxe | Luxury Futuristic (70): floating glass, gardens, gold trim |
| lobby_billion | Brutalist Billionaire (85): huge concrete and gold, helipad, waterfall |

Also one rooftop cap per era (MAGENTA, 2048 x 512), named `roof_<era>`.

## 3. Turrets (MAGENTA, 768 x 768, side view facing right, on a short mount)
turret_mg (machine gun), turret_auto (autocannon), turret_net (net launcher), turret_gatling, turret_laser, turret_missile, turret_rail, turret_plasma. Boxy, realistic, sci-fi. Make a plain version first; gold upgraded versions can come later.

## 4. World backdrops (FULL SCENE, 2048 x 1024, no buildings, horizon at about 40 percent height)
bg_tahoe_day, bg_tahoe_night, bg_moab_day, bg_moab_night. Painted panorama skies and landscapes that will sit behind the base.

## 5. Icons and badges (GREEN, 512 x 512, centered, simple and readable when tiny)
- **Resources:** icon_cash, icon_food, icon_power, icon_tech, icon_adventure (a star token).
- **Results:** badge_victory (trophy), badge_defeat (dizzy stars), badge_levelup, badge_clone_caught.
- **Faction emblems:** fac_nus (New United States), fac_icr (Independent California Republic), fac_atlantis, fac_skyvegas, fac_badlands, fac_clones, fac_raiderkings. These are original symbols, not real flags.
- **Gear:** wpn_slingshot, wpn_bb, wpn_kunai, wpn_bow, wpn_staff, wpn_handgun, wpn_katana, wpn_rifle, wpn_assault, wpn_mg, wpn_laser, wpn_plasma, wpn_rail (all toy-safe stun tech), armor_padded, armor_kevlar, armor_plate, armor_power, armor_nano, outfit_jumpsuit, outfit_gi, outfit_flight, outfit_labcoat, outfit_tactical, outfit_suit.

## 6. Enemy bases to raid (FULL SCENE, 1024 x 640, a distant view of the camp)
ebase_badlands_camp, ebase_badlands_outpost, ebase_clone_lab, ebase_raider_fortress, ebase_warlord_citadel.

## 7. Mission landmark cards (FULL SCENE, 1024 x 640, scenic view, used on mission and recon screens)
- **Tahoe:** card_emerald_bay, card_sand_harbor, card_tahoe_city, card_truckee, card_south_lake.
- **Moab:** card_delicate_arch, card_balanced_rock, card_fiery_furnace, card_slickrock, card_colorado_river.

## 8. Academy and lessons
- **Teacher (GREEN, full body like the crew):** char_teacher_01. A friendly older flight instructor with a headset around the neck and a tablet in one hand.
- **Lesson cards (FULL SCENE, 1024 x 640):** lesson_how_wings_lift, lesson_reading_a_map, lesson_weather_and_clouds, lesson_lake_tahoe_facts, lesson_arches_rock_science, lesson_engines_101.

## 9. Screens (FULL SCENE)
- splash_based (1024 x 1536 portrait): the Commander standing in front of the base at sunset. Leave room at the top for the logo (no text).
- app_icon (1024 x 1024): the Commander's head and shoulders on teal, bold and simple.

## Still open from earlier lists
- **Enemies (MONSTER_RUN):** enemy_l1_raider_f, enemy_l1_thief_f, the five level 2 animals, and the T. rex.
- **Vehicles (VEHICLE_RUN):** 16 left. The Cybertruck is done.
- **Crew variety (CREW_VARIETY_RUN):** 5 lineups.

## Priority order
1. Room interiors L1 and L5. 2. Lobby eras. 3. Turrets. 4. Vehicles. 5. Icons and badges. 6. Academy. 7. Backdrops. 8. Enemy bases and landmark cards. 9. Splash and icon.

Save into the Drive folder `BASED Art` with these exact file names. Put any subfolder in the right place: Rooms, Exteriors, Turrets, Vehicles, Enemies, Icons, Academy or Screens.
