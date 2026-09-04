# Security Policy

## Scope

This repository contains implementation guidance, conformance tooling, experimental proof profiles and supporting documentation for a DTG ZKP fork. It is not the authoritative upstream DTG specification and does not provide production certification.

Security reports should distinguish between:

- defects in fork-owned code, fixtures, workflows or documentation;
- weaknesses in an experimental construction/profile used here;
- issues that belong to an upstream DTG specification or external dependency.

The maintainers will route upstream-owned findings to the appropriate authority rather than silently redefining upstream semantics in this fork.

## Reporting a vulnerability

Do not disclose an exploitable vulnerability in a public issue before maintainers have had an opportunity to assess it. Use GitHub's private vulnerability reporting capability for this repository when available. If that capability is unavailable, contact the repository owner through a private channel and provide the repository name, affected revision, reproduction steps, impact, and any available mitigation.

Do not include secrets, personal data, private keys, production credentials, or unrelated sensitive material in a report.

## Supported versions

The maintained security surface is the current `main` branch and the latest published fork release, where one exists. Historical releases and superseded experimental profiles may remain available for auditability but are not implicitly supported.

## Security assurance boundary

Passing repository CI, semantic conformance tests or construction-level fixtures does not establish production security, cryptographic soundness for every deployment, independent interoperability, biometric correctness, governance legitimacy or deployment-specific assurance. Missing evidence remains missing evidence.

Security-relevant fixes should normally preserve an Issue → PR → tests → merge trail, including the affected claim, regression evidence, compatibility impact and residual risk.