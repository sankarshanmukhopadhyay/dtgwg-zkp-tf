#!/usr/bin/env python3
from pathlib import Path
import csv,re,sys
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/'docs/implementation-guide'; errors=[]
rows=list(csv.DictReader((G/'conformance/test-matrix.csv').open()))
actual=len(rows)
pattern=re.compile(r'\b(\d+) conformance (?:cases|tests)\b',re.I)
for p in G.rglob('*.md'):
 for m in pattern.finditer(p.read_text()):
  if int(m.group(1))!=actual: errors.append(f'{p.relative_to(ROOT)} states {m.group(1)}; actual is {actual}')
if errors:
 print('Generated count validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Generated count validation passed ({actual} conformance cases).')
