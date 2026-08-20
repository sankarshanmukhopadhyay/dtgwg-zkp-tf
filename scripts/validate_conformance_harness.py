#!/usr/bin/env python3
from pathlib import Path
import csv,json,sys
from jsonschema import validate
R=Path(__file__).resolve().parents[1]
protocol={r['test_id'] for r in csv.DictReader((R/'docs/implementation-guide/conformance/test-matrix.csv').open())}
disps=list(csv.DictReader((R/'docs/implementation-guide/conformance/execution-dispositions.csv').open()))
assert {r['test_id'] for r in disps}==protocol, 'execution dispositions must cover every protocol test exactly once'
allowed={'EXECUTABLE','BLOCKED-NORMATIVE-DECISION','BLOCKED-CONSTRUCTION-SELECTION','BLOCKED-FIXTURE','MANUAL-ASSURANCE','NOT-APPLICABLE'}
assert all(r['disposition'] in allowed for r in disps)
schema=json.loads((R/'docs/implementation-guide/conformance/schemas/conformance-test-manifest.schema.json').read_text())
manifests=[]
for path in sorted((R/'conformance-harness/examples').glob('*-manifest.json')):
 manifest=json.loads(path.read_text()); validate(manifest,schema); manifests.append((path,manifest))
exec_ids={r['test_id'] for r in disps if r['disposition']=='EXECUTABLE'}
manifest_ids=[x['test_id'] for _,manifest in manifests for x in manifest['tests']]
assert len(manifest_ids)==len(set(manifest_ids)), 'executable test IDs must occur in exactly one manifest'
assert set(manifest_ids)==exec_ids, 'manifests must cover every executable disposition exactly once'
assert len(exec_ids)>=8
print(f'Conformance harness validation passed: {len(exec_ids)} executable across {len(manifests)} manifests, {len(protocol)-len(exec_ids)} governed non-executable cases')
