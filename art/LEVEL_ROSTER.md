# BASED Commander: Level Roster
<!-- Transcribed from J's handwritten notes, 2026-10-22 -->

## Levels
- L1 (Mission: Base Raid): Female Thief + Crow
- L2: Male Thief + Coyote
- L3: Raiders with pistols
- L4: Bears + Skunk
- L5: Alligator + Soldiers with rifles
- L6: Mutant Bear
- L7: L1 + L3 x2 (Female Thief + Crow, plus Raiders with pistols x2)
- L8: Radioactive Crocodile
- L9: Superbear
- L10: Raider riding Bear + Female Thief with Crow + Skunk
- L11: Dinosaur
- L12: Clone Bears x2 + Superbear
- L13: Dragon
- L14: Mercenary riding Dragon

## Enemy types (derived from levels, 16 total)
- Humans: Female Thief, Male Thief, Raider (pistol), Soldier (rifle), Mercenary
- Animals: Crow, Coyote, Skunk, Bear, Alligator
- Powered-up animals: Mutant Bear, Clone Bear, Superbear, Radioactive Crocodile
- Giants: Dinosaur, Dragon

## Mounts (rider mechanic)
- L10: Raider rides Bear
- L14: Mercenary rides Dragon

## Open questions
- Group sizes for Raiders (L3, L7), Bears (L4), Soldiers (L5)
- "Mission: Base Raid": L1 name or game-wide mission type?
- Clone Bears (L12): copies of Superbear or their own type?

## How the game uses it (shipped 22 October)
- Each base level sends its roster group first (`ROSTER` in prototype/based.html). Hard and Extreme raids add earlier groups behind it. Past level 14, the lead group is picked from levels 8 to 14 and more groups join every 6 levels.
- Group sizes: Raiders x2 at L3 (confirmed by J, 23 October), so L7 has four raiders (the L3 group twice). Bears x2 at L4. Soldiers x2 at L5.
- Weapons (updated 23 October): Female Thief and Male Thief carry sniper rifles, Raider an M4A1 style carbine, Soldier a rifle, Mercenary a machine gun. Animals and giants have none.
- Art stand-ins until painted art exists: Soldier uses the raider picture with a rifle. Mutant Bear is the black bear tinted green. Superbear is the giant grizzly with a gold glow. Radioactive Crocodile is the glow gator with a green glow. Dinosaur is the T. rex. Clone Bears use their own clone bear art.
- Giants (Dinosaur, Dragon, Mercenary on Dragon, Superbear) start weaker when they show up early and reach full strength around level 30.

## Phoenix's counts (28 October, shipped)
- L1: 4 Female Thieves + 4 Crows
- L2: 4 Male Thieves + 4 Coyotes
- L3: 5 Raiders with pistols
- L4: 2 Bears + 3 Skunks
- L5: 2 Alligators + 3 Soldiers with rifles
- L6: 4 Mutant Bears
- L7: 2 Dinosaurs
- L8: 4 Radioactive Crocodiles + 2 Crows
- L9: 4 Superbears + 2 Crows
- L10: 2 Raiders riding Bears + 4 Female Thieves + 4 Crows + 2 Skunks
- L11: 4 Dinosaurs
- L12: 2 Clone Bears + 4 Superbears
- L13: 2 Dragons
- L14: 4 Mercenaries riding Dragons
Balance: in big groups each member is a bit weaker (8 of one kind are about 3.5 times as tough as 1, not 8), and giants that appear early start weaker. Sniper rifles reach just under a machine gun turret's range so turrets can fire back.
