---
layout: default
title: "Experimental PR-REL Sigma Profile"
parent: "Conformance"
nav_order: 14
---
# Experimental PR-REL Sigma relationship-proof profile

**Status:** Experimental / non-normative

This profile selects a concrete construction for `PR-REL`: proving that two independently authenticated artifacts contain commitments to the same hidden value without disclosing that value or requiring a stable cross-context identifier.

The profile is based on the CFRG work items `draft-irtf-cfrg-sigma-protocols-03` (17 August 2026) and `draft-irtf-cfrg-fiat-shamir-03` (16 August 2026). Both remain Internet-Drafts and are therefore treated here as experimental construction inputs, not as a DTG-wide mandate.

## Relation proved

For Ristretto255 group generators `G` and independently derived `H`, two artifacts expose Pedersen-style commitments:

```text
C1 = m*G + r1*H
C2 = m*G + r2*H
```

The prover demonstrates knowledge of `(m, r1, r2)` satisfying both equations. The verifier learns that the same hidden scalar `m` is committed in both artifacts, but does not learn `m`, `r1`, or `r2`.

This is the concrete `PR-REL` case that corresponds to the requirements-level rule: prove the relationship required by the verifier without disclosing the durable value that creates that relationship.

## Non-interactive construction

The local executable profile uses the standard three-move linear-relation proof shape and applies a Fiat-Shamir challenge bound to:

- the profile/domain identifier;
- the two commitment encodings;
- the prover commitments;
- the verifier/application context string.

The context binding is mandatory. A proof generated for one task, verifier context, evidence closure, or policy context MUST NOT verify under another context.

## Generator rule

`G` is the Ristretto255 base point. `H` is derived independently using Ristretto255 hash-to-group from a profile-specific domain string. A deployment MUST NOT choose `H` with a known discrete-log relationship to `G`.

## What this closes

| Predicate | Construction status | Notes |
|---|---|---|
| `PR-REL` | **experimental construction available** | Equality of a hidden scalar across two authenticated Pedersen-style commitments is executable and benchmarked. |
| `PR-CMP` | **partially supported** | The relationship can be established without revealing the shared value; privacy of the complete evidence closure remains separately testable. |
| `PR-HID` | **partially supported** | Pedersen-style commitments provide a hiding primitive for high-entropy scalar representations, but application encoding and low-entropy message handling require the dedicated `PR-HID` profile. |
| `PR-DEL` | **partially supported** | The construction can prove equality/linkage between committed authority inputs, but it does not itself prove delegation-chain validity, scope semantics, or governance authorization. |

## Authentication boundary

This profile proves a relationship between values represented by `C1` and `C2`. It does **not** authenticate those commitments by itself. Each commitment MUST be bound to an independently authenticated artifact, credential, Trust Task result, delegation object, registry snapshot, or other governed evidence source before the relationship proof is relied upon.

A mathematically valid equality proof over attacker-chosen unauthenticated commitments is not evidence of a legitimate DTG relationship.

## Encoding boundary

The witness `m` is a field scalar in this executable profile. Specifications using strings, identifiers, scope labels, policy identifiers, hashes, or structured objects MUST define a canonical encoding-to-scalar procedure and analyze dictionary/enumeration risk before claiming confidentiality.

This profile therefore closes the **relationship proof construction slot**, not the separate semantic question of how every DTG value is encoded safely.

## Executable evidence

`benchmarks/pr-rel-sigma/relationship-proof.mjs` implements the profile with `@noble/curves` Ristretto255 primitives. The CI workflow executes:

1. a deterministic positive vector;
2. failure after changing the second committed value;
3. failure after changing the verifier/application context;
4. repeated proof generation with fresh prover randomness; and
5. proof-generation and verification benchmarks.

The emitted JSON is construction evidence. Hosted-runner timing values are informational and MUST NOT be used as normative performance thresholds.

## Relationship to modular commit-and-prove work

The July 2026 `draft-bormann-jwp-modular-bbs` proposal independently describes the same broader architectural direction: fresh commitments to hidden credential messages can feed chained sub-proofs such as equality proofs. This profile does not adopt that credential format, but the direction supports the DTG requirement that authenticated proof inputs be exposed in a form that can participate in private composition.

## Promotion criteria

Promotion beyond experimental status requires:

- CFRG review/status changes for the Sigma/Fiat-Shamir drafts to be reassessed;
- an encoding profile for each concrete DTG relationship type;
- independent implementation evidence for the exact relation and serialization claimed here;
- adversarial review of transcript/domain separation and commitment authentication boundaries;
- representative constrained-device and server benchmarks; and
- confirmation that surrounding evidence does not reintroduce the correlator hidden by this proof.

Until then, this is executable construction evidence for `PR-REL`, not a universal DTG proof-system selection.
