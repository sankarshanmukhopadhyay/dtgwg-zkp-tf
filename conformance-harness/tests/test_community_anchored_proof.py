import json
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "community-anchored-proof.json"


def evaluate(case):
    i = case["inputs"]

    if not i["third_party_membership_evidence_checkable"]:
        return "indeterminate"
    if not i["holder_relationship_credential"] or not i["holder_membership_same_community"]:
        return "fail"
    if not i["counterparty_membership_same_community"]:
        return "fail"
    if not i["holder_bound"] or not i["challenge_bound"]:
        return "fail"
    if not i["credentials_current"]:
        return "fail"
    if not i["status_private"]:
        return "fail"
    if i["reusable_binder"]:
        return "fail"
    return "pass"


def test_community_anchored_proof_semantics():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert data["source"] == "https://docs.fpp.storm.ws/dtg-community-anchored-proof-adr.html"
    cases = data["cases"]
    assert {case["id"] for case in cases} == {f"CAP-{n:03d}" for n in range(1, 8)}
    assert {case["name"] for case in cases} >= {"ACCEPTS", "REJECTS", "UNLINKABLE", "CURRENT"}
    for case in cases:
        assert evaluate(case) == case["expected"], case["id"]
        assert case["predicate_ids"]


def test_clause_3_missing_evidence_is_not_silently_accepted():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    clause3 = next(case for case in data["cases"] if case["id"] == "CAP-006")
    assert evaluate(clause3) == "indeterminate"
