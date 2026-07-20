---
layout: default
title: "Proof-system and profile migration"
parent: "Lifecycle and Migration"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Proof-system and profile migration

Algorithm agility is operational only when a profile defines separable cryptographic and semantic layers, signed negotiation, overlap, deprecation, downgrade prevention and evidence continuity.

A migration plan covers proof-system identifiers, circuits or statements, parameters and proving keys, attestation compatibility, enrolment-root treatment, nullifier continuity, registry and policy versions, archived decision interpretation, rollback prohibition and final retirement. Cross-version tests demonstrate that old and new implementations reach deterministic outcomes during the overlap period and reject an unauthorized downgrade.
