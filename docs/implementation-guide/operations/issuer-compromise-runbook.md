---
layout: default
title: "Issuer compromise runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Issuer compromise runbook

## Trigger and detection

A suspected or confirmed compromise of an issuer signing key, issuance service, privileged administrative identity, policy publication channel or issuance data path. Treat an unexplained signing event or unauthorised schema/policy change as sufficient to start containment while classification proceeds.

## Decision authority and scope

The issuer security authority or incident commander classifies the technical incident. The governance authority responsible for issuer recognition determines whether issuing authority must be suspended, narrowed or withdrawn. These authorities should be named before production.

## Immediate containment

Freeze affected signing/administrative capability, block new issuance from the affected path, preserve key and issuance evidence, and prevent verifier fallback to stale keys or cached issuer state. If scope cannot be bounded quickly, suspend affected issuer authority rather than allowing continued ambiguous reliance.

## Evidence to preserve

Preserve key identifiers, HSM/KMS events, signed policy/schema versions, issuance decision identifiers, deployment digests, administrative approvals and status-publication evidence. Avoid bulk copying holder source evidence unless necessary and specifically authorised.

## Recovery procedure

Generate replacement keys in the approved protection boundary; determine which credentials require revocation, replacement or re-issuance; publish governed status and recognition changes; validate propagation to independent verifiers; and re-enable issuance only after clean-build and policy checks pass.

## Recovery test and closure

Exercise issuance and verification with the replacement state, verify rejection of compromised/retired keys, test status freshness and reconstruct at least one historical decision. Closure requires both technical recovery evidence and approval from the authority that suspended or narrowed issuer trust.

## Communications and redress

Notify affected registries/status services, relying parties and holders according to the approved communication policy. Provide a correction/re-issuance path where legitimate holders are affected. Record residual-risk decisions and any population for which compromise scope remains uncertain.

## Minimum evidence produced

- incident or change identifier and classification;
- named decision/closure authorities;
- affected scope and effective times;
- relevant signed state, policy/configuration and software/key versions;
- containment and enforcement actions;
- recovery-test results;
- exceptions and residual-risk approvals; and
- closure record plus redress/correction references where applicable.

[Back to Operational playbooks →](README.md)
