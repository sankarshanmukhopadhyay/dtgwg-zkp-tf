#!/usr/bin/env python3
from pathlib import Path
import csv, re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
GUIDE=ROOT/'docs/implementation-guide'
SEC=GUIDE/'security'
errors=[]
yaml_path=SEC/'threat-matrix.yaml'
csv_path=SEC/'threat-matrix.csv'
if not yaml_path.exists(): errors.append('Missing canonical threat-matrix.yaml')
if not csv_path.exists(): errors.append('Missing generated threat-matrix.csv')
if errors:
    print('Threat-model validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
data=yaml.safe_load(yaml_path.read_text(encoding='utf-8'))
rows=data.get('threats',[])
required=['threat_id','domain','title','asset_property','profiles','component','trust_boundary','threat_actor','adversary_capability','collusion_assumption','preconditions','attack_path','context_scope','time_horizon','alongside_information','technical_effect','human_institutional_harm','preventive_detective_corrective_controls','control_owner','verification_method','conformance_requirement','residual_risk','deployment_decision','severity','harm_ids','status']
seen=set()
for i,row in enumerate(rows,1):
    missing=[k for k in required if not str(row.get(k,'')).strip()]
    if missing: errors.append(f"row {i}: missing {','.join(missing)}")
    tid=row.get('threat_id','')
    if not re.fullmatch(r'THR-\d{3}',tid): errors.append(f"row {i}: invalid threat_id {tid}")
    if tid in seen: errors.append(f"row {i}: duplicate threat_id {tid}")
    seen.add(tid)
    if row.get('severity') not in {'low','medium','high','critical'}: errors.append(f"{tid}: invalid severity")
    if not re.search(r'CTL-[A-Z]{3}',row.get('preventive_detective_corrective_controls','')): errors.append(f"{tid}: no canonical control")
    if row.get('deployment_decision','').strip()=='' : errors.append(f"{tid}: no disposition")
with csv_path.open(encoding='utf-8') as f: csv_rows=list(csv.DictReader(f))
if len(csv_rows)!=len(rows): errors.append(f"YAML/CSV row mismatch: {len(rows)} vs {len(csv_rows)}")
# boundary fixture claim parameters
bf=GUIDE/'conformance/fixtures/boundary-record.json'
if not bf.exists(): errors.append('Missing boundary-record fixture')
# test references
matrix=(GUIDE/'conformance/test-matrix.csv').read_text(encoding='utf-8')
for req in ['CT-SEC-BOUNDARY-POS-01','CT-SEC-LIFE-NEG-01','CT-SEC-MED-NEG-01','CT-SEC-MIG-NEG-01']:
    if req not in matrix: errors.append(f'Missing required security test {req}')
if errors:
    print('Threat-model validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Threat-model validation passed: {len(rows)} canonical threats with controls and dispositions.')
