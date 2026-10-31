# Put the new painted bodies into the game: SPRITES, anchor tables, outfit variants, and the stand-in recruit looks.
import sys, io, base64, json, re
from PIL import Image
GAME, BOD = sys.argv[1], sys.argv[2]
info = json.load(open(f'{BOD}/bodies.json'))
def webp(im, q=82):
    b = io.BytesIO(); im.save(b, 'WEBP', quality=q, alpha_quality=90, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
ARMORED = {'chef','ninja','mech','suit','scout','titan','medic','mb@merc','f@merc'}
parts = []
for k, v in info.items():
    full = webp(Image.open(f'{BOD}/{k}.png'))
    face = Image.open(f'{BOD}/{k}_face.png'); face = face.resize((160, 160), Image.LANCZOS)
    flags = ',dressed:1' + (',armored:1' if k in ARMORED else '') + (',s:1.06' if k == 'titan' else '')
    parts.append("'%s':{w:%d,h:%d%s,full:'%s',face:'%s'}" % (k, v['w'], v['h'], flags, full, webp(face, 80)))
s = open(GAME, encoding='utf-8').read(); n0 = len(s)
i = s.find('const SPRITES={'); j = s.find('};', i)
assert i > 0 and j > i
s = s[:i] + '// painted bodies (Based Art 2.0): the Commander in each outfit, and recruit looks borrowed from the Legendary armor sheets until recruit sheets exist\nconst SPRITES={' + ',\n'.join(parts) + '}' + s[j+1:]
def table(name, field, nd=3):
    d = {k: v[field] for k, v in info.items()}
    return 'const %s=%s;' % (name, json.dumps(d, separators=(',', ':')))
for name, field in (('HAND','hand'), ('FAR','far'), ('CHIN','chin'), ('TORSO','torso')):
    s, n = re.subn(r'const %s=\{[^\n]*?\};' % name, lambda m: table(name, field), s, count=1); assert n == 1, name
# the Commander's outfit picks a whole outfit picture; power and nano armor show the armored merc suit
old = "let PSEQ=0;\nfunction personSVG(c,vb){\n  if(c.art&&SPRITES[c.art]){const A=SPRITES[c.art];"
new = ("const CMD_FIT={flight:'casual',suit:'exec',labcoat:'exec',gi:'recruit'};\n"
       "function bodyArt(c){const a=c.art;if(a!=='mb'&&a!=='f') return a;const v=(c.armor==='power'||c.armor==='nano')?'merc':CMD_FIT[c.outfit];return v&&SPRITES[a+'@'+v]?a+'@'+v:a}\n"
       "let PSEQ=0;\nfunction personSVG(c,vb){\n  if(c.art&&SPRITES[c.art]){const ak=bodyArt(c),A=SPRITES[ak];if(ak!==c.art) c=Object.assign({},c,{art:ak});")
assert s.count(old) == 1; s = s.replace(old, new)
old = "over=outfitOver(c,+x,tp,w,h)+armorOver(c,+x,tp,w,h)"
assert s.count(old) == 1; s = s.replace(old, "over=(A.dressed?'':outfitOver(c,+x,tp,w,h))+(A.armored?'':armorOver(c,+x,tp,w,h))")
old = "CREW_LOOKS=['chef','ninja','mech','suit','scout'];"
assert s.count(old) == 1; s = s.replace(old, "CREW_LOOKS=['chef','ninja','mech','suit','scout','titan','medic'];")
old = "const ROLE_LOOK={armory:'mech',food:'chef',barracks:'ninja',fitness:'ninja',power:'mech',tech:'mech',hq:'suit',hangar:'scout'};"
assert s.count(old) == 1; s = s.replace(old, "const ROLE_LOOK={armory:'mech',food:'chef',barracks:'ninja',fitness:'titan',power:'mech',tech:'mech',hq:'suit',hangar:'scout',med:'medic'};")
open(GAME, 'w', encoding='utf-8').write(s); print('game file', n0, '->', len(s))
