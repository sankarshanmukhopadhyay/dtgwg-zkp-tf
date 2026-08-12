---
layout: default
title: "DTG Interoperability"
parent: "Implementation Guide"
nav_order: 9
has_children: true
---
# DTG interoperability

This section makes the ZKP implementation workspace's dependencies on adjacent Decentralized Trust Graph (DTG) work explicit, reviewable and machine-verifiable. It does not import authority from another repository by reference alone. Each dependency records the external authority, the direction of dependency, the evidence consumed by a ZKP profile, unresolved assumptions, and the control plane that remains responsible for resolution.

{: .governance }
A successful ZKP verification does not create credential semantics, delegated authority, ceremony authority, registry recognition, or governance legitimacy. Those properties remain governed by their authoritative specifications and frameworks.

## Release objective

The v0.4.0 interoperability programme turns cross-repository assumptions into traceable assurance inputs. It focuses on active DTG work that materially affects ZKP semantics: credential relationships, Trust Tasks and Trust Ceremonies, and RAHP specification pressure testing.

## Documents

- [DTG dependency model](dtg-dependency-model.md)
- [Credential proof inputs](credential-proof-inputs.md)
- [Authority and evidence boundaries](authority-and-evidence-boundaries.md)
- [Portfolio alignment register](portfolio-alignment-register.yaml)
- [DTG ZKP dependency diagram](../diagrams/D-030-dtg-zkp-dependency-map.md)


## Portfolio situational awareness

For a current cross-workstream view, use the independently maintained [DTG Portfolio Monitor](https://sankarshanmukhopadhyay.github.io/dtg-portfolio-monitor/). Its [Portfolio Status](https://sankarshanmukhopadhyay.github.io/dtg-portfolio-monitor/portfolio-status/) and domain views can help identify repository movement that may trigger review of this alignment register.

{: .governance }
The portfolio monitor is **contextual evidence, not an authority source**. Dependency status in this repository must still be verified against the owning specification repository, task-force decision, issue, discussion, pull request or release before an implementation decision is changed.

## Machine-verifiable register

`portfolio-alignment-register.yaml` is the canonical cross-repository dependency inventory for this workspace. `scripts/validate_interoperability.py` verifies required authority, relationship, status, evidence and unresolved-assumption fields and prevents an external dependency from being represented without an explicit authority owner.
