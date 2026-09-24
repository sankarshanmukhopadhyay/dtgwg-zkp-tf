from __future__ import annotations

from .base import ConformanceAdapter
from .status_root import StatusRootAdapter
from .transcript import TranscriptBindingAdapter
from ..models import AdapterResponse


class CommunityAnchoredProofAdapter(ConformanceAdapter):
    """Construction-neutral semantic composition for canonical record 010."""

    CAPABILITIES = {"community-anchored-proof"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_community_anchored_proof":
            return AdapterResponse("blocked", "unsupported-cap-operation", {})

        if request.get("relationship_credential_authentic") is not True:
            return AdapterResponse("rejected", "vrc-signature-invalid", {})

        if request.get("presenter_membership_path_valid") is not True:
            return AdapterResponse("rejected", "presenter-not-member", {"component": "001"})

        if request.get("voucher_membership_path_valid") is not True:
            return AdapterResponse("rejected", "voucher-not-member", {"component": "001"})

        if request.get("same_community_root") is not True:
            return AdapterResponse("rejected", "community-root-mismatch", {"component": "001"})

        linkage_mode = request.get("voucher_linkage_mode")
        if linkage_mode == "directed-same-identifier":
            pass
        elif linkage_mode == "co-control-attestation":
            if request.get("voucher_linkage_artifact_valid") is not True:
                return AdapterResponse("rejected", "voucher-linkage-invalid", {"component": "007"})
        else:
            return AdapterResponse("blocked", "voucher-linkage-unavailable", {
                "component": "007",
                "required": ["directed-same-identifier", "co-control-attestation"],
            })

        if request.get("presenter_linkage_valid") is not True:
            return AdapterResponse("rejected", "presenter-linkage-invalid", {"component": "007"})

        if request.get("distinct_member_leaves") is not True:
            return AdapterResponse("rejected", "self-vouch", {"component": "005"})

        if request.get("holder_binding_valid") is not True:
            return AdapterResponse("rejected", "holder-binding-invalid", {"component": "004"})

        statuses = request.get("statuses")
        if not isinstance(statuses, list) or len(statuses) != 3:
            return AdapterResponse("blocked", "status-evidence-incomplete", {"component": "006"})
        for idx, status_request in enumerate(statuses):
            result = StatusRootAdapter().execute("evaluate_status_root", status_request)
            if result.status != "accepted":
                reason = "handle-revoked" if result.reason_code == "handle-revoked" else result.reason_code
                return AdapterResponse(result.status, reason, {
                    "component": "006",
                    "statusIndex": idx,
                    "statusReason": result.reason_code,
                    **result.output,
                })

        transcript_request = request.get("transcript")
        if not isinstance(transcript_request, dict):
            return AdapterResponse("blocked", "transcript-evidence-missing", {"component": "003"})
        transcript = TranscriptBindingAdapter().execute("evaluate_transcript_binding", transcript_request)
        if transcript.status != "accepted":
            return AdapterResponse(transcript.status, transcript.reason_code, {
                "component": "003",
                **transcript.output,
            })

        if request.get("reuse_detection_declared") is True:
            if not request.get("scoped_nullifier_present"):
                return AdapterResponse("rejected", "scoped-nullifier-missing", {"component": "002"})
        elif request.get("scoped_nullifier_present"):
            return AdapterResponse("rejected", "undeclared-nullifier-present", {"component": "002"})

        if request.get("reusable_cross_context_binder") is True:
            return AdapterResponse("rejected", "cross-context-linkability", {
                "privacyBoundary": "P4",
            })

        if request.get("claim_counterparty_consent_to_disclosure") is True:
            return AdapterResponse("rejected", "counterparty-consent-not-established", {
                "semanticBoundary": "record-010-does-not-establish",
            })

        return AdapterResponse("accepted", "community-anchored-proof-semantics-satisfied", {
            "canonicalRecord": "010",
            "components": ["001", "002", "003", "004", "005", "006", "007"],
            "voucherOfflineAtPresentation": True,
            "constructionExecutionEstablished": False,
            "crossImplementationEstablished": False,
        })
