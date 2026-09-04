---
layout: default
title: "Public repository baseline"
nav_order: 40
---
# Public repository baseline

This page records the evidence state for the public-repository baseline tracked in issue #18. It is an assurance record, not a substitute for GitHub repository settings or upstream authority.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose, maturity, intended users, authority and limits | verified | `README.md`, `PROJECT-STATUS.yaml` | None identified at repository-document level. |
| Reproducible validation | verified | `README.md`; `python3 scripts/validate_all.py`; `pytest -q conformance-harness/tests` | Hosted-runner behaviour and external dependencies remain operational dependencies. |
| License | verified | `LICENSE` | Upstream/JDF provenance obligations still apply to carried material. |
| Contribution and support routing | verified | `CONTRIBUTING.md`, `SUPPORT.md`, local issue/PR templates | Maintainer response times are not guaranteed. |
| Conduct expectations | verified | `CODE_OF_CONDUCT.md` | Enforcement remains a maintainer/platform responsibility. |
| Security reporting and supported surface | verified | `SECURITY.md` | Private vulnerability reporting availability is a GitHub setting and must be checked separately. |
| Workflow permissions | partially_verified | Workflows declare explicit permissions; quality validation is read-only; upstream synchronisation declares write scopes required to open issues/PRs and push its sync branch | Privileged workflows remain consequential trust surfaces and require periodic review. |
| Dependency/update management | verified | `.github/dependabot.yml` groups GitHub Actions and Python updates | Tagged GitHub Actions are not equivalent to immutable commit-SHA pinning; this remains a hardening opportunity unless/update until repository policy requires SHA pinning. |
| Deterministic conformance/negative evidence | verified | `scripts/validate_all.py`, conformance harness, construction/profile evidence workflows | Independent DTG-specific interoperability remains incomplete and is not inferred from local tests. |
| Release/version/provenance boundaries | verified | `PROJECT-STATUS.yaml`, release notes, upstream synchronisation governance | Fork releases do not imply upstream adoption. |
| Docs/Pages alignment | verified_by_ci | `.github/workflows/pages.yml` and repository validators | A successful Pages run remains required for each publication-changing PR. |
| Authority and scope boundaries | verified | `README.md`, `PROJECT-STATUS.yaml`, upstream synchronisation governance | None: upstream normative authority remains explicitly external. |
| Experimental vs normative material | verified | README and conformance documentation mark construction profiles non-normative | Promotion still requires explicit governed decision and stronger evidence. |
| `main` protection/ruleset | evidence_required | GitHub rulesets API returned no active repository ruleset during the 2026-09-04 baseline review | Force-push/delete and required-check protection cannot be claimed until a repository ruleset/equivalent is configured and re-observed. |

## Completion rule

Repository-owned baseline gaps may be closed in code and documentation. GitHub-hosted controls such as rulesets and private vulnerability reporting remain external configuration evidence: missing evidence MUST NOT be interpreted as PASS.

When the `main` ruleset is configured, update this record with the observed ruleset identity, required checks, bypass authority and verification date.