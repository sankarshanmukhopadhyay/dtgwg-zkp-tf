---
layout: default
title: "B1 context-delimiter impact"
parent: "Decision Governance"
grand_parent: "Implementation Guide"
nav_order: 5
has_toc: true
---
# B1 context-delimiter impact assessment

The fork implements a context as a versioned governance object that defines an intentional linkability domain. It is not reducible to a verifier hostname, ecosystem label or nullifier input string.

## Release increment

v0.3.0 adds a canonical context descriptor schema, valid and invalid fixtures, explicit change-authority fields and controls against silent expansion through common ownership, federation, merger or shared infrastructure.

## Ratification-sensitive surfaces

- nullifier scope and epoch derivation;
- verifier-set membership and versioning;
- human-readable context notice;
- migration and appeal;
- cross-context linkage prohibitions;
- conformance claims that depend on domain separation.

Discussion #13 records this as an adopted working position for the v0.4 requirements progression. The fork implementation remains non-normative and is subject to amendment through Task Force decision governance.
