---
layout: default
title: "Traceability Matrices"
parent: "Implementation Guide"
nav_order: 19
has_children: true
has_toc: true
---
# Living matrices

| Matrix | Purpose | Rows |
|---|---|---|
| scenario-index.csv | master catalogue | 30 (all UC-001..UC-030) |
| adr-scenario-map.csv | decision traceability | 25 |
| predicate-scenario-map.csv | predicate coverage | 72 |
| threat-scenario-map.csv | adversary coverage | 46 |
| ownership-map.csv | workstream responsibility | 10 |
| maturity-map.csv | readiness evidence | 8 |

## Regenerating

These CSVs are curated by hand against the pressure-test corpus,
`taxonomy/predicates.md`, `taxonomy/adversaries.md` and
`architecture/06-ownership-model.md`. There is no automated extraction
tool yet — this is itself an open item (see `maturity-map.csv`, row
"Predicate taxonomy").

Run `python3 scripts/validate_conformance.py` from the repository root
after any edit to these CSVs. It rejects:

- placeholder (header-only) matrices;
- any `predicate_id` not defined in `taxonomy/predicates.md`;
- any `adversary_id` not defined in `taxonomy/adversaries.md`;
- any `scenario_id` not present as a `UC-NNN` heading in
  `scenarios/pressure-test-use-case-corpus.md`;
- any `adr_id` in `adr-scenario-map.csv` without a matching file in `adr/`.

## Coverage notes

`predicate-scenario-map.csv` and `threat-scenario-map.csv` currently cover
26 and 30 of the 30 scenarios respectively. The four scenarios absent from
the predicate map (UC-017, UC-026, UC-027, UC-029) are explicitly
profile-dependent in the corpus ("Required predicates: Depends on target
profile" / "Any" / "Varies") rather than omitted by mistake — see
`maturity-map.csv` for how this is tracked.
