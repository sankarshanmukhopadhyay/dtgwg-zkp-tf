---
layout: default
title: "DTG ZKP Pressure-Test Corpus (Enhanced)"
parent: "Scenarios"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# DTG ZKP Pressure-Test Corpus (Enhanced)

## Executive Summary

This document is an implementation-validation companion to the DTG ZKP specification. It organizes pressure-test scenarios into an implementation-oriented catalogue, coverage matrices, detailed scenario tables, readiness gates, and a phased roadmap.

---

# 1. Executive Use Case Catalogue

| ID | Use Case | Domain | Primary Goal | Core Predicates | Primary Pressure | Dependencies | Priority |
|---|---|---|---|---|---|---|---|
| UC-001 | Privacy-Preserving Account Creation | Identity | One account/person | L,P,U,H,F | Sybil resistance | Registry, Issuer | P0 |
| UC-002 | Anonymous Community Participation | Social | Anonymous participation | P,U,F | Unlinkability | Wallet | P0 |
| UC-003 | Age Verification | Commerce | Threshold proof | R,F | Selective disclosure | Attribute issuer | P1 |
| UC-004 | High-Value Transaction | Finance | Step-up auth | L,H,F | Replay | Wallet | P0 |
| UC-005 | Account Recovery | Identity | Safe recovery | L,P,U,F | Continuity | Recovery service | P0 |
| UC-006 | Same Human Login | Identity | Continuity | L,H,F | Account takeover | Wallet | P0 |
| UC-007 | Benefit Claims | Government | One claim | P,U | Duplicate claims | Registry | P1 |
| UC-008 | Anonymous Ballot | Civic | One vote | P,U | Privacy | Governance | P1 |
| UC-009 | Human Authorises Agent | AI | Delegation | L,H,F | Delegation | Trust Tasks | P0 |
| UC-010 | Agent Step-up | AI | Intent confirmation | L,H,F | Intent drift | Trust Tasks | P0 |
| UC-011 | Agent Presentation | AI | Delegated proof | H | Delegation | Credentials | P1 |
| UC-012 | Issuer Suspension | Governance | Status semantics | Status | Lifecycle | Registry | P0 |
| UC-013 | Policy Version Change | Governance | Versioning | Policy | Migration | Registry | P0 |
| UC-014 | Registry Offline | Infrastructure | Offline verify | Status | Resilience | Registry | P1 |
| UC-015 | Registry Conflict | Federation | Recognition | Accreditation | Governance | Registries | P1 |
| UC-016 | Cross-border Recognition | Federation | Mutual trust | Liveness | Mapping | Governance | P1 |
| UC-017 | Low-end Devices | Runtime | Deployability | Any | Performance | Wallet | P0 |
| UC-018 | Offline Presentation | Runtime | Disconnected use | Any | Replay | Wallet | P1 |
| UC-019 | Shared Device | Consumer | Isolation | Holder | Leakage | Wallet | P1 |
| UC-020 | Accessibility | Inclusion | Alternative liveness | Liveness | Accessibility | Provider | P0 |
| UC-021 | Compromised Wallet | Security | Separate key/human | L,H | Theft | Recovery | P0 |
| UC-022 | Malicious Provider | Governance | Assurance boundary | Liveness | Trust | Accreditation | P0 |
| UC-023 | Malicious Verifier | Privacy | Correlation | Nullifier | Linkability | Wallet | P0 |
| UC-024 | Issuer+Verifier Collusion | Privacy | Collusion | Any | Correlation | Governance | P0 |
| UC-025 | Composite Proofs | Architecture | Composition | Multiple | Fingerprinting | Trust Tasks | P0 |
| UC-026 | Algorithm Upgrade | Crypto | Migration | Any | Downgrade | Profiles | P0 |
| UC-027 | Appeals | Governance | Redress | Any | Explainability | Policy | P0 |
| UC-028 | Emergency Mode | Resilience | Degraded ops | Any | Exception handling | Governance | P2 |
| UC-029 | Batch Verification | Scale | Throughput | Any | Logging | Infrastructure | P1 |
| UC-030 | Interoperability | Conformance | Cross-vendor | All | Spec ambiguity | All | P0 |

Legend: L=Liveness, P=Personhood, U=Scoped Uniqueness, H=Holder Binding, F=Freshness, R=Range Proof.

# 2. Coverage Matrices

## Capability Coverage

| Capability | Representative Use Cases |
|---|---|
| Liveness | UC001,004,006,009,010,020 |
| Holder Binding | UC004,006,009,021 |
| Nullifiers | UC001,002,007,008,023 |
| Agent Delegation | UC009-011 |
| Registry Lifecycle | UC012-016 |
| Recovery | UC005,021 |
| Offline | UC014,018 |
| Accessibility | UC020 |
| Proof Composition | UC025 |
| Crypto Agility | UC026 |

## Threat Coverage

| Threat | Covered |
|---|:--:|
| Replay | ✓ |
| Deepfake | ✓ |
| Wallet Theft | ✓ |
| Issuer Collusion | ✓ |
| Verifier Collusion | ✓ |
| Metadata Correlation | ✓ |
| Downgrade | ✓ |
| Registry Failure | ✓ |
| Offline Double Spend | ✓ |

## Governance Coverage

| Topic | Use Cases |
|---|---|
| Accreditation | UC012-016 |
| Revocation | UC012 |
| Appeals | UC027 |
| Recognition | UC015-016 |
| Liability | UC022,027 |
| Accessibility | UC020 |

## Implementation Roadmap

| Release | Scope |
|---|---|
| MVP | UC001-006 |
| v1.1 | UC007-016 |
| v2 | UC017-030 |

---

# 3. Detailed Use Cases

The detailed catalogue follows the same template for every scenario.

## Template

| Field | Description |
|---|---|
| Objective | Why the scenario exists |
| Actors | Primary participants |
| Context Boundary | Scope in which predicates apply |
| Preconditions | Assumptions |
| Required Predicates | Liveness, Holder Binding, etc. |
| Nominal Flow | Happy path |
| Expected Output | Verifier result |
| Privacy Claim | Information minimisation |
| Named Adversaries | Threat model |
| Governance Dependencies | Accreditation, Registry, Policy |
| Failure Modes | Operational failures |
| What the Proof Does NOT Establish | Explicit non-claims |
| Pressure Points | Architectural stress |
| Conformance Tests | Expected validation |
| Priority | P0/P1/P2 |

---

For each of UC-001 through UC-030, instantiate the above template using the scenario definitions from the original corpus. This creates a consistent, review-friendly specification where every scenario occupies a compact two-page maximum layout.

# 4. Readiness Gates

- Predicate completeness
- Privacy clarity
- Assurance clarity
- Lifecycle completeness
- Interoperability
- Operational viability
- Governance and redress

# 5. Conformance Suite

- Positive tests
- Negative tests
- Privacy tests
- Lifecycle tests
- Cross-vendor interoperability
- Performance benchmarks
- Accessibility validation
- Threat simulations

# 6. Open Questions

Carry forward the 18 open questions from the original corpus, grouped into:
- Predicate semantics
- Privacy
- Governance
- Lifecycle
- AI delegation
- Registry integration
- Crypto agility

# 7. Recommended Working Group Programme

Phase 1 — Ratify corpus

Phase 2 — Map profiles

Phase 3 — Produce conformance suite

Phase 4 — Cross-vendor plugfest

Phase 5 — Feed IIW Working Draft

