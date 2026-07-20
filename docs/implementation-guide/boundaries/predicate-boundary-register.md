---
layout: default
title: "Predicate boundary register"
parent: "Assurance and Disclosure Boundaries"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Predicate boundary register

| Predicate | Assurance boundary | Disclosure boundary | Required profile treatment |
|---|---|---|---|
| PR-LIV | Valid qualifying attestation possession under named policy | Policy, assurance, freshness and presentation-event surface | Minimum Liveness and Extended Personhood |
| PR-PER | Satisfaction of a named personhood policy | Policy class, issuer-set and possible population inference | Extended Personhood |
| PR-ISS | Issuer membership in an accepted framework | Framework, assurance class and optionally concealed issuer membership | Both profiles where issuer qualification is required |
| PR-UNQ | Reuse detection for one enrolled secret in a scope and epoch | Linkability within scope, root membership and epoch continuity | Extended Personhood only |
| PR-HLD | Control of holder key or secret | Key continuity and device/runtime observations | Both profiles |
| PR-FRE | Binding to canonical challenge and transcript | Request timing, audience, purpose and event observability | Both profiles |
| PR-RNG | Attested value satisfies a range | Range, rarity and combination inference | Optional extension |

Implementations instantiate the templates for each supported predicate and cross-reference applicable threats and tests.
