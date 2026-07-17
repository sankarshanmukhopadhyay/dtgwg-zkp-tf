---
layout: default
title: Issuance flow
nav_order: 2
parent: Diagrams
has_toc: true
---
# Issuance flow

```mermaid
sequenceDiagram
 participant G as Governance authority
 participant A as Accreditation authority
 participant I as Issuer
 participant H as Holder wallet
 G->>A: Publish policy and assurance class
 A->>I: Accredit issuer
 H->>I: Enrolment evidence and holder binding
 I->>H: Issue status-bearing attestation
 I->>A: Audit/status evidence
```

## Interpretation

Issuance depends on governance and accreditation before cryptographic proof use. The credential records the policy and assurance basis rather than implying that proof mechanics created the assurance.
