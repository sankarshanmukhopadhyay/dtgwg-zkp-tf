#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
paths=list((ROOT/'docs/implementation-guide/conformance/fixtures').glob('*.json'))+list((ROOT/'docs/implementation-guide/conformance/schemas').glob('*.json'))
errors=[]
for p in paths:
 try:
  obj=json.loads(p.read_text(encoding='utf-8'))
  if not isinstance(obj,dict) or not obj: errors.append(f"{p.relative_to(ROOT)}: expected a non-empty JSON object")
 except Exception as e: errors.append(f"{p.relative_to(ROOT)}: {e}")
if errors:
 print('Fixture validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Fixture validation passed: {len(paths)} JSON files parsed.')
