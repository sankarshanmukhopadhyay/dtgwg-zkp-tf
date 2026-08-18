---
layout: default
title: "Pressure Test — Witnessed Relationship ZKP"
parent: "Cross-Specification Pressure Tests"
nav_order: 6
---
# Pressure test — witnessed relationship ZKP

## Review record

| Field | Value |
|---|---|
| Review ID | ZPT-005 |
| Target | Trust Tasks witnessed relationship flows + Credential Spec VWC semantics |
| Trust Tasks revision | `7e0d755f5b815498c861cacecee5cae49b3f14eb` |
| Credential Spec revision | `b89f389abbdae77ba60b673c0836c781c2b54169` |
| Reviewed | 2026-08-18 |
| Trigger | concrete `vrc/relationships/*` and `witness/*` Trust Task flows plus required VWC edge digest |

## Scenario

```text
relationship proposal
    -> relationship credential
    -> witness session
    -> witness submission
    -> VWC / edge digest / task digest
    -> ZK predicate
    -> relying-party decision
```

The pressure test asks whether the proof can demonstrate a bounded witnessed-relationship predicate without allowing witness evidence from another edge, another session or another context to satisfy the statement.

## Affected parties

Both relationship participants, witness operators, credential subjects, wallet holders, verifiers, relying parties and people exposed to correlation through stable relationship or witness references.

## Findings

| Finding | Threat | Primary disposition | Evidence of closure |
|---|---|---|---|
| F-020: witness evidence can be paired with the wrong relationship if the exact VRC/edge is not content-bound | [`THR-046`](../reference/identifier-register.md#thr-046) | `already-addressed` plus conformance evidence | required VWC edge digest validated against the exact VRC |
| F-021: task id or session id equality can pair evidence with a different document | [`THR-050`](../reference/identifier-register.md#thr-050) | `companion-specification` | task digest/content-bound citation validated where relied upon |
| F-022: a stable edge, witness or enactment reference can become a cross-context correlation handle | [`THR-049`](../reference/identifier-register.md#thr-049) | `companion-specification` | scoped/minimised transcript commitment and declared correlation assessment |
| F-023: a valid witness credential can be misread as relationship authority, consent or current relationship status | [`THR-048`](../reference/identifier-register.md#thr-048) | `governance` | separate authority/status evidence at relying-party decision time |
| F-024: historical witness evidence can survive revocation of the relationship or credential and be treated as current | [`THR-052`](../reference/identifier-register.md#thr-052) | `runtime-control` | explicit as-of/current semantics and status evaluation |

## Required negative tests

A conformant implementation should reject at least:

1. a VWC whose digest does not reproduce over the supplied VRC;
2. a witness submission bound to a different witness session/challenge;
3. task citation evidence whose task digest does not reproduce over the named document;
4. an edge-valid witness credential used as evidence that unresolved P-DID/R-DID/M-DID identities are equivalent;
5. a current-authority decision made solely from historical witness evidence after relationship or credential revocation; and
6. a proof that exposes a stable witness/edge identifier outside the declared linkability context without explicit policy.

## Recommendation

Treat the required VWC digest as the edge-binding primitive and the Trust Task digest as the content-binding primitive where task evidence leaves the exchange. Keep relationship authority, current status and identifier equivalence as separate evidence domains.

## Retest trigger

Re-run when witness-session semantics, task-digest rules, VWC digest semantics, relationship status semantics or identifier-linkage semantics change.
