---
layout: default
title: "Threat Matrix"
parent: "Security"
grand_parent: "Implementation Guide"
nav_order: 3
---
# Threat matrix

The canonical machine-readable source is `threat-matrix.yaml`. This generated view contains **52 threats**.

| Threat | Domain | Title | Severity | Controls | Requirement | Status |
|---|---|---|---|---|---|---|
| THR-001 | cryptographic | Forged proof accepted | critical | CTL-AGL; independent implementation tests; parameter integrity | SEC-001 | baseline |
| THR-002 | cryptographic | Replay across requests | high | CTL-TRN | SEC-002 | baseline |
| THR-003 | cryptographic | Cross-domain transcript substitution | high | CTL-TRN | SEC-003 | baseline |
| THR-004 | cryptographic | Setup or parameter compromise | critical | CTL-AGL; transparent parameter governance | SEC-004 | baseline |
| THR-005 | cryptographic | Prover side-channel leakage | high | hardened implementation; CTL-OBS | SEC-005 | baseline |
| THR-006 | holder | Transferred key treated as human continuity | high | CTL-TRN; separate liveness and holder claims; recovery controls | SEC-006 | baseline |
| THR-007 | enrolment | False biometric determination attested | critical | issuer governance, audit, CTL-RED | SEC-007 | baseline |
| THR-008 | enrolment | Duplicate enrolment under same issuer | high | CTL-LCM; deduplication controls; recovery continuity | SEC-008 | baseline |
| THR-009 | enrolment | Cross-issuer duplicate enrolment | high | CTL-GOV; narrow claims; issuer coordination policy | SEC-009 | baseline |
| THR-010 | privacy | Stable enrolment root enables population correlation | critical | CTL-CTX; CTL-LCM; commitments | SEC-010 | baseline |
| THR-011 | privacy | Unbounded nullifier creates permanent identifier | critical | CTL-CTX; CTL-LCM; retention controls | SEC-011 | baseline |
| THR-012 | privacy | Issuer identity inferred despite concealment | high | CTL-SCH; CTL-CMP | SEC-012 | baseline |
| THR-013 | privacy | Attestation metadata correlates presentations | critical | CTL-SCH; selective disclosure | SEC-013 | baseline |
| THR-014 | privacy | Registry or status lookup reveals subject activity | high | privacy-preserving status; CTL-OBS | SEC-014 | baseline |
| THR-015 | privacy | Issuer-verifier collusion crosses context boundary | critical | CTL-CTX; CTL-SCH; minimization | SEC-015 | baseline |
| THR-016 | composition | Rare predicate bundle fingerprints subject | high | CTL-CMP; request minimization | SEC-016 | baseline |
| THR-017 | composition | Individually safe proofs leak jointly | high | CTL-CMP; single-statement composition where viable | SEC-017 | baseline |
| THR-018 | observable-event | Presentation timing and frequency reveal behaviour | medium | CTL-OBS; batching; retention limits | SEC-018 | baseline |
| THR-019 | observable-event | Error and retry behaviour becomes oracle | medium | CTL-OBS; uniform external errors; bounded retries | SEC-019 | baseline |
| THR-020 | governance | Unauthorized issuer accepted | critical | CTL-GOV; signed versioned records | SEC-020 | baseline |
| THR-021 | governance | Policy version substitution | high | CTL-GOV; CTL-AGL | SEC-021 | baseline |
| THR-022 | governance | Revoked or suspended state accepted | critical | CTL-GOV; deterministic unavailable behaviour | SEC-022 | baseline |
| THR-023 | governance | Assurance class inflation | high | issuer audit; CTL-GOV; CTL-RED | SEC-023 | baseline |
| THR-024 | governance | Agent key control mistaken for delegated authority | critical | CTL-GOV; separate delegation object; scope checks | SEC-024 | baseline |
| THR-025 | lifecycle | Algorithm downgrade during negotiation | critical | CTL-AGL; signed policy and downgrade prevention | SEC-025 | baseline |
| THR-026 | lifecycle | Enrolment root outlives defensible protection | critical | CTL-LCM; rotation and deletion evidence | SEC-026 | baseline |
| THR-027 | lifecycle | Migration splits verification state | high | CTL-LCM; coordinated effective times | SEC-027 | baseline |
| THR-028 | lifecycle | Recovery resets reuse protections | critical | CTL-LCM; recovery continuity and adjudication | SEC-028 | baseline |
| THR-029 | mediated-proving | Mediator retains witness-related data | critical | CTL-MED; data minimization; audit | SEC-029 | baseline |
| THR-030 | operational | Silent fallback lowers assurance or increases disclosure | high | CTL-FBK; explicit consent and receipts | SEC-030 | baseline |
| THR-031 | operational | Offline verification uses stale governance state | high | bounded offline policy; CTL-GOV | SEC-031 | baseline |
| THR-032 | operational | Logs become cross-context correlation store | critical | CTL-OBS; minimization; access controls | SEC-032 | baseline |
| THR-033 | human-experience | Context boundary is unintelligible to affected person | high | CTL-HUM; user-facing context test | SEC-033 | baseline |
| THR-034 | human-experience | Accessibility path creates disproportionate disclosure | high | accessible equivalent path; CTL-FBK; CTL-HUM | SEC-034 | baseline |
| THR-035 | redress | Decision cannot be contested or corrected | critical | CTL-RED; ownership model | SEC-035 | baseline |
| THR-036 | governance | Context silently expands through organizational change | critical | CTL-CTX; versioned change and migration | SEC-036 | baseline |
| THR-037 | governance | Governance authority capture | critical | CTL-GOV; CTL-RED | SEC-037 | RAHP-adapted |
| THR-038 | ecosystem | Concentrated provider coercion | critical | CTL-GOV; CTL-LCM | SEC-038 | RAHP-adapted |
| THR-039 | assurance | Assurance evidence fabricated or selectively omitted | critical | CTL-GOV; CTL-OBS | SEC-039 | RAHP-adapted |
| THR-040 | operations | Governance process exhaustion | high | CTL-RED; CTL-GOV | SEC-040 | RAHP-adapted |
| THR-041 | human-operations | AI-assisted operator social engineering | critical | CTL-GOV; CTL-HUM | SEC-041 | RAHP-adapted |
| THR-042 | policy | Discriminatory predicate or profile selection | critical | CTL-HUM; CTL-RED; CTL-SCH | SEC-042 | RAHP-adapted |
| THR-043 | governance | Risk acceptance laundering | critical | CTL-GOV; CTL-LCM | SEC-043 | RAHP-adapted |
| THR-044 | observability | Metric gaming or observability suppression | high | CTL-OBS; CTL-GOV | SEC-044 | RAHP-adapted |
| THR-045 | affected-parties | Affected-party harm remains invisible | high | CTL-RED; CTL-HUM; CTL-GOV | SEC-045 | RAHP-adapted |
| THR-046 | credential-semantics | Unproven identifier linkage accepted as proof input | critical | CTL-GOV; CTL-SCH; CTL-TRN | ZKP-LINK-01 | cross-specification |
| THR-047 | privacy | Identifier linkage creates cross-context correlation | critical | CTL-CTX; CTL-SCH; CTL-OBS | ZKP-LINK-03 | cross-specification |
| THR-048 | governance | Task or ceremony participation treated as authority | critical | CTL-GOV; CTL-AGL; CTL-TRN | ZKP-TASK-02 | cross-specification |
| THR-049 | privacy | Ceremony identifier becomes stable correlation handle | high | CTL-CTX; CTL-OBS; CTL-SCH | ZKP-CER-01 | cross-specification |
| THR-050 | protocol | Valid proof bound to wrong Trust Task | critical | CTL-TRN; CTL-AGL | ZKP-TASK-04 | cross-specification |
| THR-051 | agentic-delegation | Agent presents valid human proof outside delegated scope | critical | CTL-GOV; CTL-AGL; CTL-LCM | ZKP-TASK-02 | cross-specification |
| THR-052 | lifecycle | Historical ceremony evidence reinterpreted under changed policy | high | CTL-LCM; CTL-GOV; CTL-OBS | ZKP-TASK-03 | cross-specification |
