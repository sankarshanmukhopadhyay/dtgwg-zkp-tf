#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'docs/implementation-guide/conformance'
pairs={
 'local-proving-deployment.json':'deployment-profile.schema.json',
 'remote-proving-deployment.json':'deployment-profile.schema.json',
 'hybrid-proving-deployment.json':'deployment-profile.schema.json',
 'deployment-evidence-example.json':'deployment-evidence.schema.json'}
errors=[]
for fixture,schema in pairs.items():
 data=json.loads((BASE/'fixtures'/fixture).read_text()); sch=json.loads((BASE/'schemas'/schema).read_text())
 for e in Draft202012Validator(sch).iter_errors(data): errors.append(f'{fixture}: {e.message}')
if errors:
 print('Deployment profile validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Deployment profile validation passed.')
