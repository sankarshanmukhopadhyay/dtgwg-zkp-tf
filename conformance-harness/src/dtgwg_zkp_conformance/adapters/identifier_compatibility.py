from __future__ import annotations

from .base import ConformanceAdapter
from ..models import AdapterResponse


class IdentifierCompatibilityAdapter(ConformanceAdapter):
    """Classify implementation compatibility with canonical record 007."""

    CAPABILITIES = {"identifier-common-control-compatibility"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "assess_record_007_compatibility":
            return AdapterResponse("blocked", "unsupported-identifier-operation", {})

        if request.get("same_identifier") is True:
            return AdapterResponse("accepted", "record-007-not-required", {
                "semanticRoute": "same-identifier",
                "note": "No cross-identifier common-control proposition is needed.",
            })

        if request.get("relation") == "hidden-field-equality":
            return AdapterResponse("rejected", "use-record-009-not-007", {
                "semanticRoute": "record-009",
            })

        if request.get("controller_secret_available") is not True:
            if request.get("counterparty_produced_linkage") is True:
                return AdapterResponse("accepted", "counterparty-linkage-artifact-required", {
                    "semanticRoute": "issuance-time-linkage",
                    "presenterWitness": False,
                })
            return AdapterResponse("rejected", "controller-witness-unavailable", {
                "semanticRoute": "external-linkage-required",
            })

        if request.get("zk_openable_commitment_present") is True:
            return AdapterResponse("accepted", "record-007-compatible", {
                "semanticRoute": "common-control",
                "identifierMethod": request.get("identifier_method"),
            })

        if request.get("document_extensible") is False:
            return AdapterResponse("rejected", "identifier-not-zk-openable", {
                "identifierMethod": request.get("identifier_method"),
                "reason": "no place for the required ZK-openable commitment in the selected identifier profile",
            })

        return AdapterResponse("blocked", "zk-openable-commitment-evidence-required", {
            "identifierMethod": request.get("identifier_method"),
            "documentExtensible": request.get("document_extensible"),
        })
