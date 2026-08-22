---
layout: default
title: "Composed Proof Responsibility Model"
parent: "Architecture"
nav_order: 12
---
# Composed proof responsibility model

Privacy-preserving verification is a cross-specification composition problem. The architecture separates four responsibilities so that privacy requirements do not become coupled to one proof construction.

```text
Governance
    |
    v
Semantic predicates
    |
    v
Evidence / proof interfaces
    |
    v
Private proof construction
```

## 1. Governance

Governance defines which predicates, disclosure allowances, privacy classes, freshness rules, acceptable issuer or authority sets and proof profiles are permitted for a deployment.

Governance can select among available profiles; it cannot compensate for an upstream interface that makes disclosure of a durable cross-context correlator unavoidable.

## 2. Semantic predicates

Credential, Trust Task, delegation and other domain specifications define the propositions a relying party is entitled to establish. They SHOULD express the narrowest predicate required by the relying decision rather than treating available fields as mandatory disclosures.

Examples include issuer-set membership, action-within-scope, non-revocation as of a defined time and current delegated authority under a selected policy.

## 3. Evidence and proof interfaces

Evidence-producing specifications expose authenticated data and relationship inputs needed to establish the semantic predicates. Where the governing profile requires privacy, those interfaces MUST avoid making a durable correlator the only way to establish a relationship unless that disclosure is explicitly part of the profile.

This is the principal cross-specification obligation. Once a durable identifier, delegation ancestry or subject-specific resolution key is made semantically mandatory, a downstream ZK construction may be unable to recover the intended unlinkability property.

## 4. Private proof construction

The ZKP/proof layer selects constructions that prove the predicates and relationships with the required disclosure, integrity, unlinkability, freshness and performance properties.

The architecture deliberately does not require a particular commitment, selective-disclosure signature, accumulator, Merkle structure, PRF, SNARK or other proof system at this layer.

## Composition rule

A composed transaction inherits neither the privacy label nor the assurance label of its strongest component. The complete evidence closure must be evaluated against the declared adversary, horizon and governance profile.

See [Composed-presentation privacy and evidence closure](../boundaries/composed-presentation-privacy.md) for the operational boundary method and [Composed-presentation privacy tests](../conformance/composed-presentation-privacy-tests.md) for negative conformance cases.