---
layout: default
title: "Decision register"
parent: "Decision Governance"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Decision register

The register is generated conceptually from the machine-readable source and records two independent states: the upstream Task Force decision state and the implementation state of this fork.

| ID | Decision | Upstream status | Fork status | Normative effect |
|---|---|---|---|---|
| A1 | Predicate-over-attestation boundary | `ratified` | `implemented-as-working-baseline` | non-normative |
| A2 | Context-dependent unlinkability target | `ratified` | `implemented-as-working-baseline` | non-normative |
| A3 | Minimum Liveness and Extended Personhood split | `ratified` | `implemented-as-working-baseline` | non-normative |
| A4 | Paired assurance and disclosure boundaries | `ratified` | `implemented-as-working-baseline` | non-normative |
| A5 | Parameterized privacy and assurance claims | `ratified` | `implemented-as-working-baseline` | non-normative |
| A6 | Nullifier means scoped reuse detection | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| A7 | Delegation remains separate structured evidence | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B1 | Purpose-and-governance-bounded context delimiter | `adopted-working-position` | `implemented-as-working-baseline` | non-normative |
| B2 | Issuer-verifier collusion resistance target | `adopted-working-position` | `implemented-as-working-baseline` | non-normative |
| B3 | Primary profile split | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B4 | Issuer concealment remains profile-specific | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B5 | Boundary records required per predicate | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B6 | Attestation schema determines both boundaries | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B7 | Bounded epochs, cryptoperiods and assurance horizons | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B8 | Agent authority remains separate evidence | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B9 | Mediated proving requires explicit controlled profile | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| B10 | Human legibility is a context conformance requirement | `pending-ratification` | `implemented-as-working-baseline` | non-normative |
| C1 | Specific cryptographic constructions per predicate | `deferred` | `deferred` | non-normative |

## Interpretation

`implemented-as-working-baseline` means the fork contains documentation, schemas, fixtures or tests based on the recorded position; it does not by itself determine upstream status. `adopted-working-position` records an upstream working definition or position that is no longer treated as an open question but has not been recorded as ratified. A transition to `ratified` or `ratified-with-amendment` requires a ratification record identifying the authority, source, date and resulting impact review.
