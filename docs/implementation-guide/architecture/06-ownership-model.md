---
layout: default
title: "Concern ownership model"
parent: "Architecture"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Concern ownership model

| Concern | ZKP TF | Credentials TF | Trust Tasks TF | Registry work | Human Experience | Governance |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| proof statement/profile | P | C | C | I | C | I |
| credential semantics | C | P | I | I | C | C |
| presentation transcript | P | C | C | I | C | I |
| agent delegation | C | C | P | I | C | C |
| accreditation discovery | I | I | I | P | C | C |
| assurance meaning | C | C | I | C | C | P |
| disclosure meaning and user comprehension | C | C | I | I | P | C |
| context definition and human legibility | C | I | C | C | P | P |
| status and recognition | C | C | I | P | C | P |
| fallback and assurance downgrade | C | C | C | I | P | P |
| mediated proving experience and disclosure | C | I | I | I | P | P |
| accessibility and assisted use | I | C | C | I | P | C |
| consent, notice, and meaningful choice | I | C | C | I | P | P |
| observable-event and behavioural leakage | C | I | C | I | P | C |
| conformance scenarios | P | C | C | C | C | C |
| human-experience conformance scenarios | C | C | C | I | P | C |
| reliance policy | I | I | I | C | C | P |
| explanation, correction, and challenge | I | C | C | C | P | P |
| redress and liability | I | I | I | I | C | P |

Legend: P primary; C contributor/consulted; I informed.

## Interpretation

Human experience is an architectural concern, not a downstream interface activity. A concern requires Human Experience participation where its implementation affects a person's ability to understand the assurance being requested, perceive the applicable context, recognize disclosure or correlation consequences, choose among available proving or fallback modes, access an equivalent pathway, or exercise correction, challenge, and redress.

A cryptographically valid mechanism does not satisfy this ownership model when the relevant assurance, context, disclosure, downgrade, or recourse condition is materially illegible or inaccessible to the affected person.
