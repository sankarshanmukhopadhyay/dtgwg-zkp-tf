---
layout: default
title: "Proof-system migration runbook"
parent: "Operations"
grand_parent: "Implementation Guide"
nav_order: 7
has_toc: true
---
# Proof-system migration runbook

## Trigger and detection

Approval of a new proof construction/profile, deprecation of an existing version, material cryptographic weakness, dependency retirement or interoperability transition.

## Decision authority and scope

Profile/specification governance authorises supported versions and retirement. Deployment operators may schedule rollout but cannot extend acceptance of a deprecated construction beyond the approved window without an explicit residual-risk decision.

## Immediate containment

Freeze unsafe version negotiation, reject ambiguous or silent downgrade, and if a weakness is active restrict affected profiles while migration evidence is produced.

## Evidence to preserve

Preserve proof-system/profile identifiers, implementation versions, negotiation transcripts or reason codes, fixture digests, conformance results, activation/retirement decisions and archived-verification capability.

## Recovery procedure

Execute the [proof-system migration profile](../lifecycle/proof-system-migration-profile.md) and [D-020](../diagrams/D-020-proof-system-migration.md): establish dual-version test parity where safe, deploy explicit negotiation, migrate issuers/wallets/verifiers, then retire the old version.

## Recovery test and closure

Run positive, negative, downgrade and malformed cases against every supported combination; verify old-version rejection after retirement; and reconstruct archived decisions using their recorded version. Closure requires profile-governance acceptance of migration evidence and remaining exceptions.

## Communications and redress

Publish supported-version timelines and operator actions early enough for independent implementations to migrate. Document any users or ecosystems stranded by the transition and the approved mitigation/redress route.

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
