# BASED: Art Brief for Image Generation

Hand this whole file to ChatGPT (or any image generator). Goal: replace the game's hand-drawn vector art with real illustrated anime art that drops straight into the game.

## 1. The game in one paragraph
BASED is a kid-friendly (age 9+) mobile base builder, side view like Fallout Shelter or SimTower, set 500 years in the future at real places: the Moab desert (red rock arches) and Lake Tahoe and Truckee (pine forest, snowy mountains). You build rooms above and below ground, recruit an anime ninja crew, defend against raiders with turrets, and fly real vehicles on missions. Combat is non-lethal (stun, knockout, heal). Tone: adventurous and cool, never gory or dystopian.

## 2. Style rules (apply to every image)
- Realistic anime: grounded, adult proportions (about 7.5 heads tall), sharp eyes, clean cel shading with one soft highlight. Think modern anime films and premium mobile games, not chibi or cartoon.
- Lighting from the upper left on everything, so assets match when combined.
- Palette accents: gunmetal gray, teal or turquoise (#2FD4D9), white. Enemies lean rust orange and red.
- No text, logos, watermarks or real brand marks inside the images.
- Transparent background (PNG) unless the item says "backdrop".
- Side view facing RIGHT for characters, enemies and vehicles (the game flips them when needed).

## 3. Do this first: one style sheet
Before the full list, generate ONE character style sheet (the Commander, three poses) and approve it. Then reuse that image as the reference for every later prompt so the whole set looks like one artist made it. Consistency is the hardest part, so lock it early.

## 4. Asset list

### A. Crew characters (highest priority)
Full body, standing, facing right, empty right hand at hip height (weapons get added separately), 512 x 1024 px.
- 3 physiques: Novice (slim), Intermediate (athletic), Advanced (muscular).
- 6 outfits: Base Jumpsuit, Ninja Gi, Flight Suit, Lab Coat, Tactical Gear, Business Suit.
- Mix of skin tones, hair styles and genders across the set.
- Start with 6 characters (one per outfit, mixed physiques), then expand.
- Plus a head and shoulders portrait of each, 512 x 512, for the avatar and crew card.

### B. Clones (the shapeshifter bad guys)
Same as a crew member, plus a long tan trench coat and green bare feet (their giveaway). 2 to 3 variants, 512 x 1024.

### C. Weapons (separate, so any character can hold any weapon)
Side view, pointing right, 512 x 256: Slingshot, BB Gun, Kunai, Bow, Bo Staff, Handgun, Katana, Rifle, Assault Rifle, Machine Gun, Laser Rifle, Plasma Blaster, Rail Gun. Futuristic but toy-safe looking (stun tech, glowing blue or teal).

### D. Armor (overlay vests)
Front of torso, 512 x 512: Padded Vest, Kevlar, Plate, Power Armor, Nano Suit.

### E. Enemies and bosses
Side view facing right, 1024 x 768:
- Dune Buggy raider, Dirt Bike raider, Scorpion Tank (desert), Yeti (mountain), Junk Drone.
- Bosses (bigger, 1536 x 1024): Badlands Warlord Rig (desert), Ancient Snow Titan (mountain).
- Factions: Badlands Gang, Clone Syndicate, Raider Kings. Menacing but not scary-scary.

### F. Vehicles
Side profile facing right, 1024 x 512, realistic but with a light anime finish: Cessna 182, Aero L-39, Huey helicopter, F-16, MiG-29, F/A-18, F-22, Hover Bike, Rocket, Mustang, Cybertruck, Ferrari, Tank, Mech, Speedboat. (Real vehicles are fine; avoid visible manufacturer logos.)

### G. Room interiors (backdrops, no people)
Front-facing cutaway room, 1024 x 768, empty floor space in the middle for characters to stand: HQ, Sleeping Quarters, Food Hall, Power Core, Fitness Dojo, Barracks, Tech Lab, Hangar. Bonus: a "Level 5 luxury" version of each.

### H. Building exterior (the ground floor lobby), backdrop, 2048 x 1024
One facade per era, same camera angle, with an entrance door in the center: Minimalist Brutalist (concrete bunker), Futuristic, Vintage (neon), Antique (stone and brass), Ultra Modern (glass and teal), Luxury, Brutalist Billionaire (concrete, gold, helipad).

### I. Turrets
Boxy and realistic, 512 x 512, facing right: Machine Gun, Autocannon, Net Launcher, Gatling, Laser, Missile, Rail Gun, Plasma.

### J. World backdrops, 2048 x 1024
Painted panoramic sky and landscape: Moab desert with arches, and Lake Tahoe with pines and snowy peaks.

## 5. File naming (so they drop straight into the game)
Lowercase, no spaces: `char_gi_advanced_01.png`, `portrait_gi_advanced_01.png`, `clone_01.png`, `wpn_katana.png`, `armor_kevlar.png`, `enemy_buggy.png`, `boss_titan.png`, `veh_f22.png`, `room_hq.png`, `room_hq_lux.png`, `lobby_billion.png`, `tur_laser.png`, `bg_moab.png`.

## 6. Prompt template (copy, fill the brackets)
> Realistic anime game asset, [SUBJECT], side view facing right, full body, clean cel shading, light from the upper left, gunmetal gray and teal accents, kid-friendly futuristic adventure, transparent background, no text, no logo, matching the style of the attached reference sheet. Size [W x H].

## 7. Hand-back
Put the finished PNGs in the shared Drive folder `BASED Art`, using the names above. Claude will pull them into the game, swap out the vector art, and keep the vector art as a fallback for anything missing.

## 8. Priority order
1. Style sheet. 2. Crew (A) and portraits. 3. Enemies and bosses (E). 4. Lobby facades (H). 5. Rooms (G). 6. Weapons and armor (C, D). 7. Vehicles (F). 8. Turrets (I). 9. Backdrops (J).
