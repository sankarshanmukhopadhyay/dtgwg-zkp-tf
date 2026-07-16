---
title: Composition and reconstruction assessment
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Composition and reconstruction assessment

A proof is assessed together with every credential field, protocol element, registry query, error path and retained record presented or produced in the same transaction.

## Required assessment

1. enumerate all predicates and proofs composed in one request;
2. identify shared hidden relations, commitments, roots and subject bindings;
3. test rare combinations, ordering, length and proof-shape fingerprints;
4. analyse sequential composition across sessions, verifiers and contexts;
5. include status traffic, request timing, retries and decision receipts;
6. state whether recursive composition or folding was considered and why it is or is not deployable;
7. map each leakage path to a disclosure boundary, threat and conformance test.

A bundle of individually sound proofs is not assumed to preserve the privacy claims of each component.
