---
layout: default
title: Upstream Construction Record Crosswalk
nav_order: 40
parent: Conformance
has_toc: true
---
# Upstream Construction Record Crosswalk

This crosswalk maps existing downstream implementation and assurance evidence to the canonical construction records in `trustoverip/dtgwg-zkp-spec` at commit `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

It is deliberately **not** a downstream construction-record schema. The upstream record model remains authoritative where it speaks. The machine-readable companion is [`upstream-construction-record-crosswalk.json`](upstream-construction-record-crosswalk.json).

## Governing rule

Downstream assets are treated as an **evidence pool**, not as a semantic baseline.

For each local profile, fixture family or pressure test, the question is:

1. which upstream proposition does it actually exercise;
2. whether the existing evidence remains valid under that proposition;
3. whether the asset is additive assurance/implementation evidence rather than specification semantics; and
4. whether a local abstraction should be retired because upstream now owns the semantic surface.

## Primary mappings

| Downstream asset | Canonical upstream relationship | Disposition |
|---|---|---|
| EXP-PR-REL-SIGMA-01 | Record 009 directly; record 007 only when the hidden scalar is explicitly the controller secret under the chosen identifier/key profile | **reuse_evidence** |
| EXP-PR-HID-PEDERSEN-01 | Record 008 blinded binder / commitment opening | **reuse_evidence** |
| PR-RES profiles | Record 006 for non-revocation/currentness; record 001 only where an authenticated snapshot supplies a membership root | **retain_downstream_extension** |
| EXP-BBS-2023-01 | Supporting evidence for holder-binding/selective-disclosure profiles, but not equivalent to records 004 or 011 | **retain_downstream_extension** |
| Community-Anchored Proof fixtures | Record 010 plus components 001–007 as applicable | **reuse_evidence** |
| Composed-presentation privacy fixtures | Negative-space evidence for records 008, 012, 020 and 021 | **retain_downstream_extension** |
| Asymmetric-edge privacy fixtures | Pressure-test input for record 013 | **retain_downstream_extension** |
| Trust-task ZKP integration | Integration evidence for records 003/008/020/021 | **retain_downstream_extension** |

## Semantic abstractions to retire or narrow

### PR-REL

The local label `PR-REL` should no longer be used as though it names one canonical relation.

The existing Sigma construction most directly implements **record 009, Hidden-value equality across credentials** when the commitments represent authenticated credential fields. It may also provide evidence toward **record 007, Common control across identifiers**, but only when the compared hidden value is explicitly the controller secret required by the selected identifier/key profile.

Those are different propositions and must remain different.

### PR-HID

The local `PR-HID` profile remains useful as an implementation/evidence identifier, but the overlapping semantic proposition is now upstream **record 008, Blinded binder**.

The local dictionary-recovery and stable-binder negative cases remain valuable because record 008 explicitly says that hiding a plaintext does not establish unlinkability when a reusable visible commitment remains.

### PR-RES

`PR-RES` currently combines several resolution semantics. That is too broad to operate as one semantic primitive.

Upstream **record 006** owns the ZKP-side proposition for non-revocation against a status root. Registry membership, accreditation, authorization, root authority, cache policy and live-lookup privacy remain distinct external/downstream concerns. The local resolution profiles should therefore survive as implementation/deployment evidence, not as a competing construction definition.

### Evidence lifecycle

Local evidence states must not be mistaken for upstream record states.

Where a downstream asset is mapped to a construction record, use the upstream lifecycle:

`requested → specified → constructed → run → vetted → published`

Downstream may retain stricter assurance gates such as independent interoperability, RAHP review or deployment evidence. Those gates are additive and do not change the upstream record state.

## Important non-equivalences

### BBS evidence is not a DTG construction record

The BBS profile has useful external interoperability evidence for its own cryptographic capabilities. It does **not** automatically establish the witness relations, registry semantics, transcript semantics or composition clauses required by DTG records 004, 010 or 011.

### Semantic harnesses are not proof-system runtimes

The Community-Anchored Proof and privacy harnesses are useful proposition-level positive/negative evidence. Passing them does not establish that a circuit or proof implementation exists, is secure, or is independently reproduced.

### Assurance fixtures do not create specification semantics

The downstream repository contains privacy, deployment, operations, incident, risk, RAHP and DPIP material that has no one-to-one upstream construction record. Those assets remain intentionally downstream unless a future upstream specification explicitly owns the same proposition.

## Consequences for existing issues

- **#14 Community-Anchored Proof** should consume record 010 and its component records rather than define PR-* primitives independently.
- **#28 promotion blockers** remains valid. A local implementation that passes repository CI does not advance an upstream record to `run`, `vetted` or `published`.
- **#32 mutual-edge admissibility** should treat record 013 as the semantic anchor but keep execution bounded while canonical main still lists it as `requested`.
- **#33 VAC authority-chain assurance** should use record 021 and record 009 for hidden chain-link equality, preserving the authority-vs-delegation boundary.

## Migration rule

When changing an existing downstream artifact:

1. cite the pinned upstream record and commit;
2. state whether the artifact is `reuse_evidence`, `retain_downstream_extension`, `superseded`, `propose_upstream_gap` or `needs_judgment`;
3. remove local semantic wording that conflicts with or duplicates the upstream record;
4. preserve stronger negative and assurance evidence when it does not redefine the proposition; and
5. never claim an upstream record-state advance from downstream evidence alone.

This crosswalk should be refreshed whenever the canonical upstream construction-record set materially changes.
