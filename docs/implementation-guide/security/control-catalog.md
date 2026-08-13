---
layout: default
title: "Control catalogue"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Control catalogue

| Control ID | Control | Primary owner | Evidence |
|---|---|---|---|
| [`CTL-TRN`](../reference/identifier-register.md#ctl-trn) | canonical domain-separated transcript binding | wallet and verifier | fixtures and replay tests |
| [`CTL-SCH`](../reference/identifier-register.md#ctl-sch) | field-level schema minimization and correlation review | issuer and profile authority | schema register and combination analysis |
| [`CTL-CTX`](../reference/identifier-register.md#ctl-ctx) | governed context and epoch derivation | context authority | decision record and nullifier vectors |
| [`CTL-GOV`](../reference/identifier-register.md#ctl-gov) | accreditation, policy and status authority separation | governance authority | signed records and audit trail |
| [`CTL-MED`](../reference/identifier-register.md#ctl-med) | mediated-prover isolation and non-retention | mediator operator | configuration, logs policy and audit |
| [`CTL-LCM`](../reference/identifier-register.md#ctl-lcm) | cryptoperiod, rotation and migration controls | profile authority and operators | lifecycle plan and transition tests |
| [`CTL-CMP`](../reference/identifier-register.md#ctl-cmp) | composition and reconstruction assessment | profile designer and verifier | joint-leakage test report |
| [`CTL-FBK`](../reference/identifier-register.md#ctl-fbk) | explicit fallback and downgrade policy | verifier and wallet | user disclosure and negative tests |
| [`CTL-OBS`](../reference/identifier-register.md#ctl-obs) | observable-event minimization | protocol and operations owners | traffic analysis and retention review |
| [`CTL-RED`](../reference/identifier-register.md#ctl-red) | decision evidence, contest and correction | verifier and redress authority | receipts and redress exercise |
| [`CTL-HUM`](../reference/identifier-register.md#ctl-hum) | human-legible context and assurance disclosure | product and governance owners | usability and comprehension evidence |
| [`CTL-AGL`](../reference/identifier-register.md#ctl-agl) | negotiated algorithm agility with downgrade prevention | profile and implementation owners | cross-version and deprecation tests |

## Relationship to RAHP controls

RAHP `CT-xx` controls informed the separation between continuous controls and binary guardrails. The ZKP `CTL-xxx` families remain repository-specific and are not identifier-equivalent. See [RAHP adoption and adaptation](rahp-adoption-and-adaptation.md).
