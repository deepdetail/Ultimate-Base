# Cut the three-quarter view (top row, panel 2) out of each character sheet, key it, trim it, and measure anchors.
import sys, os, json, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from key import key_green, key_magenta, trim
from PIL import Image
SRC, OUT = sys.argv[1], sys.argv[2]
C = SRC + '/Characters/'
JOBS = {  # game body key: sheet (missing sheets are skipped)
  'bruiser_m': SRC+'/Characters/Recruits/Bruiser/char_bruiser_m_outfit_recruit_sheet.png',
  'bruiser_m@casual': SRC+'/Characters/Recruits/Bruiser/char_bruiser_m_outfit_casual_sheet.png',
  'bruiser_m@exec': SRC+'/Characters/Recruits/Bruiser/char_bruiser_m_outfit_exec_sheet.png',
  'bruiser_m@tactical': SRC+'/Characters/Recruits/Bruiser/char_bruiser_m_outfit_tactical_sheet.png',
  'bruiser_m@merc': SRC+'/Characters/Recruits/Bruiser/char_bruiser_m_outfit_merc_sheet.png',
  'bruiser_f': SRC+'/Characters/Recruits/Bruiser/char_bruiser_f_outfit_recruit_sheet.png',
  'bruiser_f@casual': SRC+'/Characters/Recruits/Bruiser/char_bruiser_f_outfit_casual_sheet.png',
  'bruiser_f@exec': SRC+'/Characters/Recruits/Bruiser/char_bruiser_f_outfit_exec_sheet.png',
  'bruiser_f@tactical': SRC+'/Characters/Recruits/Bruiser/char_bruiser_f_outfit_tactical_sheet.png',
  'bruiser_f@merc': SRC+'/Characters/Recruits/Bruiser/char_bruiser_f_outfit_merc_sheet.png',
  'sprinter_m': SRC+'/Characters/Recruits/Sprinter/char_sprinter_m_outfit_recruit_sheet.png',
  'sprinter_m@casual': SRC+'/Characters/Recruits/Sprinter/char_sprinter_m_outfit_casual_sheet.png',
  'sprinter_m@exec': SRC+'/Characters/Recruits/Sprinter/char_sprinter_m_outfit_exec_sheet.png',
  'sprinter_m@tactical': SRC+'/Characters/Recruits/Sprinter/char_sprinter_m_outfit_tactical_sheet.png',
  'sprinter_m@merc': SRC+'/Characters/Recruits/Sprinter/char_sprinter_m_outfit_merc_sheet.png',
  'sprinter_f': SRC+'/Characters/Recruits/Sprinter/char_sprinter_f_outfit_recruit_sheet.png',
  'sprinter_f@casual': SRC+'/Characters/Recruits/Sprinter/char_sprinter_f_outfit_casual_sheet.png',
  'sprinter_f@exec': SRC+'/Characters/Recruits/Sprinter/char_sprinter_f_outfit_exec_sheet.png',
  'sprinter_f@tactical': SRC+'/Characters/Recruits/Sprinter/char_sprinter_f_outfit_tactical_sheet.png',
  'sprinter_f@merc': SRC+'/Characters/Recruits/Sprinter/char_sprinter_f_outfit_merc_sheet.png',
}
def bg_kind(a):
    e = np.concatenate([a[:8].reshape(-1,3), a[:, :8].reshape(-1,3)]).astype(int)
    g = (e[:,1] - np.maximum(e[:,0], e[:,2])).mean(); m = (np.minimum(e[:,0], e[:,2]) - e[:,1]).mean()
    return 'green' if g > m else 'magenta'
def separators(dark, axis_len, thr=0.8):
    # divider lines are thin and run the full height; dark clothing is wide or broken, so drop wide groups
    idx = np.where(dark > thr)[0]; groups = []
    for i in idx:
        if groups and i - groups[-1][-1] <= 2: groups[-1].append(i)
        else: groups.append([i])
    return [int(np.mean(g)) for g in groups if len(g) <= 6]
