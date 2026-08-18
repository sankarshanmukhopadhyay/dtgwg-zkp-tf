---
layout: default
title: "DTG Dependency Model"
parent: "DTG Interoperability"
nav_order: 1
---
# DTG dependency model

The durable architectural question is not “which repositories does ZKP depend on?” It is:

> **Which externally governed semantics, states or evidence can change the validity or interpretation of a ZKP decision?**

A repository is recorded because it hosts or implements one of those authority/evidence surfaces.

## Current dependency model

| Concern | Authority / evidence source | Class | ZKP may consume | ZKP must not infer |
|---|---|---|---|---|
| Credential semantics and edge evidence | `trustoverip/dtgwg-cred-spec` | `semantic-runtime` | claims, status, relationship semantics, VRC/VWC edge digest evidence | identity equivalence or controller continuity not actually evidenced |
| Identifier linkage | Credential Spec issue #9 and any adopted resolution | `semantic-runtime` | explicit P-DID/R-DID/M-DID linkage evidence when defined | common subject/controller from co-possession |
| Trust Task exchange | `trustoverip/dtgwg-trust-tasks-tf` | `semantic-runtime` | task id, audience, challenge, constraints, task digest, task-control state, evidence references | authorization from task participation, proof validity or transport identity |
| Effect-time authority | Trust Tasks plus applicable delegation/status authorities | `semantic-runtime` | current authority, delegation, status and task-control evidence before a consequential effect | that evidence valid at acceptance remains valid at effect time |
| Trust Ceremonies | Trust Tasks ceremony/enactment work | `conditional-composition` | bounded ceremony/enactment context where a profile explicitly composes with it | authority, consent or artifact validity from ceremony membership/completion |
| Witnessed relationship exchange | Trust Tasks witness/VRC flows plus Credential Spec VWC semantics | `conditional-composition` | task digest, VRC digest, witness evidence and exact edge binding | relationship authority or subject equivalence from witness validity alone |
| Delegated agent action | Trust Tasks plus applicable delegation/mandate governance | `semantic-runtime` | separately verifiable principal, agent, scope, expiry, constraint and revocation evidence | delegation from holder binding or successful ZKP verification |
| Risks and harms | DTG RAHP TF provenance; RAHP Toolkit v1.1 operational method | `assurance-method` | pressure-test method, portable assurance patterns, evidence and retest expectations | new normative ZKP requirements without ZKP governance action |
| Verifiable data structures | `trustoverip/dtgwg-vds-tf` | `conditional-composition` | governed data-structure integrity/provenance evidence if selected by a profile | semantic authority merely because a structure verifies |
| Agent naming | `trustoverip/dtgwg-agent-names-tf` | `conditional-composition` | scoped naming/resolution evidence if an agent-facing profile requires it | agent authority, identity continuity or delegation from a resolved name |
| Human trust experience | `trustoverip/dtgwg-htx-tf` | `conditional-composition` | interaction/notice evidence where a profile makes user comprehension or action explicit | consent or authority from presentation of an interface alone |
| Implementation evidence | OpenVTC repositories tracked by the Portfolio Monitor | `implementation-evidence` | test vectors, deployment evidence and interoperability observations | normative semantics from implementation behaviour |

## Core invariants

### Proof validity is not task authority

The Trust Tasks work now makes the authorization boundary explicit. The ZKP composition must preserve:

```text
proof_valid
    != task_accepted
    != task_authorized
    != authority_still_valid_at_effect_time
    != effect_completed
```

A verifier or consumer can require all five, but evidence for one must not be substituted for another.

### Acceptance-time evidence can become stale

Long-running, suspended or resumed tasks create a time-of-check/time-of-effect boundary. Where an irreversible or consequential effect depends on current status, mandate, policy or task-control state, the relevant evidence must be re-evaluated at the control point defined by the owning specification.

### Edge binding is not subject equivalence

Credential Spec now requires the VWC digest needed to bind witnessed evidence to a specific relationship edge. That materially improves edge integrity. It does **not**, by itself, resolve the separate P-DID/R-DID/M-DID subject/controller linkage question tracked by Credential Spec issue #9.

## Dependency rule

Every external dependency used by a ZKP profile MUST identify:

1. `authority`: the owner of the dependent semantic or state;
2. `dependency_class`: why the dependency is material;
3. `consumes`: the concrete evidence or semantics consumed;
4. `lifecycle`: what can invalidate or supersede that evidence;
5. `must_not_infer`: conclusions forbidden without additional evidence;
6. `reviewed_revision`: the source revision examined where the dependency is active;
7. `retest_triggers`: events that require re-examination; and
8. `resolution_authority`: who can resolve, revoke or redefine the dependency.

## Direction of authority

Dependencies flow **into** a ZKP profile as governed semantics, state or evidence. A ZKP verification result flows **out** only as a bounded result about the statement actually proved. No dependency edge grants this repository authority to redefine another specification.

## Portfolio tracking

The Portfolio Monitor is used to detect churn. It is not copied wholesale into this register. A repository is promoted from `observed` to a material dependency only when a change can alter proof inputs, transcript binding, verifier policy, authority interpretation, privacy properties or assurance evidence.
