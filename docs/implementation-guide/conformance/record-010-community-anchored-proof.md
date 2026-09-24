---
layout: default
title: "Record 010 Community-Anchored Proof Evidence"
parent: "Conformance"
nav_order: 48
---
# Record 010 Community-Anchored Proof evidence

This downstream evidence profile consumes canonical upstream record 010 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

It replaces the earlier generic “Clause 3 dependency” posture with the more precise witness paths now present in canonical record 010:

1. the voucher's VMC grant and membership path under `root_C`; and
2. voucher linkage established either by:
   - one `directed` identifier reused for the VMC and VRC inside the intended community scope; or
   - an authenticated co-control linkage artifact produced by the voucher at issuance, consumed under record 007.

The presenter never derives the voucher's controller secret.

## What is executable now

The semantic composition adapter executes positive and negative cases for:

- relationship-credential authenticity;
- presenter and voucher membership under one community root;
- voucher linkage availability and swapped/invalid linkage;
- distinct membership leaves / self-vouch rejection;
- holder binding;
- three status-bearing artifacts using the reusable record-006 adapter;
- transcript binding using the reusable record-003 adapter;
- optional scoped nullifier discipline;
- cross-context binder rejection; and
- the negative-space rule that the proof does not establish counterparty consent to the disclosure.

The fixture corpus is in `fixtures/record-010-community-anchored-proof.json`.

## Clause 3 result

Clause 3 is no longer represented as an undifferentiated unknown.

It has a **sound semantic implementation path** when the presenter has:

- the voucher's community membership witness/path for the accepted `root_C`; and
- one of the canonical linkage routes above.

If neither linkage route exists, the result is `blocked / voucher-linkage-unavailable`, not PASS.

This is a materially narrower dependency than the older “third-party membership evidence checkable” Boolean.

## Evidence-gate result

Under the downstream evidence-state model:

- record 010 has **semantic composition evidence**;
- it does **not** yet receive the downstream `implemented` construction label;
- it is not independently reproduced;
- it is not cross-implementation interoperable;
- no upstream lifecycle state is advanced.

The reason is straightforward: this repository still has no concrete end-to-end cryptographic implementation of all record-010 clauses.

## Remaining construction gates

The remaining work is now specific:

1. choose and document the exact construction profile for authenticated VRC/VMC proof inputs and membership/non-revocation composition;
2. implement the concrete prover and verifier for the whole record-010 statement;
3. produce cryptographic positive/negative vectors corresponding to the semantic cases;
4. measure prover time/memory, verifier cost and proof/transport size;
5. reproduce the exact profile independently; and
6. perform cross-implementation verification for X2.

Credential-owned record-007 commitment/linkage serialization and authoritative registry freshness/propagation remain external inputs rather than local semantics.

## Requirement matrix

The machine-readable [record-010 requirement matrix](record-010-requirement-matrix.json) covers P1–P5, S1–S5, C1–C4, T1–T4, D1–D3 and X1–X3, and records the remaining gate for each requirement.

This is the restart baseline for any concrete CAP construction work.
