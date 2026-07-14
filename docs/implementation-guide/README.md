# Implementation & Interoperability Guide

**Status:** Incubating  
**Normative status:** Non-normative unless explicitly marked

## Purpose

This workspace pressure-tests whether DTG ZKP profiles are implementable across
biometric providers, issuers, wallets, verifiable trust agents, agents, verifiers,
trust registries, and governance frameworks.

It focuses on semantic interoperability, privacy boundaries, assurance dependencies,
lifecycle behaviour, operational resilience, accessibility, and conformance.

## Structure

| Directory | Purpose |
|---|---|
| `architecture/` | principles, layers, trust boundaries, ownership, quality attributes |
| `adr/` | decisions and rationale |
| `taxonomy/` | predicates, adversaries, lifecycle and validation classifications |
| `scenarios/` | structured pressure-test use cases |
| `matrices/` | traceability and coverage tables |
| `conformance/` | tests, fixtures and plugfest planning |
| `editorial/` | templates and contribution conventions |
| `appendices/` | glossary and references |
| `diagrams/` | Mermaid sources and diagram register |

## Inherited drafting rules

Every privacy claim names its adversary and horizon. Every predicate states what it
does not establish. Conjecture is labelled as conjecture.
