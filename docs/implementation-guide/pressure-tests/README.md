---
layout: default
title: "Cross-Specification Pressure Tests"
parent: "Implementation Guide"
nav_order: 8
has_children: true
---
# Cross-specification pressure tests

These reviews apply the RAHP specification-pressure-testing method to DTG dependencies that materially affect ZKP correctness, privacy, authority interpretation or assurance. They are reproducible review records, not claims that this repository governs the target specification.

{: .governance }
Each finding is assigned to the narrowest control plane with legitimate authority and an evidence path. A ZKP-side mitigation does not close an upstream specification gap unless the owning authority resolves it.

## Method adapted from RAHP

Each review records:

1. target repository/work and review date;
2. affected parties and scenarios;
3. reused or newly articulated ZKP threat hypotheses;
4. harmful inference or governance-invalid states;
5. control and evidence path;
6. primary disposition (`specification`, `companion-specification`, `governance`, `implementation-guidance`, `runtime-control`, `operational-policy`, `out-of-scope`, `risk-accepted`, `already-addressed`, or `resolved-by-pr`);
7. actionable recommendation; and
8. retest trigger.

This preserves the RAHP principle that a pressure test must leave enough evidence to answer what was reviewed, which risks fired, who owns resolution, what evidence can demonstrate closure, and when the review should be re-run.

## Reviews

- [Credential linkage](dtg-credential-linkage.md)
- [Trust Task ZKP exchange](trust-task-zkp-exchange.md)
- [Trust Ceremony composition](trust-ceremony-zkp-composition.md)
- [Agent-mediated ZKP](agent-mediated-zkp.md)
