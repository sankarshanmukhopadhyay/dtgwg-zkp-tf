#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"
REGISTER = GUIDE / "interoperability" / "portfolio-alignment-register.yaml"
errors = []
required_files = [
    GUIDE / "interoperability" / "README.md",
    GUIDE / "interoperability" / "dtg-dependency-model.md",
    GUIDE / "interoperability" / "credential-proof-inputs.md",
    GUIDE / "interoperability" / "authority-and-evidence-boundaries.md",
    GUIDE / "diagrams" / "D-030-dtg-zkp-dependency-map.md",
]
for path in required_files:
    if not path.exists():
        errors.append(f"Missing {path.relative_to(ROOT)}")
try:
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
except Exception as exc:
    errors.append(f"Invalid portfolio alignment register: {exc}")
    data = {}
rows = data.get("dependencies", []) if isinstance(data, dict) else []
required_ids = {"DTG-CREDENTIALS", "DTG-TRUST-TASKS", "DTG-RAHP"}
ids = {row.get("id") for row in rows if isinstance(row, dict)}
missing = required_ids - ids
if missing:
    errors.append("Missing dependencies: " + ", ".join(sorted(missing)))
for row in rows:
    if not isinstance(row, dict):
        errors.append("Dependency row is not an object")
        continue
    for key in ("id", "authority", "relationship", "status", "consumes", "must_not_infer", "unresolved", "evidence", "resolution_authority"):
        if key not in row:
            errors.append(f"{row.get('id','<unknown>')}: missing {key}")
    if not row.get("authority") or not row.get("resolution_authority"):
        errors.append(f"{row.get('id','<unknown>')}: authority must be explicit")
    if not isinstance(row.get("evidence", []), list) or not row.get("evidence"):
        errors.append(f"{row.get('id','<unknown>')}: evidence must be a non-empty list")
fixture_dir = GUIDE / "conformance" / "fixtures" / "interoperability"
fixtures = []
if fixture_dir.exists():
    import json
    for path in sorted(fixture_dir.glob("*.json")):
        try:
            fixture = json.loads(path.read_text(encoding="utf-8"))
            fixtures.append(fixture)
            for key in ("fixture_id", "scenario_id", "kind", "expected"):
                if not fixture.get(key):
                    errors.append(f"{path.name}: missing {key}")
        except Exception as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
if len(fixtures) != 10:
    errors.append(f"Expected 10 interoperability fixtures, got {len(fixtures)}")
if errors:
    print("Interoperability validation failed:")
    for error in errors:
        print("- " + error)
    sys.exit(1)
print(f"Interoperability validation passed: {len(rows)} governed DTG dependencies and {len(fixtures)} executable fixtures.")
