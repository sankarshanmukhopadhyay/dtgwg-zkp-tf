from dtgwg_zkp_conformance.runner import run_manifest
from dtgwg_zkp_conformance.adapters.mock import MockAdapter
def test_runner_passes_matching_case():
 m={"implementation":{"name":"m"},"profile":"CL-1","tests":[{"test_id":"CT-X","operation":"verify","expected_status":"accepted","request":{"mock_case":"valid-bound-proof"}}]}
 assert run_manifest(m,MockAdapter())["results"][0]["status"]=="PASS"
