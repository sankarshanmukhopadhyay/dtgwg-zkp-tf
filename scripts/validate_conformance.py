#!/usr/bin/env python3
"""
Validates the internal consistency of the implementation-guide conformance
suite and traceability matrices.

Run from the repository root:

    python3 scripts/validate_conformance.py

Checks performed:
  1. Every predicate_id used in conformance test matrices and
     matrices/predicate-scenario-map.csv exists in taxonomy/predicates.md.
  2. Every adversary_id used in conformance test matrices and
     matrices/threat-scenario-map.csv exists in taxonomy/adversaries.md.
  3. Every scenario_id used anywhere exists as a UC-NNN heading in
     scenarios/pressure-test-use-case-corpus.md.
  4. Every adr_id used in matrices/adr-scenario-map.csv exists as an
     ADR-NNN file in adr/.
  5. Every conformance level (CL-1..CL-4) present in the aggregate test
     corpus has at least one positive and at least one negative test case.
  6. No CSV under matrices/ or conformance/ is header-only (a placeholder).
  7. Every test_id across the aggregate conformance corpus is unique.
  8. Every composed-presentation fixture case referenced by the machine-
     readable matrix exists in the executable semantic fixture set.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "implementation-guide"

TAXONOMY_PREDICATES = GUIDE / "taxonomy" / "predicates.md"
TAXONOMY_ADVERSARIES = GUIDE / "taxonomy" / "adversaries.md"
SCENARIO_CORPUS = GUIDE / "scenarios" / "pressure-test-use-case-corpus.md"
ADR_DIR = GUIDE / "adr"
MATRICES_DIR = GUIDE / "matrices"
CONFORMANCE_DIR = GUIDE / "conformance"
TEST_MATRIX = CONFORMANCE_DIR / "test-matrix.csv"
COMPOSED_TEST_MATRIX = CONFORMANCE_DIR / "composed-presentation-test-matrix.csv"
COMPOSED_FIXTURE = ROOT / "conformance-harness" / "examples" / "composed-presentation-privacy.json"

REQUIRED_MATRIX_CSVS = [
    "scenario-index.csv",
    "adr-scenario-map.csv",
    "predicate-scenario-map.csv",
    "threat-scenario-map.csv",
    "ownership-map.csv",
    "maturity-map.csv",
]


def extract_ids(path: Path, pattern: str) -> set:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(pattern, text))


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate_test_rows(rows, source_name, known_predicates, known_adversaries, known_scenarios,
                       seen_ids, level_type_counts, errors):
    valid_levels = {"CL-1", "CL-2", "CL-3", "CL-4"}
    valid_types = {"positive", "negative"}

    for i, row in enumerate(rows, start=2):
        test_id = row.get("test_id", "")
        level = row.get("level", "")
        sid = row.get("scenario_id", "")
        test_type = row.get("test_type", "")
        preds = [p for p in row.get("predicate_ids", "").split(";") if p]
        adv = row.get("adversary_id", "")

        if not test_id:
            errors.append(f"{source_name}:{i}: missing test_id")
        elif test_id in seen_ids:
            errors.append(f"{source_name}:{i}: duplicate test_id '{test_id}'")
        else:
            seen_ids.add(test_id)

        if level not in valid_levels:
            errors.append(f"{source_name}:{i}: unknown level '{level}' (expected one of {sorted(valid_levels)})")
        if sid not in known_scenarios:
            errors.append(f"{source_name}:{i}: unknown scenario_id '{sid}'")
        if test_type not in valid_types:
            errors.append(f"{source_name}:{i}: test_type must be 'positive' or 'negative', got '{test_type}'")
        for p in preds:
            if p not in known_predicates:
                errors.append(f"{source_name}:{i}: unknown predicate_id '{p}' in predicate_ids")
        if adv and adv not in known_adversaries:
            errors.append(f"{source_name}:{i}: unknown adversary_id '{adv}'")
        if not row.get("description", "").strip():
            errors.append(f"{source_name}:{i}: empty description (placeholder row)")
        if not row.get("expected_result", "").strip():
            errors.append(f"{source_name}:{i}: empty expected_result (placeholder row)")

        if level in valid_levels and test_type in valid_types:
            level_type_counts.setdefault(level, {"positive": 0, "negative": 0})
            level_type_counts[level][test_type] += 1


def main() -> int:
    errors = []

    for required in [TAXONOMY_PREDICATES, TAXONOMY_ADVERSARIES, SCENARIO_CORPUS,
                     TEST_MATRIX, COMPOSED_TEST_MATRIX, COMPOSED_FIXTURE]:
        if not required.exists():
            errors.append(f"Missing required file: {required.relative_to(ROOT)}")
    if errors:
        print("Documentation validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    known_predicates = extract_ids(TAXONOMY_PREDICATES, r"\bPR-[A-Z]{3}\b")
    known_adversaries = extract_ids(TAXONOMY_ADVERSARIES, r"\bADV-[A-Z]{1,2}\b")
    known_scenarios = extract_ids(SCENARIO_CORPUS, r"\bUC-\d{3}\b")
    known_adrs = {p.stem.split("-")[0] + "-" + p.stem.split("-")[1]
                  for p in ADR_DIR.glob("ADR-*.md") if p.stem != "ADR-TEMPLATE"}

    if not known_predicates:
        errors.append(f"No PR-xxx predicate IDs found in {TAXONOMY_PREDICATES.relative_to(ROOT)}")
    if not known_adversaries:
        errors.append(f"No ADV-x adversary IDs found in {TAXONOMY_ADVERSARIES.relative_to(ROOT)}")
    if not known_scenarios:
        errors.append(f"No UC-NNN scenario IDs found in {SCENARIO_CORPUS.relative_to(ROOT)}")

    for name in REQUIRED_MATRIX_CSVS:
        path = MATRICES_DIR / name
        if not path.exists():
            errors.append(f"Missing required matrix: {path.relative_to(ROOT)}")
            continue
        rows = read_csv_rows(path)
        if not rows:
            errors.append(f"Placeholder matrix (header only, no data rows): {path.relative_to(ROOT)}")

    pred_scenario_path = MATRICES_DIR / "predicate-scenario-map.csv"
    if pred_scenario_path.exists():
        for i, row in enumerate(read_csv_rows(pred_scenario_path), start=2):
            pid, sid = row.get("predicate_id", ""), row.get("scenario_id", "")
            if pid not in known_predicates:
                errors.append(f"{pred_scenario_path.name}:{i}: unknown predicate_id '{pid}'")
            if sid not in known_scenarios:
                errors.append(f"{pred_scenario_path.name}:{i}: unknown scenario_id '{sid}'")
            if row.get("required_optional") not in ("required", "optional"):
                errors.append(f"{pred_scenario_path.name}:{i}: required_optional must be 'required' or 'optional', got '{row.get('required_optional')}'")

    threat_scenario_path = MATRICES_DIR / "threat-scenario-map.csv"
    if threat_scenario_path.exists():
        for i, row in enumerate(read_csv_rows(threat_scenario_path), start=2):
            aid, sid = row.get("adversary_id", ""), row.get("scenario_id", "")
            if aid not in known_adversaries:
                errors.append(f"{threat_scenario_path.name}:{i}: unknown adversary_id '{aid}'")
            if sid not in known_scenarios:
                errors.append(f"{threat_scenario_path.name}:{i}: unknown scenario_id '{sid}'")

    adr_scenario_path = MATRICES_DIR / "adr-scenario-map.csv"
    if adr_scenario_path.exists():
        for i, row in enumerate(read_csv_rows(adr_scenario_path), start=2):
            adr_id, sid = row.get("adr_id", ""), row.get("scenario_id", "")
            if adr_id not in known_adrs:
                errors.append(f"{adr_scenario_path.name}:{i}: unknown adr_id '{adr_id}'")
            if sid not in known_scenarios:
                errors.append(f"{adr_scenario_path.name}:{i}: unknown scenario_id '{sid}'")

    scenario_index_path = MATRICES_DIR / "scenario-index.csv"
    if scenario_index_path.exists():
        for i, row in enumerate(read_csv_rows(scenario_index_path), start=2):
            sid = row.get("scenario_id", "")
            if sid not in known_scenarios:
                errors.append(f"{scenario_index_path.name}:{i}: unknown scenario_id '{sid}'")
            if row.get("priority") not in ("P0", "P1", "P2"):
                errors.append(f"{scenario_index_path.name}:{i}: priority must be P0/P1/P2, got '{row.get('priority')}'")

    assurance_path = CONFORMANCE_DIR / "assurance-test-dispositions.csv"
    if assurance_path.exists():
        seen_assurance = set()
        for i, row in enumerate(read_csv_rows(assurance_path), start=2):
            aid, sid = row.get("assurance_test_id", ""), row.get("scenario_id", "")
            if not aid or aid in seen_assurance:
                errors.append(f"{assurance_path.name}:{i}: missing or duplicate assurance_test_id '{aid}'")
            seen_assurance.add(aid)
            if sid not in known_scenarios:
                errors.append(f"{assurance_path.name}:{i}: unknown scenario_id '{sid}'")
            if row.get("status") not in ("defined", "executed", "passed", "failed"):
                errors.append(f"{assurance_path.name}:{i}: invalid status '{row.get('status')}'")

    legacy_rows = read_csv_rows(TEST_MATRIX)
    composed_rows = read_csv_rows(COMPOSED_TEST_MATRIX)
    if not legacy_rows:
        errors.append(f"Placeholder conformance suite (header only): {TEST_MATRIX.relative_to(ROOT)}")
    if not composed_rows:
        errors.append(f"Placeholder composed-presentation suite (header only): {COMPOSED_TEST_MATRIX.relative_to(ROOT)}")

    seen_ids = set()
    level_type_counts = {}
    validate_test_rows(legacy_rows, TEST_MATRIX.name, known_predicates, known_adversaries,
                       known_scenarios, seen_ids, level_type_counts, errors)
    validate_test_rows(composed_rows, COMPOSED_TEST_MATRIX.name, known_predicates, known_adversaries,
                       known_scenarios, seen_ids, level_type_counts, errors)

    fixture_data = json.loads(COMPOSED_FIXTURE.read_text(encoding="utf-8"))
    fixture_ids = {case.get("id") for case in fixture_data.get("cases", [])}
    referenced_fixture_ids = set()
    for i, row in enumerate(composed_rows, start=2):
        fid = row.get("fixture_case_id", "")
        if not fid:
            errors.append(f"{COMPOSED_TEST_MATRIX.name}:{i}: missing fixture_case_id")
        elif fid not in fixture_ids:
            errors.append(f"{COMPOSED_TEST_MATRIX.name}:{i}: unknown fixture_case_id '{fid}'")
        else:
            referenced_fixture_ids.add(fid)
    orphan_fixtures = fixture_ids - referenced_fixture_ids
    if orphan_fixtures:
        errors.append(f"Unreferenced composed-presentation fixture cases: {sorted(orphan_fixtures)}")

    for level in sorted(level_type_counts):
        counts = level_type_counts[level]
        if counts["positive"] == 0:
            errors.append(f"Conformance level {level} has no positive test case")
        if counts["negative"] == 0:
            errors.append(f"Conformance level {level} has no negative test case")

    if errors:
        print("Conformance validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    total = len(legacy_rows) + len(composed_rows)
    print("Conformance validation passed.")
    print(f"scripts/validate_conformance.py: {total}/{total} aggregate test rows OK across {len(level_type_counts)} conformance levels")
    print(f"  legacy matrix: {len(legacy_rows)} rows")
    print(f"  composed-presentation matrix: {len(composed_rows)} rows / {len(fixture_ids)} executable semantic fixtures")
    for level in sorted(level_type_counts):
        c = level_type_counts[level]
        print(f"  {level}: {c['positive']} positive / {c['negative']} negative")
    return 0


if __name__ == "__main__":
    sys.exit(main())
