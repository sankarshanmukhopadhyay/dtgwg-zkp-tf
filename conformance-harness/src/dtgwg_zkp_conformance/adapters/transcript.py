from __future__ import annotations

from .base import ConformanceAdapter
from ..models import AdapterResponse


class TranscriptBindingAdapter(ConformanceAdapter):
    """Semantic adapter for upstream construction record 003 boundaries."""

    CAPABILITIES = {"transcript-binding"}

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        if operation != "evaluate_transcript_binding":
            return AdapterResponse("blocked", "unsupported-transcript-operation", {})

        proof_digest = request.get("proof_transcript_digest")
        supplied_digest = request.get("supplied_transcript_digest")
        if not proof_digest or not supplied_digest:
            return AdapterResponse("blocked", "transcript-digest-missing", {})

        if proof_digest != supplied_digest:
            return AdapterResponse("rejected", "transcript-digest-mismatch", {
                "proofTranscriptDigest": proof_digest,
                "suppliedTranscriptDigest": supplied_digest,
            })

        if request.get("canonical_encoding_valid") is False:
            return AdapterResponse("rejected", "canonical-encoding-invalid", {
                "proofBindingValid": True,
                "policyLayer": "canonicalization",
            })

        if request.get("predicate_accepted") is False:
            return AdapterResponse("rejected", "predicate-not-accepted", {
                "proofBindingValid": True,
                "policyLayer": "predicate-acceptance",
            })

        if request.get("audience_match") is False:
            return AdapterResponse("rejected", "audience-mismatch", {
                "proofBindingValid": True,
                "policyLayer": "verifier-policy",
            })

        if request.get("context_match") is False:
            return AdapterResponse("rejected", "context-mismatch", {
                "proofBindingValid": True,
                "policyLayer": "verifier-policy",
            })

        if request.get("challenge_match") is False:
            return AdapterResponse("rejected", "challenge-mismatch", {
                "proofBindingValid": True,
                "policyLayer": "verifier-policy",
            })

        if request.get("expired") is True:
            return AdapterResponse("rejected", "transcript-expired", {
                "proofBindingValid": True,
                "policyLayer": "freshness",
            })

        if request.get("replay_seen") is True:
            return AdapterResponse("rejected", "transcript-replay", {
                "proofBindingValid": True,
                "policyLayer": "replay-policy",
            })

        return AdapterResponse("accepted", "transcript-bound-and-policy-accepted", {
            "proofBindingValid": True,
            "canonicalEncodingChecked": request.get("canonical_encoding_valid") is True,
            "predicateAcceptanceChecked": request.get("predicate_accepted") is True,
            "freshnessChecked": request.get("expired") is False,
            "replayChecked": request.get("replay_seen") is False,
        })
