#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,sys,yaml
ROOT=Path(__file__).resolve().parents[1]
G=ROOT/'docs/implementation-guide'; errors=[]
required=[G/'security/security-guardrails.md',G/'security/risk-appetite-and-acceptance-policy.md',G/'security/security-and-trust-metrics.md',G/'security/rahp-adoption-and-adaptation.md',G/'conformance/security-assurance-tests.md',G/'matrices/rahp-adaptation-map.csv',G/'matrices/guardrail-assurance-map.csv',G/'matrices/threat-metric-map.csv']
for p in required:
    if not p.exists(): errors.append(f'Missing {p.relative_to(ROOT)}')
upstream='94d17a6f5e8b448aae4698ff183e77a4a2f7a083'
if upstream not in (G/'security/rahp-adoption-and-adaptation.md').read_text(): errors.append('RAHP reviewed commit not pinned')
with (G/'matrices/guardrail-assurance-map.csv').open() as f: rows=list(csv.DictReader(f))
if len(rows)!=14: errors.append(f'Expected 14 guardrail mappings, got {len(rows)}')
for r in rows:
    if not re.fullmatch(r'ZGR-\d{2}',r['guardrail_id']): errors.append('Invalid guardrail ID')
    if not re.fullmatch(r'ZAT-\d{2}',r['assurance_test_id']): errors.append('Invalid assurance test ID')
for name in ['security-assurance-result.schema.json','security-metric-evidence.schema.json','residual-risk-approval.schema.json']:
    json.loads((G/'conformance/schemas'/name).read_text())
data=yaml.safe_load((G/'security/threat-matrix.yaml').read_text())
ids={x['threat_id'] for x in data['threats']}
for n in range(37,46):
    if f'THR-{n:03d}' not in ids: errors.append(f'Missing THR-{n:03d}')
fixture=json.loads((G/'conformance/fixtures/residual-risk-approval-example.json').read_text())
if fixture.get('risk_appetite_class')=='prohibited' and fixture.get('decision')=='accept': errors.append('Prohibited risk accepted')
if errors:
 print('Security-assurance validation failed:');[print('- '+e) for e in errors];sys.exit(1)
print(f'Security-assurance validation passed: {len(rows)} guardrails mapped; {len(ids)} threats; RAHP provenance pinned.')
