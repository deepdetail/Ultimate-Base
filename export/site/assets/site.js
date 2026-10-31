// Download App: the browser's own install prompt where it has one (Chrome, Edge, Android), short steps everywhere else,
// and the App Store once the iPhone app is live. Set APP_STORE_URL to the App Store link then.
const APP_STORE_URL='';
let installEvent=null;
window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();installEvent=e});
window.addEventListener('appinstalled',()=>show('installed'));
const ua=navigator.userAgent;
const isIOS=/iPad|iPhone|iPod/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
const isMacSafari=!isIOS&&/Macintosh/.test(ua)&&/Safari/.test(ua)&&!/Chrome|Chromium|Edg|Firefox/.test(ua);
const installed=()=>window.matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
const STEPS={
  ios:['Install on iPhone or iPad',['Open basedcommander.com in Safari and tap LAUNCH IN BROWSER, so the game is on screen.','Tap Share (the square with an arrow). If you do not see it, tap the ••• button first.','Tap Add to Home Screen, then Add.'],'BASED Commander then opens full screen from your home screen, with its own icon, and plays offline.'],
  mac:['Install on a Mac',['In Safari, click LAUNCH IN BROWSER so the game is on screen.','Open the File menu and choose Add to Dock, then Add.'],'It opens in its own window and plays offline. In Chrome or Edge, use the install icon in the address bar instead.'],
  other:['Install the app',['Open basedcommander.com in Chrome or Edge.','Click the install icon at the right of the address bar, or open the browser menu and choose Install BASED Commander.'],'Some browsers, like Firefox, may not show an install option. You can always play right in the browser.'],
  installed:['Already installed',[],'BASED Commander is installed on this device. Open it from your home screen or your apps.']
};
function show(kind){
  const d=document.getElementById('steps');if(!d) return;const [title,list,note]=STEPS[kind];
  d.querySelector('h3').textContent=title;
  const ol=d.querySelector('ol');ol.innerHTML='';list.forEach(s=>{const li=document.createElement('li');li.textContent=s;ol.appendChild(li)});ol.hidden=!list.length;
  d.querySelector('p').textContent=note;
  if(typeof d.showModal==='function') d.showModal();else d.setAttribute('open','');
}
document.querySelectorAll('[data-install]').forEach(b=>b.addEventListener('click',async e=>{
  e.preventDefault();
  if(isIOS&&APP_STORE_URL){location.href=APP_STORE_URL;return}
  if(installed()) return show('installed');
  if(installEvent){installEvent.prompt();const r=await installEvent.userChoice.catch(()=>({}));installEvent=null;if(r&&r.outcome==='accepted') show('installed');return}
  show(isIOS?'ios':isMacSafari?'mac':'other');
}));
document.querySelectorAll('[data-close]').forEach(b=>b.addEventListener('click',()=>{const d=b.closest('dialog');if(d.close) d.close();else d.removeAttribute('open')}));
// offline play after the first visit (https only)
if('serviceWorker' in navigator&&location.protocol==='https:') navigator.serviceWorker.register('sw.js').catch(()=>{});
