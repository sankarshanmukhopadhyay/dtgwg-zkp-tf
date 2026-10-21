---
layout: default
title: "Record 003 Transcript-Binding Evidence"
parent: "Conformance"
nav_order: 41
---
# Record 003 transcript-binding evidence

This downstream evidence profile is pinned to canonical upstream construction record 003 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

It tests the boundary between **proof binding to a supplied transcript digest** and the verifier responsibilities that record 003 explicitly does not establish by itself.

## Clause-to-test matrix

| Surface | Evidence | Result |
|---|---|---|
| proof constrains the supplied transcript digest | CT-INT-TASK-POS-01 plus adapter unit negative | accept exact digest; reject substituted digest |
| audience binding | adapter unit negative | reject mismatched audience even when proof digest binding is otherwise valid |
| governed context binding | adapter unit negative | reject mismatched context |
| challenge binding | adapter unit negative | reject mismatched challenge |
| freshness | adapter unit negative | reject expiry as verifier policy, not as a property inferred from digest binding |
| replay | CT-INT-TASK-NEG-01 | reject a previously seen transcript under replay policy |
| canonical encoding | adapter unit negative | reject an incorrectly derived/canonicalized digest even when the proof constrains that supplied scalar |
| predicate/profile acceptance | adapter unit negative | reject an unknown/unaccepted predicate identifier independently of digest binding |

## Assurance boundary

A valid record-003 binding proves only that the proof constrains the supplied transcript scalar. It does **not** prove that:

- the verifier calculated that scalar from the right bytes;
- canonical encoding was correct;
- the audience, challenge or context are acceptable under current policy;
- the request is fresh;
- the same transcript has not already been consumed;
- a predicate/profile identifier is meaningful or accepted; or
- the surrounding Trust Task completed.

These checks are therefore represented as separate policy-layer outcomes in the executable adapter.

## Reuse

The evidence is intended to be reused by:

- record 010 Community-Anchored Proof work (#14);
- record 021 VAC assurance (#33);
- record 006/currentness composition where a status assertion is task-bound;
- Trust Task integration profiles; and
- record 013 mutual-edge admissibility once its canonical clauses advance beyond `requested`.

No upstream evidence-state advancement is claimed by these downstream tests.


## Pinned construction reproduction path (2026-10-21)

The authoritative record 003 at `trustoverip/dtgwg-zkp-spec@aa4e285bbed35ecb2cacb660f798968c9a9793b5` points to a separate experimental construction laboratory. The laboratory is available at `mitchuski/dtgwg-zkp-mage@1be94c809da595f5eac76f6d99c7195a574b20db`. Its `runtimes/canonical/test.mjs` checks descriptor/transcript encoding, while `runtimes/circom-gadget/test.mjs` includes genuine Groth16 proof verification, particularly **Z9** (transcript scalar substitution fails) and **Z10** (the nullifier remains stable across transcripts).

The dedicated [pinned laboratory workflow](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/blob/main/.github/workflows/upstream-record003-lab.yml) checks out that exact lab revision, runs canonical encoder tests, builds a **lab-only** proving setup and attempts Z9/Z10 within the upstream suite. The workflow outcome, not the existence of this document, is the execution evidence.

**Scope:** The reference gadget uses a local, fixed-entropy single-contributor setup, not a production trusted ceremony. Its binding is to a supplied scalar with a dummy-square constraint; this is not a blanket claim about transcript bytes, verifier policy or simulation extractability. The canonical record and lab live in distinct repositories with distinct authority. No downstream `current` promotion occurs unless the pinned workflow has passed and explicit clause-specific review resolves the remaining non-implications.
