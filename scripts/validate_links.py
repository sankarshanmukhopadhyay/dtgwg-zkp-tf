#!/usr/bin/env python3
from pathlib import Path
import re, sys, urllib.parse
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in ROOT.rglob('*.md'):
 if '.git' in p.parts: continue
 text=p.read_text(encoding='utf-8')
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
  target=target.strip().split()[0].strip('<>')
  if target.startswith(('http://','https://','mailto:','#')): continue
  raw=urllib.parse.unquote(target.split('#')[0])
  if not raw: continue
  dest=(p.parent/raw).resolve()
  try: dest.relative_to(ROOT.resolve())
  except ValueError: errors.append(f"{p.relative_to(ROOT)}: link escapes repository: {target}"); continue
  if not dest.exists(): errors.append(f"{p.relative_to(ROOT)}: missing target {target}")
if errors:
 print('Link validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Link validation passed.')
