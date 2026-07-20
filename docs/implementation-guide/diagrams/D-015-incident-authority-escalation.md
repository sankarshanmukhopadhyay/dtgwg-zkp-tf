---
layout: default
title: "Incident authority and escalation"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 15
has_toc: true
---
# Incident authority and escalation

```mermaid
flowchart TD
 D[Detection] --> T[Triage authority]
 T --> C[Containment]
 C --> G[Governance decision]
 G --> R[Revocation or correction]
 R --> E[Evidence and notification]
 E --> V[Recovery validation]
 V --> Z[Closure authority]
```

## Interpretation

Operational responders contain; authorized governance actors change authority or status.

## Assurance use

Use this diagram with the applicable deployment profile, scenario, threat-control mapping and evidence record. The diagram is explanatory; the linked records remain authoritative.
