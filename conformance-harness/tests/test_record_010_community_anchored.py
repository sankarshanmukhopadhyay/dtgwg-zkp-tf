import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.community_anchored import CommunityAnchoredProofAdapter


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "record-010-community-anchored-proof.json"
MATRIX = ROOT / "docs" / "implementation-guide" / "conformance" / "record-010-requirement-matrix.json"


def test_record_010_fixture_suite():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    adapter = CommunityAnchoredProofAdapter()
    for case in suite["cases"]:
        response = adapter.execute("evaluate_community_anchored_proof", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_success_is_semantic_not_construction_promotion():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    positive = suite["cases"][0]
    response = CommunityAnchoredProofAdapter().execute("evaluate_community_anchored_proof", positive["input"])
    assert response.status == "accepted"
    assert response.output["constructionExecutionEstablished"] is False
    assert response.output["crossImplementationEstablished"] is False


def test_requirement_matrix_covers_adr_surface():
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    ids = {row["id"] for row in matrix["requirements"]}
    expected = {f"P{n}" for n in range(1,6)} | {f"S{n}" for n in range(1,6)} | {f"C{n}" for n in range(1,5)} | {f"T{n}" for n in range(1,5)} | {f"D{n}" for n in range(1,4)} | {f"X{n}" for n in range(1,4)}
    assert ids == expected


def test_clause_3_without_linkage_is_blocked_not_accepted():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    case = next(c for c in suite["cases"] if c["name"] == "LINKAGE-MISSING")
    response = CommunityAnchoredProofAdapter().execute("evaluate_community_anchored_proof", case["input"])
    assert response.status == "blocked"
    assert response.reason_code == "voucher-linkage-unavailable"
