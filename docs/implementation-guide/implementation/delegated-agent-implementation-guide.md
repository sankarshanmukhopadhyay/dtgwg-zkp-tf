---
layout: default
title: "Delegated-agent implementation guide"
parent: "Implementation"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# Delegated-agent implementation guide

Agent authority must be explicit, scoped, time-bounded and revocable. Holder binding establishes control of proof material; it does not establish that a software agent is authorised to act for a principal.

{: .governance }
Treat delegation as a separate authority layer that consumes a proof result. Never encode “valid proof = authorised agent action”.

## Delegation record

A machine-evaluable delegation should identify at least:

- principal;
- agent or agent instance/class as required by the governance model;
- permitted actions;
- resource, relying-party or context scope;
- quantitative or qualitative limits;
- validity start/end;
- delegation/policy version;
- step-up conditions;
- revocation/suspension reference; and
- evidence/receipt requirements.

## Execution pipeline

Use [D-033 — Delegated-Agent Authority Transaction](../diagrams/D-033-delegated-agent-authority-transaction.md) for the cross-role authority flow among principal, wallet/prover, agent, verifier and authority/status source.


`task/request → agent identity/control → delegation resolution → proof acquisition/presentation → verifier predicate evaluation → delegation scope check → relying-party policy → action → receipt/evidence`

The ordering matters. Task context can constrain what is happening, but task context is not itself authority. See [ADR-013](../adr/ADR-013-task-context-not-authority.md).

## Wallet interaction

An agent should use an explicit wallet capability/API that can distinguish:

- unattended policy-permitted proving;
- proving that requires holder confirmation;
- proving that requires stronger step-up; and
- requests that are prohibited regardless of agent instruction.

The wallet must not surrender unrestricted proof capability to an agent because the agent can invoke a local API.

## Revocation and continuity

Check delegation status close enough to the action to meet the risk profile. Define what happens when the principal revokes authority while an agent is in a multi-step workflow. Long-running tasks should have checkpoints or re-authorisation rules rather than assuming authority remains valid indefinitely.

## Agent change and substitution

If an agent implementation, model, operator, toolchain or execution environment changes materially, determine whether the existing delegation still applies. A delegation to a named service may not automatically extend to a new sub-agent, model provider or tool with broader capabilities.

## Evidence and receipts

For material actions, retain evidence sufficient to show:

- which principal authorised which agent;
- the scope and policy in force;
- the proof/predicate result consumed;
- the action actually attempted/performed;
- any step-up decision; and
- the final outcome and revocation state.

Minimise evidence so that accountability does not become continuous surveillance of the principal.

## Failure cases to test

- no delegation;
- expired/revoked delegation;
- scope expansion;
- sub-agent substitution;
- task replay;
- proof valid but action prohibited;
- holder refuses step-up;
- authority revoked mid-workflow; and
- agent compromise.

## Evidence to produce

- delegation schema/profile;
- authority resolution logic;
- scope/limit test suite;
- revocation tests;
- step-up policy/results;
- agent substitution policy;
- action receipt examples; and
- privacy/retention assessment.

## Related guidance

Read [trust-task ZKP profile](../interoperability/trust-task-zkp-profile.md), [authority and evidence boundaries](../interoperability/authority-and-evidence-boundaries.md), [agent-mediated pressure test](../pressure-tests/agent-mediated-zkp.md), [agent delegation flow](../diagrams/D-004-agent-delegation-flow.md) and [ADR-001](../adr/ADR-001-holder-binding-not-delegation.md).

[Back to component implementation guides →](README.md)
