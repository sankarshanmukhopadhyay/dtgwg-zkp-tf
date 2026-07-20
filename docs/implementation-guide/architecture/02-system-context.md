---
layout: default
title: "System context"
parent: "Architecture"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# System context

The DTG ZKP environment is an authority-mediated proof system, not a direct cryptographic conversation between a holder and verifier. Governance authorities define accepted policies and assurance classes. Accreditation authorities establish which issuers or evidence providers may act under those policies. Issuers make attestations. Holders or authorized agents generate presentations. Verifiers apply a versioned relying-party policy and consult registry state where required. Auditors and redress bodies inspect the evidence produced by these actions.

| Actor | Authority or responsibility | Evidence produced |
|---|---|---|
| Governance authority | defines policy, assurance and recognition rules | policy versions, decisions, appeals |
| Accreditation authority | accredits and suspends evidence providers | accreditation records and status |
| Issuer | issues status-bearing attestations | credential, issuance and status records |
| Holder | controls credential material and approves presentation | consent or request-acceptance record |
| Wallet | constructs requests and presentations for the holder | canonical transcript and local audit event |
| Principal | grants authority to an agent | delegation evidence |
| Agent | acts within delegated scope | action request and delegation reference |
| Verifier | validates proof and applies reliance policy | decision receipt |
| Registry operator | publishes governed state | signed/versioned registry snapshot |
| Auditor or redress body | reviews evidence and disputes | findings and remediation decision |

A conforming design keeps policy decision points distinct from policy enforcement points. Verification software may enforce a relying-party policy, but it does not create the authority that makes the policy legitimate.
