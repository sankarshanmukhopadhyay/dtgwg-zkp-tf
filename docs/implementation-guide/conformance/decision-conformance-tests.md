---
layout: default
title: "Decision conformance tests"
parent: "Conformance"
grand_parent: "Implementation Guide"
nav_order: 10
has_toc: true
---
# Decision conformance tests

The v0.3.0 tests operationalise the two open, load-bearing upstream decisions without claiming that either has been ratified.

## B1 context integrity

- validate canonical identity, authority, purpose, verifier set, epoch and linkability semantics;
- reject silent verifier-set expansion;
- reject unbounded ecosystem contexts;
- require human-readable shared-context discovery, notice and appeal.

## B2 privacy-claim discipline

- validate named privacy classes and their evidence minima;
- reject a PC-3 claim without an adversary model, correlation assessment, lifecycle profile and test results;
- force downgrade when evidence expires or a stable cross-context correlator is detected;
- prohibit translating scoped reuse detection into a global uniqueness claim.

The machine-readable index is [`decision-conformance-matrix.csv`](decision-conformance-matrix.csv).
