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
| [`ZAT-01`](../reference/identifier-register.md#zat-01) | control effectiveness | [`ZGR-01`](../reference/identifier-register.md#zgr-01) | forged or malformed proofs and unapproved parameters are rejected |
| [`ZAT-02`](../reference/identifier-register.md#zat-02) | control effectiveness | [`ZGR-02`](../reference/identifier-register.md#zgr-02) | replay and cross-domain substitution are rejected |
| [`ZAT-03`](../reference/identifier-register.md#zat-03) | governance assurance | [`ZGR-03`](../reference/identifier-register.md#zgr-03) | context and epoch changes require authorised, versioned decisions |
| [`ZAT-04`](../reference/identifier-register.md#zat-04) | human-impact assurance | [`ZGR-04`](../reference/identifier-register.md#zgr-04) | combined disclosures remain within the approved privacy claim |
| [`ZAT-05`](../reference/identifier-register.md#zat-05) | operational resilience | [`ZGR-05`](../reference/identifier-register.md#zgr-05) | stale state is rejected or bounded degraded mode is invoked |
| [`ZAT-06`](../reference/identifier-register.md#zat-06) | control effectiveness | [`ZGR-06`](../reference/identifier-register.md#zgr-06) | mediator cannot retain or expose witness material outside the approved boundary |
| [`ZAT-07`](../reference/identifier-register.md#zat-07) | governance assurance | [`ZGR-07`](../reference/identifier-register.md#zgr-07) | expired, revoked, wrong-audience and out-of-scope delegation fails |
| [`ZAT-08`](../reference/identifier-register.md#zat-08) | human-impact assurance | [`ZGR-08`](../reference/identifier-register.md#zgr-08) | fallback is explicit and does not silently increase disclosure |
| [`ZAT-09`](../reference/identifier-register.md#zat-09) | human-impact assurance | [`ZGR-09`](../reference/identifier-register.md#zgr-09) | a contested decision can be evidenced, reviewed and corrected |
| [`ZAT-10`](../reference/identifier-register.md#zat-10) | operational resilience | [`ZGR-10`](../reference/identifier-register.md#zgr-10) | downgrade fails and migration rollback follows authorised state |
| [`ZAT-11`](../reference/identifier-register.md#zat-11) | operational resilience | [`ZGR-11`](../reference/identifier-register.md#zgr-11) | incident declaration, containment and restoration authority is exercised in a tabletop |
| [`ZAT-12`](../reference/identifier-register.md#zat-12) | human-impact assurance | [`ZGR-12`](../reference/identifier-register.md#zgr-12) | supported accessible paths provide materially equivalent privacy and assurance |
| [`ZAT-13`](../reference/identifier-register.md#zat-13) | governance assurance | [`ZGR-13`](../reference/identifier-register.md#zgr-13) | prohibited, expired or insufficiently authorised acceptance is rejected |
| [`ZAT-14`](../reference/identifier-register.md#zat-14) | governance assurance | [`ZGR-14`](../reference/identifier-register.md#zgr-14) | metric data flow satisfies minimisation and retention constraints |

Results use the machine-readable schema and must identify tested version, environment, evidence references, tester, authority and disposition.
