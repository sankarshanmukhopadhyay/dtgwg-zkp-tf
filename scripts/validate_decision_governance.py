#!/usr/bin/env python3
from pathlib import Path
import json, csv, sys
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'docs/implementation-guide/decisions/decision-register.yaml'
errors=[]
try:
    data=json.loads(REG.read_text(encoding='utf-8'))
except Exception as exc:
    print(f'Decision governance validation failed: {exc}')
    sys.exit(1)
allowed=set(data.get('status_vocabulary',[]))
ids=set()
for d in data.get('decisions',[]):
    did=d.get('id')
    if not did or did in ids: errors.append(f'duplicate or missing decision id: {did}')
    ids.add(did)
    for field in ('upstream_status','fork_status'):
        if d.get(field) not in allowed: errors.append(f'{did}: invalid {field} {d.get(field)}')
    if d.get('upstream_status') in {'ratified','ratified-with-amendment'} and not d.get('ratification_record'):
        errors.append(f'{did}: ratified state requires ratification_record')
required={'A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','C1','C2','C3'}
if ids != required:
    errors.append(f'decision id set mismatch; missing={sorted(required-ids)} extra={sorted(ids-required)}')
for name in ('context-descriptor.schema.json','privacy-claim.schema.json'):
    p=ROOT/'docs/implementation-guide/conformance/schemas'/name
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'{name}: {exc}')
mat=ROOT/'docs/implementation-guide/conformance/decision-conformance-matrix.csv'
with mat.open(encoding='utf-8',newline='') as fh:
    rows=list(csv.DictReader(fh))
if not rows: errors.append('decision conformance matrix is empty')
for row in rows:
    if row.get('decision_id') not in {'B1','B2'}: errors.append(f"unexpected decision test target: {row.get('decision_id')}")
if errors:
    print('Decision governance validation failed:')
    for e in errors: print('- '+e)
    sys.exit(1)
print(f'Decision governance validation passed: {len(ids)} decisions and {len(rows)} B1/B2 tests registered.')
