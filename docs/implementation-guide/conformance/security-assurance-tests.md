---
layout: default
title: "Security assurance tests"
parent: "Conformance and Assurance"
grand_parent: "Implementation Guide"
nav_order: 8
has_toc: true
---
# Security assurance tests

Protocol conformance proves implementation behaviour against a profile. Security assurance additionally tests control effectiveness, governance authority, operational resilience and affected-party outcomes. This separation adapts the RAHP assurance-test model for ZKP implementations.

| Test ID | Class | Guardrail | Required result |
|---|---|---|---|
| ZAT-01 | control effectiveness | ZGR-01 | forged or malformed proofs and unapproved parameters are rejected |
| ZAT-02 | control effectiveness | ZGR-02 | replay and cross-domain substitution are rejected |
| ZAT-03 | governance assurance | ZGR-03 | context and epoch changes require authorised, versioned decisions |
| ZAT-04 | human-impact assurance | ZGR-04 | combined disclosures remain within the approved privacy claim |
| ZAT-05 | operational resilience | ZGR-05 | stale state is rejected or bounded degraded mode is invoked |
| ZAT-06 | control effectiveness | ZGR-06 | mediator cannot retain or expose witness material outside the approved boundary |
| ZAT-07 | governance assurance | ZGR-07 | expired, revoked, wrong-audience and out-of-scope delegation fails |
| ZAT-08 | human-impact assurance | ZGR-08 | fallback is explicit and does not silently increase disclosure |
| ZAT-09 | human-impact assurance | ZGR-09 | a contested decision can be evidenced, reviewed and corrected |
| ZAT-10 | operational resilience | ZGR-10 | downgrade fails and migration rollback follows authorised state |
| ZAT-11 | operational resilience | ZGR-11 | incident declaration, containment and restoration authority is exercised in a tabletop |
| ZAT-12 | human-impact assurance | ZGR-12 | supported accessible paths provide materially equivalent privacy and assurance |
| ZAT-13 | governance assurance | ZGR-13 | prohibited, expired or insufficiently authorised acceptance is rejected |
| ZAT-14 | governance assurance | ZGR-14 | metric data flow satisfies minimisation and retention constraints |

Results use the machine-readable schema and must identify tested version, environment, evidence references, tester, authority and disposition.
