---
layout: default
title: "Attestation correlation-surface assessment"
parent: "Information Model"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
---
# Attestation correlation-surface assessment

The assessment evaluates individual fields and combinations. A field with modest standalone risk may become identifying when combined with a rare assurance class, exact issuance time, schema version and verifier-visible status index.

## Required procedure

1. Enumerate all disclosed, derived and externally resolved values.
2. Measure value cardinality and rarity in the intended population.
3. compare records across issuers, verifiers, contexts and epochs.
4. include ordering, encoding length, proof size and error behaviour.
5. model issuer-verifier and verifier-verifier collusion.
6. test whether status and registry traffic restores a hidden identifier.
7. document mitigations, residual risk and the assurance horizon.

The deployment evidence bundle includes the field register, combination tests and an explicit decision for every high or critical correlation risk.
