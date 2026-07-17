---
layout: default
title: Deployment viewpoint
nav_order: 10
parent: Architecture
has_toc: true
---
# Deployment viewpoint

Deployment architecture separates authority, data exposure and operational control.

| Zone | Components | Principal controls | Evidence |
|---|---|---|---|
| Holder | wallet, protected storage, local prover | consent, key protection, request rendering | device/profile statement |
| Proving service | isolated proof workers | job isolation, non-retention, tenant separation | deletion and isolation evidence |
| Issuer | enrollment, approval, signing, status | separation of duties, protected keys | issuance and status audit |
| Verifier | edge, verifier, policy, resolver | staged decisions, policy versioning | decision receipt |
| Registry | publication, recognition, cache | signed state, freshness, conflict policy | resolver trace |
| Assurance | monitoring, incident, evidence | restricted access, integrity, redress | evidence package |

Reference deployment profiles are maintained under [secure deployment](../deployment/README.md). Local, remote and hybrid proving are distinct profiles because they expose different actors to credential, witness, request and timing data.

Production deployments document key custody, network boundaries, administrative identities, supply-chain controls, observability, recovery and residual-risk authority.
