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
| proof constrains the supplied transcript digest | R003-POS-001 / NEG-001 | accept exact digest; reject substituted digest |
| audience binding | R003-NEG-002 | reject mismatched audience even when proof digest binding is otherwise valid |
| governed context binding | R003-NEG-003 | reject mismatched context |
| challenge binding | R003-NEG-004 | reject mismatched challenge |
| freshness | R003-NEG-005 | reject expiry as verifier policy, not as a property inferred from digest binding |
| replay | R003-NEG-006 | reject a previously seen transcript under replay policy |
| canonical encoding | R003-NEG-007 | reject an incorrectly derived/canonicalized digest even when the proof constrains that supplied scalar |
| predicate/profile acceptance | R003-NEG-008 | reject an unknown/unaccepted predicate identifier independently of digest binding |

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
