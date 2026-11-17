"""Maintain legacy links. Public portfolio content is maintained in IRATT/portfolios."""
from pathlib import Path
import json
R=Path(__file__).parent
DEST={"index.html":"mit/","portfolio.html":"","bacnet.html":"bacnet/","schneider.html":"schneider/","cdcdp.html":"cdcdp/"}
for name,dest in DEST.items():
 url='https://iratt.github.io/portfolios/'+dest
 (R/name).write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Portfolio moved | Ian Alleyne</title><link rel="canonical" href="'+url+'"><script>location.replace('+json.dumps(url)+'+location.search+location.hash)</script><noscript><meta http-equiv="refresh" content="0;url='+url+'"></noscript></head><body><a href="'+url+'">Open Ian Alleyne’s portfolio</a></body></html>')
