# Dragon animation run (flying, fire breath, hit, knocked out)

Yes: this is just a handful of extra still images. The game flips between them and adds the motion in code (bobbing, wing timing, the flame stretching toward its target, screen shake). No video or 3D model needed.

## How to run it in ChatGPT (one chat, in this order)

1. Start a NEW chat. Upload the current dragon picture first (art/enemies/enemy_l4_dragon_01.png, or the pet dragon you want animated).
2. Paste prompt 0 (the lock-in). It tells ChatGPT to keep this exact dragon for every picture.
3. Paste prompts 1 to 8 one at a time in the same chat. After each image, check it against the checklist below, then click the download arrow on the image itself (not "save page") and save it with the name in the prompt.
4. If one drifts (new colors, different horns, dragon got smaller), say: "Redo that. Same dragon as the first picture, same size and position, only the pose changes." Do not move on with a drifted frame.
5. Drop the PNGs in the Drive Pets folder (pet dragons) or Exteriors (enemy dragon) and tell Claude. Claude keys out the magenta, lines the frames up, and wires them in.

## Checklist for every frame
- Same dragon: same colors, horns, belly plates, tail tip.
- Same size and same spot in the picture. The body stays in the middle so frames do not jump when they swap.
- Facing RIGHT, three quarters view. (The game flips it for enemies.)
- Solid flat magenta background, nothing else behind it. No pink or purple in the fire.
- Fire is NOT drawn on the dragon frames (except prompt 7, which is fire by itself). Keeping fire separate lets the game aim it and stretch it.

## What each picture is for

| # | File | Used for |
|---|---|---|
| 1 | dragon_fly_up.png | flying, wings at the top of the flap |
| 2 | dragon_fly_down.png | flying, wings at the bottom of the flap (1 and 2 swap fast = flapping) |
| 3 | dragon_glide.png | hovering between flaps, map and pet screen |
| 4 | dragon_windup.png | about to breathe: head back, chest glowing |
| 5 | dragon_breathe.png | breathing: head forward, mouth open (fire added by the game) |
| 6 | dragon_claw.png | close attack: front claw swipe |
| 7 | fx_fire_breath.png | the flame stream by itself |
| 8 | fx_fireball.png | a single fireball (for long-range shots and turret hits) |
| 9 | dragon_hit.png | flinch when it takes damage |
| 10 | dragon_ko.png | knocked out: lying down, dizzy stars (kid friendly, no injuries) |

Minimum to look great: 1, 2, 4, 5, 7. The rest are nice to have.

For the rider dragon (Level 14) make the same set without the rider. The game places the rider on top. For a pet dragon, use the same prompts and swap the dragon name in prompt 0.

## Prompts

### 0. Lock-in (paste right after uploading the dragon picture)
```
This is the dragon from my kids' mobile game BASED Commander. I am going to ask for several pictures of THIS EXACT dragon in different poses for a simple game animation. Every picture must keep the same dragon: same colors, same horns, same belly plates, same wing shape, same tail, same proportions. Keep the same art style: semi-realistic anime game art with a bold Marvel comic edge, clean dark line art, cel shading, strong highlights, light from the upper left. Every picture: the dragon faces RIGHT in three quarters view, full body in frame including wings and tail, same size, centered at the same spot, wide 1536 x 1024 canvas, solid flat magenta background (#FF00FF), no shadow, no ground, no gradient, no checkerboard, no text, no borders. It is a kids' game: powerful but not gory, no blood. Reply "ready" and wait for my first pose.
```

### 1. dragon_fly_up.png
```
Pose 1, save name dragon_fly_up.png. The same dragon flying in the air: both wings raised high above its back at the top of a wing beat, wing tips pointing up, legs tucked under its body, tail stretched out behind. Mouth closed. Same size and position as the original, magenta background, nothing else changes.
```

### 2. dragon_fly_down.png
```
Pose 2, save name dragon_fly_down.png. Exactly the same flying dragon as pose 1, same body position, same head, same tail. ONLY the wings change: both wings swept down below its body at the bottom of a wing beat, wing tips pointing down. Magenta background.
```

### 3. dragon_glide.png
```
Pose 3, save name dragon_glide.png. Same flying dragon, same body position as pose 1. Wings spread straight out to the sides, flat, gliding. Mouth closed. Magenta background.
```

### 4. dragon_windup.png
```
Pose 4, save name dragon_windup.png. Same dragon flying, wings half open. It is about to breathe fire: head and neck pulled back, chest and throat glowing bright orange from inside, mouth closed, a little smoke from its nostrils. No flames yet. Same size and position. Magenta background.
```

### 5. dragon_breathe.png
```
Pose 5, save name dragon_breathe.png. Same dragon, same body position as pose 4. Now its head and neck thrust forward toward the right, mouth wide open roaring, throat glowing orange. Do NOT draw any fire coming out; the game adds the flames separately. Magenta background.
```

### 6. dragon_claw.png
```
Pose 6, save name dragon_claw.png. Same dragon, hovering low, swiping forward to the right with one front claw, a quick white motion arc behind the claw. Mouth closed, focused face. No blood. Same size and position. Magenta background.
```

### 7. fx_fire_breath.png
```
Picture 7, save name fx_fire_breath.png. No dragon this time. Only a stream of dragon fire by itself, a cone of flame that starts narrow and bright yellow white at the LEFT edge and spreads wider to the right, orange and red with dark smoke curls at the far end, same comic cel shaded style. It fills the canvas from left to right. Fire colors only: yellow, orange, red. No pink, no purple. Solid flat magenta background (#FF00FF), nothing else.
```

### 8. fx_fireball.png
```
Picture 8, save name fx_fireball.png. No dragon. A single round fireball flying to the right, bright yellow core, orange and red flames trailing behind it to the left, a few sparks, same comic cel shaded style, centered, about 40 percent of the canvas. Fire colors only, no pink or purple. Solid flat magenta background (#FF00FF).
```

### 9. dragon_hit.png
```
Pose 9, save name dragon_hit.png. Same dragon flying, flinching from being hit: head pulled back and eyes squeezed shut, wings jerked up, body tilted back a little, a small white impact flash near its chest. No blood, no wounds. Same size and position. Magenta background.
```

### 10. dragon_ko.png
```
Pose 10, save name dragon_ko.png. Same dragon, knocked out cartoon style: lying on its belly with wings flopped out to the sides, eyes as little swirls, tongue out a bit, three small cartoon stars circling its head. Funny, not hurt. No blood. Magenta background.
```

## Pet dragon note
For a pet dragon, upload its adult picture and in prompt 0 change the first sentence to "This is my kid's pet dragon (Storm, Sun, Ember or Frost) from BASED Commander." Storm breathes lightning, so swap fire in prompts 4, 5, 7 and 8 for "crackling blue white lightning". Frost breathes "icy blue frost with snowflakes". Ember and Sun keep fire.
