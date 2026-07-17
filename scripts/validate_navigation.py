#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]; errors=[]
for p in ROOT.rglob('*.md'):
 if any(x in p.parts for x in ['vendor','_site']): continue
 t=p.read_text(encoding='utf-8')
 if p.name!='README.md' and ('docs/implementation-guide' in str(p)) and not t.startswith('---'):
  pass
 if t.startswith('---'):
  parts=t.split('---',2)
  if len(parts)<3: errors.append(f'Unclosed front matter: {p.relative_to(ROOT)}')
  elif 'title:' not in parts[1]: errors.append(f'Missing title in front matter: {p.relative_to(ROOT)}')
if errors:
 print('Navigation validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Navigation validation passed.')
