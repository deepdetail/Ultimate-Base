# Encode the keyed weapon art as WebP and wire it into the game file (in place).
import sys, os, re, io, base64, json
from PIL import Image
GAME, WPN = sys.argv[1], sys.argv[2]
def webp(im, long_side, q=82):
    im = im.copy(); s = long_side / max(im.size)
    if s < 1: im = im.resize((max(1, round(im.width*s)), max(1, round(im.height*s))), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=q, alpha_quality=90, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode(), im.size
W = ['slingshot','bb','kunai','shuriken','bow','staff','handgun','katana','rifle','assault','mg','laser','plasma','rail']
FX = ['arrow','kunai_throw','laser_beam','muzzle_flash','pellet','plasma_ball','rail_trail','shuriken_spin','slash_arc']
s = open(GAME, encoding='utf-8').read(); n0 = len(s); sizes = {}
# 1) shop pictures replace the weapon icons one for one
for k in W:
    uri, sz = webp(Image.open(f'{WPN}/shop_{k}.png'), 256); sizes['weapon:'+k] = sz
    pat_obj = re.compile(r"'weapon:%s':'[^']*'" % k); pat_set = re.compile(r"GSPR\['weapon:%s'\]='[^']*';" % k)
    if pat_set.search(s): s = pat_set.sub(lambda m: "GSPR['weapon:%s']='%s';" % (k, uri), s, count=1)
    elif pat_obj.search(s): s = pat_obj.sub(lambda m: "'weapon:%s':'%s'" % (k, uri), s, count=1)
    else: sys.exit('no slot for weapon:' + k)
# 2) held pictures and attack effects in one block, where the old single held:bow lived
held = {}
for k in W:
    uri, sz = webp(Image.open(f'{WPN}/held_{k}.png'), 320); held['held:'+k] = uri; sizes['held:'+k] = sz
for k in FX:
    uri, sz = webp(Image.open(f'{WPN}/fx_{k}.png'), 256, q=80); held['fx:'+k] = uri; sizes['fx:'+k] = sz
block = "// weapons as held (side view, pointing right; grips in GRIP) and attack effects (glow, drawn with screen blending)\nObject.assign(GSPR,{" + ",".join("'%s':'%s'" % kv for kv in held.items()) + "});"
pat = re.compile(r"GSPR\['held:bow'\]='[^']*';")
if not pat.search(s): sys.exit('no held:bow slot')
s = pat.sub(lambda m: block, s, count=1)
# 3) the back quiver: stand the painted quiver upright (arrows up), then trim
q = Image.open(f'{WPN}/held_quiver.png').rotate(37, resample=Image.BICUBIC, expand=True)
bb = q.getchannel('A').point(lambda v: 255 if v > 24 else 0).getbbox(); q = q.crop(bb)
uri, sz = webp(q, 320); sizes['quiver'] = sz
pat = re.compile(r"const QUIVER_SRC='[^']*';")
if not pat.search(s): sys.exit('no QUIVER_SRC')
s = pat.sub(lambda m: "const QUIVER_SRC='%s';" % uri, s, count=1)
open(GAME, 'w', encoding='utf-8').write(s)
json.dump({k: list(v) for k, v in sizes.items()}, open(f'{WPN}/sizes.json', 'w'))
print('game file', n0, '->', len(s), 'bytes')
