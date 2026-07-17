---
layout: default
title: Deployment principles
nav_order: 2
parent: Implementation Guide
has_toc: true
---
# Deployment principles

1. Minimize observable credential, proof and request data.
2. Separate cryptographic, policy, registry and administrative authority.
3. Authenticate every control-plane action.
4. Make stale, unavailable and conflicting state explicit.
5. Preserve evidence without creating a correlation service.
6. Fail closed for unsupported, ambiguous or downgraded profiles.
7. Exercise revocation, rollback and recovery before production.
8. Record residual risks at the authority that accepts them.
