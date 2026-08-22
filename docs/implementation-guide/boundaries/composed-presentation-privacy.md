---
layout: default
title: "Composed-Presentation Privacy"
parent: "Assurance and Disclosure Boundaries"
nav_order: 5
---
# Composed-presentation privacy and evidence closure

Privacy claims in DTG-style proof flows are properties of the complete verification transaction, not of an individual credential or proof object in isolation.

A credential can support selective disclosure or a zero-knowledge presentation and still participate in a linkable transaction when satisfying its semantics requires disclosure or resolution of additional evidence. Relevant evidence can include Trust Task artefacts, delegation evidence, status and revocation data, issuer or accreditation membership, registry state, policy identifiers, receipts, logs and network-visible resolution events.

## Evidence closure

For a requested verification predicate `P`, the **evidence closure** is the minimum complete set of artefacts, relationships and external observations needed by the verifier to establish `P` under the selected profile.

```text
verification predicate P
        |
        +-- credential / attestation evidence
        +-- Trust Task or workflow evidence
        +-- delegation / mandate evidence
        +-- status / revocation evidence
        +-- registry / accreditation evidence
        +-- policy / governance evidence
        +-- resolution and protocol metadata
        |
        v
composed presentation and decision
```

The disclosure boundary MUST analyse this closure as one composition. A privacy claim is incomplete if it considers only fields disclosed from the primary credential while ignoring stable identifiers, ancestry, status queries, registry lookups or other supporting artefacts needed for the decision.

## Cross-specification responsibility model

The composition boundary is intentionally construction-neutral.

1. **Governance** defines which predicates, privacy classes, disclosure allowances, freshness rules and proof profiles are acceptable.
2. **Credential and domain specifications** define the semantic predicates that must be established and the authenticated data needed to support them.
3. **Trust Tasks and other evidence-producing interfaces** expose sufficient authenticated proof inputs so that required relationships can be established without forcing disclosure of durable cross-context correlators unless the governing profile explicitly requires that disclosure.
4. **The ZKP/proof layer** selects constructions that establish those predicates and relationships with the required disclosure, unlinkability, integrity and assurance properties.

A downstream proof construction cannot repair an upstream interface that has made disclosure of a durable correlator semantically mandatory. Privacy therefore remains cross-cutting even when proof construction is owned by the ZKP layer.

## Predicate-oriented modelling

Profiles SHOULD start from the proposition a verifier needs to establish rather than from the fields a credential happens to contain.

Examples include:

- prefer `issuer is a member of acceptable issuer set S` when the verifier does not need the issuer's exact identifier;
- prefer `requested action is within authorised scope` when disclosure of the complete scope is unnecessary;
- prefer `presenter currently has authority derived from an acceptable principal under the selected delegation profile` when disclosure of delegation ancestry is unnecessary;
- prefer `credential is not revoked as of T` over disclosure of a subject- or credential-specific status identifier when the status mechanism can support that predicate privately.

This principle does not require any specific set-membership, commitment, accumulator, selective-disclosure or ZK construction.

## Confidential binding is not the same as hashing

A deterministic digest provides integrity binding but does not automatically provide hiding.

Where the input domain is small or feasibly enumerable — for example a short scope vocabulary, policy identifier, assurance class or status value — an observer may recover the input by enumerating candidates and recomputing the digest.

A profile that relies on a binder for confidentiality MUST therefore state the hiding property it requires and MUST NOT treat a deterministic digest of feasibly enumerable input as a confidential commitment. Construction selection may satisfy this requirement with an appropriate nonce, salt, hiding commitment or another construction, but this boundary document does not prescribe one.

## External resolution and online correlation

Privacy-preserving profiles SHOULD permit verification without verifier-originated network interactions that disclose the subject, credential, presentation or verification event to an authoritative third party.

This is a design objective rather than an absolute prohibition on live lookup. Some profiles may legitimately require current status, rapidly changing authorisation or other fresh state. Where a verifier-originated lookup is required, the profile MUST document:

- what the contacted service learns;
- whether the request contains a stable or quasi-stable identifier;
- whether repeated requests can be linked;
- the applicable retention and logging assumptions;
- the effect on the declared privacy class; and
- whether cached, holder-carried, batched, privacy-preserving or offline evidence is an acceptable alternative.

## Primitive reuse does not collapse semantics

Registry membership, accreditation, anchoring, revocation and authorisation may sometimes use the same family of proof primitives. That reuse does not make the predicates semantically equivalent.

A profile MUST preserve the independent governance authority, lifecycle, freshness, failure semantics and accountability model of each predicate even when their cryptographic realization shares a construction.

## Required boundary record

For every material composed predicate, the boundary record SHOULD capture:

| Field | Required question |
|---|---|
| Predicate | What proposition is the verifier entitled to conclude? |
| Evidence closure | Which artefacts and external state are required to establish it? |
| Visible values | Which stable or quasi-stable values are exposed to each actor? |
| Relationship proof inputs | Which authenticated inputs are required to prove cross-artifact relationships? |
| Online observations | Which network actors learn that verification occurred? |
| Adversary and horizon | Against whom, and for how long, does the privacy claim hold? |
| Governance profile | Which disclosure and freshness choices are permitted? |
| Construction status | Which mechanism is selected, experimental or still deferred? |

## Review rule

A composed presentation MUST NOT inherit the strongest privacy label of its component credentials or proofs. The privacy class of the transaction is bounded by the weakest material disclosure or correlation surface in its evidence closure.

This rule is especially important for delegation, Trust Task composition, status evaluation and registry/accreditation checks, where an otherwise unlinkable leaf proof can become linkable through supporting evidence.