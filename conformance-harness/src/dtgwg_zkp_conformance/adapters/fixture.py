from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Callable

from .base import ConformanceAdapter
from ..models import AdapterResponse


class FixtureAdapter(ConformanceAdapter):
    """Evaluate repository-owned semantic fixtures without a proof system."""

    CAPABILITIES = {
        "attestation-schema",
        "context-governance",
        "lifecycle-bounds",
        "revocation-timing",
        "resource-profile",
        "mediated-fallback",
    }

    def __init__(self, fixture_root: Path):
        self.fixture_root = fixture_root.resolve()
        self.operations: dict[str, Callable[[dict[str, Any]], AdapterResponse]] = {
            "evaluate_attestation_schema": self._attestation_schema,
            "evaluate_context_governance": self._context_governance,
            "evaluate_lifecycle": self._lifecycle,
            "evaluate_revocation_timing": self._revocation_timing,
            "evaluate_resource_profile": self._resource_profile,
            "evaluate_mediated_fallback": self._mediated_fallback,
        }

    def describe_capabilities(self) -> set[str]:
        return set(self.CAPABILITIES)

    def execute(self, operation: str, request: dict) -> AdapterResponse:
        fixture_ref = request.get("fixture")
        if not isinstance(fixture_ref, str) or not fixture_ref:
            return AdapterResponse("blocked", "fixture-reference-missing", {})

        path = (self.fixture_root / fixture_ref).resolve()
        if path != self.fixture_root and self.fixture_root not in path.parents:
            return AdapterResponse("blocked", "fixture-outside-root", {})
        if not path.is_file():
            return AdapterResponse("blocked", "fixture-not-found", {"fixture": fixture_ref})

        raw = path.read_bytes()
        fixture = json.loads(raw)
        if fixture.get("operation") != operation:
            return AdapterResponse(
                "blocked",
                "fixture-operation-mismatch",
                {"fixtureOperation": fixture.get("operation")},
            )
        evaluator = self.operations.get(operation)
        if evaluator is None:
            return AdapterResponse("blocked", "unsupported-fixture-operation", {})

        response = evaluator(fixture.get("input", {}))
        evidence = dict(response.output)
        evidence.update(
            {
                "fixture": fixture_ref,
                "fixtureDigest": f"sha256:{sha256(raw).hexdigest()}",
                "fixtureSchemaVersion": fixture.get("schemaVersion"),
            }
        )
        return AdapterResponse(response.status, response.reason_code, evidence)

    @staticmethod
    def _attestation_schema(data: dict[str, Any]) -> AdapterResponse:
        stable_fingerprint = (
            data.get("assuranceValueScope") != "shared"
            or data.get("issuanceTimeDisclosure") == "exact"
            or bool(data.get("issuerSpecificFields"))
        )
        if stable_fingerprint:
            return AdapterResponse("rejected", "stable-schema-fingerprint", {})
        return AdapterResponse("accepted", "correlation-threshold-satisfied", {})

    @staticmethod
    def _context_governance(data: dict[str, Any]) -> AdapterResponse:
        required = {
            "authority",
            "purpose",
            "verifierSet",
            "epoch",
            "permittedLinkage",
            "prohibitedLinkage",
            "humanLegibleBoundary",
            "collusionTarget",
        }
        missing = sorted(key for key in required if not data.get(key))
        if missing:
            return AdapterResponse(
                "rejected", "context-governance-incomplete", {"missing": missing}
            )
        return AdapterResponse("accepted", "context-governance-complete", {})

    @staticmethod
    def _lifecycle(data: dict[str, Any]) -> AdapterResponse:
        bounded = {
            "rootCryptoperiodDays": data.get("rootCryptoperiodDays"),
            "nullifierEpochDays": data.get("nullifierEpochDays"),
            "retentionDays": data.get("retentionDays"),
            "assuranceHorizonDays": data.get("assuranceHorizonDays"),
        }
        invalid = sorted(
            key for key, value in bounded.items() if not isinstance(value, int) or value <= 0
        )
        if data.get("retentionPolicy") == "indefinite":
            invalid.append("retentionPolicy")
        if invalid:
            return AdapterResponse(
                "rejected", "lifecycle-unbounded", {"invalid": sorted(set(invalid))}
            )
        return AdapterResponse("accepted", "lifecycle-bounded", bounded)

    @staticmethod
    def _revocation_timing(data: dict[str, Any]) -> AdapterResponse:
        suspension = data.get("suspensionEffectiveAt")
        verification = data.get("verificationAt")
        verifiers = data.get("verifiers", [])
        if not isinstance(suspension, int) or not isinstance(verification, int):
            return AdapterResponse("blocked", "invalid-status-timeline", {})
        if len(verifiers) < 2 or any(
            verifier.get("evaluationRule") != "effective-at-verification"
            for verifier in verifiers
        ):
            return AdapterResponse("rejected", "status-semantics-diverged", {})
        decision = "suspended" if suspension <= verification else "active"
        return AdapterResponse(
            "accepted",
            "deterministic-status-outcome",
            {"verifierOutcomes": [decision for _ in verifiers]},
        )

    @staticmethod
    def _resource_profile(data: dict[str, Any]) -> AdapterResponse:
        measurement = data.get("measurement", {})
        ceiling = data.get("ceiling", {})
        minimum = data.get("minimumCapabilities", {})
        capabilities = data.get("deviceCapabilities", {})
        capability_shortfall = sorted(
            key
            for key, value in minimum.items()
            if not isinstance(capabilities.get(key), (int, float))
            or capabilities[key] < value
        )
        if capability_shortfall and not data.get("fallbackPolicyAuthorized"):
            return AdapterResponse(
                "rejected",
                "insufficient-capability-no-fallback",
                {"capabilityShortfall": capability_shortfall},
            )
        exceeded = sorted(
            key
            for key, limit in ceiling.items()
            if not isinstance(measurement.get(key), (int, float))
            or measurement[key] > limit
        )
        if exceeded:
            return AdapterResponse(
                "rejected", "resource-ceiling-exceeded", {"exceeded": exceeded}
            )
        return AdapterResponse(
            "accepted", "resource-ceiling-satisfied", {"measurement": measurement}
        )

    @staticmethod
    def _mediated_fallback(data: dict[str, Any]) -> AdapterResponse:
        if not data.get("fallbackPolicyAuthorized"):
            return AdapterResponse("rejected", "silent-fallback-not-authorized", {})
        if not data.get("verifierFallbackIndicator"):
            return AdapterResponse("rejected", "fallback-indicator-missing", {})
        if data.get("mediatorCanReconstructProtectedInputs") is not False:
            return AdapterResponse("rejected", "mediator-privacy-boundary-failed", {})
        return AdapterResponse(
            "accepted", "authorized-mediated-fallback", {"fallback": "mediated"}
        )
