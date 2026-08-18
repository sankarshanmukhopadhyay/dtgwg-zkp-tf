#!/usr/bin/env python3
from pathlib import Path
import csv, json, re, sys
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/'docs/implementation-guide'
def rows(name):
 with (G/'matrices'/name).open(encoding='utf-8') as f: return list(csv.DictReader(f))
scenarios={r['scenario_id']:r for r in rows('scenario-index.csv')}
preds={}; threats={}; adrs={}
for r in rows('predicate-scenario-map.csv'): preds.setdefault(r['scenario_id'],[]).append(r['predicate_id'])
for r in rows('threat-scenario-map.csv'): threats.setdefault(r['scenario_id'],[]).append(r['adversary_id'])
for r in rows('adr-scenario-map.csv'): adrs.setdefault(r['scenario_id'],[]).append(r['adr_id'])
tests={}
with (G/'conformance/test-matrix.csv').open(encoding='utf-8') as f:
 for r in csv.DictReader(f): tests.setdefault(r['scenario_id'],[]).append(r['test_id'])
assurance={}
assurance_path=G/'conformance/assurance-test-dispositions.csv'
if assurance_path.exists():
 with assurance_path.open(encoding='utf-8') as f:
  for r in csv.DictReader(f): assurance.setdefault(r['scenario_id'],[]).append(r['assurance_test_id'])
out=[]
for sid in sorted(scenarios):
 out.append({'scenario_id':sid,'title':scenarios[sid]['title'],'predicates':sorted(set(preds.get(sid,[]))),'adversaries':sorted(set(threats.get(sid,[]))),'adrs':sorted(set(adrs.get(sid,[]))),'tests':sorted(set(tests.get(sid,[]))),'assurance_tests':sorted(set(assurance.get(sid,[])))})
path=G/'matrices/generated-traceability.json'; path.write_text(json.dumps(out,indent=2)+"\n")
missing=[x['scenario_id'] for x in out if not x['tests'] and not x['assurance_tests']]
print(f'Traceability generated: {len(out)} scenarios, {sum(len(x["tests"]) for x in out)} conformance references and {sum(len(x["assurance_tests"]) for x in out)} assurance references.')
if missing: print('Informational: scenarios without conformance cases: '+', '.join(missing))
