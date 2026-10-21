#!/usr/bin/env python3
"""Construction-neutral adversarial experiments, NOT a record-013 verifier.

Models observable response/fairness/state behavior only; does not define or
interpret canonical record-013 public inputs or proof statements.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class LocalDecision:
    accepted: bool
    epoch: int
    negotiation: str
    committed: bool


def mutual_observation(a: LocalDecision, b: LocalDecision, *, expected_epoch: int, negotiation: str) -> str:
    """Conservative decision over local booleans, not a canonical protocol."""
    if a.negotiation != negotiation or b.negotiation != negotiation:
        return "REJECTED_REPLAY"
    if a.epoch != expected_epoch or b.epoch != expected_epoch:
        return "INDETERMINATE_STALE_POLICY"
    if not a.committed or not b.committed:
        return "INCOMPLETE_EXCHANGE"
    if not a.accepted or not b.accepted:
        return "NOT_MUTUALLY_ACCEPTED"
    return "LOCALLY_ACCEPTED_NOT_PUBLISHED"


def possible_thresholds(probes: list[tuple[int, bool]], domain: range) -> set[int]:
    """Example adversary learning a secret threshold from observed yes/no replies."""
    return {threshold for threshold in domain
            if all((query >= threshold) == answer for query, answer in probes)}


def leakage_example(secret: int, domain: range) -> dict:
    """Binary search only the observable yes/no oracle. Synthetic policy assumption."""
    candidates = set(domain)
    probes = []
    while len(candidates) > 1:
        test = sorted(candidates)[(len(candidates) - 1) // 2]
        reply = test >= secret
        probes.append((test, reply))
        candidates = possible_thresholds(probes, domain)
    return {"probes": probes, "remaining": candidates, "domain_size": len(domain)}


def cross_epoch_oracle(secret_by_epoch: dict[int, int], domain: range) -> dict[int, dict]:
    """Demonstrate policy-delta leakage from repeated *synthetic* yes/no queries."""
    if not secret_by_epoch or any(threshold not in domain for threshold in secret_by_epoch.values()):
        raise ValueError("threshold outside enumerated domain")
    return {epoch: leakage_example(threshold, domain) for epoch, threshold in sorted(secret_by_epoch.items())}


def assess_concurrent_negotiations(decisions: list[tuple[LocalDecision, LocalDecision]]) -> str:
    """Treat concurrent local exchanges as independent; never infer atomic publication."""
    seen = set()
    for a, b in decisions:
        if a.negotiation != b.negotiation or a.negotiation in seen:
            return "REJECTED_CONTEXT_COLLISION"
        seen.add(a.negotiation)
        outcome = mutual_observation(a, b, expected_epoch=a.epoch, negotiation=a.negotiation)
        if outcome != "LOCALLY_ACCEPTED_NOT_PUBLISHED":
            return outcome
    return "NO_ATOMIC_PUBLICATION_ASSURANCE"


def coalition_view(observed: list[tuple[str, str, bool]]) -> dict[str, set[tuple[str, bool]]]:
    """Show colluding observers can pool visible response-channel metadata."""
    result: dict[str, set[tuple[str, bool]]] = {}
    for observer, negotiation, response in observed:
        result.setdefault(negotiation, set()).add((observer, response))
    return result
