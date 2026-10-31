# Builds art/CREW_SHEET_RUN.md and art/crew_prompts.html (copy-button page) from one list, so they never drift apart.
# Phoenix's answers (31 October 2026): 16 recruit kinds, each a boy and a girl (32), eight natural abilities (two kinds
# each), plus 8 Legendary characters with fixed names, half boys and half girls, one of each per player.
import html,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLE=("These two character sheets are the approved art style for my kids' mobile game BASED Commander (year 2526, age 9+): "
 "realistic anime, adult proportions, detailed cel shading, clean dark line art, light from the upper left. Copy that style exactly. ")
BASE_LAYER="a fitted, modest future base-layer singlet in charcoal gray with thin teal seams, neck to mid-thigh, short sleeves, plain gray slip-on socks"
LEG_LAYER="a fitted, modest future base-layer singlet in charcoal gray with thin GOLD seams and a small gold star on the chest, neck to mid-thigh, short sleeves, plain gray slip-on socks"
COLORS="medium-brown hair and a medium skin tone (the game recolors skin and hair later, so keep them plain and even)"
SHEET=("Make ONE character sheet, wide 1536 x 1024, two rows of panels separated by thin dark lines, every figure the same height and scale, "
 "feet on one baseline per row. TOP ROW, five panels, standing relaxed, arms slightly away from the body, empty hands: "
 "1 front; 2 front three quarter turned toward the RIGHT; 3 side facing RIGHT; 4 back three quarter; 5 back. "
 "BOTTOM ROW, six panels, all facing RIGHT: 6 walk A (left foot forward, heel down); 7 walk B (passing, legs together); "
 "8 jump (knees tucked); 9 crouch; 10 hold pose (both hands forward at chest height gripping nothing, ready to hold a tool or weapon); "
 "11 knocked out (sitting, dizzy cartoon stars, no injuries). "
 "Solid pure green #00FF00 background, no shadow, no checkerboard, no text, no numbers, no logos. Kid-friendly.")
ACTION=("ONE wide image, six panels in a row separated by thin dark lines, all facing RIGHT, same scale and baseline: "
 "walk A (left foot forward, heel down); walk B (passing, legs together); jump (knees tucked); crouch; hold pose (both hands forward at chest height gripping nothing); "
 "knocked out (sitting, dizzy cartoon stars, no injuries). Solid pure green #00FF00 background, no text.")
# ability: (name, what it does in the game)
AB={'str':('Strength','Athlete: more health in battles'),'battle':('Battle','Soldier: hits harder in battles'),
    'cha':('Charisma','Leader: keeps roommates happy and working faster'),'iq':('IQ','Genius: smarter, earns more in HQ'),
    'med':('Med','Healer: knocked out crew heal faster'),'tech':('Tech','Nerd: more power and faster repairs'),
    'sci':('Scientist','Research: more tech points, spots clones'),'pilot':('Driving and Pilot','Adventurer: faster, safer missions')}
