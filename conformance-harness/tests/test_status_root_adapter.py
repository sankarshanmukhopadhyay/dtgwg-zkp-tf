import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.status_root import StatusRootAdapter


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "record-006-status-root.json"


def test_record_006_fixture_suite():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    adapter = StatusRootAdapter()
    for case in suite["cases"]:
        response = adapter.execute("evaluate_status_root", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_proof_validity_does_not_establish_root_authority():
    adapter = StatusRootAdapter()
    response = adapter.execute("evaluate_status_root", {
        "root_known": True,
        "root_authentic": False,
        "root_age_seconds": 10,
        "max_age_seconds": 300,
        "proof_non_membership_valid": True,
        "handle_revoked": False,
        "acquisition_mode": "shared-cache",
        "authority_observation_declared": False,
    })
    assert response.reason_code == "status-root-unauthenticated"


def test_live_lookup_requires_declared_privacy_degradation():
    adapter = StatusRootAdapter()
    response = adapter.execute("evaluate_status_root", {
        "root_known": True,
        "root_authentic": True,
        "root_age_seconds": 0,
        "max_age_seconds": 0,
        "proof_non_membership_valid": True,
        "handle_revoked": False,
        "acquisition_mode": "live-subject-specific",
        "authority_observation_declared": False,
    })
    assert response.reason_code == "status-privacy-degradation-undeclared"
