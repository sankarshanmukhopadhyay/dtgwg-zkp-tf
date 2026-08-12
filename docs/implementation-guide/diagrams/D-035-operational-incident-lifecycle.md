---
layout: default
title: "Operational Incident Lifecycle"
parent: "Diagrams"
grand_parent: "Implementation Guide"
nav_order: 35
has_toc: true
---
# Operational Incident Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Normal
    Normal --> Degraded: monitoring threshold or dependency failure
Authority: pre-authorised operations policy
    Normal --> Contained: confirmed incident
Authority: incident commander / security authority
    Degraded --> Contained: incident confirmed or risk threshold exceeded
    Degraded --> Normal: dependency restored + recovery test passes
    Contained --> Suspended: trust decision cannot be safely bounded
Authority: suspension authority
    Contained --> Recovering: containment complete + recovery approved
    Suspended --> Recovering: restoration authority approves remediation
    Recovering --> Restored: independent recovery tests pass
Evidence: test results + approved state versions
    Restored --> Normal: closure authority accepts residual risk
Evidence: closure record
    Recovering --> Contained: recovery test fails
```

## Interpretation

Operational state changes are governance decisions. Detection alone does not grant authority to suspend a trust service, and technical recovery alone does not authorise restoration. Each runbook therefore names who may classify, contain, suspend, restore and close the event, and which evidence supports those transitions.

`Degraded` is a bounded operating mode with explicit prohibitions and expiry. It must not become an indefinite weaker-assurance state. `Restored` is intentionally separate from `Normal` so that post-recovery evidence, monitoring and closure can be completed before normal governance assumptions resume.
