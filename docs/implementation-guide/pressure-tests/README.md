---
layout: default
title: "Cross-Specification Pressure Tests"
parent: "Implementation Guide"
nav_order: 14
has_children: true
---
# Cross-specification pressure tests

These reviews apply the RAHP specification-pressure-testing method to external semantics, state and evidence that can materially affect ZKP correctness, privacy, authority interpretation or assurance. They are reproducible review records, not claims that this repository governs the target specification.

{: .governance }
Each finding is assigned to the narrowest control plane with legitimate authority and an evidence path. A ZKP-side mitigation does not close an upstream specification gap unless the owning authority resolves it.

## Current operating model

The pressure-test programme is driven by the [cross-specification assurance register](../interoperability/cross-spec-assurance-register.yaml). The register records the reviewed revision, current status and retest triggers for each material or exploratory composition.

The [DTG Portfolio Monitor](https://sankarshanmukhopadhyay.github.io/dtg-portfolio-monitor/) supplies change awareness. It does not alter findings automatically. A portfolio event only creates a reason to inspect the authoritative source and decide whether a review must be rerun.

## Method adapted from RAHP

Each substantive review records:

1. target repository/work and reviewed revision;
2. affected parties and scenarios;
3. reused or newly articulated ZKP threat hypotheses;
4. harmful inference or governance-invalid states;
5. control and evidence path;
6. primary disposition (`specification`, `companion-specification`, `governance`, `implementation-guidance`, `runtime-control`, `operational-policy`, `out-of-scope`, `risk-accepted`, `already-addressed`, or `resolved-by-pr`);
7. actionable recommendation; and
8. retest trigger.

This preserves the RAHP principle that a pressure test must leave enough evidence to answer what was reviewed, which risks fired, who owns resolution, what evidence can demonstrate closure, and when the review should be re-run.

## Substantive reviews

- [ZPT-001 — Credential linkage](dtg-credential-linkage.md)
- [ZPT-002 — Trust Task ZKP exchange](trust-task-zkp-exchange.md)
- [ZPT-003 — Trust Ceremony composition](trust-ceremony-zkp-composition.md)
- [ZPT-004 — Agent-mediated ZKP](agent-mediated-zkp.md)
- [ZPT-005 — Witnessed relationship ZKP](witnessed-relationship-zkp.md)
- [ZPT-006 — Trust Task lifecycle ZKP](trust-task-lifecycle-zkp.md)
- [RAHP v1.1 lifecycle and assurance refresh](rahp-v1.1-refresh.md)

## Exploratory tracks

The register also records exploratory tracks for VDS, Agent Names, HTX and OpenVTC implementation evidence. These entries deliberately have no standalone pressure-test page until a concrete ZKP composition exists.

`exploratory-no-active-binding` means **examined and not currently a material dependency**, not “ignored”.

## Cross-specification invariants

Across all reviews:

```text
cryptographic validity
    != semantic validity
    != authorization
    != current lifecycle state
    != relying-party acceptance
    != effect completion
```

Every equality that matters must be backed by evidence owned by the authority entitled to make it.
