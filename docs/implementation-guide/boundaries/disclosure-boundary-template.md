---
layout: default
title: "Disclosure boundary template"
parent: "Assurance and Disclosure Boundaries"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
nav_exclude: true
---
# Disclosure boundary template

| Field | Required content |
|---|---|
| Boundary ID | Stable `DB-xxx` identifier |
| Predicate/profile | Applicable predicate and profile identifiers |
| Intended disclosure | Information deliberately revealed |
| Derived disclosure | Information inferable from values, cardinality or combinations |
| Against whom | Observer and collusion model |
| For how long | Session, epoch, credential lifetime, log retention and assurance horizon |
| Alongside what | Credential fields, proof shape, registry traffic, network data and events |
| Recipient | Issuer, verifier, mediator, registry, auditor or observer |
| Persistence | Ephemeral, epoch-bound, cryptoperiod-bound or retained |
| Reconstruction risk | Cross-session, cross-verifier and cross-context inference |
| Data minimization | Required suppression, coarsening, commitment or selective disclosure |
| Failure conditions | Conditions that defeat the privacy claim |
| Threat references | Applicable `THR-xxx` identifiers |
| Conformance evidence | Differential, correlation, inspection or audit method |

Disclosure analysis includes the observable fact that a presentation occurred, its timing, frequency, retry path and fallback mode. Transcript zero knowledge does not remove these channels.
