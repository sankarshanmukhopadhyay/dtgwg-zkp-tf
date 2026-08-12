---
layout: default
title: "Auditor and assessor guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Auditor and assessor guide

Assessment follows evidence from claim to implementation to operation. The assessor's job is not to re-run one successful proof; it is to determine whether the system's stated assurance and privacy claims remain true across authority, lifecycle, failure and recovery conditions.

## Assessment scope

Define before testing:

- implementation and deployment versions;
- profiles and predicates claimed;
- organisations/roles in scope;
- governance and authority sources;
- environments and trust boundaries;
- period under review;
- conformance level or assurance target;
- exclusions and inherited controls; and
- independence of the assessor.

## Evidence layers

Distinguish four evidence classes:

| Evidence class | Examples |
|---|---|
| Design | Architecture, ADRs, boundary records, threat model, schemas |
| Implementation | Code/configuration, fixtures, test results, interface behaviour |
| Operational | Logs, key events, status history, incident/recovery exercises, change records |
| Independent observation | Reperformed tests, sampled decisions, external registry snapshots, assessor findings |

A design claim with no runtime evidence should not be scored as an implemented control. A passing runtime test should not be used to infer governance authority that was never established.

## Sampling strategy

Sample accepted, rejected, stale, unavailable, revoked, delegated, recovery and redress paths. Include at least one negative or adversarial case for each material assurance claim.

Where privacy claims depend on an adversary model, test the named observer/collusion boundary rather than only checking that the proof payload hides attributes.

## Authority and delegation review

For sampled decisions, reconstruct:

1. who had authority to define the predicate/profile;
2. who authorised the issuer;
3. which registry/status state applied;
4. whether an agent acted and under what delegation;
5. which relying-party policy authorised the final action; and
6. who could revoke, override or correct the outcome.

## Lifecycle and historical-state review

Test whether the deployment can explain a decision after policy changes, credential revocation, issuer withdrawal, key rotation or proof-system migration. Evidence should support the relevant effective-time question, not merely show current state.

## Privacy review

Use the [privacy class model](../privacy/privacy-class-model.md), [observable-event analysis](../privacy/observable-event-analysis.md) and [composition assessment](../privacy/composition-and-reconstruction-assessment.md). Review network/service metadata, logs, analytics, registry queries and retained evidence as well as cryptographic payloads.

## Findings and dispositions

Every finding should state:

- claim/control tested;
- evidence inspected;
- observed result;
- affected scope;
- severity/materiality;
- accountable owner;
- remediation or risk-acceptance authority;
- target/retest condition; and
- closure evidence.

Do not mark a finding closed because a document was updated if the finding concerns runtime behaviour.

## Minimum assessment evidence

- signed/identified assessment scope;
- implementation and profile conformance statements;
- test/fixture versions;
- sample register;
- findings and dispositions;
- residual-risk approvals;
- exceptions/limitations; and
- reproducibility instructions.

## Related guidance

Read [conformance levels](../conformance/levels.md), [conformance evidence guide](../guide/conformance-evidence-guide.md), [security assurance tests](../conformance/security-assurance-tests.md), [requirement index](../appendices/REQUIREMENT-INDEX.md) and [risk acceptance](../security/risk-appetite-and-acceptance-policy.md).

[Back to component implementation guides →](README.md)
