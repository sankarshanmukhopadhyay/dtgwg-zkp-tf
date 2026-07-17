---
layout: default
title: Issuer implementation guide
nav_order: 2
parent: Implementation Guide
has_toc: true
---
# Issuer implementation guide

The issuer is authoritative only for the attestation it is empowered to make. It shall version schemas and policies, bind issuance to an accountable process, protect signing keys, publish status with clear time semantics and preserve evidence needed to investigate incorrect issuance.

## Required controls

- separation of enrollment, approval and signing authority;
- canonical subject and holder-binding inputs;
- schema and policy versioning;
- deterministic expiry, suspension and revocation;
- emergency key replacement;
- privacy-minimized audit evidence;
- correction and redress route.

The issuer must not imply that possession of a valid proof establishes facts outside the approved assurance boundary.
