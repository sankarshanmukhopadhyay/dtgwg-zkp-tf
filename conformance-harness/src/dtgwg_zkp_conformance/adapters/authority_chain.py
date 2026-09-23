from __future__ import annotations

from .base import ConformanceAdapter
from .status_root import StatusRootAdapter
from .transcript import TranscriptBindingAdapter
from ..models import AdapterResponse


class AuthorityChainAdapter(ConformanceAdapter):
    """Downstream semantic pressure-test adapter for canonical record 021."""

    CAPABILITIES = {"vac-authority-chain"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_vac_authority_chain":
            return AdapterResponse("blocked", "unsupported-authority-chain-operation", {})

        if request.get("claim_delegation") is True:
            return AdapterResponse("rejected", "delegation-not-established", {
                "semanticBoundary": "record-021-authority-not-record-020-delegation"
            })

        if request.get("claim_task_completed") is True:
            return AdapterResponse("rejected", "task-completion-not-established", {
                "semanticBoundary": "trust-task-effect-external"
            })

        if request.get("action_conferred") is not True:
            return AdapterResponse("rejected", "action-not-conferred", {})

        if request.get("scope_widened") is True or request.get("validity_extended") is True:
            return AdapterResponse("rejected", "attenuation-widens", {})

        depth = request.get("depth")
        if not isinstance(depth, int) or depth < 1:
            return AdapterResponse("blocked", "chain-depth-invalid", {})
        if depth > 8:
            return AdapterResponse("rejected", "depth-ceiling-exceeded", {"depth": depth})

        if request.get("attenuation_limit_ok") is not True:
            return AdapterResponse("rejected", "attenuation-limit-exceeded", {})

        if request.get("link_issuer_matches_parent_subject") is not True:
            return AdapterResponse("rejected", "link-issuer-mismatch", {
                "component": "009",
                "semanticRoute": "hidden-value-equality"
            })

        if request.get("parent_digest_matches") is not True:
            return AdapterResponse("rejected", "parent-digest-mismatch", {
                "component": "009"
            })

        if request.get("signatures_valid") is not True:
            return AdapterResponse("rejected", "link-signature-invalid", {})

        if request.get("root_governing") is not True:
            return AdapterResponse("rejected", "root-not-governing", {
                "component": "001"
            })

        if request.get("leaf_key_match") is not True:
            return AdapterResponse("rejected", "leaf-key-mismatch", {
                "component": "004"
            })

        status_request = request.get("status")
        if not isinstance(status_request, dict):
            return AdapterResponse("blocked", "status-evidence-missing", {})
        status = StatusRootAdapter().execute("evaluate_status_root", status_request)
        if status.status != "accepted":
            reason = "link-revoked" if status.reason_code == "handle-revoked" else status.reason_code
            return AdapterResponse(status.status, reason, {
                "component": "006",
                "statusReason": status.reason_code,
                **status.output,
            })

        transcript_request = request.get("transcript")
        if not isinstance(transcript_request, dict):
            return AdapterResponse("blocked", "transcript-evidence-missing", {})
        transcript = TranscriptBindingAdapter().execute("evaluate_transcript_binding", transcript_request)
        if transcript.status != "accepted":
            return AdapterResponse(transcript.status, transcript.reason_code, {
                "component": "003",
                **transcript.output,
            })

        if request.get("claim_chain_length_hidden") is True and request.get("fixed_or_padded_shape") is not True:
            return AdapterResponse("rejected", "chain-length-leakage-unmitigated", {
                "privacyBoundary": "proof-shape"
            })

        if request.get("claim_hidden_from_registry") is True and status_request.get("acquisition_mode") == "live-subject-specific":
            return AdapterResponse("rejected", "registry-observation-not-hidden", {
                "privacyBoundary": "status-acquisition"
            })

        return AdapterResponse("accepted", "vac-authority-chain-accepted", {
            "authorityEstablished": True,
            "delegationEstablished": False,
            "taskCompletionEstablished": False,
            "components": ["001", "003", "004", "006", "009"],
            "depth": depth,
        })
