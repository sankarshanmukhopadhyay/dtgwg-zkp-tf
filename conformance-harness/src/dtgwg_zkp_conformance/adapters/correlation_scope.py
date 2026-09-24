from __future__ import annotations

from .base import ConformanceAdapter
from ..models import AdapterResponse


class CorrelationScopeAdapter(ConformanceAdapter):
    """Validate correlation-scope semantics without inventing a serialization term."""

    CAPABILITIES = {"correlation-scope-semantics"}
    ALLOWED = {"pairwise", "directed", "public"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_correlation_scope":
            return AdapterResponse("blocked", "unsupported-correlation-operation", {})

        declared = request.get("declared_scope")
        if declared not in self.ALLOWED:
            return AdapterResponse("rejected", "invalid-correlation-scope", {
                "allowed": sorted(self.ALLOWED),
                "declared": declared,
            })

        if request.get("scope_inferred_from_role") is True:
            return AdapterResponse("rejected", "role-scope-conflation", {
                "role": request.get("role"),
                "declaredScope": declared,
            })

        required_max = request.get("required_max_scope")
        order = {"pairwise": 0, "directed": 1, "public": 2}
        if required_max in self.ALLOWED and order[declared] > order[required_max]:
            return AdapterResponse("rejected", "scope-too-broad-for-context", {
                "declaredScope": declared,
                "requiredMaxScope": required_max,
            })

        return AdapterResponse("accepted", "correlation-scope-accepted", {
            "declaredScope": declared,
            "role": request.get("role"),
            "serializationProperty": None,
            "contextTerm": None,
        })
