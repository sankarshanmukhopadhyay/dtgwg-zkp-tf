import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.identifier_compatibility import IdentifierCompatibilityAdapter


ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "record-007-identifier-compatibility.json"


def test_record_007_compatibility_matrix():
    suite = json.loads(MATRIX.read_text(encoding="utf-8"))
    adapter = IdentifierCompatibilityAdapter()
    for case in suite["cases"]:
        response = adapter.execute("assess_record_007_compatibility", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_hidden_equality_does_not_become_common_control():
    response = IdentifierCompatibilityAdapter().execute(
        "assess_record_007_compatibility",
        {
            "same_identifier": False,
            "relation": "hidden-field-equality",
            "controller_secret_available": False,
            "identifier_method": "credential-field",
            "document_extensible": False,
            "zk_openable_commitment_present": False,
        },
    )
    assert response.reason_code == "use-record-009-not-007"


def test_counterparty_secret_cannot_be_assumed_available():
    response = IdentifierCompatibilityAdapter().execute(
        "assess_record_007_compatibility",
        {
            "same_identifier": False,
            "relation": "common-control",
            "controller_secret_available": False,
            "counterparty_produced_linkage": False,
            "identifier_method": "counterparty-identifier",
            "document_extensible": True,
            "zk_openable_commitment_present": True,
        },
    )
    assert response.reason_code == "controller-witness-unavailable"
