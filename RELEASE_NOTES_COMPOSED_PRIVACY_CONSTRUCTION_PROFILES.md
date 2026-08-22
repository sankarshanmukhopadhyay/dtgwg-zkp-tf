# Composed-privacy construction and profile pressure tests

This change record summarizes the downstream experimental work that followed completion of the construction-neutral composed-presentation privacy requirements.

## Evidence tracks

- **BBS credential layer (`EXP-BBS-2023-01`)** — executable correctness/benchmark evidence plus externally sourced independent interoperability evidence for the BBS features actually covered by the W3C report.
- **Cross-artifact relationship proof (`EXP-PR-REL-SIGMA-01`)** — Ristretto255 linear-relation Sigma proof with context-bound Fiat-Shamir transformation, positive/negative vectors and benchmark evidence.
- **Confidential binder (`EXP-PR-HID-PEDERSEN-01`)** — randomized Ristretto255 Pedersen-style commitments, low-entropy dictionary-attack regression, opening tests, same-value unlinkability checks and benchmark evidence.
- **External resolution (`PR-RES`)** — explicit machine-readable profiles for shared/cached Bitstring Status List evidence, carried authenticated snapshots and governed live lookup with declared privacy degradation.

## Architectural result

The experiments support the separation established by the requirements work: semantic predicates define **what must be provable**, evidence interfaces expose authenticated proof inputs, and construction/profile choices define **how** the property is realized. No single cryptographic primitive is treated as the semantic definition of status, registry membership, accreditation, authorization or delegation.

## Maturity boundary

These profiles are experimental and non-normative. Governed promotion, representative-device evidence and independent DTG-specific interoperability remain separate maturity gates.
