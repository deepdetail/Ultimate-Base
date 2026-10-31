# Key a flat green (or magenta) screen, or a black background for glow effects, then trim.
import sys, numpy as np
from PIL import Image
def key_green(im, lo=40, hi=110):
    a = np.asarray(im.convert('RGB')).astype(np.int32)
    r, g, b = a[...,0], a[...,1], a[...,2]
    gs = g - np.maximum(r, b)                      # how green a pixel is
    alpha = 1 - np.clip((gs - lo) / (hi - lo), 0, 1)
    # despill: pull leftover green down to the other channels on soft edges
    g2 = np.where(gs > 0, np.maximum(r, b) + (gs * (1 - np.clip(gs/hi, 0, 1)) * 0.25).astype(np.int32), g)
    out = np.dstack([r, np.minimum(g, g2), b, (alpha * 255).astype(np.int32)]).clip(0, 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')
def key_magenta(im, lo=40, hi=110):
    a = np.asarray(im.convert('RGB')).astype(np.int32)
    r, g, b = a[...,0], a[...,1], a[...,2]
    ms = np.minimum(r, b) - g
    alpha = 1 - np.clip((ms - lo) / (hi - lo), 0, 1)
    out = np.dstack([r, g, b, (alpha * 255).astype(np.int32)]).clip(0, 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')
def key_black(im):
    # glow on black: alpha from brightness, colors un-premultiplied so it can sit on any background
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    al = np.clip((a.max(axis=2) - 0.06) / 0.94, 0, 1)
    rgb = np.where(al[...,None] > 0.001, np.clip(a / np.maximum(al[...,None], 1e-3), 0, 1), 0)
    return Image.fromarray((np.dstack([rgb, al]) * 255).astype(np.uint8), 'RGBA')
def trim(im, pad=6, thr=24):
    al = np.asarray(im)[..., 3]
    ys, xs = np.where(al > thr)
    if not len(xs): return im, (0, 0, im.width, im.height)
    box = (max(0, xs.min()-pad), max(0, ys.min()-pad), min(im.width, xs.max()+1+pad), min(im.height, ys.max()+1+pad))
    return im.crop(box), box
