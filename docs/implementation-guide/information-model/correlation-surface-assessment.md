---
title: Attestation correlation-surface assessment
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
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
