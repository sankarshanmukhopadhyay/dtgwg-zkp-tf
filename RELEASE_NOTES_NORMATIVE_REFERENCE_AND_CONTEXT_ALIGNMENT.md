# Release notes: Normative reference and context alignment

## Summary

This update reconciles the implementation guide against the task force's own discussion record: Discussion #3 ("Which proof type(s) do we need?") and Discussion #8 ("What counts as a context?"). It fixes a documentation defect, carries the normative reference (IACR ePrint 2026/333) into the implementation guide for the first time, and corrects guide language that described the context model as untouched when a draft V1 definition already exists elsewhere in the same repository. It remains proof-system agnostic and preserves the Minimum Liveness and Extended Personhood profile split.

## Fixed

- removed a verbatim-duplicated "Boundary and assurance model" section and a stray extra heading in the main guide, left behind by a prior merge.

## Added

- IACR ePrint 2026/333 as a normative reference in `appendices/REFERENCES.md`, matching the citation already established at repository root;
- cross-references from ADR-002, ADR-003 and ADR-006 through ADR-009 to the normative reference in each ADR's Context section;
- a non-normative subsection (§12.5) on multi-issuer assurance aggregation in the predicate and assurance-boundary decision document, recording the normative reference's mis-issuance bound as decision input for accreditation profiles that cite more than one issuer;
- a corresponding cross-reference from ADR-004 to that subsection.

## Changed

- the main guide's context section (§5.2) and known-decision-dependencies list (§12) no longer describe the context and epoch model as an untouched open question; they now state that a draft V1 definition exists at `boundaries/predicate-assurance-boundary-decision.md` §6 and `boundaries/context-decision-record.md`, and that ratification, not drafting, is what remains open.

## Deliberately unresolved

No cryptographic construction is selected or implied as ratified, and the draft V1 context definition is decision input rather than a ratified specification. Both remain task-force decisions. The multi-issuer assurance aggregation mechanism is recorded as an option, not a requirement, pending a task-force decision on whether any profile mandates it.
