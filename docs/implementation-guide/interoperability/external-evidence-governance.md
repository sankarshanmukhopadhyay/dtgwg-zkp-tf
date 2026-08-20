---
layout: default
title: External Evidence Governance
parent: DTG Interoperability
nav_order: 8
has_toc: true
---
# External evidence governance

External laboratories, implementations and fixture repositories can inform
the construction-selection and interoperability process without becoming
dependencies or normative authorities. Each reviewed source is recorded in
[`external-evidence-register.yaml`](external-evidence-register.yaml) with a
pinned revision, authority class, licence status, permitted use, conformance
credit and retest triggers.

## Admission rules

An external source with an unverified or incompatible licence:

- is reference and independently observed evidence only;
- is not copied, translated, vendored or packaged by this repository;
- is not downloaded or executed by release CI;
- receives no conformance credit; and
- cannot block a release.

Descriptions of public repository state do not transfer its code, fixtures,
circuits or generated artefacts into this fork. If licensing later becomes
verifiable, a new review must explicitly change the permitted-use and
conformance-credit fields before any import or reproduction is proposed.

## Evidence progression

`none` means that the source is recorded but supplies no release evidence.
`observational` means that independently documented results may be considered
as experimental input. `reproduced` requires a permissible licence, pinned
inputs, an independent run, digest-bound output and a review that identifies
the exact claims supported and not supported.

The repository-owned semantic fixtures remain the v0.5.0 executable baseline.
They were derived from this fork's own requirements and assurance records and
do not incorporate external fixture content.
