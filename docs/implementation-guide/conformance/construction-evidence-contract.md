---
layout: default
title: "Construction evidence contract"
parent: "Conformance"
nav_order: 25
---
# Construction evidence contract

Construction/profile evidence is normalized through [`construction-evidence-manifest.json`](./construction-evidence-manifest.json) and validated against [`construction-evidence-manifest.schema.json`](./schemas/construction-evidence-manifest.schema.json).

The contract does not make different proof constructions semantically equivalent. It provides a common evidence envelope so automation and portfolio consumers can distinguish what was executed from what remains unverified.

Each profile records:

- `profile_id` and claim layer;
- normative status;
- repository evidence state;
- workflow and artifact provenance;
- independent-interoperability state;
- source/provenance paths; and
- a claim boundary that prevents local evidence from being interpreted more broadly than warranted.

## Anti-overclaim invariants

`scripts/validate_construction_evidence.py` enforces two consequential rules in addition to JSON Schema validation:

1. interoperability cannot be `verified` or `complete` unless the evidence is explicitly independent; and
2. an overall evidence state cannot be `complete` unless interoperability is also `complete`.

It also rejects duplicate profile identifiers and missing repository-local provenance/evidence paths.

These checks are part of `scripts/validate_all.py`, so malformed or overstated evidence fails the repository completion gate.

## Adding another profile

A new construction or profile should first preserve its construction-specific evidence and semantics. Then add one manifest entry that points at those artifacts. Local round-tripping by two adapters from the same implementation does not count as independent interoperability.

For Community-Anchored Proof work, this contract is the evidence envelope to use once concrete Clause 3 inputs are available from the owning DTG layers.