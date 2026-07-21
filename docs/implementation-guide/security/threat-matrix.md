---
layout: default
title: "Threat matrix"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 7
has_toc: true
---
# Threat matrix

The canonical source is `threat-matrix.yaml`. Rows marked `RAHP-adapted` extend the existing ZKP model using the governance and harms-prevention method documented in [RAHP adoption and adaptation](rahp-adoption-and-adaptation.md).

**Canonical threats:** 45

| ID | Domain | Threat | Severity | Controls | Harm | Status |
|---|---|---|---|---|---|---|
| THR-001 | cryptographic | Forged proof accepted | critical | CTL-AGL; independent implementation tests; parameter integrity | HRM-IMP;HRM-ECO | baseline |
| THR-002 | cryptographic | Replay across requests | high | CTL-TRN | HRM-IMP;HRM-ECO | baseline |
| THR-003 | cryptographic | Cross-domain transcript substitution | high | CTL-TRN | HRM-IMP;HRM-GOV | baseline |
| THR-004 | cryptographic | Setup or parameter compromise | critical | CTL-AGL; transparent parameter governance | HRM-IMP;HRM-SYS | baseline |
| THR-005 | cryptographic | Prover side-channel leakage | high | hardened implementation; CTL-OBS | HRM-PRV;HRM-IMP | baseline |
| THR-006 | holder | Transferred key treated as human continuity | high | CTL-TRN; separate liveness and holder claims; recovery controls | HRM-IMP;HRM-AUT | baseline |
| THR-007 | enrolment | False biometric determination attested | critical | issuer governance, audit, CTL-RED | HRM-EXC;HRM-IMP;HRM-RED | baseline |
| THR-008 | enrolment | Duplicate enrolment under same issuer | high | CTL-LCM; deduplication controls; recovery continuity | HRM-ECO;HRM-GOV | baseline |
| THR-009 | enrolment | Cross-issuer duplicate enrolment | high | CTL-GOV; narrow claims; issuer coordination policy | HRM-GOV;HRM-ECO | baseline |
| THR-010 | privacy | Stable enrolment root enables population correlation | critical | CTL-CTX; CTL-LCM; commitments | HRM-PRV;HRM-SYS | baseline |
| THR-011 | privacy | Unbounded nullifier creates permanent identifier | critical | CTL-CTX; CTL-LCM; retention controls | HRM-PRV;HRM-AUT | baseline |
| THR-012 | privacy | Issuer identity inferred despite concealment | high | CTL-SCH; CTL-CMP | HRM-PRV;HRM-REP | baseline |
| THR-013 | privacy | Attestation metadata correlates presentations | critical | CTL-SCH; selective disclosure | HRM-PRV | baseline |
| THR-014 | privacy | Registry or status lookup reveals subject activity | high | privacy-preserving status; CTL-OBS | HRM-PRV;HRM-SYS | baseline |
| THR-015 | privacy | Issuer-verifier collusion crosses context boundary | critical | CTL-CTX; CTL-SCH; minimization | HRM-PRV;HRM-SYS | baseline |
| THR-016 | composition | Rare predicate bundle fingerprints subject | high | CTL-CMP; request minimization | HRM-PRV;HRM-REP | baseline |
| THR-017 | composition | Individually safe proofs leak jointly | high | CTL-CMP; single-statement composition where viable | HRM-PRV | baseline |
| THR-018 | observable-event | Presentation timing and frequency reveal behaviour | medium | CTL-OBS; batching; retention limits | HRM-PRV;HRM-AUT | baseline |
| THR-019 | observable-event | Error and retry behaviour becomes oracle | medium | CTL-OBS; uniform external errors; bounded retries | HRM-PRV;HRM-SYS | baseline |
| THR-020 | governance | Unauthorized issuer accepted | critical | CTL-GOV; signed versioned records | HRM-GOV;HRM-IMP | baseline |
| THR-021 | governance | Policy version substitution | high | CTL-GOV; CTL-AGL | HRM-GOV;HRM-ECO | baseline |
| THR-022 | governance | Revoked or suspended state accepted | critical | CTL-GOV; deterministic unavailable behaviour | HRM-IMP;HRM-ECO | baseline |
| THR-023 | governance | Assurance class inflation | high | issuer audit; CTL-GOV; CTL-RED | HRM-GOV;HRM-ECO | baseline |
| THR-024 | governance | Agent key control mistaken for delegated authority | critical | CTL-GOV; separate delegation object; scope checks | HRM-AUT;HRM-ECO;HRM-IMP | baseline |
| THR-025 | lifecycle | Algorithm downgrade during negotiation | critical | CTL-AGL; signed policy and downgrade prevention | HRM-IMP;HRM-PRV | baseline |
| THR-026 | lifecycle | Enrolment root outlives defensible protection | critical | CTL-LCM; rotation and deletion evidence | HRM-PRV;HRM-SYS | baseline |
| THR-027 | lifecycle | Migration splits verification state | high | CTL-LCM; coordinated effective times | HRM-EXC;HRM-RED | baseline |
| THR-028 | lifecycle | Recovery resets reuse protections | critical | CTL-LCM; recovery continuity and adjudication | HRM-ECO;HRM-GOV | baseline |
| THR-029 | mediated-proving | Mediator retains witness-related data | critical | CTL-MED; data minimization; audit | HRM-PRV;HRM-SYS | baseline |
| THR-030 | operational | Silent fallback lowers assurance or increases disclosure | high | CTL-FBK; explicit consent and receipts | HRM-AUT;HRM-EXC;HRM-PRV | baseline |
| THR-031 | operational | Offline verification uses stale governance state | high | bounded offline policy; CTL-GOV | HRM-ECO;HRM-GOV | baseline |
| THR-032 | operational | Logs become cross-context correlation store | critical | CTL-OBS; minimization; access controls | HRM-PRV;HRM-SYS | baseline |
| THR-033 | human-experience | Context boundary is unintelligible to affected person | high | CTL-HUM; user-facing context test | HRM-AUT;HRM-PRV | baseline |
| THR-034 | human-experience | Accessibility path creates disproportionate disclosure | high | accessible equivalent path; CTL-FBK; CTL-HUM | HRM-EXC;HRM-PRV | baseline |
| THR-035 | redress | Decision cannot be contested or corrected | critical | CTL-RED; ownership model | HRM-RED;HRM-ECO;HRM-REP | baseline |
| THR-036 | governance | Context silently expands through organizational change | critical | CTL-CTX; versioned change and migration | HRM-PRV;HRM-AUT;HRM-GOV | baseline |
| THR-037 | governance | Governance authority capture | critical | CTL-GOV; CTL-RED | HRM-GOV;HRM-SYS;HRM-EXC | RAHP-adapted |
| THR-038 | ecosystem | Concentrated provider coercion | critical | CTL-GOV; CTL-LCM | HRM-SYS;HRM-AUT;HRM-EXC | RAHP-adapted |
| THR-039 | assurance | Assurance evidence fabricated or selectively omitted | critical | CTL-GOV; CTL-OBS | HRM-GOV;HRM-SYS | RAHP-adapted |
| THR-040 | operations | Governance process exhaustion | high | CTL-RED; CTL-GOV | HRM-RED;HRM-EXC;HRM-GOV | RAHP-adapted |
| THR-041 | human-operations | AI-assisted operator social engineering | critical | CTL-GOV; CTL-HUM | HRM-IMP;HRM-GOV;HRM-SYS | RAHP-adapted |
| THR-042 | policy | Discriminatory predicate or profile selection | critical | CTL-HUM; CTL-RED; CTL-SCH | HRM-EXC;HRM-ECO;HRM-GOV | RAHP-adapted |
| THR-043 | governance | Risk acceptance laundering | critical | CTL-GOV; CTL-LCM | HRM-GOV;HRM-SYS | RAHP-adapted |
| THR-044 | observability | Metric gaming or observability suppression | high | CTL-OBS; CTL-GOV | HRM-GOV;HRM-SYS;HRM-PRV | RAHP-adapted |
| THR-045 | affected-parties | Affected-party harm remains invisible | high | CTL-RED; CTL-HUM; CTL-GOV | HRM-ECO;HRM-REP;HRM-AUT;HRM-GOV;HRM-RED | RAHP-adapted |
