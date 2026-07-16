# Guidance and evidence index

This guide is non-normative by default. The index identifies implementation expectations that should produce observable evidence.

| ID | Expectation | Primary evidence | Tests or scenarios |
|---|---|---|---|
| IG-001 | bind every proof to a canonical request transcript | transcript digest in decision receipt | UC-004, UC-006 |
| IG-002 | distinguish holder binding from delegated authority | delegation reference or explicit absence | UC-009, UC-010, ADR-001 |
| IG-003 | qualify privacy claims by adversary, context and horizon | privacy claim record | UC-023, UC-024 |
| IG-004 | record policy, registry and status versions used in a decision | decision receipt | UC-012–UC-016 |
| IG-005 | reject replay, context mismatch and silent downgrade | negative test results | UC-022, UC-025–UC-027 |
| IG-006 | make lifecycle and recovery behavior deterministic | lifecycle audit trail | UC-005 and lifecycle scenarios |
| IG-007 | document alternative paths and assurance differences | accessibility assessment | UC-017, UC-020, UC-021 |
| IG-008 | package conformance evidence reproducibly | evidence bundle | CL-1 through CL-4 |

## Boundary, threat and lifecycle requirements

| Requirement | Expectation | Evidence |
|---|---|---|
| SEC-001 | Every material predicate has linked assurance and disclosure boundary records. | boundary fixture and profile evidence |
| SEC-002 | Every material claim states against whom, for how long and alongside what it applies. | claim validation and conformance test |
| SEC-003 | Applicable canonical threats map to controls, owners, tests and residual-risk decisions. | threat matrix and deployment assessment |
| SEC-004 | Attestation fields receive individual and combination correlation analysis. | field register and assessment report |
| SEC-005 | Enrolment roots, nullifiers and privacy claims have bounded temporal controls. | lifecycle profile |
| SEC-006 | Mediated proving is explicit, isolated, non-retaining and auditable. | mediated profile and audit evidence |
| SEC-007 | Negotiation and migration prevent unauthorized downgrade. | cross-version conformance tests |
| SEC-008 | Context definitions identify collusion targets and are human-legible. | context decision record and comprehension evidence |