# 16 recruit kinds: key, name, ability, build, boy look, girl look
KINDS=[
 ('bruiser','Bruiser','str','big, heavy and broad','buzz cut and a thick neck','very short cropped hair and a strong jaw'),
 ('sprinter','Sprinter','str','lean, long-legged runner','short spiky hair and a sweatband','high ponytail and a sweatband'),
 ('trooper','Trooper','battle','athletic, square stance','crew cut','tight bun'),
 ('ranger','Ranger','battle','lean, wiry and steady','shaggy hair and a bandana around the neck','side braid and a bandana around the neck'),
 ('captain','Captain','cha','tall with upright posture','neat swept hair and a confident smile','shoulder-length wavy hair and a confident smile'),
 ('diplomat','Diplomat','cha','average, relaxed open posture','tidy short curls and friendly eyes','long straight hair tucked behind the ears and friendly eyes'),
 ('prodigy','Prodigy','iq','small and slim','round glasses and messy hair','round glasses and a messy bob'),
 ('strategist','Strategist','iq','slim, tall and calm','rectangular glasses and short neat hair','rectangular glasses and a sleek low ponytail'),
 ('paramedic','Paramedic','med','average and sturdy','short neat hair and kind eyes','neat ponytail and kind eyes'),
 ('caretaker','Caretaker','med','soft, sturdy and warm','curly hair and a gentle smile','curly hair in a high puff and a gentle smile'),
 ('hacker','Hacker','tech','slim','headphones around the neck and a swoopy fringe','headphones around the neck and an asymmetric bob'),
 ('mechanic','Mechanic','tech','stocky with thick forearms','work goggles on the forehead and a grease smudge on one cheek','two braids, work goggles on the forehead and a grease smudge on one cheek'),
 ('chemist','Chemist','sci','slim, average height','lab goggles on the forehead and tidy hair','lab goggles on the forehead and a bun'),
 ('explorer','Explorer','sci','lean and outdoorsy','windswept hair and a small compass pendant','wavy hair, freckles and a small compass pendant'),
 ('pilot','Pilot','pilot','wiry and quick','swept-back hair and aviator sunglasses pushed up on the head','short swept hair and aviator sunglasses pushed up on the head'),
 ('racer','Racer','pilot','compact and agile','spiky hair and fingerless gloves','pixie cut and fingerless gloves'),
]
# 8 Legendary characters (the first draft archetypes): fixed name and fixed colors, never recolored or renamed
LEGS=[
 ('titan','Ironclad Rex','Titan','boy','str','towering, broad shoulders, heavy muscle','black buzz cut, deep brown skin and a strong jaw'),
 ('sharpshooter','Nova Vex','Sharpshooter','girl','battle','lean athletic, very steady stance','silver-white hair in a low bun, light skin and focused violet eyes'),
 ('heart','Sunny Valor','Heart','girl','cha','sturdy and warm','bright red curly hair, freckles, light tan skin and a big smile'),
 ('brain','Quill Quantum','Brain','boy','iq','slim, a little shorter than the others','round gold glasses, messy blue-black hair and medium brown skin'),
 ('medic','Mercy Bloom','Medic','girl','med','average build, calm posture','a long dark braid, warm brown skin and a gentle face'),
 ('gearhead','Bolt Ryder','Gearhead','boy','tech','stocky with thick forearms','copper-red hair, work goggles on the forehead, pale freckled skin and a grease smudge on one cheek'),
 ('shadow','Echo Nightshade','Shadow','girl','sci','small and very agile','a short black pixie cut with one teal streak, olive skin and sharp green eyes'),
 ('ace','Skye Maverick','Ace','boy','pilot','wiry and quick','swept-back blond hair, tan skin and aviator sunglasses pushed up on the head'),
]
FIX=["Keep the face, hair, colors and body exactly like the sheet. Only fix the panel I name.",
 "Keep every panel the same height and scale, feet on one baseline in each row.",
 "Redo it on a solid pure green #00FF00 background with no shadow.",
 "Same image with no text, numbers, letters or logos anywhere."]
chats=[]
for k,name,ab,build,lm,lf in KINDS:
  for sx,word,look in (('m','boy',lm),('f','girl',lf)):
    fn=f'char_{k}_{sx}_master_sheet.png'
    keep=f"Same character as the sheet you just made: same face, same {look}, same medium-brown hair and medium skin tone, same body size and build, same charcoal singlet with teal seams and gray socks. Do not change any colors."
    p1=STYLE+f"New crew member: {name}, a {word} (young adult), natural ability {AB[ab][0]}. Build: {build}. Look: {look}, {COLORS}. Wearing only the base layer: {BASE_LAYER}. "+SHEET+f" Save name: {fn}"
    chats.append(dict(group='Recruits',title=f'{name} ({word})',sub=f'{AB[ab][0]} · {AB[ab][1]}',file=fn,p1=p1,
      p2=keep+" The bottom row came out wrong, so make it again on its own: "+ACTION+f" Save name: char_{k}_{sx}_action_sheet.png",
      p3=keep+" Only panel {N} came out wrong. Redraw the whole sheet with every other panel unchanged and panel {N} fixed."))
