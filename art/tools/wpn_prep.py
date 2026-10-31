import os
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from key import key_green, key_black, trim
from PIL import Image
SRC, OUT = sys.argv[1], sys.argv[2]
info = {}
for kind, folder, keyer in (('shop','Weapons/Shop',key_green), ('held','Weapons/Held',key_green), ('fx','Weapons/Attack FX',key_black)):
    d = os.path.join(SRC, folder)
    for f in sorted(os.listdir(d)):
        if not f.endswith('.png'): continue
        im = Image.open(os.path.join(d, f)); k = keyer(im); t, box = trim(k)
        name = f[:-4]; t.save(os.path.join(OUT, name + '.png'))
        info[name] = {'src': list(im.size), 'box': [int(v) for v in box], 'size': list(t.size)}
json.dump(info, open(os.path.join(OUT, 'info.json'), 'w'), indent=1)
print(len(info), 'processed')
