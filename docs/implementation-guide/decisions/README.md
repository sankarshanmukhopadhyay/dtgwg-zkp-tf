---
layout: default
title: "Decision Governance"
parent: "Implementation Guide"
nav_order: 16
has_children: true
has_toc: true
---
# Decision Governance

This section separates the fork's implementation baseline from decisions formally ratified by the DTG ZKP Task Force. It provides machine-readable decision state, upstream traceability, impact analysis and controlled status transitions.

{: .governance }
A decision implemented in this fork is not automatically a ratified Task Force decision. Normative effect is determined by the recorded decision authority and upstream status.

## Core artefacts

- [Decision register](decision-register.md)
- [Upstream decision crosswalk](upstream-decision-crosswalk.md)
- [Ratification and amendment procedure](ratification-procedure.md)
- [Ratification record template](ratification-record-template.md)
- [B1 context-delimiter impact assessment](B1-context-delimiter-impact.md)
- [B2 collusion-target impact assessment](B2-collusion-target-impact.md)

The machine-readable source is [`decision-register.yaml`](decision-register.yaml). Validation is performed by `scripts/validate_decision_governance.py`.
