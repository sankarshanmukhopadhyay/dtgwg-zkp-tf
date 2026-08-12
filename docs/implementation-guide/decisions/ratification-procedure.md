---
layout: default
title: "Ratification and amendment procedure"
parent: "Decision Governance"
grand_parent: "Implementation Guide"
nav_order: 3
has_toc: true
---
# Ratification and amendment procedure

## Entry criteria

A status transition requires an attributable upstream source, a decision date, the responsible authority and an exact outcome. Silence, implementation progress or editorial consensus inside the fork is not sufficient.

## Transition sequence

The [decision ratification and impact propagation flow](../diagrams/D-037-decision-ratification-impact-propagation.md) is the visual control model for this procedure.


1. Record the upstream outcome in a ratification record.
2. Update `decision-register.yaml`.
3. Run the decision-impact validator.
4. Review affected ADRs, requirements, schemas, fixtures, tests and guidance.
5. Mark incompatible artefacts as amended, superseded or blocked.
6. Regenerate the readiness report and release evidence.

## Required impact questions

- Does the decision change the meaning of a predicate or profile?
- Does it strengthen or weaken a privacy or assurance claim?
- Does it alter a context, epoch, schema or adversary assumption?
- Do existing fixtures remain valid?
- Do conformance tests need new positive or negative cases?
- Does the affected-person notice or redress path change?

No ratified status may be published while an unresolved contradiction remains in the impact report.
