---
layout: default
title: "CAP Construction Selection Gate"
parent: "Conformance"
nav_order: 50
---

# Record 010: construction-selection gate

**Decision:** not frozen. This is an implementation feasibility gate for [issue #54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54), nested under [v0.7.0 programme #67](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/67). It does not assert that any candidate meets canonical record 010, or that upstream has adopted its semantics.

The canonical baseline is `trustoverip/dtgwg-zkp-spec@cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`. The existing [requirement matrix](record-010-requirement-matrix.json) remains the coverage baseline and [proof-claim boundaries](proof-claim-boundaries.md) constrain consumer inference. The [machine-readable candidate/gate register](cap-construction-selection.json) is an engineering selection aid, not a replacement authority.

## Candidate routes

| Route | Reason to investigate | Main falsification risk |
|---|---|---|
| SNARK-style joint circuit | All predicates can potentially share one compositional proof statement | Signature compatibility, circuit constraints, setup/security assumptions and engineering cost |
| Commit-and-prove | Potentially reuses credential signature and authenticated commitment profiles | Subproof composition may fail to prove shared witness consistency |
| Hybrid bound receipts | Separately executable subproofs can be integrated incrementally | A collection of verified components may not amount to the canonical joint proposition, and may reveal linking metadata |

These are **hypotheses**, not three established implementations. Choosing whichever yields the fastest passing fixtures would violate the canonical record.

## Mandatory selection checks

The gate IDs in the JSON register map to P1–P5, S1–S5, C1–C4, T1–T4, D1–D3 and X1–X3 in the existing record-010 requirement matrix.

A selection must demonstrate:

1. One precise canonical statement and its witness relationships, including both voucher membership and issuance-time directed identifier **or** authenticated co-control linkage. The voucher remains offline at proving time.
2. Cryptographic evidence that all consumed subproofs and statements refer to the intended community root, subject, scope, status context and transcript; a semantic mock is insufficient.
3. Negative cases for swapped voucher linkage, wrong root, invalid credential, replayed transcript, stale status and self-vouch attempts, with explicit expected rejection or indeterminate behavior.
4. Proof-to-claim non-implication integration. A valid proof may not entail voucher consent, distinct-human uniqueness, unconditional unlinkability or external authorization.
5. Concrete Credential/Registry representation and freshness assumptions, marked *experimental and external*, rather than silently invented as downstream normative semantics.
6. Repeatable D1/D2/D3 measurement methods and fully specified environment and version identity.
7. Independent-reproduction and X2 requirements retained as **separate future evidence gates**. A second invocation of one operator's implementation is not independence.

## Decision protocol

Implement the smallest *falsifiable spike* for the top candidate. If witness consistency or authoritative input compatibility fails, retain the failure evidence and evaluate another route. Do not freeze a profile merely because individual primitives verify.

Before `decision` can change to `frozen`, require an attributable review documenting the exact implementation/version, which route was selected, why alternatives were rejected, clause-by-clause execution references, known limitations, and rejected stronger inference tests. Run `python3 scripts/validate_cap_selection.py` and the repository full validation suite. The validator enforces structural consistency and explicitly blocks unsupported frozen decisions; it does not independently prove cryptographic validity.

## Stop/advance boundary

It is productive to finish this selection gate before writing the full prover. It is **not** productive to claim #54 complete, advance record 010 to a constructed upstream lifecycle state, or cut v0.7.0 with only this design exercise. Subsequent construction work follows #54; independent qualification follows #55.