def panel(im):
    a = np.asarray(im.convert('RGB')).astype(np.int32); H, W = a.shape[:2]
    dark = (a.sum(axis=2) < 200)
    rows = separators(dark.mean(axis=1), H)
    mid = [r for r in rows if H*0.35 < r < H*0.65]; split = mid[0] if mid else H//2
    top = dark[:split]
    cols = []
    for thr in (0.95, 0.9, 0.85, 0.8):
        cols = [c for c in separators(top.mean(axis=0), W, thr) if 8 < c < W-8]
        if len(cols) >= 4: break
    edges = [0] + cols + [W]
    # a divider hidden behind dark clothing: split any gap that is about two panels wide
    while len(edges) < 6:
        gaps = [edges[i+1]-edges[i] for i in range(len(edges)-1)]; i = int(np.argmax(gaps))
        edges.insert(i+1, edges[i] + gaps[i]//2)
    if len(edges) != 6: raise SystemExit('expected 5 top panels, found %d (%s)' % (len(edges)-1, cols))
    avg = W / 5
    if min(edges[i+1]-edges[i] for i in range(5)) < 0.6*avg: edges = [int(round(i*avg)) for i in range(6)]
    x0, x1 = edges[1]+3, edges[2]-3
    return im.crop((x0, 3, x1, split-3)), bg_kind(a)
def anchors(t):
    al = np.asarray(t)[..., 3] > 40; H, W = al.shape; out = {}
    ys = np.arange(H)
    # near and far fists: the right-most and left-most silhouette points at hip height, then the centroid of that end
    def fist(side):
        band = (ys > H*0.40) & (ys < H*0.62) if side > 0 else (ys > H*0.45) & (ys < H*0.60)
        xs_ext = [(np.where(al[y])[0].max() if side > 0 else np.where(al[y])[0].min(), y) for y in ys[band] if al[y].any()]
        xe, ye = (max if side > 0 else min)(xs_ext)
        r = int(H*0.035); y0, y1 = max(0, ye-r), min(H, ye+r)
        sub = al[y0:y1]; xx = np.where(sub)[1]
        sel = xx > xe - 2*r if side > 0 else xx < xe + 2*r
        yy = np.where(sub)[0][sel] + y0; xx = xx[sel]
        return [round(float(xx.mean())/W, 3), round(float(yy.mean())/H, 3)]
    out['hand'] = fist(1); out['far'] = fist(-1)
    # chin: the narrowest row between the head and the shoulders
    widths = np.array([(np.ptp(np.where(al[y])[0]) if al[y].any() else 0) for y in range(H)])
    lo, hi = int(H*0.08), int(H*0.2); neck = lo + int(np.argmin(widths[lo:hi]))
    out['chin'] = round(neck/H - 0.004, 3)
    # torso: silhouette at the shoulders, trimmed in a little for the chest
    ys_ = int(neck + H*0.045); xs = np.where(al[ys_])[0]; x0, x1 = xs.min()/W, xs.max()/W; pad = (x1-x0)*0.1
    out['torso'] = [round(float(x0+pad), 3), round(float(x1-pad), 3), round(ys_/H, 3), round(ys_/H + 0.2, 3)]
    return out
info = {}
for key, path in JOBS.items():
    if not os.path.exists(path): print('skip (not uploaded yet):', key); continue
    im = Image.open(path); p, kind = panel(im)
    k = (key_green if kind == 'green' else key_magenta)(p); t, box = trim(k, pad=2, thr=40)
    s = 440 / t.height; t = t.resize((max(1, round(t.width*s)), 440), Image.LANCZOS)
    t.save(f'{OUT}/{key}.png'); a = anchors(t)
    # face for portraits: a square around the head
    al = np.asarray(t)[..., 3] > 40; hh = int(a['chin']*440); hx = np.where(al[:hh].any(axis=0))[0]
    cx = (hx.min()+hx.max())/2; side = int(hh*1.25); fx0 = int(max(0, cx-side/2)); face = t.crop((fx0, 0, fx0+side, side))
    bg = Image.new('RGBA', face.size, (0,0,0,0)); bg.paste(face, (0,0), face); bg.save(f'{OUT}/{key}_face.png')
    info[key] = dict(a, w=t.width, h=t.height, bg=kind)
json.dump(info, open(f'{OUT}/bodies.json', 'w'), indent=1)
for k, v in info.items(): print(k, v)
