from pathlib import Path
import re,json,hashlib,urllib.request
root=Path('jessica/public')
for p in root.rglob('*.html'):
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'<iframe\b[^>]*src=["\'][^"\']*studioninja[^"\']*["\'][^>]*>.*?</iframe>','<p style="padding:30px;text-align:center">Local preview — contact form delivery is disabled.</p>',s,flags=re.S|re.I)
 s=re.sub(r'\s+srcset=["\'][^"\']*["\']','',s)
 p.write_text(s,encoding='utf-8')
print('Disabled external contact forms and responsive remote image variants')
