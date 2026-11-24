import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFORMANCE = ROOT / "docs/implementation-guide/conformance"


def test_changed_canonical_records_do_not_inherit_old_evidence():
    delta = json.loads((CONFORMANCE / "canonical-reconciliation.json").read_text())
    rows = {row["record"]: row for row in delta["record_impacts"]}
    for record in ("007", "009", "010", "013"):
        assert rows[record]["disposition"] == "stale"
    for record in ("022", "024", "025"):
        assert rows[record]["disposition"] == "not_assessed"
    assert rows["006"]["disposition"] == "retest_required"


def test_historical_evidence_pin_is_not_observed_head():
    delta = json.loads((CONFORMANCE / "canonical-reconciliation.json").read_text())
    gates = json.loads((CONFORMANCE / "evidence-promotion-gates.json").read_text())
    assert gates["authority"]["upstream_commit"] == delta["canonical"]["prior_revision"]
    assert gates["authority"]["upstream_commit"] != delta["canonical"]["current_revision"]
