import json
from pathlib import Path

from dtgwg_zkp_conformance.adapters.authority_chain import AuthorityChainAdapter


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "docs" / "implementation-guide" / "conformance" / "fixtures" / "record-021-vac-authority-chain.json"


def test_record_021_fixture_suite():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    adapter = AuthorityChainAdapter()
    for case in suite["cases"]:
        response = adapter.execute("evaluate_vac_authority_chain", case["input"])
        assert [response.status, response.reason_code] == case["expected"], case["id"]


def test_success_does_not_establish_delegation_or_task_completion():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    positive = next(case for case in suite["cases"] if case["id"] == "R021-POS-001")
    response = AuthorityChainAdapter().execute("evaluate_vac_authority_chain", positive["input"])
    assert response.status == "accepted"
    assert response.output["authorityEstablished"] is True
    assert response.output["delegationEstablished"] is False
    assert response.output["taskCompletionEstablished"] is False


def test_chain_link_equality_uses_record_009_boundary():
    suite = json.loads(FIXTURES.read_text(encoding="utf-8"))
    case = next(case for case in suite["cases"] if case["id"] == "R021-NEG-ISSUER")
    response = AuthorityChainAdapter().execute("evaluate_vac_authority_chain", case["input"])
    assert response.output["component"] == "009"
    assert response.output["semanticRoute"] == "hidden-value-equality"
