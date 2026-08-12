---
layout: default
title: "Issuer implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Issuer implementation guide

The issuer is authoritative only for the attestation it is empowered to make. It is responsible for the governed process that converts upstream evidence into a signed attestation and for preserving the lifecycle semantics that downstream proofs rely on.

{: .warning }
A valid ZK proof can demonstrate possession of an attestation satisfying a predicate. It does not retroactively validate the issuer's enrolment, biometric, liveness, uniqueness or personhood process.

## Responsibilities

An issuer implementation should:

- verify that the issuer is authorised for the claimed profile, predicate and population;
- apply a versioned issuance policy and schema;
- bind the attestation to the intended holder-control mechanism;
- minimise fields before signing rather than relying on the prover to hide unnecessary data later;
- protect signing keys and separate enrolment, approval and signing authority where appropriate;
- publish deterministic expiry, suspension, revocation and replacement semantics;
- preserve evidence sufficient to investigate incorrect issuance without creating an unnecessary identity database; and
- provide correction, appeal and reissuance paths.

## Inputs and authority dependencies

| Input | Required question |
|---|---|
| Governance mandate | Who authorises this issuer to make this class of attestation? |
| Predicate/profile | What exact downstream statement may be proven? |
| Enrolment/liveness method | What evidence is accepted and to what assurance level? |
| Schema | Which signed fields are necessary, and what correlation risk does each add? |
| Holder binding | What secret/key is bound and how is control established? |
| Status policy | When do suspension, revocation, expiry and replacement take effect? |
| Registry recognition | How can a verifier determine issuer authority at a relevant time? |

## Issuance pipeline

`authority check → enrolment evidence → policy evaluation → holder binding → schema minimisation → approval → signing → delivery → status publication → evidence retention`

Each stage should have a stable decision identifier and policy/schema version. Where a human or external service makes an upstream determination, record its evidence reference and accountable operator/service rather than importing opaque assertions into the signed credential.

## Schema and correlation discipline

Use the [attestation schema profile](../information-model/attestation-schema-profile.md) and [correlation-surface assessment](../information-model/correlation-surface-assessment.md). In particular:

- avoid globally stable subject identifiers unless the profile explicitly requires them;
- distinguish cryptographic binding material from human-readable identifiers;
- do not include verifier-specific or transaction-specific data in a reusable attestation;
- version schema changes and document their privacy impact; and
- treat every new signed field as a possible cross-context correlation handle.

## Lifecycle and status

Use [D-034 — Credential and Issuer Lifecycle States](../diagrams/D-034-credential-issuer-lifecycle-states.md) to make the issuing/status transition authority explicit and to keep credential state distinct from issuer-key lifecycle.


The issuer must define state transitions and their effective-time semantics. At minimum support: `valid`, `suspended` where used, `revoked`, `expired`, `replaced/superseded` where used, and `unknown/unavailable` at the verifier boundary.

A status event should produce evidence of the authority, reason class, effective time, publication time, affected scope and replacement relationship if any. Key compromise handling must distinguish compromise of an issuer signing key from incorrect issuance of an individual attestation.

## Security controls

Apply the [production security baseline](../deployment/production-security-baseline.md) and [key management guidance](../deployment/key-and-secret-management.md). Required issuer-specific controls include signing-key isolation, approval separation, issuance rate and anomaly monitoring, authenticated schema/policy publication, auditable administrative actions and tested emergency key replacement.

## Privacy and evidence retention

Issuer evidence is often the highest-risk data in the system. Separate:

- evidence necessary to prove that an issuance decision followed policy;
- data needed to support correction/redress; and
- data that is merely operationally convenient.

Set explicit retention and deletion periods for each class. A ZKP deployment should not become an excuse to retain richer upstream evidence indefinitely.

## Failure and recovery cases

Test at least: malformed enrolment evidence, unsupported schema, duplicate/ambiguous enrolment where relevant, signing service unavailable, policy version mismatch, status publication delay, issuer key compromise, incorrect issuance, reissuance after recovery and attempted proof using superseded credentials.

## Evidence to produce

- issuer authorisation/recognition reference;
- issuance policy and schema versions;
- key identifier and rotation history;
- sample signed attestation with synthetic data;
- positive and negative issuance test results;
- status/lifecycle event evidence;
- privacy/retention statement;
- compromise exercise evidence; and
- correction/redress procedure.

## Related guidance

Read [assurance boundaries](../boundaries/README.md), [information model](../information-model/README.md), [registry implementation](registry-implementation-guide.md), [issuer compromise runbook](../operations/issuer-compromise-runbook.md) and [conformance](../conformance/README.md).

[Back to component implementation guides →](README.md)