for k,lname,kind,word,ab,build,look in LEGS:
  sx='m' if word=='boy' else 'f';fn=f'char_leg_{k}_{sx}_master_sheet.png'
  keep=f"Same character as the sheet you just made: {lname}, same face, same {look}, same body size and build, same charcoal singlet with gold seams and the gold star. Do not change any colors."
  p1=STYLE+f"New LEGENDARY crew member named {lname}, the {kind}, a {word} (young adult), natural ability {AB[ab][0]}. Build: {build}. Look: {look}. These colors are fixed, keep them exactly. Wearing only the legendary base layer: {LEG_LAYER}. A heroic, special look, still kid-friendly. "+SHEET+f" Save name: {fn}"
  chats.append(dict(group='Legendary',title=f'{lname} · {kind} ({word})',sub=f'{AB[ab][0]} · {AB[ab][1]}',file=fn,p1=p1,
    p2=keep+" The bottom row came out wrong, so make it again on its own: "+ACTION+f" Save name: char_leg_{k}_{sx}_action_sheet.png",
    p3=keep+" Only panel {N} came out wrong. Redraw the whole sheet with every other panel unchanged and panel {N} fixed."))
for i,c in enumerate(chats): c['n']=i+1
# markdown
md=["# Crew sheet run: 40 ChatGPT chats (32 recruits + 8 Legendary)","",
"Decided with Phoenix: see art/CHARACTER_SYSTEM.md. Each character gets ONE master sheet with the five-view turnaround on top and the six action poses underneath, so every pose is drawn in the same image and stays the same person and colors.","",
"## How to run each chat","1. Start a NEW ChatGPT chat for every character (40 chats). Never mix two characters in one chat.",
"2. Attach the two Commander sheets (art/commander) to the first message as the style reference.",
"3. Paste Prompt 1. Check the result against the checklist.",
"4. If only the bottom row is wrong, paste Prompt 2 in the same chat (it repeats the same-character, same-colors reminder) and save that as the action sheet.",
"5. If one panel is wrong, paste Prompt 3 with the panel number filled in.",
"6. Save with the download arrow on the image (not save page) and rename to the save name. Drop into Drive: BASED Art/Characters/<kind>.","",
"Recruits are drawn with plain medium-brown hair and medium skin because the game recolors them per recruit. Legendary characters keep their own fixed colors and gold-seam base layer.","",
"## Checklist","- 11 figures: five on top, six underneath, same person in all of them.","- Same face, hair, skin tone and singlet colors in every panel.","- Every figure the same height, feet on one line per row.","- Facing RIGHT where the prompt says right.","- Solid pure green background, no text or numbers.","",
"## Fix lines (same chat, one at a time)"]+["```\n"+f+"\n```" for f in FIX]+[""]
grp=None
for c in chats:
  if c['group']!=grp: grp=c['group'];md+=[f"# {grp}" if grp=='Legendary' else "# Recruits (16 kinds x boy and girl)",""]
  md+=[f"## Chat {c['n']}: {c['title']}",f"{c['sub']}. Save name: `{c['file']}`","","Prompt 1 (attach the two Commander sheets):","```\n"+c['p1']+"\n```","Prompt 2 (only if the bottom row fails):","```\n"+c['p2']+"\n```","Prompt 3 (only if one panel fails, put the number in for {N}):","```\n"+c['p3']+"\n```",""]
md+=["## Outfits come next","After a character's master sheet is approved, outfits use the same chat: attach that master sheet and send the outfit prompt from art/CHARACTER_SYSTEM.md section 8 (top row only, five views), with the same-character reminder at the start."]
open(os.path.join(ROOT,'CREW_SHEET_RUN.md'),'w').write('\n'.join(md)+'\n')
# html page
def blk(label,txt):
  return f'<div class="p"><div class="ph"><span>{html.escape(label)}</span><button type="button" class="cp">Copy</button></div><pre>{html.escape(txt)}</pre></div>'
def card(c):
  return (f'<section class="card{" leg" if c["group"]=="Legendary" else ""}" id="c{c["n"]}"><h2><span class="num">{c["n"]}</span>{html.escape(c["title"])}</h2><div class="fn">{html.escape(c["sub"])} · save as <code>{html.escape(c["file"])}</code></div>'
    +blk('Prompt 1 · attach the two Commander sheets',c['p1'])+'<details><summary>Backup prompts</summary>'+blk('Prompt 2 · only if the bottom row fails',c['p2'])+blk('Prompt 3 · only if one panel fails (fill in {N})',c['p3'])+'</details></section>')
