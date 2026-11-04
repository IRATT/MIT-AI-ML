"""Check page coverage, grade reconciliation and local links without a browser."""
import json, pathlib
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
ROOT=pathlib.Path(__file__).parent
data=json.loads((ROOT/'data/modules.json').read_text())
assert len(data)==24
assert sum(m['earned'] for m in data)==sum(m['possible'] for m in data)==813
assert sum(len(m['activities']) for m in data)==144
assert all(m['earned']==m['possible'] and all(g['earned']==g['possible'] for g in m['activities']) for m in data)
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
pages={}
for p in ROOT.rglob('*.html'):
    parser=Links();parser.feed(p.read_text());pages[p.resolve()]=parser
    assert parser.h1==1,(p,'expected one h1')
errors=[]
for p,parser in pages.items():
    for link in parser.links:
        u=urlparse(link)
        if u.scheme or link.startswith('//'):continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        if not target.exists():errors.append((str(p.relative_to(ROOT)),link,'missing file'))
        elif u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append((str(p.relative_to(ROOT)),link,'missing anchor'))
assert not errors,errors
public='\n'.join(p.read_text() for p in ROOT.rglob('*') if p.suffix in ['.html','.json'])
assert '/submissions/' not in public
print(f'PASS: {len(pages)} HTML pages; 24 modules; 144 activities; 813/813 points; all internal links and anchors resolve; no private learner links.')
