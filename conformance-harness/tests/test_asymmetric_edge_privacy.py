import json
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "asymmetric-edge-privacy.json"


def evaluate(case):
    i = case["inputs"]
    cid = case["id"]

    if cid == "AE-PRIV-001":
        return "pass" if i["private_half_hidden"] and i["public_half_exposed"] and not i["reusable_private_binder"] else "fail"
    if cid == "AE-PRIV-002":
        return "fail" if i["public_half_exposed"] and i["claim_relationship_unlinkable"] else "pass"
    if cid == "AE-PRIV-003":
        return "fail" if i["proof_valid"] and i["reusable_private_binder"] and i["cross_context_comparison"] else "pass"
    if cid == "AE-PRIV-004":
        return "fail" if i["public_graph_joinable"] and i["claim_context_unlinkable"] else "pass"
    if cid == "AE-PRIV-005":
        return "indeterminate" if i["proof_valid"] and not i["common_vtn_evidenced"] and i["claim_common_vtn"] else "pass"
    if cid == "AE-PRIV-006":
        return "pass" if i["both_halves_privately_proven"] and not i["reusable_binder"] and not i["contradictory_public_context"] and i["construction_evidence_complete"] else "fail"
    raise AssertionError(f"unknown asymmetric-edge case: {cid}")


def test_asymmetric_edge_privacy_semantics():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    cases = data["cases"]
    assert {case["id"] for case in cases} == {f"AE-PRIV-{n:03d}" for n in range(1, 7)}
    for case in cases:
        assert evaluate(case) == case["expected"], case["id"]
        assert case["predicate_ids"]
        assert case["scenario_id"] == "UC-ASYM-EDGE"
        assert case["claim_subject"] in {"identifier", "credential-half", "relationship", "presentation", "contextual-graph", "trust-context"}
