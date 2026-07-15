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
