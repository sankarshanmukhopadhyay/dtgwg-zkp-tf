#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs/implementation-guide/diagrams'; errors=[]
files=sorted(D.glob('D-*.md')); ids=[]
for p in files:
 m=re.match(r'(D-\d{3})-',p.name)
 if not m: errors.append('Invalid diagram filename: '+p.name); continue
 ids.append(m.group(1)); t=p.read_text()
 if '```mermaid' not in t: errors.append('Missing Mermaid source: '+p.name)
 if 'Interpretation' not in t: errors.append('Missing textual interpretation: '+p.name)
reg=(D/'README.md').read_text()
for i in ids:
 if i not in reg: errors.append('Diagram not registered: '+i)
if len(ids)!=len(set(ids)): errors.append('Duplicate diagram IDs')
if errors:
 print('Diagram validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Diagram validation passed ({len(ids)} diagrams).')
