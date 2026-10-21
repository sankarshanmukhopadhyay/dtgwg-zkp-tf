import json
from pathlib import Path
from dtgwg_zkp_conformance.adapters.sorted_neighbours import (
    adjacent_neighbours_claim_absent, guarded_non_membership, is_strictly_sorted
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "docs/implementation-guide/conformance/fixtures/record-006-sortedness.json"

def test_canonical_006_sortedness_counterexamples():
    rows = json.loads(FIXTURE.read_text())["cases"]
    for row in rows:
        assert adjacent_neighbours_claim_absent(row["handles"], row["handle"], row["index"]) is row["naive"], row["id"]
        assert guarded_non_membership(row["handles"], row["handle"], row["index"]) is row["guarded"], row["id"]

def test_present_handle_can_falsely_appear_absent_without_sorting():
    handles = [1, 7, 5, 9]
    assert 5 in handles
    assert adjacent_neighbours_claim_absent(handles, 5, 0)
    assert not is_strictly_sorted(handles)
    assert not guarded_non_membership(handles, 5, 0)
