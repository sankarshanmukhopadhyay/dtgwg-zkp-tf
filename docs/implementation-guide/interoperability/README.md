---
layout: default
title: "DTG Interoperability"
parent: "Implementation Guide"
nav_order: 9
has_children: true
---
# DTG interoperability

This section treats interoperability as a governed evidence boundary. The ZKP workspace consumes externally governed semantics, state and evidence, but does not acquire authority over the repositories that define them.

{: .governance }
A successful ZKP verification does not create credential semantics, delegated authority, task authority, ceremony authority, registry recognition or governance legitimacy. Those conclusions remain controlled by their owning specifications, runtime authorities and relying-party policy.

## Current maintenance objective

The interoperability model is maintained independently of release cadence. Its purpose is to answer four questions for every material cross-specification dependency:

1. **Who has authority?** Which specification, registry, governance body or runtime control plane owns the semantic or state?
2. **What evidence crosses the boundary?** Which concrete artifact, digest, status result, task field, delegation record or policy version is consumed?
3. **What can invalidate it?** Which lifecycle transition, revocation, suspension, policy change, task control operation or dependency change requires re-evaluation?
4. **What can be tested?** Which positive and negative evidence demonstrates that implementations preserve the boundary?

Repositories are therefore treated as locations of authority and evidence, not as the architecture itself.

## Dependency classes

The portfolio is intentionally not mirrored wholesale into this repository.

| Class | Meaning | Current examples |
|---|---|---|
| `semantic-runtime` | A change can alter proof meaning, verifier acceptance, authority interpretation or required runtime state. | Credential Spec, Trust Tasks |
| `assurance-method` | A method shapes how risks, harms, controls and evidence are tested but does not create ZKP normative authority. | DTG RAHP provenance; RAHP Toolkit v1.1 operational method |
| `conditional-composition` | Material only when a selected ZKP profile composes with the external work. | Trust Ceremonies, VDS, Agent Names, HTX |
| `implementation-evidence` | Supplies interoperability or conformance evidence but is never the semantic authority. | OpenVTC implementation repositories |

## Documents

- [DTG dependency model](dtg-dependency-model.md)
- [Credential proof inputs](credential-proof-inputs.md)
- [Authority and evidence boundaries](authority-and-evidence-boundaries.md)
- [Portfolio alignment register](portfolio-alignment-register.yaml)
- [Cross-specification assurance register](cross-spec-assurance-register.yaml)
- [DTG ZKP dependency diagram](../diagrams/D-030-dtg-zkp-dependency-map.md)
- [Cross-specification pressure tests](../pressure-tests/README.md)

## Portfolio situational awareness

The independently maintained [DTG Portfolio Monitor](https://sankarshanmukhopadhyay.github.io/dtg-portfolio-monitor/) is the discovery and change-awareness source for this workspace. Its repository model currently tracks active, transitional and implementation repositories across Trust Tasks, credentials, ZKP, RAHP, HTX, VDS, Agent Names and OpenVTC.

{: .governance }
The Portfolio Monitor is **a review trigger, not an authority source**. A monitor event may mark a dependency or pressure test `review-required`; it must not silently change ZKP semantics. Any consequential update must be verified against the owning repository, decision, issue, pull request, release or runtime authority.

The intended operating loop is:

```text
portfolio change
    -> material semantic/evidence surface?
    -> mark relevant cross-spec review as review-required
    -> inspect authoritative source
    -> rerun targeted pressure test
    -> record evidence and disposition
    -> human/governance acceptance
```

## Machine-verifiable registers

`portfolio-alignment-register.yaml` is the canonical inventory of external authority/evidence dependencies.

`cross-spec-assurance-register.yaml` is the canonical inventory of pressure tests, reviewed revisions, retest triggers and review status.

`scripts/validate_interoperability.py` verifies both registers, required pressure-test documents, authority ownership, dependency classes, reviewed revisions, retest triggers and the existing executable interoperability fixtures.
