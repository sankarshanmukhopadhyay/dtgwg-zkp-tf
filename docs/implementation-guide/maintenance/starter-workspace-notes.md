---
layout: default
title: "DTG ZKP Implementation & Interoperability Guide Workspace"
parent: "Maintenance Notes"
grand_parent: "Implementation Guide"
nav_order: 2
has_toc: true
nav_exclude: true
---
# DTG ZKP Implementation & Interoperability Guide Workspace

Branch-ready documentation package for addition to a fork of
`trustoverip/dtgwg-zkp-tf`.

This package is additive. The upstream project narrative is preserved separately in
`UPSTREAM_README.md`, while the fork root README describes the implementation workspace.
The package does not replace upstream drafting rules, upstream normative decisions, or a
future normative specification.

## Start here

1. Read `docs/implementation-guide/README.md`.
2. Review the architecture principles and ownership model.
3. Record decisions with the ADR template.
4. add pressure-test scenarios with the scenario template.
5. Run `python scripts/validate_docs.py`.

## Suggested branch and commit

- Branch: `docs/implementation-interoperability-guide`
- Commit: `docs: scaffold ZKP implementation and interoperability guide`

Documentation follows the upstream CC BY 4.0 terms. Utility scripts follow Apache-2.0.
