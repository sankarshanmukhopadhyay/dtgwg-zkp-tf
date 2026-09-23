from __future__ import annotations

from .base import ConformanceAdapter
from ..models import AdapterResponse


class StatusRootAdapter(ConformanceAdapter):
    """Semantic adapter for record 006 plus explicit verifier-side boundaries."""

    CAPABILITIES = {"status-root-currentness"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_status_root":
            return AdapterResponse("blocked", "unsupported-status-operation", {})

        if request.get("root_known") is not True:
            return AdapterResponse("rejected", "status-root-unknown", {
                "proofLayer": "not-evaluable",
                "policyLayer": "root-selection",
            })

        if request.get("root_authentic") is not True:
            return AdapterResponse("rejected", "status-root-unauthenticated", {
                "proofLayer": "not-authoritative",
                "policyLayer": "root-authenticity",
            })

        age = request.get("root_age_seconds")
        max_age = request.get("max_age_seconds")
        if not isinstance(age, int) or not isinstance(max_age, int) or age < 0 or max_age < 0:
            return AdapterResponse("blocked", "status-freshness-input-invalid", {})
        if age > max_age:
            return AdapterResponse("rejected", "rl-root-stale", {
                "proofLayer": "not-evaluated",
                "policyLayer": "freshness",
                "rootAgeSeconds": age,
                "maxAgeSeconds": max_age,
            })

        if request.get("proof_non_membership_valid") is not True:
            reason = "handle-revoked" if request.get("handle_revoked") is True else "non-membership-proof-invalid"
            return AdapterResponse("rejected", reason, {
                "proofLayer": "non-membership",
                "rootAgeSeconds": age,
            })

        acquisition = request.get("acquisition_mode")
        if acquisition == "holder-carried" and request.get("snapshot_authenticated") is not True:
            return AdapterResponse("rejected", "carried-snapshot-unauthenticated", {
                "proofBindingValid": True,
                "policyLayer": "root-distribution",
            })
        if acquisition == "live-subject-specific" and request.get("authority_observation_declared") is not True:
            return AdapterResponse("rejected", "status-privacy-degradation-undeclared", {
                "proofBindingValid": True,
                "policyLayer": "privacy",
            })
        if acquisition not in {"shared-cache", "holder-carried", "live-subject-specific"}:
            return AdapterResponse("blocked", "status-acquisition-mode-unsupported", {})

        return AdapterResponse("accepted", "non-revoked-at-accepted-root-state", {
            "proofBindingValid": True,
            "rootAuthenticityChecked": True,
            "freshnessChecked": True,
            "acquisitionMode": acquisition,
            "authorityObservationDeclared": request.get("authority_observation_declared") is True,
        })
