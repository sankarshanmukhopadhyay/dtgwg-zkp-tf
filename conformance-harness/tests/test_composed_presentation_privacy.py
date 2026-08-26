import json
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "composed-presentation-privacy.json"


def evaluate(case):
    i = case["inputs"]
    cid = case["id"]

    if cid == "CP-PRIV-001":
        return "fail" if i["stable_lookup_reference"] and i["lookup_linkable"] and not i["declared_correlation"] else "pass"
    if cid == "CP-PRIV-002":
        return "fail" if i["ancestry_disclosed"] and i["ancestry_cross_context_linkable"] and not i["governance_requires_ancestry"] else "pass"
    if cid == "CP-PRIV-003":
        return "fail" if i["deterministic_digest_only"] and i["input_feasibly_enumerable"] else "pass"
    if cid == "CP-PRIV-004":
        return "fail" if i["predicate_requires_set_membership_only"] and i["exact_issuer_disclosed"] and not i["governance_requires_exact_issuer"] else "pass"
    if cid == "CP-PRIV-005":
        return "fail" if i["components_private_standalone"] and i["shared_cross_context_handle"] else "pass"
    if cid == "CP-PRIV-006":
        return "fail" if i["verifier_originated_live_lookup"] and i["service_observes_verification"] and not i["observation_declared"] else "pass"
    if cid == "CP-PRIV-007":
        return "fail" if i["shared_proof_primitive"] and i["semantics_collapsed"] else "pass"
    if cid == "CP-PRIV-008":
        return "pass" if i["private_half_hidden"] and i["public_half_exposed"] and not i["reusable_private_binder"] and i["claim_subject"] == "credential-half" else "fail"
    if cid == "CP-PRIV-009":
        return "fail" if i["public_half_exposed"] and i["claim_relationship_unlinkable"] else "pass"
    if cid == "CP-PRIV-010":
        return "fail" if i["proof_valid"] and i["reusable_private_binder"] and i["cross_context_comparison"] else "pass"
    if cid == "CP-PRIV-011":
        return "fail" if i["private_half_hidden"] and i["public_graph_joinable"] and i["claim_context_unlinkable"] else "pass"
    if cid == "CP-PRIV-012":
        return "indeterminate" if i["proof_valid"] and not i["common_vtn_evidenced"] and i["claim_common_vtn"] else "pass"
    if cid == "CP-PRIV-013":
        return "pass" if i["both_halves_privately_proven"] and not i["reusable_binder"] and not i["contradictory_public_context"] and i["construction_evidence_complete"] else "fail"
    raise AssertionError(f"unknown composed privacy case: {cid}")


def test_composed_presentation_privacy_semantics():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    cases = data["cases"]
    assert {case["id"] for case in cases} == {f"CP-PRIV-{n:03d}" for n in range(1, 14)}
    for case in cases:
        assert evaluate(case) == case["expected"], case["id"]
        assert case["predicate_ids"]
        assert case["scenario_id"].startswith("UC-")
        assert case["adversary_id"].startswith("ADV-")
