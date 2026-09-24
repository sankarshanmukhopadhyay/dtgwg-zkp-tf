import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.correlation_scope import CorrelationScopeAdapter


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "correlation-scope-semantics.json"


def test_correlation_scope_fixture_suite():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    adapter = CorrelationScopeAdapter()
    for case in suite["cases"]:
        response = adapter.execute("evaluate_correlation_scope", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_role_never_infers_scope():
    response = CorrelationScopeAdapter().execute(
        "evaluate_correlation_scope",
        {
            "declared_scope": "directed",
            "role": "member",
            "scope_inferred_from_role": True,
            "required_max_scope": "directed",
        },
    )
    assert response.reason_code == "role-scope-conflation"


def test_no_serialization_property_is_invented():
    response = CorrelationScopeAdapter().execute(
        "evaluate_correlation_scope",
        {
            "declared_scope": "pairwise",
            "role": "relationship-counterparty",
            "scope_inferred_from_role": False,
            "required_max_scope": "pairwise",
        },
    )
    assert response.output["serializationProperty"] is None
    assert response.output["contextTerm"] is None
