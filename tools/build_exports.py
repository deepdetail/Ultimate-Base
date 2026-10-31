#!/usr/bin/env python3
"""Build the two take-away versions of the game from prototype/based.html.

    python3 tools/build_exports.py

Makes:
  dist/web/                      a folder any static web host can serve (also opens by double-click)
  dist/BASED-Commander-web.zip   that folder, zipped
  ios/BASEDCommander/Web/        the game inside the Xcode project (refreshed every run)
  dist/BASED-Commander-iOS.zip   the whole Xcode project, zipped, ready to open on a Mac

Everything the game needs is bundled (three.js r128 and its two add-ons, the two fonts, the map
terrain), so both versions work with no internet. dist/ is not committed; ios/ is.
"""
import json, os, re, shutil, subprocess, sys, time, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'prototype', 'based.html')
TERRAIN = os.path.join(ROOT, 'prototype', 'terrain.json')
VENDOR = os.path.join(ROOT, 'export', 'vendor')
ICONS = os.path.join(ROOT, 'export', 'icons')
WEB_README = os.path.join(ROOT, 'export', 'web', 'README.md')
DIST = os.path.join(ROOT, 'dist')
IOS = os.path.join(ROOT, 'ios')
IOS_WEB = os.path.join(IOS, 'BASEDCommander', 'Web')
APPICON = os.path.join(IOS, 'BASEDCommander', 'Assets.xcassets', 'AppIcon.appiconset', 'AppIcon-1024.png')


def swap(html, old, new, what):
    """Replace text that must be there exactly once, so a game change can never slip past silently."""
    n = html.count(old)
    if n != 1:
        sys.exit(f'build_exports: expected 1 match for {what}, found {n}. Update tools/build_exports.py.')
    return html.replace(old, new)


