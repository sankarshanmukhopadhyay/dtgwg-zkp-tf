---
layout: default
title: "Record 006 Currentness and Status-Root Evidence"
parent: "Conformance"
nav_order: 42
---
# Record 006 currentness and status-root evidence

This downstream evidence profile is pinned to canonical upstream construction record 006 at `cfd94063e5cfee7ba6df4dcfd28c10399a0ffd0a`.

Record 006 establishes non-revocation **against an accepted status root at an epoch/state**. The downstream tests deliberately keep five questions separate:

1. is the supplied root known;
2. is it authenticated as coming from an acceptable authority;
3. is it fresh enough under the relying policy;
4. does the non-membership proof hold against that root; and
5. did root acquisition introduce a privacy observation that the deployment must disclose?

## Executable cases

| Case | Expected outcome | Boundary exercised |
|---|---|---|
| R006-POS-CACHED | accept | current authenticated root delivered through shared/cache distribution |
| R006-NEG-STALE | reject `rl-root-stale` | proof validity cannot cure stale state |
| R006-NEG-REVOKED | reject `handle-revoked` | handle is in the revoked set |
| R006-NEG-UNKNOWN-ROOT | reject `status-root-unknown` | verifier has no accepted state anchor |
| R006-NEG-UNAUTHENTIC-ROOT | reject `status-root-unauthenticated` | root authority/authenticity is not established by a ZKP |
| R006-POS-CARRIED | accept | authenticated holder-carried state can avoid a live subject lookup |
| R006-NEG-CARRIED-AUTH | reject | carried state without source authentication is insufficient |
| R006-POS-LIVE-DECLARED | accept | live lookup is permitted when its observation is explicitly governed |
| R006-NEG-LIVE-UNDECLARED | reject | hidden privacy degradation is not allowed |

Machine-readable cases live in `fixtures/record-006-status-root.json` and are exercised in the repository test suite.

## Relationship to PR-RES

The existing PR-RES profiles remain useful **deployment evidence**, but are not a semantic replacement for record 006.

- shared/cached status evidence maps cleanly to a privacy-preserving distribution profile;
- holder-carried authenticated snapshots can supply accepted state without a verifier-originated subject lookup;
- live lookup remains a governed deployment option with explicit privacy degradation.

Registry membership, accreditation, authorization and credential status remain distinct semantics even if they reuse similar root/set machinery.

## External remainder for #27

These tests intentionally do not decide:

- which registry/governance actor is authoritative for a given root;
- the normative maximum root age;
- the allowed propagation delay after suspension/revocation;
- whether a particular ecosystem permits subject-specific live lookup;
- the semantic relationship between membership, accreditation, authorization and status.

Those remain external governance/specification inputs under #27.

## Reuse

The status-root adapter and fixture suite can be consumed by record 010 Community-Anchored Proof (#14), record 021 VAC assurance (#33), and other composed constructions without treating a valid non-membership proof as proof of current governance authority.
