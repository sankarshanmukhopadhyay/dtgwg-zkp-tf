#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'docs/implementation-guide'
OPS = BASE / 'operations'
errors = []

runbooks = [
    'policy-update-runbook.md',
    'registry-status-runbook.md',
    'revocation-propagation-runbook.md',
    'issuer-compromise-runbook.md',
    'verifier-compromise-runbook.md',
    'wallet-compromise-and-recovery-runbook.md',
    'key-rotation-runbook.md',
    'proof-system-migration-runbook.md',
    'degraded-mode-runbook.md',
    'redress-and-correction-runbook.md',
]
required_sections = [
    '## Trigger and detection',
    '## Decision authority and scope',
    '## Immediate containment',
    '## Evidence to preserve',
    '## Recovery procedure',
    '## Recovery test and closure',
    '## Communications and redress',
    '## Minimum evidence produced',
]

for filename in runbooks:
    path = OPS / filename
    if not path.exists():
        errors.append('Missing runbook: ' + filename)
        continue
    text = path.read_text(encoding='utf-8')
    for section in required_sections:
        if section not in text:
            errors.append(f'{filename}: missing required section {section}')

# Incident evidence is a guide rather than an event-specific runbook, but it must
# expose the same authority/evidence/recovery discipline where applicable.
evidence_guide = OPS / 'incident-evidence-guide.md'
if not evidence_guide.exists():
    errors.append('Missing runbook: incident-evidence-guide.md')
else:
    text = evidence_guide.read_text(encoding='utf-8')
    for section in required_sections:
        if section not in text:
            errors.append(f'incident-evidence-guide.md: missing required section {section}')

# The readiness checklist is part of the operational control surface.
if not (OPS / 'operational-readiness-checklist.md').exists():
    errors.append('Missing operational readiness checklist')

for fixture, schema in [
    ('operational-readiness-example.json', 'operational-readiness.schema.json'),
    ('incident-evidence-example.json', 'incident-evidence.schema.json'),
    ('residual-risk-approval-example.json', 'residual-risk-approval.schema.json'),
]:
    data = json.loads((BASE / 'conformance/fixtures' / fixture).read_text())
    sch = json.loads((BASE / 'conformance/schemas' / schema).read_text())
    for e in Draft202012Validator(sch).iter_errors(data):
        errors.append(f'{fixture}: {e.message}')

if errors:
    print('Operational validation failed:')
    [print('- ' + e) for e in errors]
    sys.exit(1)
print(f'Operational validation passed: {len(runbooks)} runbooks + incident evidence guide structurally complete.')
