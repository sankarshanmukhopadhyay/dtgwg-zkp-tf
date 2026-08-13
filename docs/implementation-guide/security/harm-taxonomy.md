---
layout: default
title: "Harm taxonomy"
parent: "Threats, Harms and Controls"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Harm taxonomy

| Harm ID | Harm class | Examples |
|---|---|---|
| [`HRM-PRV`](../reference/identifier-register.md#hrm-prv) | privacy and surveillance | cross-context tracking, behavioural reconstruction, persistent observability |
| [`HRM-EXC`](../reference/identifier-register.md#hrm-exc) | exclusion and denial | inaccessible proving path, false rejection, silent fallback failure |
| [`HRM-IMP`](../reference/identifier-register.md#hrm-imp) | impersonation and misuse | forged proof, transferred credential, unauthorized agent action |
| [`HRM-AUT`](../reference/identifier-register.md#hrm-aut) | autonomy and coercion | coerced presentation, hidden context expansion, unintelligible consent |
| [`HRM-ECO`](../reference/identifier-register.md#hrm-eco) | economic and service loss | denied benefit, transaction failure, fraud loss, recovery cost |
| [`HRM-REP`](../reference/identifier-register.md#hrm-rep) | reputational harm | incorrect personhood or risk inference, public status exposure |
| [`HRM-GOV`](../reference/identifier-register.md#hrm-gov) | governance and legitimacy | unauthorized accreditation, opaque exception, unreviewable decision |
| [`HRM-RED`](../reference/identifier-register.md#hrm-red) | redress failure | no contest route, missing evidence, correction not propagated |
| [`HRM-SYS`](../reference/identifier-register.md#hrm-sys) | systemic concentration | mediator honeypot, registry capture, single-provider dependency |

Threat reviews record both immediate technical effect and downstream harm. A technically valid rejection can still create unacceptable exclusion or redress risk.
