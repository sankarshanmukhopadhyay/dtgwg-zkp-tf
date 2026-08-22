---
layout: default
title: "Composed-Presentation Privacy Tests"
parent: "Conformance"
nav_order: 12
---
# Composed-presentation privacy tests

These construction-neutral cases test whether a profile's privacy claim survives the complete evidence closure needed for verification. They are negative semantics tests: a cryptographically valid component proof can still fail the declared privacy profile when supporting evidence introduces an avoidable correlation surface.

## Test model

Each case records:

- the primary credential/proof privacy property;
- the additional evidence required to establish the requested predicate;
- the correlation channel introduced by that evidence;
- the expected conformance result; and
- the remediation property, without prescribing a cryptographic construction.

## CP-PRIV-001 — status lookup reveals a stable credential reference

**Given** a selectively disclosed or ZK credential presentation that does not reveal a stable subject identifier,

**and** the verifier must query a status service using a stable credential- or subject-specific reference,

**when** that service can associate repeated lookups with the same credential, subject or verifier,

**then** a profile claiming unlinkability against the status service or status-service/verifier collusion **MUST fail** unless the correlation surface is explicitly allowed by the declared privacy class.

**Remediation property:** status evaluation must be possible under the selected privacy profile without an undeclared durable cross-context correlation channel, or the profile must declare the weaker privacy class.

## CP-PRIV-002 — delegation ancestry defeats leaf unlinkability

**Given** a leaf delegation credential that supports selective disclosure or unlinkable presentation,

**and** verification of current authority requires disclosure of a stable delegation ancestry or principal identifier,

**when** that ancestry permits cross-context correlation of otherwise unlinkable leaf presentations,

**then** an end-to-end unlinkability claim **MUST fail** unless disclosure of the ancestry is explicitly required and accounted for by the governing profile.

**Remediation property:** the delegation/evidence interface must expose sufficient authenticated proof inputs to establish the required authority predicate without mandatory disclosure of durable ancestry where the profile requires stronger privacy.

## CP-PRIV-003 — enumerable digest is misclassified as confidential binding

**Given** a profile attempts to hide a value such as a scope, assurance class or policy identifier by disclosing only a deterministic digest,

**and** the underlying input domain is small enough to enumerate feasibly,

**when** an observer can recover the original value by hashing candidate inputs,

**then** a confidentiality or hiding claim based solely on that digest **MUST fail**.

**Remediation property:** the binder must provide the hiding property required by the profile; a deterministic integrity digest alone is insufficient for feasibly enumerable inputs.

## CP-PRIV-004 — registry/accreditation resolution leaks exact issuer unnecessarily

**Given** the semantic predicate required by the relying decision is only that the issuer belongs to an acceptable issuer or accreditation set,

**and** the profile nevertheless requires disclosure or online resolution of an exact stable issuer identifier,

**when** that identifier creates correlation not required by the predicate,

**then** a data-minimisation or issuer-concealment claim **MUST fail** unless the governing profile explicitly requires exact issuer disclosure.

**Remediation property:** model and prove the narrowest predicate the verifier requires, while preserving governance and freshness semantics of the set-membership/accreditation decision.

## CP-PRIV-005 — individually private components become linkable when composed

**Given** two or more credentials, proofs or Trust Task artefacts each satisfy their standalone privacy tests,

**and** a composed transaction exposes a shared identifier, timestamp pattern, receipt, correlation handle, network observation or other quasi-stable value across the evidence set,

**when** the declared adversary can use that value to link presentations across contexts,

**then** the composed presentation **MUST fail** the stronger unlinkability claim even though every individual component passed its standalone test.

**Remediation property:** assess the complete evidence closure and either remove/minimise the material correlation surface or declare the privacy class actually achieved.

## CP-PRIV-006 — live authoritative lookup is undeclared in the privacy profile

**Given** a profile requires verifier-originated access to authoritative current state,

**when** the contacted service learns that a particular subject, credential, presentation or verifier is participating in a verification event,

**and** this observation is not captured in the disclosure boundary and privacy-class evidence,

**then** the profile **MUST fail** its privacy conformance review.

A live lookup is not automatically non-conformant. The failure is the undeclared or unbounded correlation surface.

## CP-PRIV-007 — common proof primitive collapses distinct governance semantics

**Given** registry membership, accreditation, revocation or authorisation use the same family of set-membership or non-membership proofs,

**when** an implementation treats those predicates as having interchangeable authority, freshness, lifecycle or failure semantics merely because the proof mechanism is shared,

**then** semantic conformance **MUST fail**.

**Remediation property:** preserve the independent governance authority, evaluation time, lifecycle, status and failure meaning of every predicate even where constructions are reused.

## Evidence expectations

A profile claiming composed-presentation privacy should retain evidence showing:

1. the requested predicate and its minimum evidence closure;
2. all stable and quasi-stable values visible to each actor;
3. verifier-originated network interactions and what each contacted service learns;
4. the declared adversary and privacy horizon;
5. the governing profile's intentional disclosure allowances;
6. any construction-dependent hiding or membership assumptions; and
7. the result of these negative cases or equivalent tests.

These tests complement standalone credential, proof and transcript tests. Passing component tests is necessary but not sufficient for an end-to-end privacy claim.
