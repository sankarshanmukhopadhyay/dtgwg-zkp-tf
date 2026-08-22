import json
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "pr-res-profiles.json"


def evaluate(case):
    profile = case["profile_id"]
    i = case["inputs"]

    if i.get("representation_semantics_collapsed", False):
        return "fail"

    if profile == "RES-BSL-CACHE-01":
        if i["evidence_age_seconds"] > i["max_age_seconds"]:
            return "fail"
        if not i["whole_shared_list"] or i["subject_specific_lookup"]:
            return "fail"
        if i["live_authoritative_lookup"]:
            return "fail"
        return "pass"

    if profile == "RES-CARRIED-SNAPSHOT-01":
        if not i["snapshot_authenticated"] or not i["evidence_binding_verified"]:
            return "fail"
        if i["evidence_age_seconds"] > i["max_age_seconds"]:
            return "fail"
        if i["live_authoritative_lookup"]:
            return "fail"
        return "pass"

    if profile == "RES-LIVE-DECLARED-01":
        if not i["governance_permits_live_lookup"]:
            return "fail"
        if not i["live_authoritative_lookup"]:
            return "fail"
        if not i["authority_observation_declared"]:
            return "fail"
        if i["privacy_claim"] != "degraded":
            return "fail"
        return "pass"

    raise AssertionError(f"unknown PR-RES profile: {profile}")


def test_pr_res_profiles():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    cases = data["cases"]
    assert {case["id"] for case in cases} == {f"PR-RES-{n:03d}" for n in range(1, 10)}
    assert {case["profile_id"] for case in cases} == {
        "RES-BSL-CACHE-01",
        "RES-CARRIED-SNAPSHOT-01",
        "RES-LIVE-DECLARED-01",
    }
    for case in cases:
        assert case["predicate_ids"] == ["PR-RES"]
        assert evaluate(case) == case["expected"], case["id"]


def test_at_least_one_profile_avoids_verifier_authority_lookup():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    passing = [case for case in data["cases"] if case["expected"] == "pass"]
    assert any(not case["inputs"].get("live_authoritative_lookup", False) for case in passing)


def test_live_lookup_requires_explicit_privacy_degradation():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    live_cases = [case for case in data["cases"] if case["profile_id"] == "RES-LIVE-DECLARED-01"]
    assert any(case["expected"] == "fail" for case in live_cases)
    assert any(
        case["expected"] == "pass"
        and case["inputs"]["authority_observation_declared"]
        and case["inputs"]["privacy_claim"] == "degraded"
        for case in live_cases
    )
