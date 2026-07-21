from .base import ConformanceAdapter
from ..models import AdapterResponse

class MockAdapter(ConformanceAdapter):
    """NON-CRYPTOGRAPHIC TEST DOUBLE. NOT A REFERENCE ZKP IMPLEMENTATION."""
    def describe_capabilities(self):
        return {"transcript-binding","expiry","context-binding","delegation-binding","profile-negotiation","decision-receipt"}
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
        }
        status,reason=table.get(case,("blocked","unsupported-mock-case"))
        return AdapterResponse(status,reason,{"operation":operation,"mock_case":case})
