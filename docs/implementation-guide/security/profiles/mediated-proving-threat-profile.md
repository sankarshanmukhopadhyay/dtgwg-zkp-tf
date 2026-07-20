---
layout: default
title: "Mediated proving threat profile"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Mediated proving threat profile

Applies whenever proof generation depends on a remote or operator-controlled service and requires explicit non-retention and isolation evidence.

| Threat ID | Threat | Severity | Required disposition |
|---|---|---|---|
| THR-001 | Forged proof accepted | critical | prohibit on broken profile |
| THR-002 | Replay across requests | high | mitigate |
| THR-003 | Cross-domain transcript substitution | high | mitigate |
| THR-004 | Setup or parameter compromise | critical | transfer or prohibit |
| THR-005 | Prover side-channel leakage | high | mitigate |
| THR-006 | Transferred key treated as human continuity | high | mitigate |
| THR-007 | False biometric determination attested | critical | mitigate |
| THR-013 | Attestation metadata correlates presentations | critical | mitigate |
| THR-014 | Registry or status lookup reveals subject activity | high | mitigate |
| THR-016 | Rare predicate bundle fingerprints subject | high | mitigate |
| THR-017 | Individually safe proofs leak jointly | high | mitigate |
| THR-018 | Presentation timing and frequency reveal behaviour | medium | accept with bounded claim |
| THR-019 | Error and retry behaviour becomes oracle | medium | mitigate |
| THR-020 | Unauthorized issuer accepted | critical | mitigate |
| THR-021 | Policy version substitution | high | mitigate |
| THR-022 | Revoked or suspended state accepted | critical | mitigate |
| THR-023 | Assurance class inflation | high | mitigate |
| THR-025 | Algorithm downgrade during negotiation | critical | mitigate |
| THR-027 | Migration splits verification state | high | mitigate |
| THR-029 | Mediator retains witness-related data | critical | mitigate or prohibit |
| THR-030 | Silent fallback lowers assurance or increases disclosure | high | mitigate |
| THR-031 | Offline verification uses stale governance state | high | mitigate |
| THR-032 | Logs become cross-context correlation store | critical | mitigate |
| THR-034 | Accessibility path creates disproportionate disclosure | high | mitigate |
| THR-035 | Decision cannot be contested or corrected | critical | mitigate |
