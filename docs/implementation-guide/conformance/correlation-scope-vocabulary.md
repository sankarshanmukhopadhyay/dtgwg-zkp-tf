---
layout: default
title: "Correlation-Scope Vocabulary"
parent: "Conformance"
nav_order: 47
---
# Correlation-scope vocabulary

The downstream repository follows the current Credential Specification correlation-scope vocabulary:

- `pairwise` — known to exactly one counterparty;
- `directed` — known to a holder-chosen set of counterparties;
- `public` — correlation is unbounded.

The vocabulary answers **how widely an identifier may be correlated**. Credential role answers **what role the holder plays**. The two are independent.

## Retired terminology

The former R-DID / M-DID / C-DID / P-DID categories are treated as historical/provenance terminology only. They MUST NOT be used as active identifier types or as shortcuts for correlation scope.

Likewise, the earlier `community` scope value is not part of the current three-value vocabulary. A historical fixture using `community` must be re-decided as `pairwise` or `directed` according to the actual intended correlation boundary.

## Role-vs-scope rule

A verifier MUST NOT infer correlation scope from:

- membership role;
- issuer role;
- relationship-counterparty role;
- persona;
- credential type; or
- DID method.

A role may make a declaration impossible or inappropriate under an owning specification, but it does not itself determine the scope.

Executable cases in `fixtures/correlation-scope-semantics.json` include an explicit role/scope conflation failure.

## Serialization boundary

Credential Specification issue #46 remains open and has not named:

- the property that carries the declaration; or
- the `@context` term.

Therefore this repository deliberately models the scope as a semantic input named `declared_scope` **inside test fixtures only**. That fixture key is not a proposed credential property and MUST NOT appear in interoperability claims as though it were canonical wire syntax.

When #46 resolves, downstream serialization fixtures should be added in a separate change against the adopted property/context term.
