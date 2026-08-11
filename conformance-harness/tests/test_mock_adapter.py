from dtgwg_zkp_conformance.adapters.mock import MockAdapter
def test_positive_and_negative():
 a=MockAdapter(); assert a.execute("verify",{"mock_case":"valid-bound-proof"}).status=="accepted"; assert a.execute("verify",{"mock_case":"transaction-mismatch"}).reason_code=="transcript-binding-mismatch"

def test_interoperability_boundaries():
 a=MockAdapter()
 assert a.execute("evaluate_relationship",{"mock_case":"implicit-co-possession"}).reason_code=="relationship-not-established"
 assert a.execute("verify_task_binding",{"mock_case":"task-replay"}).reason_code=="task-binding-mismatch"
 assert a.execute("evaluate_authority",{"mock_case":"ceremony-without-delegation"}).reason_code=="delegation-absent-or-revoked"
 assert a.execute("evaluate_correlation",{"mock_case":"stable-cross-context-handle"}).reason_code=="cross-context-correlation"
