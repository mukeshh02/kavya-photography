import concurrent.futures as cf, urllib.request as req, urllib.parse as up, re, html, hashlib, json
from pathlib import Path
BASE='https://www.jessicaabbyphotography.com.au'
HERE=Path(__file__).resolve().parent
ROOT=HERE/'public'
ROOT.mkdir(exist_ok=True)
allowed={'www.jessicaabbyphotography.com.au','jessicaabbyphotography.com.au','format.creatorcdn.com','fonts.creatorcdn.com','bucket2.format-assets.com','js.format.com'}
seen=set(); failed=[]; pages=[]; mapping={}
def norm(v,base):
 v=html.unescape(v.replace('\\/','/')).strip()
 if v.startswith(('data:','mailto:','tel:','#','javascript:')): return
 u=up.urlsplit(up.urljoin(base,v))
 if u.hostname not in allowed: return
 if any(x in u.path for x in ['/admin','/api/','/users/','/cart','/login']): return
 return up.urlunsplit((u.scheme,u.netloc,u.path,u.query,''))
def dest(url):
 u=up.urlsplit(url)
 if 'jessicaabbyphotography.com.au' in u.netloc:
  p=u.path.lstrip('/')
  if not Path(p).suffix: p=p.rstrip('/')+'/index.html' if p else 'index.html'
  return ROOT/p
 ext=Path(up.unquote(u.path)).suffix
 if not re.fullmatch(r'\.[a-zA-Z0-9]{1,5}',ext): ext='.bin'
 return ROOT/'assets'/u.hostname/(hashlib.sha256(url.encode()).hexdigest()[:24]+ext)
def fetch(url):
 target=dest(url)
 try:
  if target.exists(): data=target.read_bytes(); kind='text/html' if target.suffix=='.html' else ('text/css' if target.suffix=='.css' else '')
  else:
   with req.urlopen(req.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r: data=r.read(); kind=r.headers.get('Content-Type','')
   target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
  mapping[url]='/'+target.relative_to(ROOT).as_posix()
  children=set()
  if any(k in kind for k in ['text/html','text/css','javascript']):
   s=data.decode('utf-8',errors='replace')
   if 'text/html' in kind: pages.append(url)
   values=re.findall(r'''(?:src|href|poster|data-src|data-lazy-src)\s*=\s*["']([^"']+)["']''',s)
   values+=re.findall(r'''url\(\s*["']?([^\s)"']+)''',s)
   # src attributes already provide the displayed image.
   for v in values:
    child=norm(v,url)
    if child: children.add(child)
  return children
 except Exception as e: failed.append({'url':url,'error':str(e)}); return set()
queue={BASE+'/'}
with cf.ThreadPoolExecutor(max_workers=16) as pool:
 while queue:
  batch=sorted(queue-seen)
  if not batch: break
  seen.update(batch); queue=set()
  for children in pool.map(fetch,batch): queue.update(children-seen)
  print('Downloaded',len(mapping),'Pending',len(queue),'Pages',len(pages),'Failed',len(failed),flush=True)
replacements=sorted(mapping.items(),key=lambda v:len(v[0]),reverse=True)
for p in ROOT.rglob('*'):
 if p.suffix not in {'.html','.css','.js'}: continue
 s=p.read_text(encoding='utf-8',errors='replace')
 for old,new in replacements:
  s=s.replace(old,new).replace(html.escape(old,quote=True),new).replace(old.replace('/','\\/'),new.replace('/','\\/'))
 s=s.replace(BASE,'').replace('https://jessicaabbyphotography.com.au','')
 if p.suffix=='.html': s=s.replace('<head>','<head><script>document.addEventListener("submit",function(e){e.preventDefault();alert("Local preview: form delivery is disabled.")},true);</script>',1)
 p.write_text(s,encoding='utf-8')
(HERE/'mirror-report.json').write_text(json.dumps({'pages':sorted(set(pages)),'downloaded':len(mapping),'failures':failed},indent=2))
print('DONE',len(mapping),'files',len(set(pages)),'pages',len(failed),'failures',flush=True)
