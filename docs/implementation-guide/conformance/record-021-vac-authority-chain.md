---
layout: default
title: "Record 021 VAC Authority-Chain Assurance"
parent: "Conformance"
nav_order: 45
---
# Record 021 VAC authority-chain assurance

This downstream pressure-test profile is pinned to canonical upstream construction record 021 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

It consumes the reusable record-003 transcript and record-006 currentness evidence created under #45 rather than rebuilding those semantics inside the VAC test.

## Clause-to-test mapping

| Record 021 surface | Executable evidence |
|---|---|
| action is conferred; scope/validity only narrow | R021-NEG-ACTION, R021-NEG-WIDEN |
| depth ≤ 8 and every attenuation limit respected | R021-NEG-DEPTH, R021-NEG-LIMIT |
| child issuer equals parent subject; parent digest matches | R021-NEG-ISSUER, R021-NEG-PARENT; semantic component is record 009 |
| every hidden link is authenticated | R021-NEG-SIG |
| root issuer is the governing party under root_G | R021-NEG-ROOT; component record 001 |
| presenter controls the leaf subject key | R021-NEG-KEY; component record 004 |
| status-bearing links are unrevoked at accepted state | R021-NEG-REVOKED; reuses record-006 adapter |
| whole show is bound to one transcript | R021-NEG-TRANSCRIPT; reuses record-003 adapter |

## Authority-versus-delegation boundary

R021-NEG-DELEGATION makes the critical distinction executable:

> A valid VAC chain establishes that the presenter **acts as itself under attenuated authority**. It does not appoint the presenter to act in another party's name.

Delegation is the sibling record 020 proposition and must remain separately evidenced.

Similarly, R021-NEG-TASK rejects the inference that valid authority proves an action was performed or a Trust Task completed.

## Privacy pressure tests

Two record-021 limitations are explicit test surfaces:

- **chain length:** R021-NEG-CHAIN-LENGTH rejects a claim that ancestry length is hidden when the proof shape is neither fixed nor padded;
- **registry observation:** R021-NEG-REGISTRY-PRIVACY rejects an unconditional privacy claim when status is obtained through a live subject-specific lookup.

These are assurance tests around the canonical proposition, not new record semantics.

## Residual external dependencies

The executable suite still does not establish:

- that the governing party remains entitled to govern the scope beyond the accepted `root_G` state;
- who sets the freshness/propagation rules for registry state;
- whether the leaf subject independently qualifies where the governing policy requires it;
- a production fixed-shape/padded chain construction;
- distinct controllers at every hop;
- cryptographic implementation correspondence or independent reproduction.

Those remain explicit assurance/promotion dependencies under #28 and the relevant upstream authorities.

## Evidence

Machine-readable cases are in `fixtures/record-021-vac-authority-chain.json` and are executed by the conformance-harness test suite.
