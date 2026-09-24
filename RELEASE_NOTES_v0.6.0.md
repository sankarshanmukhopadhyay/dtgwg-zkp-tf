# v0.6.0 — Canonical ZKP Evidence and Composition Baseline

v0.6.0 establishes a new downstream engineering baseline for the DTG ZKP implementation and interoperability fork. The release aligns downstream evidence with the canonical upstream construction-record model, introduces explicit evidence-maturity controls, and advances Community-Anchored Proof from a broad dependency statement to an executable semantic composition with precise remaining construction and interoperability gates.

## Canonical authority baseline

This release is pinned to:

- ZKP specification authority: `trustoverip/dtgwg-zkp-spec@cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`
- ZKP task-force baseline: `trustoverip/dtgwg-zkp-tf@a42bf8c06875cde7c2c9b578279c1be2c682f8ba`

Open upstream ZKP PRs #11 and #12 are not part of this release baseline and remain non-canonical until merged upstream.

The downstream repository remains an implementation, interoperability and assurance workspace. It does not redefine the upstream construction records.

## Highlights

### Canonical construction-record evidence

The downstream repository now carries reusable semantic and assurance evidence for:

- **record 003 — transcript binding**
  - digest/request binding;
  - audience, context and challenge mutation;
  - expiry and replay;
  - canonicalization and predicate-policy boundaries.

- **record 006 — non-revocation/currentness**
  - accepted, stale, unknown and unauthenticated roots;
  - revoked handles;
  - holder-carried authenticated snapshots;
  - live-lookup privacy degradation;
  - explicit separation of proof validity, root authority and freshness policy.

- **record 007 — common control across identifiers**
  - compatibility analysis for current identifier/key shapes;
  - explicit distinction between common control and record-009 hidden equality;
  - presenter-versus-counterparty witness boundaries;
  - identification of the missing normative commitment/profile inputs.

- **record 008 — blinded binder**
  - commitment opening;
  - plaintext leakage;
  - low-entropy deterministic-binder enumeration;
  - visible stable-binder correlation;
  - source-artifact authentication;
  - explicit non-inference of task completion.

- **record 021 — VAC authority chain**
  - attenuation, action, scope and depth;
  - hidden link equality;
  - signature, governing-root and leaf-key checks;
  - currentness and transcript composition;
  - authority-versus-delegation separation;
  - chain-length and registry-observation privacy pressure tests.

### Evidence-state promotion gates

v0.6.0 introduces a machine-readable downstream evidence model with four additive local labels:

- `implemented`
- `independently_reproduced`
- `interoperable`
- `assurance_reviewed`

The model distinguishes:

- deterministic semantic evidence;
- cryptographic execution;
- independent reproduction;
- cross-implementation evidence;
- privacy/adversarial evidence;
- currentness/status evidence;
- performance measurements; and
- audit/security review.

An explicit independent-reproduction contract prevents same-operator code paths or CI reruns from being presented as independent evidence.

Most importantly, downstream labels cannot imply or advance the upstream lifecycle:

`requested → specified → constructed → run → vetted → published`

A downstream green build therefore does not make an upstream construction record `vetted` or `published`.

### Correlation-scope convergence

Active downstream correlation-scope semantics now use the current Credential Specification vocabulary:

- `pairwise`
- `directed`
- `public`

Retired R-DID / M-DID / C-DID / P-DID terminology is retained only where historical provenance requires it.

Role, persona, credential type and DID method are explicitly prevented from being treated as substitutes for correlation scope.

Credential Specification issue #46 still owns the unresolved serialized property and `@context` term. v0.6.0 deliberately does not invent either.

### Community-Anchored Proof / record 010

Community-Anchored Proof is now rebased directly onto canonical **record 010** and components 001–007.

The earlier broad Clause-3 dependency has been replaced by explicit canonical witness routes:

1. the voucher's VMC membership grant/path under `root_C`; plus
2. either:
   - one `directed` identifier used across the relevant intra-community VMC/VRC context; or
   - an authenticated record-007 co-control linkage artifact produced by the voucher at issuance.

The downstream semantic composition now exercises:

- relationship-credential authenticity;
- presenter and voucher membership;
- common-community root;
- voucher linkage;
- self-vouch rejection;
- holder binding;
- currentness/revocation;
- transcript binding;
- optional scoped-nullifier discipline;
- cross-context correlation; and
- counterparty-consent negative space.

A machine-readable requirement matrix now covers ADR-001 requirements P1–P5, S1–S5, C1–C4, T1–T4, D1–D3 and X1–X3.

## What v0.6.0 does not claim

This release does **not** claim that record 010 has a complete end-to-end cryptographic implementation.

In particular, v0.6.0 does not yet provide:

- a concrete complete record-010 reference prover/verifier;
- cryptographic vectors for the whole composed statement;
- D1–D3 end-to-end prover/verifier/transport measurements;
- independent reproduction of the exact CAP profile; or
- cross-implementation ADR-001 X2 evidence.

Those remaining propositions are tracked explicitly:

- **#54** — concrete record-010 reference prover/verifier profile, cryptographic vectors and D1–D3 measurements;
- **#55** — independent reproduction and cross-implementation verification.

Credential- and Registry-owned residual inputs remain tracked separately rather than being manufactured downstream.

## Validation

The release workflow runs the complete repository validation suite before publication:

`python scripts/validate_all.py --evidence-dir results`

The v0.6.0 tranche was developed through issue/branch/PR flow, with Repository Quality and Conformance Harness gates passing before merge for the substantive work.

The GitHub Release is created from the merged `main` revision associated with this release-notes file and is marked as the latest release. Publication is performed by `.github/workflows/release.yml`.

## Release boundary

v0.6.0 is an immutable downstream semantic, conformance and assurance baseline from which the concrete CAP construction work in #54 and independent interoperability work in #55 can proceed.

It is intentionally a stronger engineering baseline without being described as an upstream specification adoption or a completed cryptographic interoperability milestone.
