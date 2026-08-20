#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,sys,yaml
ROOT=Path(__file__).resolve().parents[1]
G=ROOT/'docs/implementation-guide'; errors=[]
required=[G/'security/security-guardrails.md',G/'security/risk-appetite-and-acceptance-policy.md',G/'security/security-and-trust-metrics.md',G/'security/rahp-adoption-and-adaptation.md',G/'conformance/security-assurance-tests.md',G/'matrices/rahp-adaptation-map.csv',G/'matrices/requirements-assurance-map.csv',G/'matrices/guardrail-assurance-map.csv',G/'matrices/threat-metric-map.csv']
for p in required:
    if not p.exists(): errors.append(f'Missing {p.relative_to(ROOT)}')
historical='94d17a6f5e8b448aae4698ff183e77a4a2f7a083'
current='6a95a9a2a948ece93a75e9583554b448714ef4c4'
adoption=(G/'security/rahp-adoption-and-adaptation.md').read_text()
if historical not in adoption: errors.append('Historical RAHP provenance commit not pinned')
if current not in adoption: errors.append('Current RAHP v1.1 reviewed commit not pinned')
with (G/'matrices/guardrail-assurance-map.csv').open() as f: rows=list(csv.DictReader(f))
if len(rows)!=14: errors.append(f'Expected 14 guardrail mappings, got {len(rows)}')
for r in rows:
    if not re.fullmatch(r'ZGR-\d{2}',r['guardrail_id']): errors.append('Invalid guardrail ID')
    if not re.fullmatch(r'ZAT-\d{2}',r['assurance_test_id']): errors.append('Invalid assurance test ID')
for name in ['security-assurance-result.schema.json','security-metric-evidence.schema.json','residual-risk-approval.schema.json']:
    json.loads((G/'conformance/schemas'/name).read_text())
with (G/'matrices/requirements-assurance-map.csv').open() as f: req_rows=list(csv.DictReader(f))
expected={f'LIV-LCM-{n:02d}' for n in range(1,7)} | {f'LIV-ALG-{n:02d}' for n in range(1,9)} | {'LIV-UNIQ-06','LIV-UNIQ-07'}
covered={r['requirement_id'] for r in req_rows}
missing=sorted(expected-covered)
if missing: errors.append('Missing requirement assurance mappings: '+', '.join(missing))
requirements=(ROOT/'proof-of-liveness-requirements.md').read_text()
for rid in expected:
    if rid not in requirements: errors.append(f'Requirement mapping references missing source requirement {rid}')
data=yaml.safe_load((G/'security/threat-matrix.yaml').read_text())
ids={x['threat_id'] for x in data['threats']}
for n in range(37,53):
    if f'THR-{n:03d}' not in ids: errors.append(f'Missing THR-{n:03d}')
fixture=json.loads((G/'conformance/fixtures/residual-risk-approval-example.json').read_text())
if fixture.get('risk_appetite_class')=='prohibited' and fixture.get('decision')=='accept': errors.append('Prohibited risk accepted')
if errors:
 print('Security-assurance validation failed:');[print('- '+e) for e in errors];sys.exit(1)
print(f'Security-assurance validation passed: {len(rows)} guardrails mapped; {len(ids)} threats; {len(req_rows)} requirement mappings; RAHP v1.1 provenance pinned.')
