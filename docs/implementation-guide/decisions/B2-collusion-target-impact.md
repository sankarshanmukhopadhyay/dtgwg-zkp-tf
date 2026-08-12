---
layout: default
title: "B2 collusion-target impact"
parent: "Decision Governance"
grand_parent: "Implementation Guide"
nav_order: 6
has_toc: true
---
# B2 collusion-target impact assessment

The fork treats issuer-verifier collusion resistance as a target privacy property for the Extended Personhood Profile, not as a capability inherited automatically from a profile label or proof primitive.

## Release increment

v0.3.0 introduces named privacy classes, a machine-readable privacy claim, adversary and evidence requirements, and downgrade rules. A strong claim fails validation when the deployment omits its context descriptor, adversary model, correlation assessment, lifecycle assumptions or test evidence.

## System surfaces included

- issuer-held enrolment and schema data;
- nullifier construction and context parameters;
- status and registry interactions;
- network, timing and error observables;
- mediated-proving retention;
- recovery, reissuance and epoch rollover;
- external identifiers composed with the proof.

Discussion #13 records this as an adopted working position for the v0.4 requirements progression. The fork implementation remains non-normative and is subject to amendment through Task Force decision governance.
