# Builds art/CREW_SHEET_RUN.md and art/crew_prompts.html (copy-button page) from one list, so they never drift apart.
# Phoenix's answers (31 October 2026): 16 recruit kinds, each a boy and a girl (32), eight natural abilities (two kinds
# each), plus 8 Legendary characters with fixed names, half boys and half girls, one of each per player.
import html,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# the house look: Marvel meets anime, futuristic (same words in every prompt and in the Chrome run)
STYLE_DESC=("semi-realistic anime game art with a bold Marvel comic-book edge and futuristic year-2526 tech details, "
 "adult proportions, detailed cel shading, clean dark line art, strong highlights, light from the upper left")
STYLE=("These two character sheets are the approved art style for my kids' mobile game BASED Commander (year 2526, age 9+): "
 +STYLE_DESC+". Copy that style exactly. ")
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
AB={'str':('Strength','Athlete: more HP (health points) in battles'),'battle':('Battle','Soldier: more AP (attack points) in battles'),
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
LEG_ARMOR={
 'titan':('Titan Bulwark','heavy gunmetal plate armor with big gold-trimmed shoulder plates, armored knuckle guards and a glowing teal core in the chest'),
 'sharpshooter':('Starfall Ranger','sleek white and gunmetal light armor with long tactical coat tails and a headset visor over one eye glowing violet'),
 'heart':('Sunburst Captain','bright crimson and gold officer armor with a short cape and a glowing amber star emblem on the chest'),
 'brain':('Quantum Lab Rig','a white lab-armor coat over a light exo-frame, gold circuit lines and a small holo-display glowing on one wrist'),
 'medic':('Bloom Guardian','white and teal medic armor with soft rounded plates and a glowing green leaf-and-heart badge on one shoulder'),
 'gearhead':('Overclock Mech Suit','chunky orange and gunmetal engineer exo-armor with a tool belt, glowing teal power cells and gold bolts'),
 'shadow':('Nightshade Scout Suit','a matte black stealth suit with glowing teal hex lines, hood down and slim visor goggles'),
 'ace':('Maverick Flight Armor','pilot armor with a fleece-collar flight jacket, chest harness, wing emblem and a helmet clipped to the hip'),
}
# Armory shop pictures: each armor at Level 1, 3 and 5 (upgrades look tougher, Level 5 gets gold)
ARMOR_ART=[
 ('padded','Padded Vest',['a soft quilted padded vest in olive and gray, simple and friendly','the same vest reinforced: stitched shoulder pads, extra quilting and a teal trim line','the same vest at master level: light plate inserts, glowing teal seams and thin gold trim']),
 ('kevlar','Kevlar Vest',['a dark tactical vest with lots of pouches','the same vest reinforced: shoulder guards, more pouches and a teal stripe','the same vest at master level: a collar guard, glowing teal panel lines and thin gold trim']),
 ('plate','Ninja Plate',['a dark lacquered ninja plate armor chest piece','the same armor reinforced: layered shoulder plates and red cords','the same armor at master level: gold-edged plates and a glowing teal crest']),
 ('power','Power Armor',['a chunky gunmetal power armor chest piece with one glowing core','the same armor reinforced: bigger shoulder armor and two power cells','the same armor at master level: gold trim, a brighter triple core and glowing vents']),
 ('nano','Nano Suit',['a sleek black nano suit chest piece with teal hex lines','the same suit reinforced: raised armor ridges and brighter hex lines','the same suit at master level: gold hex accents and a glowing chest emblem']),
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
  an,ad=LEG_ARMOR[k]
  p4=(keep+f" Now {lname} wears their LEGENDARY armor, {an}: {ad}, with thin gold trim, kid-friendly, empty hands. Same ONE sheet layout as before: the same 11 panels and poses (five views on top, six action poses below, facing RIGHT where they did), same height and scale, feet on one baseline per row. Solid pure green #00FF00 background, no text, no numbers. Save name: char_leg_{k}_{sx}_armor_sheet.png")
  chats.append(dict(group='Legendary',title=f'{lname} · {kind} ({word})',sub=f'{AB[ab][0]} · {AB[ab][1]}',file=fn,p1=p1,p4=p4,armor=an,
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
  md+=[f"## Chat {c['n']}: {c['title']}",f"{c['sub']}. Save name: `{c['file']}`","","Prompt 1 (attach the two Commander sheets):","```\n"+c['p1']+"\n```","Prompt 2 (only if the bottom row fails):","```\n"+c['p2']+"\n```","Prompt 3 (only if one panel fails, put the number in for {N}):","```\n"+c['p3']+"\n```"]+([f"Prompt 4 (same chat, after the sheet is approved): Legendary armor, {c['armor']}","```\n"+c['p4']+"\n```"] if c.get('p4') else [])+[""]
md+=["## Outfits come next","After a character's master sheet is approved, outfits use the same chat: attach that master sheet and send the outfit prompt from art/CHARACTER_SYSTEM.md section 8 (top row only, five views), with the same-character reminder at the start."]
open(os.path.join(ROOT,'CREW_SHEET_RUN.md'),'w').write('\n'.join(md)+'\n')
# html page
def blk(label,txt):
  return f'<div class="p"><div class="ph"><span>{html.escape(label)}</span><button type="button" class="cp">Copy</button></div><pre>{html.escape(txt)}</pre></div>'
def card(c):
  return (f'<section class="card{" leg" if c["group"]=="Legendary" else ""}" id="c{c["n"]}"><h2><span class="num">{c["n"]}</span>{html.escape(c["title"])}</h2><div class="fn">{html.escape(c["sub"])} · save as <code>{html.escape(c["file"])}</code></div>'
    +blk('Prompt 1 · attach the two Commander sheets',c['p1'])+(blk('Prompt 4 · same chat, after the sheet: Legendary armor, '+c['armor'],c['p4']) if c.get('p4') else '')+'<details><summary>Backup prompts</summary>'+blk('Prompt 2 · only if the bottom row fails',c['p2'])+blk('Prompt 3 · only if one panel fails (fill in {N})',c['p3'])+'</details></section>')
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
<h1>Crew sheet prompts</h1><p class="lead">Marvel meets anime, futuristic. 40 ChatGPT chats: 16 recruit kinds as a boy and a girl (32), plus 8 Legendary characters with fixed names, one of each per player. Each chat makes one master sheet: five views on top, six action poses underneath.</p>
<ol class="steps"><li>Start a new ChatGPT chat for each character.</li><li>Attach the two Commander sheets, then paste Prompt 1.</li><li>Only if something is off, use a backup prompt or a fix line in the same chat.</li><li>Save with the download arrow on the image and rename it to the save name.</li></ol>
<h3>Recruits</h3><nav>{navr}</nav><h3>Legendary</h3><nav>{navl}<a href="#fix">Fix lines</a></nav>
<h3>Recruits (32)</h3>{''.join(card(c) for c in rec)}<h3>Legendary (8)</h3>{''.join(card(c) for c in leg)}<section class="card" id="fix"><h2>Fix lines</h2>{fix}</section></main>
<script>document.querySelectorAll('.cp').forEach(b=>b.addEventListener('click',async()=>{{const t=b.closest('.p').querySelector('pre').textContent;try{{await navigator.clipboard.writeText(t);b.textContent='Copied';b.classList.add('ok')}}catch(e){{const r=document.createRange();r.selectNodeContents(b.closest('.p').querySelector('pre'));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected'}}setTimeout(()=>{{b.textContent='Copy';b.classList.remove('ok')}},1600)}}));</script>
</body></html>'''
open(os.path.join(ROOT,'crew_prompts.html'),'w').write(page)

# ---------- Claude in Chrome run: the same characters plus Armory armor art, as one paste-in Markdown file ----------
def chrome_run():
  L=[]
  w=L.append
  w("# Claude in Chrome: crew and armor art (Marvel meets anime, futuristic)")
  w("")
  w("What this makes in ChatGPT, one image at a time: the 8 Legendary characters (a base sheet and a Legendary armor sheet each), the 32 recruit sheets, and 15 Armory armor pictures (5 armors at Level 1, 3 and 5). That is 63 images, so ChatGPT's daily image limit will stop it partway; it reports where to pick up.")
  w("")
  w("How to use it: open ChatGPT in Chrome, open the Claude side panel, copy everything below the line and paste it in. Have the two Commander sheets (art/commander, char_commander_m_01.png and char_commander_f_01.png) ready to attach when it asks. To continue another day, paste it again and say which part and number to start from.")
  w("")
  w("---")
  w("")
  w("Drive ChatGPT (chatgpt.com) in a NEW tab to make CHARACTER and ARMOR art for my kids' mobile game BASED Commander (age 9+, year 2526). Don't touch my other tabs. If ChatGPT isn't signed in, stop and ask me. Ask me before anything that spends money or changes account settings. Never type passwords. Keep everything kid-friendly: no blood, no injuries, all gear is toy-safe stun tech.")
  w("")
  w("HOUSE STYLE (every image): "+STYLE_DESC+". Gunmetal, white and teal (#2FD4D9) accents; gold only on Legendary gear.")
  w("")
  w("ORDER: Part A, then Part B, then Part C. Stop at the end of each part and give me the report table before going on, unless I said to keep going.")
  w("")
  w("CHARACTER CHATS (Parts A and B): one NEW ChatGPT chat per character, never two characters in one chat.")
  w("1. Start a new chat. Ask me to attach the two Commander sheets and wait until I say they are attached.")
  w("2. Build PROMPT 1 from the SHEET TEMPLATE below by filling in the {braces} from that character's line, word for word, and send it with the attachments.")
  w("3. CHECK the image. If only the bottom row is wrong, send PROMPT 2. If one panel is wrong, send PROMPT 3 with its number. Each fix only once, then move on and note it.")
  w("4. Part A only: when the sheet is accepted, send PROMPT 4 (that Legendary's armor) in the same chat, check it the same way, then start a new chat for the next character.")
  w("Every message after the first one in a character chat starts with the SAME-CHARACTER line, so the face, hair, skin and colors never drift.")
  w("")
  w("SHEET TEMPLATE (PROMPT 1):")
  w("```")
  w("These two character sheets are the approved art style for my kids' mobile game BASED Commander (year 2526, age 9+): "+STYLE_DESC+". Copy that style exactly. New {ROLE}: {KIND}, a {boy or girl} (young adult), natural ability {ABILITY}. Build: {BUILD}. Look: {LOOK}. {COLOR RULE} Wearing only the base layer: {BASE LAYER}. "+SHEET+" Save name: {SAVE NAME}")
  w("```")
  w("- ROLE for recruits: \"crew member\". For Legendaries: \"LEGENDARY crew member named {NAME}\".")
  w("- COLOR RULE for recruits: \"Medium-brown hair and a medium skin tone (the game recolors skin and hair later, so keep them plain and even).\" For Legendaries: \"These colors are fixed, keep them exactly.\"")
  w("- BASE LAYER for recruits: \""+BASE_LAYER+"\". For Legendaries: \""+LEG_LAYER+"\".")
  w("")
  w("SAME-CHARACTER line: \"Same character as the sheet you just made: same face, same hair, same skin tone, same body size and build, same base layer. Do not change any colors.\"")
  w("")
  w("PROMPT 2 (bottom row wrong): SAME-CHARACTER line, then: \"The bottom row came out wrong, so make it again on its own: "+ACTION+" Save name: {SAVE NAME with master_sheet changed to action_sheet}\"")
  w("")
  w("PROMPT 3 (one panel wrong): SAME-CHARACTER line, then: \"Only panel {N} came out wrong. Redraw the whole sheet with every other panel unchanged and panel {N} fixed.\"")
  w("")
  w("PROMPT 4 (Part A only, Legendary armor): SAME-CHARACTER line, then: \"Now {NAME} wears their LEGENDARY armor, {ARMOR}, with thin gold trim, kid-friendly, empty hands. Same ONE sheet layout as before: the same 11 panels and poses (five views on top, six action poses below, facing RIGHT where they did), same height and scale, feet on one baseline per row. Solid pure green #00FF00 background, no text, no numbers. Save name: {ARMOR SAVE NAME}\"")
  w("")
  w("CHECK every character sheet: 11 figures (five on top, six below), the same person and colors in all of them, every figure the same height with feet on one line per row, facing RIGHT where asked, solid pure green background, no text or numbers. Fix lines, once each:")
  for f in FIX: w(f"- \"{f}\"")
  w("")
  w("SAVE: download each accepted image with ChatGPT's download arrow on the image (the real PNG, never \"save page\"). Tell me the downloaded file name next to its save name. Characters go in the Drive folder BASED Art/Characters/<kind>, armor pictures in BASED Art/Armor.")
  w("")
  w("REPORT at the end of each part, or as soon as ChatGPT hits a usage limit: a table of save name, downloaded file name, PASS or FAIL, and what to redo, plus the next item to start from.")
  w("")
  w("PART A: THE 8 LEGENDARY CHARACTERS (a base sheet, then their armor sheet, in the same chat)")
  for c,(k,lname,kind,word,ab,build,look) in zip([c for c in chats if c['group']=='Legendary'],LEGS):
    sx='m' if word=='boy' else 'f';an,ad=LEG_ARMOR[k]
    w(f"A{LEGS.index((k,lname,kind,word,ab,build,look))+1}. LEGENDARY, NAME: {lname}. KIND: {kind}, a {word}. ABILITY: {AB[ab][0]}. BUILD: {build}. LOOK: {look}. SAVE NAME: char_leg_{k}_{sx}_master_sheet.png. ARMOR: {an}: {ad}. ARMOR SAVE NAME: char_leg_{k}_{sx}_armor_sheet.png")
  w("")
  w("PART B: THE 32 RECRUITS (16 kinds, a boy and a girl each; base sheet only)")
  n=0
  for k,name,ab,build,lm,lf in KINDS:
    for sx,word,look in (('m','boy',lm),('f','girl',lf)):
      n+=1;w(f"B{n}. KIND: {name}, a {word}. ABILITY: {AB[ab][0]}. BUILD: {build}. LOOK: {look}. SAVE NAME: char_{k}_{sx}_master_sheet.png")
  w("")
  w("PART C: ARMORY ARMOR PICTURES (15 images, 5 armors at Level 1, 3 and 5)")
  w("Start a new chat (no attachments) and send this ITEM STYLE LOCK first. Start a fresh chat with the lock again after C8.")
  w("```")
  w("I'm making ARMOR pictures for the Armory in my kids' mobile game BASED Commander (year 2526, age 9+). STYLE: "+STYLE_DESC+", gunmetal, white and teal (#2FD4D9) accents. Each picture is ONE armor chest piece on its own, no person wearing it, front three-quarter view, centered, filling about 80 percent of a SQUARE image. Solid pure green #00FF00 background, no shadow, no checkerboard, no text, no letters, no logos, no borders. Kid-friendly. Keep the same angle, size and style for every armor. I'll send one per message. Reply with just the image.")
  w("```")
  w("Then send each line below as its own message. For Level 3 and Level 5, send them right after Level 1 of the same armor so the design carries over. CHECK: one chest piece, no person, same angle and size as the others, green background, no text. Fix lines: \"Same armor, front three-quarter view, centered, no person.\" and \"Redo it on a solid pure green #00FF00 background with no shadow.\"")
  n=0
  for key,name,lv in ARMOR_ART:
    for i,(L_,desc) in enumerate(zip((1,3,5),lv)):
      n+=1;w(f"C{n}. armor_{key}_lv{L_}.png: {name}, Level {L_}: {desc}.")
  w("")
  w("When everything is done, list any FAIL items again so I can redo them.")
  open(os.path.join(ROOT,'CHROME_CREW_ARMOR_RUN.md'),'w').write('\n'.join(L)+'\n')
chrome_run()
print(len(chats),'chats')
