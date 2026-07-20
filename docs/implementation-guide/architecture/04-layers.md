---
layout: default
title: "Architectural layers"
parent: "Architecture"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Architectural layers

| Layer | Responsibility | Must not silently absorb |
|---|---|---|
| Governance | policy, accreditation, liability, redress | proof mechanics |
| Assurance | assurance classes and reliance semantics | civil identity by implication |
| Credential | attestation structure and issuer claims | verifier policy |
| Proof | privacy-preserving predicates | evidence correctness |
| Protocol | request, transcript, presentation, errors | governance decisions |
| Runtime | wallets, agents, issuers, verifiers | undocumented downgrade |
| Infrastructure | network, registry, storage, compute | semantic trust decisions |
