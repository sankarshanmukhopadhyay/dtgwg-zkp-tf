---
layout: default
title: "Repository documentation style profile"
parent: "Editorial and Contribution Guidance"
grand_parent: "Implementation Guide"
nav_order: 4
has_toc: true
---
# Repository documentation style profile

## 1. Authority and precedence

This repository uses a local profile based primarily on the ISO/IEC Directives, Part 2. It does not claim that repository documents are ISO or IEC publications. The following order resolves editorial conflicts:

1. `DRAFTING-RULES.md` and approved ADRs;
2. this profile;
3. ISO/IEC Directives, Part 2 principles for standards drafting;
4. the RFC Editor Style Guide for protocol-oriented material;
5. Google developer documentation guidance for procedures;
6. Merriam-Webster for ordinary US English spelling.

## 2. Language and voice

Use US English, sentence-case headings, active voice and precise claims. Prefer prose for rationale and tables for comparable fields. Avoid promotional language, anthropomorphism and claims that exceed the documented evidence.

## 3. Requirement classes

The implementation guide is non-normative by default. Use the labels below whenever a reader could mistake guidance for a requirement.

| Class | Construction | Meaning |
|---|---|---|
| Normative requirement | `MUST`, `MUST NOT`, `REQUIRED` | Binding only in a document explicitly declared normative |
| Recommendation | `should`, `should not` | Preferred implementation practice with documented exceptions |
| Permission | `may` | Permitted option |
| Capability | `can` | Technical possibility, not permission |
| External constraint | `is required by` | Obligation imposed by another authority |
| Example | `Example:` | Illustrative and non-normative |
| Open issue | `Open issue:` | Unresolved decision dependency |

Do not use uppercase RFC 2119 keywords in non-normative guidance except when quoting or explaining a normative source. A section that contains normative language shall declare its normative status and authority.

## 4. Assurance and privacy claims

Every predicate states what it establishes and what it does not establish. Every material privacy claim identifies the protected party, adversary, context, horizon, observable data, assumptions, exclusions and test method.

Do not use `anonymous`, `unlinkable`, `unobservable`, `private`, `secure`, `unique`, `personhood`, `liveness`, `minimal disclosure`, `non-correlatable` or `zero knowledge` as unqualified guarantees. Name the relevant scope and adversary.

## 5. Authority and delegation language

Identify the authority source, actor, scope, duration, enforcement point, suspension or revocation path, evidence and redress path. Do not conflate possession, holder binding, authentication, delegation, transaction authorization, registry inclusion, recognition or reliance.

## 6. Structure

Each principal implementation chapter should include purpose, actors, authority, inputs, procedure, evidence, failure behavior, security, privacy, lifecycle, conformance references and limitations where relevant. Do not publish outline markers, empty headings or questions without disposition.

## 7. Terminology and capitalization

Use glossary terms consistently. Expand an acronym on first use in each standalone document. Capitalize formal names only. Use lowercase for generic roles such as issuer, holder, agent and verifier. Use `zero-knowledge proof` as the noun and `zero-knowledge` as an adjective. Use `GitHub Pages`, `Jekyll`, `Mermaid`, `JSON` and `CSV`.

## 8. Tables, diagrams and examples

Tables require a header row and must not carry essential rationale alone. Every Mermaid diagram requires a following `Interpretation` subsection. Label examples as non-normative. Code and fixture fragments must state whether they are illustrative, canonical or experimental.

## 9. Links and references

Prefer relative links within the repository. Link to the owning document rather than duplicating definitions. Avoid bare URLs in prose when a descriptive link is possible. Keep anchors stable; record breaking changes in release notes.

## 10. Accessibility

Use descriptive link text, logical heading order and textual interpretations for diagrams. Do not encode meaning only through color. Tables should be narrow enough to render on small screens or be accompanied by prose.

## 11. Metadata

Publication-facing documents should declare title, status, normative status, owner and last-reviewed date in front matter or an equivalent visible status block.

## 12. Examples

**Compliant:** “Against `ADV-IV`, presentations in different relying-party contexts are intended to remain unlinkable for the declared epoch, subject to network-metadata exclusions.”

**Non-compliant:** “The system is fully anonymous and unlinkable.”

**Compliant:** “Holder-key control establishes possession of the configured secret. It does not establish agent authority.”

**Non-compliant:** “The holder is authorized because the proof verifies.”

## Claim completeness

Write material claims using the three-part form: against whom, for how long and alongside what. Link assurance statements to an assurance boundary and privacy statements to a disclosure boundary. Use stable `THR-xxx`, `CTL-xxx`, `AB-xxx` and `DB-xxx` identifiers where traceability is required. Do not describe a construction as selected when the task force has not ratified it.

