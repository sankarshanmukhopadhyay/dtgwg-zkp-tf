---
layout: default
title: "Community-Anchored Proof Input Contract"
parent: "DTG Interoperability"
nav_order: 8
---
# Community-Anchored Proof input contract

**Status:** Experimental construction-neutral dependency contract  
**Tracks:** [#14](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/14)  
**Source:** https://docs.fpp.storm.ws/dtg-community-anchored-proof-adr.html

## Purpose

ADR-001 requires a presenter to prove that the issuer/counterparty of a relationship credential is also a current member of the same community as the presenter, without requiring that counterparty to be online, consulted, or aware at presentation time.

This document records the minimum semantic input contract that a concrete proof construction must receive from the Credential, Trust Registry, and deployment layers. It does not choose a proof system, accumulator, commitment scheme, registry encoding, or wire format.

The contract exists to prevent an implementation from silently satisfying Clause 3 with wallet co-location, an ordinary holder assertion, a stable lookup identifier, or another fact that does not actually prove the required third-party membership relation.

## Required semantic inputs

| Input | Owning layer | Required property | ZKP-layer use |
| --- | --- | --- | --- |
| relationship credential validity evidence | Credentials / status | authentic and current relationship credential | establish Clause 1 and provenance of issuer/counterparty relation |
| holder membership evidence | Credentials / community | authentic and current membership in community `C` | establish Clause 2 |
| relationship issuer binding | Credentials | construction-neutral evidence defining which party issued the relationship credential | bind Clause 3 to the correct counterparty without disclosing its identifier |
| counterparty membership evidence | Credentials / Registry | independently checkable evidence that the bound counterparty is a member of `C` | establish Clause 3 while counterparty is offline |
| common-community relation | Credentials / Governance / Registry | unambiguous semantics for “same community C” | prove equality/set-membership relation without inventing community semantics |
| registry state identifier | Registry | independently checkable state against which membership/currentness is evaluated | bind proof to a determinable state and freshness policy |
| currentness/revocation evidence | Registry / status | proves relied-upon credentials or membership have not become invalid beyond the published bound | satisfy C1–C4 without a holder-identifying lookup |
| holder-binding evidence | Credentials / wallet profile | proves presenter is the subject/controller required by the credential semantics | satisfy S4 rather than proving mere possession of copies |
| verifier challenge and transcript | verifier / presentation protocol | audience-, context-, and freshness-bound | satisfy S5 and prevent replay |
| deliberately disclosed attributes | holder / verifier policy | explicit and minimised | define the permitted disclosure boundary for P3/P5 |

## Clause 3 sufficiency rule

Clause 3 is **not satisfied** merely because:

- the wallet possesses a copy of the counterparty's credential;
- the relationship credential names an issuer;
- a registry lookup returns a member record using a stable identifier;
- the holder asserts that the issuer belongs to the community;
- two credentials contain values that happen to compare equal without specified semantics; or
- the verifier can infer membership from external graph context.

The construction needs an independently checkable witness or equivalent proof input whose semantics bind the relationship issuer/counterparty to current membership in the same community `C`.

If no such input is available, the implementation result for Clause 3 is **INDETERMINATE / external dependency**. It must not be promoted to PASS.

## Privacy constraints on the input contract

The input contract must permit an implementation to satisfy ADR P1–P5 and C3. In particular:

1. the relationship identifier must remain hidden from the verifier;
2. the counterparty identifier must remain hidden;
3. the holder identifier must remain hidden beyond deliberate disclosure;
4. no registry witness, commitment, accumulator position, lookup key, issuer binder, or transcript value may become a reusable cross-context correlator unless the governing privacy claim explicitly permits that scope;
5. currentness checking must not create a side channel that identifies or links the holder; and
6. independently checkable registry state must not be confused with a requirement for live per-holder verifier-originated lookup.

## Issuance-time dependency rule (X3)

Any construction that requires proof material to exist at issuance time must declare it before implementation interoperability is claimed. Examples may include, depending on the chosen construction, commitments, witness material, membership-set inputs, hidden issuer bindings, or other construction-specific values.

Those examples are not requirements of ADR-001. They are candidate implementation mechanisms. The normative interoperability requirement is that any such issuance dependency is explicit, versioned, and independently implementable.

## Registry interface requirements

The Registry seam must expose enough information for a verifier to judge the relevant community and currentness state while remaining construction-neutral. At minimum, a concrete profile must state:

- what state is being relied upon;
- how that state is authenticated or independently checked;
- the freshness or maximum-age rule;
- the published bound between revocation/suspension and proof rejection;
- how a membership witness or equivalent is derived/updated;
- what observer can see a status or membership check; and
- what correlation scope any registry-facing value has.

Proof validity does not itself establish governance recognition of the community or cross-registry policy acceptance.

## Evidence states

| State | Meaning |
| --- | --- |
| `SUPPORTED` | owning layer supplies semantics and construction-neutral proof input adequate for a candidate construction |
| `CONSTRUCTION-BOUND` | semantics exist but a concrete profile must define how the input is represented/proved |
| `INDETERMINATE` | required semantic input is absent or cannot be independently checked |
| `REJECTED` | supplied evidence contradicts the required predicate, e.g. counterparty is not a current member |

## Current disposition

The ZKP fork can now test the semantic contract and reject/mark indeterminate unsupported Clause 3 claims. A production reference prover/verifier for Clause 3 remains blocked until the owning Credential/Registry layers expose a concrete, interoperable representation satisfying this contract.

That limitation is intentional: the repository should demonstrate the boundary rather than manufacture missing semantics.