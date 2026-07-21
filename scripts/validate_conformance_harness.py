#!/usr/bin/env python3
from pathlib import Path
import csv,json,sys
R=Path(__file__).resolve().parents[1]
protocol={r['test_id'] for r in csv.DictReader((R/'docs/implementation-guide/conformance/test-matrix.csv').open())}
disps=list(csv.DictReader((R/'docs/implementation-guide/conformance/execution-dispositions.csv').open()))
assert {r['test_id'] for r in disps}==protocol, 'execution dispositions must cover every protocol test exactly once'
allowed={'EXECUTABLE','BLOCKED-NORMATIVE-DECISION','BLOCKED-CONSTRUCTION-SELECTION','BLOCKED-FIXTURE','MANUAL-ASSURANCE','NOT-APPLICABLE'}
assert all(r['disposition'] in allowed for r in disps)
manifest=json.loads((R/'conformance-harness/examples/mock-manifest.json').read_text())
exec_ids={r['test_id'] for r in disps if r['disposition']=='EXECUTABLE'}
assert {x['test_id'] for x in manifest['tests']}==exec_ids
assert len(exec_ids)>=8
print(f'Conformance harness validation passed: {len(exec_ids)} executable, {len(protocol)-len(exec_ids)} governed non-executable cases')
