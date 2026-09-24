---
layout: default
title: "Downstream Evidence-State Promotion Gates"
parent: "Conformance"
nav_order: 46
---
# Downstream evidence-state promotion gates

This document defines **downstream evidence claims**, not an alternate construction-record lifecycle.

Canonical upstream lifecycle at the pinned baseline remains:

`requested → specified → constructed → run → vetted → published`

No downstream CI result, local proof round-trip, benchmark, assurance review or independent reproduction changes those upstream states.

The machine-readable source is [evidence-promotion-gates.json](evidence-promotion-gates.json).

## Downstream labels

| Label | Minimum meaning | Explicit non-implication |
|---|---|---|
| `implemented` | a named semantic or construction artifact executes repeatably with provenance | not independent, not interoperable, not upstream vetted/published |
| `independently_reproduced` | a named result is reproduced by an independent operator or independently maintained implementation | not automatically interoperable or upstream vetted |
| `interoperable` | two or more independently maintained implementations agree on the exact shared profile/vectors/protocol exchange | not a security/privacy audit and not upstream vetted |
| `assurance_reviewed` | a named claim has an explicit adversary/assurance scope, review provenance and residual risks | not proof of interoperability or independent reproduction |

These labels may coexist because they answer different questions.

## Evidence classes

Evidence must remain claim-scoped:

- **deterministic semantic** — proposition/policy behavior;
- **cryptographic execution** — a named construction actually executes;
- **independent reproduction** — a result can be reproduced independently;
- **cross-implementation** — independently maintained implementations agree on the same profile;
- **privacy/adversarial** — a named privacy claim under a stated adversary;
- **currentness/status** — a result under named root/state/freshness assumptions;
- **performance** — measured environment only;
- **audit/security review** — reviewed surface only.

A generic PASS MUST NOT collapse these classes.

## Current canonical-record evidence

| Record | Current downstream claim | Material gaps |
|---|---|---|
| 003 | implemented semantic evidence | independent reproduction; cross-implementation |
| 006 | implemented + assurance-reviewed | authoritative freshness policy; independent/cross-implementation evidence |
| 007 | assurance-reviewed compatibility analysis | normative commitment profile; cryptographic execution; independent/cross-implementation evidence |
| 008 | implemented construction evidence + assurance-reviewed | independent/cross-implementation evidence; Credential-owned member/profile |
| 021 | implemented semantic composition + assurance-reviewed | production construction; implementation correspondence; independent/cross-implementation evidence |
| 010 | no promotion label yet | clause-3 witness contract; construction execution; independent/cross-implementation evidence; performance |

## Independent reproduction contract

A reproduction is independent only when it records:

1. a different maintainer/operator or independently maintained implementation;
2. immutable source revision;
3. exact profile/vector identifier;
4. environment/runtime;
5. verifier-visible result and reason;
6. evidence artifact digest; and
7. what was **not** reproduced.

The following do not count:

- rerunning the same CI;
- two code paths under the same operator;
- semantic fixture success presented as cryptographic interoperability;
- external primitive-library interoperability presented as interoperability for a DTG composed record without DTG-specific vectors.

## Consumption by Community-Anchored Proof

Issue #14 must route every claim through this model.

In particular, record 010 cannot be called `implemented` until the concrete clause-3 path actually executes. Its current semantic fixtures remain useful, but they do not satisfy the construction-execution gate.

Likewise, X2 cannot be claimed until independent implementations exchange the exact CAP profile/vectors successfully.

## Upstream-state firewall

The following wording is prohibited in downstream release notes or evidence summaries unless the corresponding upstream repository itself records the state:

- “record N is vetted”;
- “record N is published”;
- “downstream testing promoted record N”;
- any equivalent statement that converts local evidence into an upstream lifecycle transition.

Downstream evidence should instead state the local label, evidence class, asset revision and remaining gaps.
