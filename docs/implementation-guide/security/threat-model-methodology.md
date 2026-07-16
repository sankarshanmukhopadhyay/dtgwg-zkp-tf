---
title: Threat modelling methodology
status: incubating
normative_status: non-normative
owner: DTG ZKP Task Force
last_reviewed: 2026-07-16
---


# Threat modelling methodology

## Analytical unit

Each row records a concrete threat event rather than a broad category. The row links the threatened property to the affected profile, component, boundary and human or institutional harm.

## Required dimensions

- **Against whom:** actor, capability, privilege and collusion.
- **For how long:** session, epoch, credential lifetime, cryptoperiod, retention period and assurance horizon.
- **Alongside what:** credentials, schema fields, protocol metadata, registry traffic, logs, device signals and observable events.

## Risk treatment

Likelihood and impact are deployment-specific. The baseline matrix supplies severity guidance and mandatory controls but does not pretend that one score applies everywhere. Implementers classify residual risk as `accept`, `mitigate`, `transfer` or `prohibit`, name the decision authority and attach evidence.

## Review workflow

1. instantiate profile and deployment scope;
2. select applicable canonical threats;
3. add deployment-specific threats;
4. map controls and owners;
5. test preventive, detective and corrective behaviour;
6. assess residual harm, not only technical residual risk;
7. obtain explicit disposition for high and critical residual risks;
8. regenerate traceability and conformance evidence.
