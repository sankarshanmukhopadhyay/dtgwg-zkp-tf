#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
GUIDE=ROOT/'docs/implementation-guide'
errors=[]
placeholders=[r'\bTBD\b',r'\bTODO\b',r'\(Instantiate\b',r'Summary table:',r'Threat matrix to be maintained']
for p in GUIDE.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    for pat in placeholders:
        if re.search(pat,text,re.I): errors.append(f"{p.relative_to(ROOT)}: unresolved placeholder matching {pat}")
    headings=[line for line in text.splitlines() if line.startswith('#')]
    for h in headings:
        if h.startswith('#######'): errors.append(f"{p.relative_to(ROOT)}: heading deeper than level 6: {h}")
    if '```mermaid' in text and '## Interpretation' not in text:
        errors.append(f"{p.relative_to(ROOT)}: Mermaid diagram lacks an Interpretation section")
    if p.name != 'STYLE-GUIDE.md':
        for word in ('fully anonymous','fully unlinkable','globally unique person'):
            if word.lower() in text.lower(): errors.append(f"{p.relative_to(ROOT)}: prohibited unqualified claim '{word}'")
if errors:
 print('Style validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Style validation passed.')