rec=[c for c in chats if c['group']=='Recruits'];leg=[c for c in chats if c['group']=='Legendary']
navr=''.join(f'<a href="#c{c["n"]}">{c["n"]}. {html.escape(c["title"])}</a>' for c in rec)
navl=''.join(f'<a class="lg" href="#c{c["n"]}">{c["n"]}. {html.escape(c["title"])}</a>' for c in leg)
fix=''.join(blk('Fix line',f) for f in FIX)
page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Crew Sheet Prompts</title>
<style>
:root{{--bg:#f6f4ef;--card:#fff;--ink:#1d1f24;--mute:#5d6470;--line:#e2ddd2;--acc:#0f8a8f;--gold:#a87b12;--code:#f1eee6}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#14161a;--card:#1d2026;--ink:#eceae4;--mute:#a3a9b3;--line:#2e323a;--acc:#4fd1d6;--gold:#e2b84a;--code:#262a31}}}}
:root[data-theme="dark"]{{--bg:#14161a;--card:#1d2026;--ink:#eceae4;--mute:#a3a9b3;--line:#2e323a;--acc:#4fd1d6;--gold:#e2b84a;--code:#262a31}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}}
main{{max-width:860px;margin:0 auto;padding:24px 16px 60px}}h1{{font-size:26px;margin:0 0 6px}}h3{{font-size:16px;margin:22px 0 8px}}.lead{{color:var(--mute);margin:0 0 18px}}
ol.steps{{padding-left:20px;margin:0 0 18px}}nav{{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}}nav a{{font-size:13px;color:var(--acc);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:3px 10px;background:var(--card)}}nav a.lg{{color:var(--gold);border-color:var(--gold)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:0 0 16px}}.card.leg{{border-color:var(--gold)}}h2{{font-size:18px;margin:0 0 4px;display:flex;align-items:center;gap:10px}}
.num{{display:inline-grid;place-items:center;min-width:28px;height:28px;border-radius:50%;background:var(--acc);color:var(--card);font-size:13px}}.leg .num{{background:var(--gold)}}.fn{{color:var(--mute);font-size:13px;margin:0 0 10px}}
code{{font-size:12.5px;background:var(--code);padding:1px 5px;border-radius:4px;word-break:break-all}}.p{{margin:8px 0}}.ph{{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:13px;color:var(--mute);margin:0 0 4px}}
pre{{margin:0;white-space:pre-wrap;word-wrap:break-word;background:var(--code);border-radius:8px;padding:10px 12px;font:13px/1.45 ui-monospace,Menlo,Consolas,monospace}}
.cp{{border:1px solid var(--acc);background:transparent;color:var(--acc);border-radius:8px;padding:4px 12px;font-weight:600;cursor:pointer;min-height:32px}}.cp.ok{{background:var(--acc);color:var(--card)}}
details summary{{cursor:pointer;color:var(--acc);font-size:14px;margin:8px 0 4px}}
</style></head><body><main>
<h1>Crew sheet prompts</h1><p class="lead">40 ChatGPT chats: 16 recruit kinds as a boy and a girl (32), plus 8 Legendary characters with fixed names, one of each per player. Each chat makes one master sheet: five views on top, six action poses underneath.</p>
<ol class="steps"><li>Start a new ChatGPT chat for each character.</li><li>Attach the two Commander sheets, then paste Prompt 1.</li><li>Only if something is off, use a backup prompt or a fix line in the same chat.</li><li>Save with the download arrow on the image and rename it to the save name.</li></ol>
<h3>Recruits</h3><nav>{navr}</nav><h3>Legendary</h3><nav>{navl}<a href="#fix">Fix lines</a></nav>
<h3>Recruits (32)</h3>{''.join(card(c) for c in rec)}<h3>Legendary (8)</h3>{''.join(card(c) for c in leg)}<section class="card" id="fix"><h2>Fix lines</h2>{fix}</section></main>
<script>document.querySelectorAll('.cp').forEach(b=>b.addEventListener('click',async()=>{{const t=b.closest('.p').querySelector('pre').textContent;try{{await navigator.clipboard.writeText(t);b.textContent='Copied';b.classList.add('ok')}}catch(e){{const r=document.createRange();r.selectNodeContents(b.closest('.p').querySelector('pre'));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected'}}setTimeout(()=>{{b.textContent='Copy';b.classList.remove('ok')}},1600)}}));</script>
</body></html>'''
open(os.path.join(ROOT,'crew_prompts.html'),'w').write(page)
print(len(chats),'chats')
