from pathlib import Path
import re,json,urllib.parse as up
root=Path(__file__).parent/'public'; refs=set(); missing=[]
for p in root.rglob('*.html'):
 s=p.read_text(encoding='utf-8')
 for v in re.findall(r'''(?:src|href)=["'](/[^"']*)''',s):
  v=up.unquote(up.urlsplit(v).path)
  if v.startswith('//'): continue
  refs.add(v)
for v in sorted(refs):
 p=root/v.lstrip('/')
 if not p.exists() and not (p/'index.html').exists(): missing.append(v)
report={'pages':len(list(root.rglob('*.html'))),'local_references':len(refs),'missing':missing}
(Path(__file__).parent/'audit-report.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
