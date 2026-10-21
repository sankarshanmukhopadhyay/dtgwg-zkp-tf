---
layout: default
title: "Evidence Retest Impact"
parent: "Conformance"
nav_order: 60
---

# Evidence change-impact and retest

The conservative [evidence change-impact calculator](../../../scripts/evidence_change_impact.py) compares two source-derived [evidence registry projections](evidence-registry-projection.md). It returns `RETEST_REQUIRED` when the pinned canonical authority, source register, evidence asset digests, recorded classes/labels/gaps or claimed independence changes. It never returns `PASS` for a cryptographic or governance proposition.

## Reproduce

Capture an immutable snapshot from a **known repository revision**:

```sh
python3 scripts/evidence_registry.py --output /tmp/zkp-before.json
```

After a subsequent change, run:

```sh
python3 -m scripts.evidence_change_impact --before /tmp/zkp-before.json --output /tmp/zkp-retest.json
python3 -m pytest -q scripts/tests/test_evidence_change_impact.py
```

The output identifies per-record reason codes and conservatively invalidates **all** records when the source register or upstream authority changes, since a more precise dependency graph has not yet been established. This errs toward reassessment over false confidence.

**Not yet implemented:** an event-level attributable execution record with immutable CI/job identity, measured environment, observed outcomes and external review; library dependency-manifest locking across all cryptographic components; selective dependency-graph invalidation; automated rerun orchestration; interpretation of upstream changes. A retest trigger is a *review requirement*, not an assertion that the underlying proof has failed.

The tool assumes upstream authority is governed under [#30](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/30), Credential representation under [#26](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/26), and Registry status policy under [#27](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/27).

The current release disposition remains [DEFER](zkp-local-completion.md). Retest logic improves assurance controls; it does not close full CAP construction [#54](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/54) or independent reproduction [#55](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf/issues/55).
