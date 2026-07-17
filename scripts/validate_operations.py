#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'docs/implementation-guide'; errors=[]
required=['policy-update-runbook.md','registry-status-runbook.md','revocation-propagation-runbook.md','issuer-compromise-runbook.md','verifier-compromise-runbook.md','wallet-compromise-and-recovery-runbook.md','key-rotation-runbook.md','proof-system-migration-runbook.md','degraded-mode-runbook.md','incident-evidence-guide.md','redress-and-correction-runbook.md']
for f in required:
 if not (BASE/'operations'/f).exists(): errors.append('Missing runbook: '+f)
for fixture,schema in [('operational-readiness-example.json','operational-readiness.schema.json'),('incident-evidence-example.json','incident-evidence.schema.json'),('residual-risk-approval-example.json','residual-risk-approval.schema.json')]:
 data=json.loads((BASE/'conformance/fixtures'/fixture).read_text()); sch=json.loads((BASE/'conformance/schemas'/schema).read_text())
 for e in Draft202012Validator(sch).iter_errors(data): errors.append(f'{fixture}: {e.message}')
if errors:
 print('Operational validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print('Operational validation passed.')
