---
layout: default
title: "Assurance test dispositions"
parent: "Conformance"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Assurance test dispositions

Not every scenario is best validated as a cryptographic test vector. Governance, deployment and operational scenarios use assurance tests that require a documented procedure, accountable authority, observed outcome and retained evidence.

The canonical register is [`assurance-test-dispositions.csv`](assurance-test-dispositions.csv). A disposition is not an exemption: it defines the validation path for scenarios whose decisive properties are authority, operational behavior, state propagation, isolation, recovery or redress.

## Required evidence

Each assurance test produces:

- the authority and scope under test;
- the implementation and policy versions;
- the procedure and expected result;
- observed outcomes and deviations;
- evidence references;
- unresolved limitations;
- residual-risk disposition and accountable approver.
