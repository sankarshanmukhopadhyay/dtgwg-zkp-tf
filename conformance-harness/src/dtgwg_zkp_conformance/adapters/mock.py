from .base import ConformanceAdapter
from ..models import AdapterResponse

class MockAdapter(ConformanceAdapter):
    """NON-CRYPTOGRAPHIC TEST DOUBLE. NOT A REFERENCE ZKP IMPLEMENTATION."""
    def describe_capabilities(self):
        return {"transcript-binding","expiry","context-binding","delegation-binding","profile-negotiation","decision-receipt","relationship-linkage","task-binding","authority-separation","correlation-boundary"}
    def execute(self, operation, request):
        case=request.get("mock_case")
        table={
          "valid-bound-proof": ("accepted","ok"),
          "transaction-mismatch": ("rejected","transcript-binding-mismatch"),
          "valid-scoped-nullifier": ("accepted","ok"),
          "context-substitution": ("rejected","context-mismatch"),
          "valid-delegation": ("accepted","ok"),
          "agent-key-swap": ("rejected","delegation-key-mismatch"),
          "supported-profile": ("accepted","ok"),
          "unsupported-profile": ("rejected","unsupported-profile"),
          "valid-relationship-evidence": ("accepted","ok"),
          "implicit-co-possession": ("rejected","relationship-not-established"),
          "valid-task-binding": ("accepted","ok"),
          "task-replay": ("rejected","task-binding-mismatch"),
          "valid-proof-and-delegation": ("accepted","ok"),
          "ceremony-without-delegation": ("rejected","delegation-absent-or-revoked"),
          "scoped-reference": ("accepted","ok"),
          "stable-cross-context-handle": ("rejected","cross-context-correlation"),
        }
        status,reason=table.get(case,("blocked","unsupported-mock-case"))
        return AdapterResponse(status,reason,{"operation":operation,"mock_case":case})
