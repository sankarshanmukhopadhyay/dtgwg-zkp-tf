---
layout: default
title: "Guidance and evidence index"
parent: "Appendices"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Guidance and evidence index

This guide is non-normative by default. The index identifies implementation expectations that should produce observable evidence.

| ID | Expectation | Primary evidence | Tests or scenarios |
|---|---|---|---|
| [`IG-001`](../reference/identifier-register.md#ig-001) | bind every proof to a canonical request transcript | transcript digest in decision receipt | [`UC-004`](../reference/identifier-register.md#uc-004), [`UC-006`](../reference/identifier-register.md#uc-006) |
| [`IG-002`](../reference/identifier-register.md#ig-002) | distinguish holder binding from delegated authority | delegation reference or explicit absence | [`UC-009`](../reference/identifier-register.md#uc-009), [`UC-010`](../reference/identifier-register.md#uc-010), [`ADR-001`](../reference/identifier-register.md#adr-001) |
| [`IG-003`](../reference/identifier-register.md#ig-003) | qualify privacy claims by adversary, context and horizon | privacy claim record | [`UC-023`](../reference/identifier-register.md#uc-023), [`UC-024`](../reference/identifier-register.md#uc-024) |
| [`IG-004`](../reference/identifier-register.md#ig-004) | record policy, registry and status versions used in a decision | decision receipt | [`UC-012`](../reference/identifier-register.md#uc-012)–[`UC-016`](../reference/identifier-register.md#uc-016) |
| [`IG-005`](../reference/identifier-register.md#ig-005) | reject replay, context mismatch and silent downgrade | negative test results | [`UC-022`](../reference/identifier-register.md#uc-022), [`UC-025`](../reference/identifier-register.md#uc-025)–[`UC-027`](../reference/identifier-register.md#uc-027) |
| [`IG-006`](../reference/identifier-register.md#ig-006) | make lifecycle and recovery behavior deterministic | lifecycle audit trail | [`UC-005`](../reference/identifier-register.md#uc-005) and lifecycle scenarios |
| [`IG-007`](../reference/identifier-register.md#ig-007) | document alternative paths and assurance differences | accessibility assessment | [`UC-017`](../reference/identifier-register.md#uc-017), [`UC-020`](../reference/identifier-register.md#uc-020), [`UC-021`](../reference/identifier-register.md#uc-021) |
| [`IG-008`](../reference/identifier-register.md#ig-008) | package conformance evidence reproducibly | evidence bundle | [`CL-1`](../reference/identifier-register.md#cl-1) through [`CL-4`](../reference/identifier-register.md#cl-4) |

## Boundary, threat and lifecycle requirements

| Requirement | Expectation | Evidence |
|---|---|---|
| [`SEC-001`](../reference/identifier-register.md#sec-001) | Every material predicate has linked assurance and disclosure boundary records. | boundary fixture and profile evidence |
| [`SEC-002`](../reference/identifier-register.md#sec-002) | Every material claim states against whom, for how long and alongside what it applies. | claim validation and conformance test |
| [`SEC-003`](../reference/identifier-register.md#sec-003) | Applicable canonical threats map to controls, owners, tests and residual-risk decisions. | threat matrix and deployment assessment |
| [`SEC-004`](../reference/identifier-register.md#sec-004) | Attestation fields receive individual and combination correlation analysis. | field register and assessment report |
| [`SEC-005`](../reference/identifier-register.md#sec-005) | Enrolment roots, nullifiers and privacy claims have bounded temporal controls. | lifecycle profile |
| [`SEC-006`](../reference/identifier-register.md#sec-006) | Mediated proving is explicit, isolated, non-retaining and auditable. | mediated profile and audit evidence |
| [`SEC-007`](../reference/identifier-register.md#sec-007) | Negotiation and migration prevent unauthorized downgrade. | cross-version conformance tests |
| [`SEC-008`](../reference/identifier-register.md#sec-008) | Context definitions identify collusion targets and are human-legible. | context decision record and comprehension evidence |


## DTG interoperability requirements — v0.4.0

| Requirement | Expectation | Primary evidence |
|---|---|---|
| [`ZKP-LINK-01`](../reference/identifier-register.md#zkp-link-01) | relationship-dependent proofs use explicit relationship evidence, never co-possession inference | linkage profile and negative fixture |
| [`ZKP-LINK-02`](../reference/identifier-register.md#zkp-link-02) | linkage evidence identifies provenance, authority, relationship semantics and lifecycle | verification evidence |
| [`ZKP-LINK-03`](../reference/identifier-register.md#zkp-link-03) | linkage mechanisms are assessed against privacy class and context correlation boundaries | correlation assessment |
| [`ZKP-LINK-04`](../reference/identifier-register.md#zkp-link-04) | unresolved or unverifiable required linkage fails closed | negative conformance result |
| [`ZKP-TASK-01`](../reference/identifier-register.md#zkp-task-01) | proof is bound to exact task, audience, challenge, statement and context | canonical transcript / receipt |
| [`ZKP-TASK-02`](../reference/identifier-register.md#zkp-task-02) | task/ceremony participation never substitutes for delegated authority | separate delegation evidence |
| [`ZKP-TASK-03`](../reference/identifier-register.md#zkp-task-03) | applicable policy/profile version is bound or unambiguously referenced | verification receipt |
| [`ZKP-TASK-04`](../reference/identifier-register.md#zkp-task-04) | task mismatch/replay/confused-deputy attempts fail closed | negative conformance result |
| [`ZKP-CER-01`](../reference/identifier-register.md#zkp-cer-01) | ceremony reference is minimised and not a default global correlation handle | privacy assessment |
| [`ZKP-CER-02`](../reference/identifier-register.md#zkp-cer-02) | proof/external evidence validity is evaluated independently of ceremony completion | verification result |
| [`ZKP-CER-03`](../reference/identifier-register.md#zkp-cer-03) | proof, ceremony, credential/status and authority evidence remain distinguishable | audit evidence package |
