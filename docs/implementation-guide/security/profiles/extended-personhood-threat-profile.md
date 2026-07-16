---
title: Extended Personhood threat profile
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---

# Extended Personhood threat profile

Adds scoped nullifiers, enrolment roots, context-dependent unlinkability, recovery continuity and collusion analysis.

| Threat ID | Threat | Severity | Required disposition |
|---|---|---|---|
| THR-001 | Forged proof accepted | critical | prohibit on broken profile |
| THR-002 | Replay across requests | high | mitigate |
| THR-003 | Cross-domain transcript substitution | high | mitigate |
| THR-004 | Setup or parameter compromise | critical | transfer or prohibit |
| THR-005 | Prover side-channel leakage | high | mitigate |
| THR-006 | Transferred key treated as human continuity | high | mitigate |
| THR-007 | False biometric determination attested | critical | mitigate |
| THR-008 | Duplicate enrolment under same issuer | high | mitigate |
| THR-009 | Cross-issuer duplicate enrolment | high | accept or narrow claim |
| THR-010 | Stable enrolment root enables population correlation | critical | mitigate |
| THR-011 | Unbounded nullifier creates permanent identifier | critical | mitigate |
| THR-013 | Attestation metadata correlates presentations | critical | mitigate |
| THR-014 | Registry or status lookup reveals subject activity | high | mitigate |
| THR-015 | Issuer-verifier collusion crosses context boundary | critical | accept only if disclosed or mitigate |
| THR-016 | Rare predicate bundle fingerprints subject | high | mitigate |
| THR-017 | Individually safe proofs leak jointly | high | mitigate |
| THR-018 | Presentation timing and frequency reveal behaviour | medium | accept with bounded claim |
| THR-019 | Error and retry behaviour becomes oracle | medium | mitigate |
| THR-020 | Unauthorized issuer accepted | critical | mitigate |
| THR-021 | Policy version substitution | high | mitigate |
| THR-022 | Revoked or suspended state accepted | critical | mitigate |
| THR-023 | Assurance class inflation | high | mitigate |
| THR-025 | Algorithm downgrade during negotiation | critical | mitigate |
| THR-026 | Enrolment root outlives defensible protection | critical | mitigate or prohibit unbounded use |
| THR-027 | Migration splits verification state | high | mitigate |
| THR-028 | Recovery resets reuse protections | critical | mitigate |
| THR-030 | Silent fallback lowers assurance or increases disclosure | high | mitigate |
| THR-031 | Offline verification uses stale governance state | high | mitigate |
| THR-032 | Logs become cross-context correlation store | critical | mitigate |
| THR-033 | Context boundary is unintelligible to affected person | high | mitigate |
| THR-034 | Accessibility path creates disproportionate disclosure | high | mitigate |
| THR-035 | Decision cannot be contested or corrected | critical | mitigate |
| THR-036 | Context silently expands through organizational change | critical | prohibit retroactive expansion |
