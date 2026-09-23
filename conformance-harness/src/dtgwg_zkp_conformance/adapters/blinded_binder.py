from __future__ import annotations

from .base import ConformanceAdapter
from ..models import AdapterResponse


class BlindedBinderAdapter(ConformanceAdapter):
    """Semantic adapter for canonical record 008 blinded-binder boundaries."""

    CAPABILITIES = {"blinded-binder"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_blinded_binder":
            return AdapterResponse("blocked", "unsupported-binder-operation", {})

        if request.get("source_artifact_authenticated") is not True:
            return AdapterResponse("rejected", "source-artifact-unauthenticated", {
                "proofLayer": "commitment-opening-insufficient",
            })

        if request.get("plaintext_citation_visible") is True:
            return AdapterResponse("rejected", "binder-plaintext-present", {
                "privacyLayer": "plaintext-hiding",
            })

        if request.get("opening_valid") is not True:
            return AdapterResponse("rejected", "binder-mismatch", {
                "proofLayer": "commitment-opening",
            })

        if request.get("deterministic_low_entropy_binder") is True:
            return AdapterResponse("rejected", "enumerable-binder-recoverable", {
                "privacyLayer": "dictionary-recovery",
            })

        if request.get("claim_task_completed") is True:
            return AdapterResponse("rejected", "task-completion-not-established", {
                "proofBindingValid": True,
                "semanticBoundary": "task-outcome-external",
            })

        if request.get("visible_stable_commitment") is True and request.get("claim_unlinkable") is True:
            return AdapterResponse("rejected", "stable-binder-correlatable", {
                "proofBindingValid": True,
                "privacyLayer": "presentation-correlation",
            })

        return AdapterResponse("accepted", "binder-opening-accepted", {
            "proofBindingValid": True,
            "plaintextHidden": True,
            "presentationUnlinkabilityEstablished": request.get("visible_stable_commitment") is False,
        })
