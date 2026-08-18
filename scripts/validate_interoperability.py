#!/usr/bin/env python3
from pathlib import Path
import json
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"
PORTFOLIO_REGISTER = GUIDE / "interoperability" / "portfolio-alignment-register.yaml"
ASSURANCE_REGISTER = GUIDE / "interoperability" / "cross-spec-assurance-register.yaml"

errors = []

required_files = [
    GUIDE / "interoperability" / "README.md",
    GUIDE / "interoperability" / "dtg-dependency-model.md",
    GUIDE / "interoperability" / "credential-proof-inputs.md",
    GUIDE / "interoperability" / "authority-and-evidence-boundaries.md",
    GUIDE / "interoperability" / "portfolio-alignment-register.yaml",
    GUIDE / "interoperability" / "cross-spec-assurance-register.yaml",
    GUIDE / "pressure-tests" / "README.md",
    GUIDE / "pressure-tests" / "dtg-credential-linkage.md",
    GUIDE / "pressure-tests" / "trust-task-zkp-exchange.md",
    GUIDE / "pressure-tests" / "trust-ceremony-zkp-composition.md",
    GUIDE / "pressure-tests" / "agent-mediated-zkp.md",
    GUIDE / "pressure-tests" / "witnessed-relationship-zkp.md",
    GUIDE / "pressure-tests" / "trust-task-lifecycle-zkp.md",
    GUIDE / "diagrams" / "D-030-dtg-zkp-dependency-map.md",
]
for path in required_files:
    if not path.exists():
        errors.append(f"Missing {path.relative_to(ROOT)}")


def load_yaml(path, label):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            errors.append(f"{label} must contain a YAML object")
            return {}
        return data
    except Exception as exc:
        errors.append(f"Invalid {label}: {exc}")
        return {}


portfolio = load_yaml(PORTFOLIO_REGISTER, "portfolio alignment register")
rows = portfolio.get("dependencies", [])
if not isinstance(rows, list):
    errors.append("Portfolio dependencies must be a list")
    rows = []

required_ids = {
    "DTG-CREDENTIALS",
    "DTG-TRUST-TASKS",
    "DTG-TRUST-CEREMONIES",
    "DTG-RAHP",
    "DTG-VDS",
    "DTG-AGENT-NAMES",
    "DTG-HTX",
    "OPENVTC-IMPLEMENTATIONS",
}
ids = {row.get("id") for row in rows if isinstance(row, dict)}
missing = required_ids - ids
if missing:
    errors.append("Missing dependencies: " + ", ".join(sorted(missing)))

allowed_classes = {
    "semantic-runtime",
    "assurance-method",
    "conditional-composition",
    "implementation-evidence",
}
portfolio_keys = (
    "id",
    "authority",
    "dependency_class",
    "relationship",
    "status",
    "reviewed_revision",
    "consumes",
    "lifecycle",
    "must_not_infer",
    "unresolved",
    "evidence",
    "retest_triggers",
    "resolution_authority",
)
for row in rows:
    if not isinstance(row, dict):
        errors.append("Dependency row is not an object")
        continue
    rid = row.get("id", "<unknown>")
    for key in portfolio_keys:
        if key not in row:
            errors.append(f"{rid}: missing {key}")
    if row.get("dependency_class") not in allowed_classes:
        errors.append(f"{rid}: invalid dependency_class {row.get('dependency_class')!r}")
    if not row.get("authority") or not row.get("resolution_authority"):
        errors.append(f"{rid}: authority must be explicit")
    if not row.get("reviewed_revision"):
        errors.append(f"{rid}: reviewed_revision must be explicit")
    for key in ("consumes", "lifecycle", "must_not_infer", "unresolved", "evidence", "retest_triggers"):
        if not isinstance(row.get(key, []), list):
            errors.append(f"{rid}: {key} must be a list")
    if not row.get("evidence"):
        errors.append(f"{rid}: evidence must be a non-empty list")
    if not row.get("retest_triggers"):
        errors.append(f"{rid}: retest_triggers must be a non-empty list")

monitor = portfolio.get("portfolio_monitor", {})
if monitor.get("role") != "review-trigger":
    errors.append("portfolio_monitor.role must be review-trigger")
if monitor.get("authority") is not False:
    errors.append("portfolio_monitor.authority must be false")

assurance = load_yaml(ASSURANCE_REGISTER, "cross-specification assurance register")
reviews = assurance.get("reviews", [])
if not isinstance(reviews, list):
    errors.append("Cross-specification reviews must be a list")
    reviews = []

required_review_ids = {f"ZPT-{n:03d}" for n in range(1, 11)}
review_ids = {row.get("id") for row in reviews if isinstance(row, dict)}
missing_reviews = required_review_ids - review_ids
if missing_reviews:
    errors.append("Missing cross-spec reviews: " + ", ".join(sorted(missing_reviews)))

substantive_ids = {f"ZPT-{n:03d}" for n in range(1, 7)}
for row in reviews:
    if not isinstance(row, dict):
        errors.append("Cross-spec review row is not an object")
        continue
    rid = row.get("id", "<unknown>")
    for key in (
        "id",
        "title",
        "target",
        "dependency_ids",
        "status",
        "reviewed_revision",
        "document",
        "primary_question",
        "retest_triggers",
    ):
        if key not in row:
            errors.append(f"{rid}: missing {key}")
    deps = row.get("dependency_ids", [])
    if not isinstance(deps, list) or not deps:
        errors.append(f"{rid}: dependency_ids must be a non-empty list")
    else:
        unknown = set(deps) - ids
        if unknown:
            errors.append(f"{rid}: unknown dependency ids: {', '.join(sorted(unknown))}")
    if not row.get("reviewed_revision"):
        errors.append(f"{rid}: reviewed_revision must be explicit")
    if not isinstance(row.get("retest_triggers", []), list) or not row.get("retest_triggers"):
        errors.append(f"{rid}: retest_triggers must be a non-empty list")
    doc = row.get("document")
    if rid in substantive_ids:
        if not doc:
            errors.append(f"{rid}: substantive review must name a document")
        else:
            path = ROOT / doc
            if not path.exists():
                errors.append(f"{rid}: review document does not exist: {doc}")
            else:
                text = path.read_text(encoding="utf-8")
                if rid not in text:
                    errors.append(f"{rid}: review document does not contain its review id")
    elif doc:
        path = ROOT / doc
        if not path.exists():
            errors.append(f"{rid}: optional review document does not exist: {doc}")

fixture_dir = GUIDE / "conformance" / "fixtures" / "interoperability"
fixtures = []
if fixture_dir.exists():
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
    errors.append(f"Expected 10 existing interoperability fixtures, got {len(fixtures)}")

if errors:
    print("Interoperability validation failed:")
    for error in errors:
        print("- " + error)
    sys.exit(1)

substantive = sum(1 for row in reviews if row.get("id") in substantive_ids)
exploratory = len(reviews) - substantive
print(
    "Interoperability validation passed: "
    f"{len(rows)} governed dependencies, "
    f"{substantive} substantive cross-spec reviews, "
    f"{exploratory} exploratory/evidence tracks, and "
    f"{len(fixtures)} executable fixtures."
)
