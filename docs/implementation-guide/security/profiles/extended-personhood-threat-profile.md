---
layout: default
title: "Extended Personhood threat profile"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Extended Personhood threat profile

Adds scoped nullifiers, enrolment roots, context-dependent unlinkability, recovery continuity and collusion analysis.

| Threat ID | Threat | Severity | Required disposition |
|---|---|---|---|
| [`THR-001`](../../reference/identifier-register.md#thr-001) | Forged proof accepted | critical | prohibit on broken profile |
| [`THR-002`](../../reference/identifier-register.md#thr-002) | Replay across requests | high | mitigate |
| [`THR-003`](../../reference/identifier-register.md#thr-003) | Cross-domain transcript substitution | high | mitigate |
| [`THR-004`](../../reference/identifier-register.md#thr-004) | Setup or parameter compromise | critical | transfer or prohibit |
| [`THR-005`](../../reference/identifier-register.md#thr-005) | Prover side-channel leakage | high | mitigate |
| [`THR-006`](../../reference/identifier-register.md#thr-006) | Transferred key treated as human continuity | high | mitigate |
| [`THR-007`](../../reference/identifier-register.md#thr-007) | False biometric determination attested | critical | mitigate |
| [`THR-008`](../../reference/identifier-register.md#thr-008) | Duplicate enrolment under same issuer | high | mitigate |
| [`THR-009`](../../reference/identifier-register.md#thr-009) | Cross-issuer duplicate enrolment | high | accept or narrow claim |
| [`THR-010`](../../reference/identifier-register.md#thr-010) | Stable enrolment root enables population correlation | critical | mitigate |
| [`THR-011`](../../reference/identifier-register.md#thr-011) | Unbounded nullifier creates permanent identifier | critical | mitigate |
| [`THR-013`](../../reference/identifier-register.md#thr-013) | Attestation metadata correlates presentations | critical | mitigate |
| [`THR-014`](../../reference/identifier-register.md#thr-014) | Registry or status lookup reveals subject activity | high | mitigate |
| [`THR-015`](../../reference/identifier-register.md#thr-015) | Issuer-verifier collusion crosses context boundary | critical | accept only if disclosed or mitigate |
| [`THR-016`](../../reference/identifier-register.md#thr-016) | Rare predicate bundle fingerprints subject | high | mitigate |
| [`THR-017`](../../reference/identifier-register.md#thr-017) | Individually safe proofs leak jointly | high | mitigate |
| [`THR-018`](../../reference/identifier-register.md#thr-018) | Presentation timing and frequency reveal behaviour | medium | accept with bounded claim |
| [`THR-019`](../../reference/identifier-register.md#thr-019) | Error and retry behaviour becomes oracle | medium | mitigate |
| [`THR-020`](../../reference/identifier-register.md#thr-020) | Unauthorized issuer accepted | critical | mitigate |
| [`THR-021`](../../reference/identifier-register.md#thr-021) | Policy version substitution | high | mitigate |
| [`THR-022`](../../reference/identifier-register.md#thr-022) | Revoked or suspended state accepted | critical | mitigate |
| [`THR-023`](../../reference/identifier-register.md#thr-023) | Assurance class inflation | high | mitigate |
| [`THR-025`](../../reference/identifier-register.md#thr-025) | Algorithm downgrade during negotiation | critical | mitigate |
| [`THR-026`](../../reference/identifier-register.md#thr-026) | Enrolment root outlives defensible protection | critical | mitigate or prohibit unbounded use |
| [`THR-027`](../../reference/identifier-register.md#thr-027) | Migration splits verification state | high | mitigate |
| [`THR-028`](../../reference/identifier-register.md#thr-028) | Recovery resets reuse protections | critical | mitigate |
| [`THR-030`](../../reference/identifier-register.md#thr-030) | Silent fallback lowers assurance or increases disclosure | high | mitigate |
| [`THR-031`](../../reference/identifier-register.md#thr-031) | Offline verification uses stale governance state | high | mitigate |
| [`THR-032`](../../reference/identifier-register.md#thr-032) | Logs become cross-context correlation store | critical | mitigate |
| [`THR-033`](../../reference/identifier-register.md#thr-033) | Context boundary is unintelligible to affected person | high | mitigate |
| [`THR-034`](../../reference/identifier-register.md#thr-034) | Accessibility path creates disproportionate disclosure | high | mitigate |
| [`THR-035`](../../reference/identifier-register.md#thr-035) | Decision cannot be contested or corrected | critical | mitigate |
| [`THR-036`](../../reference/identifier-register.md#thr-036) | Context silently expands through organizational change | critical | prohibit retroactive expansion |
