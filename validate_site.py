"""Verify the single page, collapsed course record, grades and legacy links."""
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).parent.resolve()
data = json.loads((ROOT / 'data/modules.json').read_text())
assert len(data) == 24
assert sum(m['earned'] for m in data) == sum(m['possible'] for m in data) == 813
assert sum(len(m['activities']) for m in data) == 144
assert all(m['earned'] == m['possible'] and all(g['earned'] == g['possible'] for g in m['activities']) for m in data)

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.modules = [], set(), set()
        self.h1, self.redirect, self.in_nav, self.nav = 0, False, False, []
        self.record_present, self.record_open = False, False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, ('Duplicate ID', a['id'])
            self.ids.add(a['id'])
        if 'data-module' in a: self.modules.add(int(a['data-module']))
        if tag == 'h1': self.h1 += 1
        if tag == 'details' and a.get('id') == 'module-record':
            self.record_present, self.record_open = True, 'open' in a
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            self.redirect = True
            self.links.append(a['content'].split('url=', 1)[1])
        if tag == 'nav': self.in_nav = True
        if tag == 'a' and self.in_nav and not urlparse(a.get('href', '')).scheme:
            self.nav.append(a['href'])
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])
    def handle_endtag(self, tag):
        if tag == 'nav': self.in_nav = False

pages = {}
for p in ROOT.rglob('*.html'):
    parser = Page()
    parser.feed(p.read_text())
    assert parser.h1 == 1, (p, 'expected one h1')
    pages[p] = parser
content = {p.name for p, parsed in pages.items() if not parsed.redirect and p.name != '404.html'}
assert content == {'index.html'}, content
assert pages[ROOT / 'index.html'].modules == set(range(1, 25))
for name in content:
    assert pages[ROOT / name].nav == ['#projects', '#recognition', '#course-record']
assert pages[ROOT / 'index.html'].record_present and not pages[ROOT / 'index.html'].record_open
errors = []
for p, parsed in pages.items():
    for link in parsed.links:
        u = urlparse(link)
        if u.scheme or link.startswith('//'): continue
        target = (p.parent / unquote(u.path)).resolve() if u.path else p
        if not target.exists(): errors.append((p.name, link, 'missing file'))
        elif u.fragment and target in pages and u.fragment not in pages[target].ids:
            errors.append((p.name, link, 'missing anchor'))
        if parsed.redirect and target in pages:
            assert not pages[target].redirect, (p, 'redirect chain')
assert not errors, errors
public = '\n'.join(p.read_text() for p in ROOT.rglob('*') if p.suffix in ['.html', '.json'])
assert '/submissions/' not in public
print(f'PASS: 1 content page, course record collapsed by default; {sum(p.redirect for p in pages.values())} legacy redirects; 24 modules; 144 activities; 813/813 points; links, anchors and redirects valid.')