def build_id():
    try:
        sha = subprocess.run(['git', '-C', ROOT, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
    except OSError:
        sha = ''
    return (sha or 'local') + '-' + time.strftime('%Y%m%d')


def page(app, bid):
    game = open(SRC, encoding='utf-8').read()
    # the game file starts with a few head tags; the exports bring their own head instead
    game = swap(game, '<meta charset="utf-8">\n', '', 'charset meta')
    game = swap(game, '<title>BASED Commander</title>\n', '', 'title')
    game = swap(game, '<meta name="claude:viewport-fit-sides" content="cover">\n', '', 'claude viewport meta')
    game = swap(game, '<link rel="preconnect" href="https://fonts.googleapis.com">\n', '', 'font preconnect')
    game = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*">\n', '', game, count=1)
    # three.js and its add-ons come from the bundle instead of a CDN
    game = swap(game, "s.src='https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'", "s.src='vendor/three/three.min.js'", 'three.js CDN')
    game = swap(game, "const base='https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/';", "const base='vendor/three/examples/js/';", 'three.js add-ons CDN')
    # the map terrain is bundled as a script, so it also works when index.html is opened straight from disk
    game = swap(game, "return fetch('terrain.json')", "if(window.BASED_TERRAIN) return Promise.resolve(TERRAIN=window.BASED_TERRAIN);return fetch('terrain.json')", 'terrain fetch')
    if app:
        # on your own iPhone the app reopens straight into the last base (the web keeps the per-visit name check)
        game = swap(game, "try{sessionStorage.removeItem('based-open')}", "try{localStorage.removeItem('based-open')}", 'lock')
        game = swap(game, "function unlock(name){try{sessionStorage.setItem('based-open',slug(name))}", "function unlock(name){try{localStorage.setItem('based-open',slug(name))}", 'unlock')
        game = swap(game, "let opened='';try{opened=sessionStorage.getItem('based-open')||''}", "let opened='';try{opened=localStorage.getItem('based-open')||''}", 'opened')
    head = [
        '<!doctype html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">',
        '<title>BASED Commander</title>',
        f'<meta name="based-build" content="{bid}">',
        '<meta name="theme-color" content="#14171B">',
        '<meta name="color-scheme" content="dark">',
        '<link rel="stylesheet" href="vendor/fonts/fonts.css">',
        '<script src="terrain.js"></script>',
    ]
    if not app:
        head += [
            '<meta name="description" content="BASED Commander: build your base, recruit a crew, catch clones and defend against raiders.">',
            '<meta name="apple-mobile-web-app-capable" content="yes">',
            '<meta name="mobile-web-app-capable" content="yes">',
            '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">',
            '<meta name="apple-mobile-web-app-title" content="BASED">',
            '<link rel="manifest" href="manifest.webmanifest">',
            '<link rel="apple-touch-icon" href="icons/icon-180.png">',
            '<link rel="icon" type="image/png" href="icons/favicon-64.png">',
        ]
    head += ['<style>html,body{margin:0;padding:0;background:#14171B}</style>', '</head>', '<body>']
    tail = ['</body>', '</html>', '']
    if not app:
        # offline play once visited (only on https hosts; double-clicked files skip it)
        tail.insert(0, "<script>if('serviceWorker' in navigator&&location.protocol==='https:')navigator.serviceWorker.register('sw.js').catch(function(){})</script>")
    return '\n'.join(head) + '\n' + game + '\n' + '\n'.join(tail)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def common_files(dst, app, bid):
    write(os.path.join(dst, 'index.html'), page(app, bid))
    terrain = json.load(open(TERRAIN, encoding='utf-8'))
    write(os.path.join(dst, 'terrain.js'), 'window.BASED_TERRAIN=' + json.dumps(terrain, separators=(',', ':')) + ';\n')
    shutil.copytree(VENDOR, os.path.join(dst, 'vendor'))


def web(bid):
    out = os.path.join(DIST, 'web')
    shutil.rmtree(out, ignore_errors=True)
    common_files(out, False, bid)
    os.makedirs(os.path.join(out, 'icons'))
    for n in ('icon-180.png', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'favicon-64.png'):
        shutil.copy(os.path.join(ICONS, n), os.path.join(out, 'icons', n))
    write(os.path.join(out, 'manifest.webmanifest'), json.dumps({
        'name': 'BASED Commander', 'short_name': 'BASED', 'start_url': './', 'scope': './',
        'display': 'standalone', 'orientation': 'portrait', 'background_color': '#14171B', 'theme_color': '#14171B',
        'icons': [
            {'src': 'icons/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
            {'src': 'icons/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
            {'src': 'icons/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
        ]}, indent=2) + '\n')
    files = ['./', 'index.html', 'terrain.js', 'manifest.webmanifest', 'vendor/three/three.min.js',
             'vendor/three/examples/js/controls/OrbitControls.js', 'vendor/three/examples/js/objects/Reflector.js',
             'vendor/fonts/fonts.css'] + ['vendor/fonts/' + f for f in sorted(os.listdir(os.path.join(VENDOR, 'fonts'))) if f.endswith('.woff2')]
    # network first: online players always get the newest game, offline players get the last one they loaded
    write(os.path.join(out, 'sw.js'), f"""const CACHE='based-{bid}';
const FILES={json.dumps(files)};
self.addEventListener('install',e=>{{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).catch(()=>{{}}))}});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin) return;
  e.respondWith(fetch(r).then(res=>{{if(res.ok){{const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp))}}return res}}).catch(()=>caches.match(r).then(m=>m||caches.match('index.html'))))}});
""")
    shutil.copy(WEB_README, os.path.join(out, 'README.md'))
    return out


def ios(bid):
    shutil.rmtree(IOS_WEB, ignore_errors=True)
    common_files(IOS_WEB, True, bid)
    shutil.copy(os.path.join(ICONS, 'icon-1024.png'), APPICON)


def zipdir(src, zpath, top):
    if os.path.exists(zpath):
        os.remove(zpath)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for base, dirs, files in os.walk(src):
            dirs[:] = sorted(d for d in dirs if d not in ('xcuserdata', 'DerivedData', '.DS_Store'))
            for f in sorted(files):
                if f == '.DS_Store':
                    continue
                full = os.path.join(base, f)
                z.write(full, os.path.join(top, os.path.relpath(full, src)))


def main():
    bid = build_id()
    os.makedirs(DIST, exist_ok=True)
    out = web(bid)
    zipdir(out, os.path.join(DIST, 'BASED-Commander-web.zip'), 'BASED-Commander-web')
    ios(bid)
    zipdir(IOS, os.path.join(DIST, 'BASED-Commander-iOS.zip'), 'BASED-Commander-iOS')
    for z in ('BASED-Commander-web.zip', 'BASED-Commander-iOS.zip'):
        print(f'{z}: {os.path.getsize(os.path.join(DIST, z)) / 1e6:.1f} MB')
    print('build', bid)


if __name__ == '__main__':
    main()
