---
layout: default
title: "Privacy class model"
parent: "Privacy Engineering"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Privacy class model

Privacy claims are deployment claims. They describe the protected boundary, adversary, duration, observable surfaces and evidence, rather than merely naming a proof system.

| Class | Minimum claim | Required evidence |
|---|---|---|
| PC-1 | Cross-context separation against non-colluding verifiers | Context descriptor, transcript tests and schema review |
| PC-2 | Cross-context separation against colluding verifiers | PC-1 evidence plus verifier-collusion tests and shared-observable assessment |
| PC-3 | Cross-context separation against issuer-verifier collusion under declared assumptions | PC-2 evidence plus issuer-data, registry/status, lifecycle and correlation-surface evidence |
| PC-R | Reduced-privacy deployment with declared correlation exposures | Exposure statement, affected-person notice and prohibited-claim acknowledgement |

## Claim discipline

A deployment must not claim a stronger class than its evidence supports. A missing adversary model, expired assurance horizon, broadened context or unassessed stable correlator causes downgrade or failure. `PC-R` is not a pass-through label; it requires explicit disclosure of the residual correlation surface.

## Non-implications

No class establishes global person uniqueness, factual correctness of an issuer determination, immunity from endpoint compromise or freedom from correlation through data outside the proof protocol.
