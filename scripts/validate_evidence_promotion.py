#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs" / "implementation-guide" / "conformance" / "evidence-promotion-gates.json"
data = json.loads(P.read_text(encoding="utf-8"))
errors = []

expected_labels = {"implemented", "independently_reproduced", "interoperable", "assurance_reviewed"}
labels = set(data.get("downstream_labels", {}))
if labels != expected_labels:
    errors.append(f"downstream labels mismatch: {sorted(labels)}")

upstream = data.get("authority", {}).get("upstream_lifecycle")
if upstream != ["requested", "specified", "constructed", "run", "vetted", "published"]:
    errors.append("canonical upstream lifecycle changed or is incomplete")

for name, spec in data.get("downstream_labels", {}).items():
    non = set(spec.get("does_not_imply", []))
    if "upstream_vetted" not in non or "upstream_published" not in non:
        errors.append(f"{name}: must explicitly not imply upstream vetted/published")

records = {row.get("record"): row for row in data.get("current_evidence", [])}
for rid in {"003", "006", "007", "008", "010", "021"}:
    if rid not in records:
        errors.append(f"missing current evidence mapping for record {rid}")
for rid, row in records.items():
    for asset in row.get("assets", []):
        if not (ROOT / asset).exists():
            errors.append(f"{rid}: missing evidence asset {asset}")
    unknown = set(row.get("labels", [])) - expected_labels
    if unknown:
        errors.append(f"{rid}: unknown downstream labels {sorted(unknown)}")

contract = data.get("independent_reproduction_contract", {})
if len(contract.get("minimum", [])) < 6:
    errors.append("independent reproduction contract is underspecified")
if not contract.get("prohibited_shortcuts"):
    errors.append("independent reproduction shortcuts must be explicit")

if errors:
    print("Evidence promotion gate validation failed:")
    for e in errors:
        print("- " + e)
    sys.exit(1)

print(f"Evidence promotion gates valid: {len(records)} canonical records mapped, {len(labels)} downstream labels.")
