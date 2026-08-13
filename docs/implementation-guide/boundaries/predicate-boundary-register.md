---
layout: default
title: "Predicate boundary register"
parent: "Assurance and Disclosure Boundaries"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Predicate boundary register

This register is the maintained operational record of predicate-level assurance and disclosure boundaries. It does not define predicate semantics independently: semantic meaning is controlled by [`proof-of-liveness-requirements.md`](../../../proof-of-liveness-requirements.md), and the decision method is defined in [`predicate-assurance-boundary-decision.md`](predicate-assurance-boundary-decision.md).

| Predicate | Assurance boundary | Disclosure boundary | Required profile treatment |
|---|---|---|---|
| [`PR-LIV`](../reference/identifier-register.md#pr-liv) | Valid qualifying attestation possession under named policy | Policy, assurance, freshness and presentation-event surface | Minimum Liveness and Extended Personhood |
| [`PR-PER`](../reference/identifier-register.md#pr-per) | Satisfaction of a named personhood policy | Policy class, issuer-set and possible population inference | Extended Personhood |
| [`PR-ISS`](../reference/identifier-register.md#pr-iss) | Issuer membership in an accepted framework | Framework, assurance class and optionally concealed issuer membership | Both profiles where issuer qualification is required |
| [`PR-UNQ`](../reference/identifier-register.md#pr-unq) | Reuse detection for one enrolled secret in a scope and epoch | Linkability within scope, root membership and epoch continuity | Extended Personhood only |
| [`PR-HLD`](../reference/identifier-register.md#pr-hld) | Control of holder key or secret | Key continuity and device/runtime observations | Both profiles |
| [`PR-FRE`](../reference/identifier-register.md#pr-fre) | Binding to canonical challenge and transcript | Request timing, audience, purpose and event observability | Both profiles |
| [`PR-RNG`](../reference/identifier-register.md#pr-rng) | Attested value satisfies a range | Range, rarity and combination inference | Optional extension |

Implementations instantiate the templates for each supported predicate and cross-reference applicable threats and tests.
