import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.blinded_binder import BlindedBinderAdapter


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "record-008-blinded-binder.json"


def test_record_008_fixture_suite():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    adapter = BlindedBinderAdapter()
    for case in suite["cases"]:
        response = adapter.execute("evaluate_blinded_binder", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_visible_commitment_can_bind_without_establishing_unlinkability():
    adapter = BlindedBinderAdapter()
    response = adapter.execute(
        "evaluate_blinded_binder",
        {
            "source_artifact_authenticated": True,
            "plaintext_citation_visible": False,
            "opening_valid": True,
            "deterministic_low_entropy_binder": False,
            "visible_stable_commitment": True,
            "claim_unlinkable": False,
            "claim_task_completed": False,
        },
    )
    assert response.status == "accepted"
    assert response.output["presentationUnlinkabilityEstablished"] is False


def test_task_completion_is_outside_record_008():
    adapter = BlindedBinderAdapter()
    response = adapter.execute(
        "evaluate_blinded_binder",
        {
            "source_artifact_authenticated": True,
            "plaintext_citation_visible": False,
            "opening_valid": True,
            "deterministic_low_entropy_binder": False,
            "visible_stable_commitment": False,
            "claim_unlinkable": False,
            "claim_task_completed": True,
        },
    )
    assert response.reason_code == "task-completion-not-established"
