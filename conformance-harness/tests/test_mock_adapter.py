from dtgwg_zkp_conformance.adapters.mock import MockAdapter
def test_positive_and_negative():
 a=MockAdapter(); assert a.execute("verify",{"mock_case":"valid-bound-proof"}).status=="accepted"; assert a.execute("verify",{"mock_case":"transaction-mismatch"}).reason_code=="transcript-binding-mismatch"
