---
layout: default
title: "Proof Claim Boundaries"
parent: "Conformance"
nav_order: 49
---

# Proof-claim boundaries and non-implication

The [versioned claim catalogue](proof-claim-boundaries.json) and its [schema](schemas/proof-claim-boundaries.schema.json) provide a **downstream, non-normative semantic test** for claims a relying application attempts to infer. The catalogue references existing canonical record IDs and the [evidence-promotion gates](evidence-promotion-gates.md). It does not change upstream construction-record status.

The decision rule is deliberately conservative:

- `ALLOWED`: the requested identifier is *exactly* the established identifier for that record.
- `REJECTED`: the requested identifier is an explicitly prohibited stronger inference.
- `INDETERMINATE`: record, established claim, or requested inference is not supported by the catalogue.

`ALLOWED` means **the semantic inference is permitted given an externally established premise**. This harness does not establish that a proof actually verified, that the premise is authentic, or that a deployment is authorized. Consumers must not interpret `INDETERMINATE` as a permit.

## Run

```sh
python3 scripts/validate_proof_claim_boundaries.py
python3 -m unittest scripts.tests.test_proof_claim_boundaries -v
python3 scripts/validate_proof_claim_boundaries.py --record 010 --established cap_semantic_composition --requested voucher_consent
```

The last command emits `REJECTED` with a nonzero status. The full repository quality gate runs the catalogue validator and its negative tests.

The initial seed set covers records **003, 006, 008, 010 and 021**. This includes explicit refusals to infer policy acceptance from transcript binding, freshness authority from status proof validity, unlinkability from hiding commitments, consent or human uniqueness from Community-Anchored Proof semantics, and delegation or task completion from a VAC authority chain.

This is **not a cryptographic verifier or arbitrary-language entailment engine**. All claim identifiers and prohibited relationships are curated and versioned. Unknown cases fail closed. Additional mappings require semantic review, traceable evidence and tests; extending the catalogue must not turn an unimplemented construction into an executed one.

## Remaining v0.7 gates

The catalogue tests invalid consumer inferences under an assumed premise. It does not fulfill record 010's concrete prover/verifier, independent reproduction or X2 interoperability gates. Proof-execution results and evidence-index digests may later bind to these claim IDs, but absent such binding no validated proof claim is asserted.
