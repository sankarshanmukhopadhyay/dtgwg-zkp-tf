---
title: Upstream synchronisation governance
---

# Upstream synchronisation governance

This repository uses a deliberately one-way control plane. The declared upstream, `trustoverip/dtgwg-zkp-tf`, is readable; this fork is the only writable target. Upstream changes are detected automatically and integrated only through a draft pull request reviewed under normal branch protections. Every monitor run publishes a workflow summary and evidence artifact. When repository Issues are enabled, detected drift is also raised as an evidence-backed issue.

## Preserved upstream project narrative

The current upstream project README is preserved in [`UPSTREAM_README.md`](../../UPSTREAM_README.md). The fork root README is intentionally fork-specific. This avoids a recurring merge pattern in which upstream project framing and fork implementation material are interleaved in one file.

When an upstream README change is integrated, maintainers should review and refresh `UPSTREAM_README.md` as part of the same synchronisation pull request. Fork-specific explanations belong in the root `README.md`, not in the preserved snapshot.

## Authority

The workflows may fetch upstream, create or update issues in this fork, create a branch in this fork, and open a draft pull request against this fork. They may not push to upstream, create an upstream issue, open an upstream pull request, approve their own change, or merge automatically.

## Procedure

1. The monitor runs every ten days or on manual dispatch.
2. A drift report distinguishes observed, reviewed and integrated commits and is published as both a workflow summary and an artifact.
3. If drift exists and Issues are enabled, the monitor creates or updates the governed drift issue. If Issues are disabled, the monitor fails visibly after preserving the evidence so that drift cannot be silently discarded.
4. A maintainer runs **Upstream synchronisation** to prepare a merge-based draft pull request.
5. Protected local paths and semantic conflicts receive human review.
6. Existing validation and publication checks remain mandatory.
7. Only a human-authorised merge integrates the upstream change.

## Revocation and evidence

Disabling the policy or workflows, or removing write permissions, immediately revokes automation authority. Checkpoint data, workflow summaries, artifacts, optional issues, pull requests, checks and merge history form the audit chain. Issue creation is a notification convenience rather than the sole evidence channel.
