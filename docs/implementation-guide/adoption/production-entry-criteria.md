---
layout: default
title: "Production entry criteria"
parent: "Adoption"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# Production entry criteria

Production entry requires a signed decision record covering:

1. approved deployment profile and topology;
2. component inventory and software provenance;
3. active profiles, policy versions and authority records;
4. key custody and administrative separation;
5. deployment threat assessment and control statement;
6. conformance and interoperability evidence;
7. tested incident, revocation, rollback and recovery runbooks;
8. privacy claim and observable-event analysis;
9. unresolved limitations and residual-risk approvals;
10. accountable production owner and next review date.

{: .evidence }
A production claim is incomplete unless the evidence can identify what was tested, against which version, by whom, and with what result.

## Required activation-gate evidence

Production entry must additionally resolve all applicable `ZGR-xx` guardrails and include `ZAT-xx` assurance results. Capability-specific gates apply separately to mediated proving, delegated agents, offline verification, proof-system migration, degraded mode and service restoration. A `BLOCKED` guardrail prevents activation. A `TIME-BOUNDED EXCEPTION` must satisfy the risk appetite policy and schema.

This gate discipline adapts RAHP phase-gate concepts to ZKP implementation and deployment lifecycle decisions.
