---
layout: default
title: "Credential and Issuer Lifecycle States"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 34
has_toc: true
---
# Credential and Issuer Lifecycle States

```mermaid
stateDiagram-v2
    [*] --> Pending: issuance decision initiated
    Pending --> Valid: authorised issuance succeeds
Evidence: policy + schema + signing key versions
    Pending --> Rejected: issuance policy denies
Evidence: reason code
    Valid --> Suspended: authorised temporary suspension
Evidence: status event
    Suspended --> Valid: authorised reinstatement
Evidence: reinstatement event
    Valid --> Revoked: authorised revocation
Evidence: effective-time status event
    Suspended --> Revoked: authorised revocation
Evidence: effective-time status event
    Valid --> Expired: validity period ends
    Valid --> Superseded: controlled replacement issued
Evidence: replacement link
    Revoked --> Reissued: correction/recovery authorises new instance
    Superseded --> Reissued: replacement process completes
    Reissued --> Valid
    Rejected --> [*]
    Expired --> [*]
```

## Interpretation

Credential lifecycle is distinct from issuer-key lifecycle. A signing-key compromise may invalidate confidence in a set of credentials without meaning that each holder committed wrongdoing; an incorrect individual issuance may require correction without compromising the issuer's entire signing authority. Implementations should record which authority caused each state transition, when the change became effective, how it was published and how replacement or re-issuance relates to the previous credential.

Historical status must not be destroyed when a credential is replaced. A verifier auditing a prior decision needs to recover the state and key/policy context that applied at that earlier time.
