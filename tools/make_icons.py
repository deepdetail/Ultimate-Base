# App and home screen icons in export/icons: the Crimson Dragon over the raid sunset canyon.
# Needs the full-size Drive PNGs (the dragon flying pose from Exteriors and the 2B6A2034 sunset from
# Enemy Bases and BG), which are not in the repository; set SP to the folder that holds them.
# Usage: python3 tools/make_icons.py export/icons
import sys
from PIL import Image,ImageFilter
import numpy as np
SP='/tmp/claude-0/-home-user-Ultimate-Base/a052f897-918f-5f35-83b3-3b25efea49e2/scratchpad'
OUT=sys.argv[1]
def key(p):
  a=np.array(Image.open(p).convert('RGBA')).astype(np.int32);r,g,b=a[...,0],a[...,1],a[...,2]
  mag=np.minimum(r,b)-g;alpha=np.clip(255-(mag-60)*255//80,0,255);spill=np.clip(mag,0,None);m=(alpha<255)|(spill>40)
  a[...,0]=np.where(m,np.minimum(r,g+spill//3),r);a[...,2]=np.where(m,np.minimum(b,g+spill//3),b);a[...,3]=alpha
  im=Image.fromarray(a.clip(0,255).astype(np.uint8),'RGBA');return im.crop(im.getchannel('A').point(lambda v:255 if v>24 else 0).getbbox())
bg=Image.open(SP+'/ebases/2B6A2034-3005-4D10-A09F-8952D9257C71.png').convert('RGB')  # 1024 x 1536 portrait sunset
W,H=bg.size
def compose(size,drag_w,dy):
  b=bg.crop((0,int(H*.30),W,int(H*.30)+W)).resize((size,size),Image.LANCZOS).convert('RGBA')
  # gentle vignette so the dragon pops
  yy,xx=np.mgrid[0:size,0:size];d=np.sqrt(((xx-size/2)/(size/2))**2+((yy-size/2)/(size/2))**2)
  v=np.clip((d-.55)/.6,0,1)*110;dark=Image.fromarray(np.dstack([np.zeros((size,size,3),np.uint8),v.astype(np.uint8)]),'RGBA');b.alpha_composite(dark)
  dr=key(SP+'/dragon/src/flyA.png');s=drag_w/dr.width;dr=dr.resize((int(dr.width*s),int(dr.height*s)),Image.LANCZOS)
  sh=Image.new('RGBA',dr.size,(0,0,0,0));sh.putalpha(dr.getchannel('A').point(lambda v:int(v*.55)));sh=sh.filter(ImageFilter.GaussianBlur(size/90))
  x=(size-dr.width)//2;y=(size-dr.height)//2+dy
  b.alpha_composite(sh,(x+size//90,y+size//60));b.alpha_composite(dr,(x,y))
  return b.convert('RGB')
ic=compose(1024,930,-36);ic.save(OUT+'/icon-1024.png')
for s in (512,192,180,167,152,120):
  ic.resize((s,s),Image.LANCZOS).save(OUT+f'/icon-{s}.png')
compose(512,400,-10).save(OUT+'/icon-maskable-512.png')
ic.resize((64,64),Image.LANCZOS).save(OUT+'/favicon-64.png')
print('icons done')
