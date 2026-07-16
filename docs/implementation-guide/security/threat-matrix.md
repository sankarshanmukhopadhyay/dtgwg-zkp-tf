---
title: Canonical threat matrix
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---

# Canonical threat matrix

This generated view summarizes the authoritative `threat-matrix.yaml`. Detailed attack paths, controls and evidence are available in the YAML and CSV views.

| ID | Domain | Threat | Profiles | Severity | Primary controls | Harm |
|---|---|---|---|---|---|---|
| THR-001 | cryptographic | Forged proof accepted | both | critical | CTL-AGL; independent implementation tests; parameter integrity | impersonation or unauthorized access |
| THR-002 | cryptographic | Replay across requests | both | high | CTL-TRN | fraud or unauthorized transaction |
| THR-003 | cryptographic | Cross-domain transcript substitution | both | high | CTL-TRN | authorization bypass |
| THR-004 | cryptographic | Setup or parameter compromise | both | critical | CTL-AGL; transparent parameter governance | system-wide compromise |
| THR-005 | cryptographic | Prover side-channel leakage | both | high | hardened implementation; CTL-OBS | identity compromise and surveillance |
| THR-006 | holder | Transferred key treated as human continuity | both | high | CTL-TRN; separate liveness and holder claims; recovery controls | impersonation |
| THR-007 | enrolment | False biometric determination attested | both | critical | issuer governance, audit, CTL-RED | exclusion or impersonation |
| THR-008 | enrolment | Duplicate enrolment under same issuer | extended | high | CTL-LCM; deduplication controls; recovery continuity | fraud and unfair access |
| THR-009 | enrolment | Cross-issuer duplicate enrolment | extended | high | CTL-GOV; narrow claims; issuer coordination policy | Sybil abuse and legitimacy loss |
| THR-010 | privacy | Stable enrolment root enables population correlation | extended | critical | CTL-CTX; CTL-LCM; commitments | surveillance |
| THR-011 | privacy | Unbounded nullifier creates permanent identifier | extended | critical | CTL-CTX; CTL-LCM; retention controls | surveillance and exclusion |
| THR-012 | privacy | Issuer identity inferred despite concealment | profile-specific | high | CTL-SCH; CTL-CMP | subject correlation and discrimination |
| THR-013 | privacy | Attestation metadata correlates presentations | both | critical | CTL-SCH; selective disclosure | surveillance |
| THR-014 | privacy | Registry or status lookup reveals subject activity | both | high | privacy-preserving status; CTL-OBS | surveillance |
| THR-015 | privacy | Issuer-verifier collusion crosses context boundary | extended | critical | CTL-CTX; CTL-SCH; minimization | surveillance and power concentration |
| THR-016 | composition | Rare predicate bundle fingerprints subject | both | high | CTL-CMP; request minimization | discrimination or surveillance |
| THR-017 | composition | Individually safe proofs leak jointly | both | high | CTL-CMP; single-statement composition where viable | surveillance |
| THR-018 | observable-event | Presentation timing and frequency reveal behaviour | both | medium | CTL-OBS; batching; retention limits | surveillance and chilling effects |
| THR-019 | observable-event | Error and retry behaviour becomes oracle | both | medium | CTL-OBS; uniform external errors; bounded retries | targeting or denial |
| THR-020 | governance | Unauthorized issuer accepted | both | critical | CTL-GOV; signed versioned records | fraud and legitimacy loss |
| THR-021 | governance | Policy version substitution | both | high | CTL-GOV; CTL-AGL | unfair or unsafe decisions |
| THR-022 | governance | Revoked or suspended state accepted | both | critical | CTL-GOV; deterministic unavailable behaviour | fraud or safety harm |
| THR-023 | governance | Assurance class inflation | both | high | issuer audit; CTL-GOV; CTL-RED | exclusion, fraud, legitimacy loss |
| THR-024 | governance | Agent key control mistaken for delegated authority | delegated use | critical | CTL-GOV; separate delegation object; scope checks | economic loss and autonomy harm |
| THR-025 | lifecycle | Algorithm downgrade during negotiation | both | critical | CTL-AGL; signed policy and downgrade prevention | forgery or privacy loss |
| THR-026 | lifecycle | Enrolment root outlives defensible protection | extended | critical | CTL-LCM; rotation and deletion evidence | surveillance and systemic compromise |
| THR-027 | lifecycle | Migration splits verification state | both | high | CTL-LCM; coordinated effective times | exclusion and dispute |
| THR-028 | lifecycle | Recovery resets reuse protections | extended | critical | CTL-LCM; recovery continuity and adjudication | fraud and unfair allocation |
| THR-029 | mediated-proving | Mediator retains witness-related data | mediated | critical | CTL-MED; data minimization; audit | surveillance and concentration harm |
| THR-030 | operational | Silent fallback lowers assurance or increases disclosure | both | high | CTL-FBK; explicit consent and receipts | exclusion, surveillance or unsafe acceptance |
| THR-031 | operational | Offline verification uses stale governance state | both | high | bounded offline policy; CTL-GOV | fraud or inconsistent treatment |
| THR-032 | operational | Logs become cross-context correlation store | both | critical | CTL-OBS; minimization; access controls | persistent tracking and institutional misuse |
| THR-033 | human-experience | Context boundary is unintelligible to affected person | extended | high | CTL-HUM; user-facing context test | autonomy and privacy harm |
| THR-034 | human-experience | Accessibility path creates disproportionate disclosure | both | high | accessible equivalent path; CTL-FBK; CTL-HUM | disproportionate exclusion and surveillance |
| THR-035 | redress | Decision cannot be contested or corrected | both | critical | CTL-RED; ownership model | economic, reputational and legitimacy harm |
| THR-036 | governance | Context silently expands through organizational change | extended | critical | CTL-CTX; versioned change and migration | surveillance and autonomy loss |
