# Add the real recruit bodies (Bruiser and Sprinter, M and F, five outfits) and point the strength jobs at them.
import sys, io, base64, json, re, numpy as np
from PIL import Image
GAME, BOD = sys.argv[1], sys.argv[2]
info = json.load(open(f'{BOD}/bodies.json'))
# the character's right fist (the picture's left), read by eye off a grid
FAR = {'bruiser_m':[.21,.49],'bruiser_m@casual':[.21,.50],'bruiser_m@exec':[.21,.48],'bruiser_m@tactical':[.19,.50],'bruiser_m@merc':[.20,.515],
       'bruiser_f':[.11,.505],'bruiser_f@casual':[.07,.49],'bruiser_f@exec':[.10,.51],'bruiser_f@tactical':[.10,.51],'bruiser_f@merc':[.11,.53],
       'sprinter_m':[.12,.52],'sprinter_m@casual':[.11,.51],'sprinter_m@exec':[.10,.51],'sprinter_m@tactical':[.13,.49],'sprinter_m@merc':[.13,.49],
       'sprinter_f':[.11,.52],'sprinter_f@casual':[.12,.51],'sprinter_f@exec':[.12,.52],'sprinter_f@tactical':[.09,.51]}
for k, v in info.items():
    v['far'] = FAR[k]
    if k.startswith('bruiser_m'):   # thick neck fooled the automatic chin; read off the picture
        al = np.asarray(Image.open(f'{BOD}/{k}.png'))[..., 3] > 40; H, W = al.shape; y = int(H*.15); xs = np.where(al[y])[0]
        x0, x1 = xs.min()/W, xs.max()/W; pad = (x1-x0)*.1
        v['chin'] = .105; v['torso'] = [round(float(x0+pad), 3), round(float(x1-pad), 3), .15, .35]
def webp(im, q=82):
    b = io.BytesIO(); im.save(b, 'WEBP', quality=q, alpha_quality=90, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
parts = []
for k, v in info.items():
    full = webp(Image.open(f'{BOD}/{k}.png')); base = k.split('@')[0]
    flags = ',dressed:1' + (',armored:1' if k.endswith('@merc') else '') + (',s:1.04' if base == 'bruiser_m' else '')
    face = (",face:'%s'" % webp(Image.open(f'{BOD}/{k}_face.png').resize((160, 160), Image.LANCZOS), 80)) if '@' not in k else ",fk:'%s'" % base
    parts.append("'%s':{w:%d,h:%d%s,full:'%s'%s}" % (k, v['w'], v['h'], flags, full, face))
s = open(GAME, encoding='utf-8').read(); n0 = len(s)
i = s.find('const SPRITES={'); j = s.find('};', i); assert i > 0 and j > i
s = s[:j] + ',\n' + ',\n'.join(parts) + s[j:]
for name, field in (('HAND','hand'), ('FAR','far'), ('CHIN','chin'), ('TORSO','torso')):
    m = re.search(r'const %s=(\{[^\n]*?\});' % name, s); d = json.loads(m.group(1))
    d.update({k: v[field] for k, v in info.items()})
    s = s.replace(m.group(0), 'const %s=%s;' % (name, json.dumps(d, separators=(',', ':'))), 1)
# strength jobs (Barracks and Dojo looks) now show real Bruiser and Sprinter recruits, boys and girls by id, outfit by what they wear
old = "function bodyArt(c){const a=c.art;if(a!=='mb'&&a!=='f') return a;"
new = ("const REC_OF={ninja:['bruiser','sprinter'],titan:['bruiser','sprinter']};\n"
       "const CREW_FIT={jumpsuit:'',flight:'casual',suit:'exec',labcoat:'exec',gi:'tactical',armor:'tactical'};\n"
       "function bodyArt(c){const a=c.art,ks=!c.isCmd&&REC_OF[a];\n"
       "  if(ks){const n=Math.abs(c.id||0),b=ks[(n>>1)%ks.length]+'_'+(n%2?'f':'m'),v=(c.armor==='power'||c.armor==='nano')?'merc':(CREW_FIT[c.outfit]||'');\n"
       "    return v&&SPRITES[b+'@'+v]?b+'@'+v:SPRITES[b]?b:a}\n"
       "  if(a!=='mb'&&a!=='f') return a;")
assert s.count(old) == 1; s = s.replace(old, new)
# portraits: outfit pictures borrow the face of their person
old = 'if(vb&&A.face) return `<svg viewBox="0 0 1 1" aria-hidden="true"><image href="${A.face}"'
assert s.count(old) == 1
s = s.replace(old, 'const FACE=A.face||(A.fk&&SPRITES[A.fk]&&SPRITES[A.fk].face);if(vb&&FACE) return `<svg viewBox="0 0 1 1" aria-hidden="true"><image href="${FACE}"')
open(GAME, 'w', encoding='utf-8').write(s); print('game file', n0, '->', len(s))
