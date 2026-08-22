---
layout: default
title: "Identifier and control register"
parent: "Reference"
grand_parent: "Implementation Guide"
nav_order: 1
has_toc: true
---
# Identifier and control register

This is the reader-facing **single register for stable identifiers used across the implementation guide**. It is an index, not a competing source of truth. Each entry gives a short conceptual meaning and points to the document that owns the full definition.

Use this register whenever an identifier appears outside its defining document. The repository validation suite checks that recognised identifier families resolve to an entry here. This makes references such as `PR-HLD`, `THR-051`, `CTL-GOV`, `ZGR-07`, or `ADR-001` understandable without requiring a reader to search the repository.

## Identifier families

| Prefix | Family | What it identifies |
|---|---|---|
| `AP-` | Architecture principle | design rules that constrain implementation choices |
| `PR-` | Predicate | a statement a proof establishes, with explicit negative meaning |
| `ADV-` | Adversary | attacker or colluding actor assumed by a claim or test |
| `CL-` | Conformance level | cumulative implementation/conformance capability tier |
| `UC-` | Scenario | pressure-test use case that exposes assumptions and obligations |
| `THR-` | Threat | canonical threat event in the security model |
| `HRM-` | Harm | downstream human, institutional, economic, or systemic harm class |
| `CTL-` | Control | preventive, detective, or corrective risk treatment |
| `ZGR-` | Guardrail | activation gate that must pass, block, or receive an eligible exception |
| `ZAT-` | Assurance test | evidence-producing test of control or guardrail effectiveness |
| `IG-` | Implementation guidance | non-normative implementation expectation with observable evidence |
| `SEC-` | Security requirement | cross-cutting boundary, lifecycle, or security expectation |
| `TCR-` | Threat conformance requirement | conformance obligation paired with a canonical threat |
| `ZKP-LINK-`, `ZKP-TASK-`, `ZKP-CER-` | Interoperability requirement | cross-specification requirement for linkage, Trust Tasks, or Trust Ceremonies |
| `ADR-` | Architecture decision | recorded design decision and its rationale |

Conformance test IDs (`CT-*`), diagram IDs (`D-*`), assurance/disclosure boundary instance IDs (`AB-*`, `DB-*`), and deployment-specific IDs are intentionally resolved by their specialised registers or artefacts rather than duplicated here. The family directory above should make that distinction explicit to readers.

**Namespace rule:** `SEC-*` is reserved for cross-cutting security requirements. Threat-specific conformance requirements use `TCR-*`; this prevents the former `SEC-*` collision between the guidance index and threat matrix. Proposed but not-yet-defined identifiers may be listed explicitly as reserved/open entries.

## Architecture principle

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="ap-01"></a>`AP-01` | Privacy is contextual | [definition](../architecture/03-principles.md) |
| <a id="ap-02"></a>`AP-02` | Proofs prove statements, not reality | [definition](../architecture/03-principles.md) |
| <a id="ap-03"></a>`AP-03` | Assurance is governance-backed | [definition](../architecture/03-principles.md) |
| <a id="ap-04"></a>`AP-04` | Personhood is not civil identity | [definition](../architecture/03-principles.md) |
| <a id="ap-05"></a>`AP-05` | Holder control is not authority | [definition](../architecture/03-principles.md) |
| <a id="ap-06"></a>`AP-06` | Context determines permitted linkability | [definition](../architecture/03-principles.md) |
| <a id="ap-07"></a>`AP-07` | Lifecycle is part of trust | [definition](../architecture/03-principles.md) |
| <a id="ap-08"></a>`AP-08` | Interoperability includes semantics | [definition](../architecture/03-principles.md) |
| <a id="ap-09"></a>`AP-09` | Accessibility is a first-class requirement | [definition](../architecture/03-principles.md) |
| <a id="ap-10"></a>`AP-10` | Production readiness is systemic | [definition](../architecture/03-principles.md) |

## Predicate

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="pr-fre"></a>`PR-FRE` | freshness | [definition](../taxonomy/predicates.md) |
| <a id="pr-hld"></a>`PR-HLD` | holder binding | [definition](../taxonomy/predicates.md) |
| <a id="pr-iss"></a>`PR-ISS` | accredited issuer | [definition](../taxonomy/predicates.md) |
| <a id="pr-liv"></a>`PR-LIV` | liveness attestation | [definition](../taxonomy/predicates.md) |
| <a id="pr-per"></a>`PR-PER` | personhood policy | [definition](../taxonomy/predicates.md) |
| <a id="pr-rng"></a>`PR-RNG` | range predicate | [definition](../taxonomy/predicates.md) |
| <a id="pr-unq"></a>`PR-UNQ` | scoped uniqueness | [definition](../taxonomy/predicates.md) |
| <a id="pr-del"></a>`PR-DEL` | delegated/current authority | [definition](../taxonomy/predicates.md) |
| <a id="pr-cmp"></a>`PR-CMP` | composed-presentation privacy across the complete evidence closure | [definition](../taxonomy/predicates.md) |
| <a id="pr-rel"></a>`PR-REL` | privacy-preserving relationship proof across artefacts/evidence | [definition](../taxonomy/predicates.md) |
| <a id="pr-hid"></a>`PR-HID` | confidential binding with an explicit hiding property | [definition](../taxonomy/predicates.md) |
| <a id="pr-res"></a>`PR-RES` | privacy-preserving external resolution | [definition](../taxonomy/predicates.md) |

## Adversary

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="adv-a"></a>`ADV-A` | malicious or compromised agent | [definition](../taxonomy/adversaries.md) |
| <a id="adv-g"></a>`ADV-G` | governance or accreditation authority acting outside mandate | [definition](../taxonomy/adversaries.md) |
| <a id="adv-i"></a>`ADV-I` | issuer | [definition](../taxonomy/adversaries.md) |
| <a id="adv-iv"></a>`ADV-IV` | issuer and verifier colluding | [definition](../taxonomy/adversaries.md) |
| <a id="adv-m"></a>`ADV-M` | mediated prover or proving-service operator | [definition](../taxonomy/adversaries.md) |
| <a id="adv-n"></a>`ADV-N` | network observer | [definition](../taxonomy/adversaries.md) |
| <a id="adv-o"></a>`ADV-O` | operational insider or log administrator | [definition](../taxonomy/adversaries.md) |
| <a id="adv-p"></a>`ADV-P` | biometric provider | [definition](../taxonomy/adversaries.md) |
| <a id="adv-r"></a>`ADV-R` | registry operator or compromised registry | [definition](../taxonomy/adversaries.md) |
| <a id="adv-u"></a>`ADV-U` | adversarial presenter | [definition](../taxonomy/adversaries.md) |
| <a id="adv-v"></a>`ADV-V` | verifier | [definition](../taxonomy/adversaries.md) |
| <a id="adv-w"></a>`ADV-W` | compromised wallet/runtime | [definition](../taxonomy/adversaries.md) |

## Conformance level

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="cl-1"></a>`CL-1` | Minimum Liveness Profile | [definition](../conformance/levels.md) |
| <a id="cl-2"></a>`CL-2` | Extended Personhood Profile | [definition](../conformance/levels.md) |
| <a id="cl-3"></a>`CL-3` | Delegated Agent Profile | [definition](../conformance/levels.md) |
| <a id="cl-4"></a>`CL-4` | Federated & Adversarial Assurance Profile | [definition](../conformance/levels.md) |

## Scenario

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="uc-001"></a>`UC-001` | Privacy-Preserving Account Creation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-002"></a>`UC-002` | Anonymous or Pseudonymous Community Participation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-003"></a>`UC-003` | Age-Threshold Access Without Date-of-Birth Disclosure | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-004"></a>`UC-004` | High-Value Financial Transaction Step-Up | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-005"></a>`UC-005` | Sensitive Account Recovery | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-006"></a>`UC-006` | Recurring Login With Same-Human Continuity | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-007"></a>`UC-007` | One-Person-One-Benefit-Claim Per Period | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-008"></a>`UC-008` | Anonymous Public Consultation or Digital Ballot | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-009"></a>`UC-009` | Human Authorises an AI Agent | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-010"></a>`UC-010` | Human Step-Up for Agent Intent Drift | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-011"></a>`UC-011` | Agent Presents Proof on Behalf of Principal | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-012"></a>`UC-012` | Issuer Suspension After Proof Issuance | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-013"></a>`UC-013` | Accreditation Framework or Policy Version Change | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-014"></a>`UC-014` | Trust Registry Unavailable or Partitioned | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-015"></a>`UC-015` | Multiple Trust Registries Disagree | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-016"></a>`UC-016` | Cross-Border Recognition of Liveness Assurance | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-017"></a>`UC-017` | Low-End or Constrained Consumer Device | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-018"></a>`UC-018` | Intermittent Connectivity and Offline Presentation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-019"></a>`UC-019` | Shared Device and Multi-User Wallet | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-020"></a>`UC-020` | Accessibility Alternative to Facial Liveness | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-021"></a>`UC-021` | Compromised Wallet Key but Live Human Present | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-022"></a>`UC-022` | Malicious or Compromised Biometric Provider | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-023"></a>`UC-023` | Malicious Verifier Attempts Cross-Context Correlation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-024"></a>`UC-024` | Issuer and Verifier Collude | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-025"></a>`UC-025` | Proof Composition Across Credentials and Trust Tasks | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-026"></a>`UC-026` | Algorithm Upgrade and Mixed-Version Ecosystem | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-027"></a>`UC-027` | Verifier Policy Error, Appeal, and Redress | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-028"></a>`UC-028` | Emergency or Disaster Operations | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-029"></a>`UC-029` | Large-Scale Batch Verification | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-030"></a>`UC-030` | Partial Deployment Across Independent Implementations | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-031"></a>`UC-031` | Migration from Conventional Identity Checks | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-032"></a>`UC-032` | Managed Enterprise Wallet Deployment | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-033"></a>`UC-033` | Multi-Tenant Verifier Isolation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-034"></a>`UC-034` | Federated Issuer Ecosystem | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-035"></a>`UC-035` | Registry Federation and Authority Transition | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-036"></a>`UC-036` | Multi-Region Verifier Deployment | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-037"></a>`UC-037` | Proof Service or Cloud-Region Outage | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-038"></a>`UC-038` | Software Supply-Chain Compromise | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-039"></a>`UC-039` | Emergency Signing-Key Rotation | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-040"></a>`UC-040` | Incorrect Policy Rollout and Rollback | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-041"></a>`UC-041` | Audit or Regulatory Evidence Request | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-042"></a>`UC-042` | Data-Subject Challenge and State Correction | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-043"></a>`UC-043` | High-Volume Burst and Abuse Traffic | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-044"></a>`UC-044` | Compromised Administrative Operator | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-045"></a>`UC-045` | Expired Privacy or Assurance Horizon | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-046"></a>`UC-046` | Cross-Organization Plugfest Onboarding | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-047"></a>`UC-047` | Cryptographic Library Vulnerability | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-048"></a>`UC-048` | Partial Rollback During Ecosystem Upgrade | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-049"></a>`UC-049` | Credential Linkage Required but Not Evidenced | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-050"></a>`UC-050` | Trust Task Proof Replayed to Another Action | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-051"></a>`UC-051` | Ceremony Context Used as Authority Evidence | [definition](../scenarios/pressure-test-use-case-corpus.md) |
| <a id="uc-052"></a>`UC-052` | Linkage or Ceremony Reference Creates Cross-Context Correlation | [definition](../scenarios/pressure-test-use-case-corpus.md) |

## Threat

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="thr-001"></a>`THR-001` | Forged proof accepted | [definition](../security/threat-matrix.md) |
| <a id="thr-002"></a>`THR-002` | Replay across requests | [definition](../security/threat-matrix.md) |
| <a id="thr-003"></a>`THR-003` | Cross-domain transcript substitution | [definition](../security/threat-matrix.md) |
| <a id="thr-004"></a>`THR-004` | Setup or parameter compromise | [definition](../security/threat-matrix.md) |
| <a id="thr-005"></a>`THR-005` | Prover side-channel leakage | [definition](../security/threat-matrix.md) |
| <a id="thr-006"></a>`THR-006` | Transferred key treated as human continuity | [definition](../security/threat-matrix.md) |
| <a id="thr-007"></a>`THR-007` | False biometric determination attested | [definition](../security/threat-matrix.md) |
| <a id="thr-008"></a>`THR-008` | Duplicate enrolment under same issuer | [definition](../security/threat-matrix.md) |
| <a id="thr-009"></a>`THR-009` | Cross-issuer duplicate enrolment | [definition](../security/threat-matrix.md) |
| <a id="thr-010"></a>`THR-010` | Stable enrolment root enables population correlation | [definition](../security/threat-matrix.md) |
| <a id="thr-011"></a>`THR-011` | Unbounded nullifier creates permanent identifier | [definition](../security/threat-matrix.md) |
| <a id="thr-012"></a>`THR-012` | Issuer identity inferred despite concealment | [definition](../security/threat-matrix.md) |
| <a id="thr-013"></a>`THR-013` | Attestation metadata correlates presentations | [definition](../security/threat-matrix.md) |
| <a id="thr-014"></a>`THR-014` | Registry or status lookup reveals subject activity | [definition](../security/threat-matrix.md) |
| <a id="thr-015"></a>`THR-015` | Issuer-verifier collusion crosses context boundary | [definition](../security/threat-matrix.md) |
| <a id="thr-016"></a>`THR-016` | Rare predicate bundle fingerprints subject | [definition](../security/threat-matrix.md) |
| <a id="thr-017"></a>`THR-017` | Individually safe proofs leak jointly | [definition](../security/threat-matrix.md) |
| <a id="thr-018"></a>`THR-018` | Presentation timing and frequency reveal behaviour | [definition](../security/threat-matrix.md) |
| <a id="thr-019"></a>`THR-019` | Error and retry behaviour becomes oracle | [definition](../security/threat-matrix.md) |
| <a id="thr-020"></a>`THR-020` | Unauthorized issuer accepted | [definition](../security/threat-matrix.md) |
| <a id="thr-021"></a>`THR-021` | Policy version substitution | [definition](../security/threat-matrix.md) |
| <a id="thr-022"></a>`THR-022` | Revoked or suspended state accepted | [definition](../security/threat-matrix.md) |
| <a id="thr-023"></a>`THR-023` | Assurance class inflation | [definition](../security/threat-matrix.md) |
| <a id="thr-024"></a>`THR-024` | Agent key control mistaken for delegated authority | [definition](../security/threat-matrix.md) |
| <a id="thr-025"></a>`THR-025` | Algorithm downgrade during negotiation | [definition](../security/threat-matrix.md) |
| <a id="thr-026"></a>`THR-026` | Enrolment root outlives defensible protection | [definition](../security/threat-matrix.md) |
| <a id="thr-027"></a>`THR-027` | Migration splits verification state | [definition](../security/threat-matrix.md) |
| <a id="thr-028"></a>`THR-028` | Recovery resets reuse protections | [definition](../security/threat-matrix.md) |
| <a id="thr-029"></a>`THR-029` | Mediator retains witness-related data | [definition](../security/threat-matrix.md) |
| <a id="thr-030"></a>`THR-030` | Silent fallback lowers assurance or increases disclosure | [definition](../security/threat-matrix.md) |
| <a id="thr-031"></a>`THR-031` | Offline verification uses stale governance state | [definition](../security/threat-matrix.md) |
| <a id="thr-032"></a>`THR-032` | Logs become cross-context correlation store | [definition](../security/threat-matrix.md) |
| <a id="thr-033"></a>`THR-033` | Context boundary is unintelligible to affected person | [definition](../security/threat-matrix.md) |
| <a id="thr-034"></a>`THR-034` | Accessibility path creates disproportionate disclosure | [definition](../security/threat-matrix.md) |
| <a id="thr-035"></a>`THR-035` | Decision cannot be contested or corrected | [definition](../security/threat-matrix.md) |
| <a id="thr-036"></a>`THR-036` | Context silently expands through organizational change | [definition](../security/threat-matrix.md) |
| <a id="thr-037"></a>`THR-037` | Governance authority capture | [definition](../security/threat-matrix.md) |
| <a id="thr-038"></a>`THR-038` | Concentrated provider coercion | [definition](../security/threat-matrix.md) |
| <a id="thr-039"></a>`THR-039` | Assurance evidence fabricated or selectively omitted | [definition](../security/threat-matrix.md) |
| <a id="thr-040"></a>`THR-040` | Governance process exhaustion | [definition](../security/threat-matrix.md) |
| <a id="thr-041"></a>`THR-041` | AI-assisted operator social engineering | [definition](../security/threat-matrix.md) |
| <a id="thr-042"></a>`THR-042` | Discriminatory predicate or profile selection | [definition](../security/threat-matrix.md) |
| <a id="thr-043"></a>`THR-043` | Risk acceptance laundering | [definition](../security/threat-matrix.md) |
| <a id="thr-044"></a>`THR-044` | Metric gaming or observability suppression | [definition](../security/threat-matrix.md) |
| <a id="thr-045"></a>`THR-045` | Affected-party harm remains invisible | [definition](../security/threat-matrix.md) |
| <a id="thr-046"></a>`THR-046` | Unproven identifier linkage accepted as proof input | [definition](../security/threat-matrix.md) |
| <a id="thr-047"></a>`THR-047` | Identifier linkage creates cross-context correlation | [definition](../security/threat-matrix.md) |
| <a id="thr-048"></a>`THR-048` | Task or ceremony participation treated as authority | [definition](../security/threat-matrix.md) |
| <a id="thr-049"></a>`THR-049` | Ceremony identifier becomes stable correlation handle | [definition](../security/threat-matrix.md) |
| <a id="thr-050"></a>`THR-050` | Valid proof bound to wrong Trust Task | [definition](../security/threat-matrix.md) |
| <a id="thr-051"></a>`THR-051` | Agent presents valid human proof outside delegated scope | [definition](../security/threat-matrix.md) |
| <a id="thr-052"></a>`THR-052` | Historical ceremony evidence reinterpreted under changed policy | [definition](../security/threat-matrix.md) |

## Threat conformance requirement

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="tcr-001"></a>`TCR-001` | Conformance obligation for `THR-001`: Forged proof accepted | [definition](../security/threat-matrix.md) |
| <a id="tcr-002"></a>`TCR-002` | Conformance obligation for `THR-002`: Replay across requests | [definition](../security/threat-matrix.md) |
| <a id="tcr-003"></a>`TCR-003` | Conformance obligation for `THR-003`: Cross-domain transcript substitution | [definition](../security/threat-matrix.md) |
| <a id="tcr-004"></a>`TCR-004` | Conformance obligation for `THR-004`: Setup or parameter compromise | [definition](../security/threat-matrix.md) |
| <a id="tcr-005"></a>`TCR-005` | Conformance obligation for `THR-005`: Prover side-channel leakage | [definition](../security/threat-matrix.md) |
| <a id="tcr-006"></a>`TCR-006` | Conformance obligation for `THR-006`: Transferred key treated as human continuity | [definition](../security/threat-matrix.md) |
| <a id="tcr-007"></a>`TCR-007` | Conformance obligation for `THR-007`: False biometric determination attested | [definition](../security/threat-matrix.md) |
| <a id="tcr-008"></a>`TCR-008` | Conformance obligation for `THR-008`: Duplicate enrolment under same issuer | [definition](../security/threat-matrix.md) |
| <a id="tcr-009"></a>`TCR-009` | Conformance obligation for `THR-009`: Cross-issuer duplicate enrolment | [definition](../security/threat-matrix.md) |
| <a id="tcr-010"></a>`TCR-010` | Conformance obligation for `THR-010`: Stable enrolment root enables population correlation | [definition](../security/threat-matrix.md) |
| <a id="tcr-011"></a>`TCR-011` | Conformance obligation for `THR-011`: Unbounded nullifier creates permanent identifier | [definition](../security/threat-matrix.md) |
| <a id="tcr-012"></a>`TCR-012` | Conformance obligation for `THR-012`: Issuer identity inferred despite concealment | [definition](../security/threat-matrix.md) |
| <a id="tcr-013"></a>`TCR-013` | Conformance obligation for `THR-013`: Attestation metadata correlates presentations | [definition](../security/threat-matrix.md) |
| <a id="tcr-014"></a>`TCR-014` | Conformance obligation for `THR-014`: Registry or status lookup reveals subject activity | [definition](../security/threat-matrix.md) |
| <a id="tcr-015"></a>`TCR-015` | Conformance obligation for `THR-015`: Issuer-verifier collusion crosses context boundary | [definition](../security/threat-matrix.md) |
| <a id="tcr-016"></a>`TCR-016` | Conformance obligation for `THR-016`: Rare predicate bundle fingerprints subject | [definition](../security/threat-matrix.md) |
| <a id="tcr-017"></a>`TCR-017` | Conformance obligation for `THR-017`: Individually safe proofs leak jointly | [definition](../security/threat-matrix.md) |
| <a id="tcr-018"></a>`TCR-018` | Conformance obligation for `THR-018`: Presentation timing and frequency reveal behaviour | [definition](../security/threat-matrix.md) |
| <a id="tcr-019"></a>`TCR-019` | Conformance obligation for `THR-019`: Error and retry behaviour becomes oracle | [definition](../security/threat-matrix.md) |
| <a id="tcr-020"></a>`TCR-020` | Conformance obligation for `THR-020`: Unauthorized issuer accepted | [definition](../security/threat-matrix.md) |
| <a id="tcr-021"></a>`TCR-021` | Conformance obligation for `THR-021`: Policy version substitution | [definition](../security/threat-matrix.md) |
| <a id="tcr-022"></a>`TCR-022` | Conformance obligation for `THR-022`: Revoked or suspended state accepted | [definition](../security/threat-matrix.md) |
| <a id="tcr-023"></a>`TCR-023` | Conformance obligation for `THR-023`: Assurance class inflation | [definition](../security/threat-matrix.md) |
| <a id="tcr-024"></a>`TCR-024` | Conformance obligation for `THR-024`: Agent key control mistaken for delegated authority | [definition](../security/threat-matrix.md) |
| <a id="tcr-025"></a>`TCR-025` | Conformance obligation for `THR-025`: Algorithm downgrade during negotiation | [definition](../security/threat-matrix.md) |
| <a id="tcr-026"></a>`TCR-026` | Conformance obligation for `THR-026`: Enrolment root outlives defensible protection | [definition](../security/threat-matrix.md) |
| <a id="tcr-027"></a>`TCR-027` | Conformance obligation for `THR-027`: Migration splits verification state | [definition](../security/threat-matrix.md) |
| <a id="tcr-028"></a>`TCR-028` | Conformance obligation for `THR-028`: Recovery resets reuse protections | [definition](../security/threat-matrix.md) |
| <a id="tcr-029"></a>`TCR-029` | Conformance obligation for `THR-029`: Mediator retains witness-related data | [definition](../security/threat-matrix.md) |
| <a id="tcr-030"></a>`TCR-030` | Conformance obligation for `THR-030`: Silent fallback lowers assurance or increases disclosure | [definition](../security/threat-matrix.md) |
| <a id="tcr-031"></a>`TCR-031` | Conformance obligation for `THR-031`: Offline verification uses stale governance state | [definition](../security/threat-matrix.md) |
| <a id="tcr-032"></a>`TCR-032` | Conformance obligation for `THR-032`: Logs become cross-context correlation store | [definition](../security/threat-matrix.md) |
| <a id="tcr-033"></a>`TCR-033` | Conformance obligation for `THR-033`: Context boundary is unintelligible to affected person | [definition](../security/threat-matrix.md) |
| <a id="tcr-034"></a>`TCR-034` | Conformance obligation for `THR-034`: Accessibility path creates disproportionate disclosure | [definition](../security/threat-matrix.md) |
| <a id="tcr-035"></a>`TCR-035` | Conformance obligation for `THR-035`: Decision cannot be contested or corrected | [definition](../security/threat-matrix.md) |
| <a id="tcr-036"></a>`TCR-036` | Conformance obligation for `THR-036`: Context silently expands through organizational change | [definition](../security/threat-matrix.md) |
| <a id="tcr-037"></a>`TCR-037` | Conformance obligation for `THR-037`: Governance authority capture | [definition](../security/threat-matrix.md) |
| <a id="tcr-038"></a>`TCR-038` | Conformance obligation for `THR-038`: Concentrated provider coercion | [definition](../security/threat-matrix.md) |
| <a id="tcr-039"></a>`TCR-039` | Conformance obligation for `THR-039`: Assurance evidence fabricated or selectively omitted | [definition](../security/threat-matrix.md) |
| <a id="tcr-040"></a>`TCR-040` | Conformance obligation for `THR-040`: Governance process exhaustion | [definition](../security/threat-matrix.md) |
| <a id="tcr-041"></a>`TCR-041` | Conformance obligation for `THR-041`: AI-assisted operator social engineering | [definition](../security/threat-matrix.md) |
| <a id="tcr-042"></a>`TCR-042` | Conformance obligation for `THR-042`: Discriminatory predicate or profile selection | [definition](../security/threat-matrix.md) |
| <a id="tcr-043"></a>`TCR-043` | Conformance obligation for `THR-043`: Risk acceptance laundering | [definition](../security/threat-matrix.md) |
| <a id="tcr-044"></a>`TCR-044` | Conformance obligation for `THR-044`: Metric gaming or observability suppression | [definition](../security/threat-matrix.md) |
| <a id="tcr-045"></a>`TCR-045` | Conformance obligation for `THR-045`: Affected-party harm remains invisible | [definition](../security/threat-matrix.md) |

## Harm

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="hrm-aut"></a>`HRM-AUT` | autonomy and coercion | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-eco"></a>`HRM-ECO` | economic and service loss | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-exc"></a>`HRM-EXC` | exclusion and denial | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-gov"></a>`HRM-GOV` | governance and legitimacy | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-imp"></a>`HRM-IMP` | impersonation and misuse | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-prv"></a>`HRM-PRV` | privacy and surveillance | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-red"></a>`HRM-RED` | redress failure | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-rep"></a>`HRM-REP` | reputational harm | [definition](../security/harm-taxonomy.md) |
| <a id="hrm-sys"></a>`HRM-SYS` | systemic concentration | [definition](../security/harm-taxonomy.md) |

## Control

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="ctl-agl"></a>`CTL-AGL` | negotiated algorithm agility with downgrade prevention | [definition](../security/control-catalog.md) |
| <a id="ctl-cmp"></a>`CTL-CMP` | composition and reconstruction assessment | [definition](../security/control-catalog.md) |
| <a id="ctl-ctx"></a>`CTL-CTX` | governed context and epoch derivation | [definition](../security/control-catalog.md) |
| <a id="ctl-fbk"></a>`CTL-FBK` | explicit fallback and downgrade policy | [definition](../security/control-catalog.md) |
| <a id="ctl-gov"></a>`CTL-GOV` | accreditation, policy and status authority separation | [definition](../security/control-catalog.md) |
| <a id="ctl-hum"></a>`CTL-HUM` | human-legible context and assurance disclosure | [definition](../security/control-catalog.md) |
| <a id="ctl-lcm"></a>`CTL-LCM` | cryptoperiod, rotation and migration controls | [definition](../security/control-catalog.md) |
| <a id="ctl-med"></a>`CTL-MED` | mediated-prover isolation and non-retention | [definition](../security/control-catalog.md) |
| <a id="ctl-obs"></a>`CTL-OBS` | observable-event minimization | [definition](../security/control-catalog.md) |
| <a id="ctl-red"></a>`CTL-RED` | decision evidence, contest and correction | [definition](../security/control-catalog.md) |
| <a id="ctl-sch"></a>`CTL-SCH` | field-level schema minimization and correlation review | [definition](../security/control-catalog.md) |
| <a id="ctl-trn"></a>`CTL-TRN` | canonical domain-separated transcript binding | [definition](../security/control-catalog.md) |

## Guardrail

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="zgr-01"></a>`ZGR-01` | Proof profile integrity | [definition](../security/security-guardrails.md) |
| <a id="zgr-02"></a>`ZGR-02` | Transcript and domain separation | [definition](../security/security-guardrails.md) |
| <a id="zgr-03"></a>`ZGR-03` | Context and nullifier governance | [definition](../security/security-guardrails.md) |
| <a id="zgr-04"></a>`ZGR-04` | Correlation and composition assessment | [definition](../security/security-guardrails.md) |
| <a id="zgr-05"></a>`ZGR-05` | Governance-state freshness | [definition](../security/security-guardrails.md) |
| <a id="zgr-06"></a>`ZGR-06` | Mediated-proving isolation | [definition](../security/security-guardrails.md) |
| <a id="zgr-07"></a>`ZGR-07` | Delegated-agent authority | [definition](../security/security-guardrails.md) |
| <a id="zgr-08"></a>`ZGR-08` | Fallback disclosure protection | [definition](../security/security-guardrails.md) |
| <a id="zgr-09"></a>`ZGR-09` | Redress and correction | [definition](../security/security-guardrails.md) |
| <a id="zgr-10"></a>`ZGR-10` | Algorithm and migration agility | [definition](../security/security-guardrails.md) |
| <a id="zgr-11"></a>`ZGR-11` | Operational evidence readiness | [definition](../security/security-guardrails.md) |
| <a id="zgr-12"></a>`ZGR-12` | Accessibility equivalence | [definition](../security/security-guardrails.md) |
| <a id="zgr-13"></a>`ZGR-13` | Risk acceptance integrity | [definition](../security/security-guardrails.md) |
| <a id="zgr-14"></a>`ZGR-14` | Monitoring privacy boundary | [definition](../security/security-guardrails.md) |

## Assurance test

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="zat-01"></a>`ZAT-01` | forged or malformed proofs and unapproved parameters are rejected | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-02"></a>`ZAT-02` | replay and cross-domain substitution are rejected | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-03"></a>`ZAT-03` | context and epoch changes require authorised, versioned decisions | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-04"></a>`ZAT-04` | combined disclosures remain within the approved privacy claim | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-05"></a>`ZAT-05` | stale state is rejected or bounded degraded mode is invoked | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-06"></a>`ZAT-06` | mediator cannot retain or expose witness material outside the approved boundary | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-07"></a>`ZAT-07` | expired, revoked, wrong-audience and out-of-scope delegation fails | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-08"></a>`ZAT-08` | fallback is explicit and does not silently increase disclosure | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-09"></a>`ZAT-09` | a contested decision can be evidenced, reviewed and corrected | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-10"></a>`ZAT-10` | downgrade fails and migration rollback follows authorised state | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-11"></a>`ZAT-11` | incident declaration, containment and restoration authority is exercised in a tabletop | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-12"></a>`ZAT-12` | supported accessible paths provide materially equivalent privacy and assurance | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-13"></a>`ZAT-13` | prohibited, expired or insufficiently authorised acceptance is rejected | [definition](../conformance/security-assurance-tests.md) |
| <a id="zat-14"></a>`ZAT-14` | metric data flow satisfies minimisation and retention constraints | [definition](../conformance/security-assurance-tests.md) |

## Implementation guidance

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="ig-001"></a>`IG-001` | bind every proof to a canonical request transcript | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-002"></a>`IG-002` | distinguish holder binding from delegated authority | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-003"></a>`IG-003` | qualify privacy claims by adversary, context and horizon | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-004"></a>`IG-004` | record policy, registry and status versions used in a decision | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-005"></a>`IG-005` | reject replay, context mismatch and silent downgrade | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-006"></a>`IG-006` | make lifecycle and recovery behavior deterministic | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-007"></a>`IG-007` | document alternative paths and assurance differences | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="ig-008"></a>`IG-008` | package conformance evidence reproducibly | [definition](../appendices/REQUIREMENT-INDEX.md) |

## Security requirement

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="sec-001"></a>`SEC-001` | Every material predicate has linked assurance and disclosure boundary records. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-002"></a>`SEC-002` | Every material claim states against whom, for how long and alongside what it applies. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-003"></a>`SEC-003` | Applicable canonical threats map to controls, owners, tests and residual-risk decisions. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-004"></a>`SEC-004` | Attestation fields receive individual and combination correlation analysis. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-005"></a>`SEC-005` | Enrolment roots, nullifiers and privacy claims have bounded temporal controls. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-006"></a>`SEC-006` | Mediated proving is explicit, isolated, non-retaining and auditable. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-007"></a>`SEC-007` | Negotiation and migration prevent unauthorized downgrade. | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="sec-008"></a>`SEC-008` | Context definitions identify collusion targets and are human-legible. | [definition](../appendices/REQUIREMENT-INDEX.md) |

## Interoperability requirement

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="zkp-cer-01"></a>`ZKP-CER-01` | ceremony reference is minimised and not a default global correlation handle | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-cer-02"></a>`ZKP-CER-02` | proof/external evidence validity is evaluated independently of ceremony completion | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-cer-03"></a>`ZKP-CER-03` | proof, ceremony, credential/status and authority evidence remain distinguishable | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-link-01"></a>`ZKP-LINK-01` | relationship-dependent proofs use explicit relationship evidence, never co-possession inference | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-link-02"></a>`ZKP-LINK-02` | linkage evidence identifies provenance, authority, relationship semantics and lifecycle | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-link-03"></a>`ZKP-LINK-03` | linkage mechanisms are assessed against privacy class and context correlation boundaries | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-link-04"></a>`ZKP-LINK-04` | unresolved or unverifiable required linkage fails closed | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-task-01"></a>`ZKP-TASK-01` | proof is bound to exact task, audience, challenge, statement and context | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-task-02"></a>`ZKP-TASK-02` | task/ceremony participation never substitutes for delegated authority | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-task-03"></a>`ZKP-TASK-03` | applicable policy/profile version is bound or unambiguously referenced | [definition](../appendices/REQUIREMENT-INDEX.md) |
| <a id="zkp-task-04"></a>`ZKP-TASK-04` | task mismatch/replay/confused-deputy attempts fail closed | [definition](../appendices/REQUIREMENT-INDEX.md) |

## Architecture decision

| ID | Conceptual meaning | Authoritative source |
|---|---|---|
| <a id="adr-001"></a>`ADR-001` | Holder binding is not agent delegation | [definition](../adr/ADR-001-holder-binding-not-delegation.md) |
| <a id="adr-002"></a>`ADR-002` | Personhood is distinct from civil identity | [definition](../adr/ADR-002-personhood-not-identity.md) |
| <a id="adr-003"></a>`ADR-003` | Nullifiers provide scoped reuse detection | [definition](../adr/ADR-003-scoped-nullifiers.md) |
| <a id="adr-004"></a>`ADR-004` | Assurance is governance-backed | [definition](../adr/ADR-004-assurance-governance.md) |
| <a id="adr-005"></a>`ADR-005` | Issuer concealment is profile-specific | [definition](../adr/ADR-005-issuer-concealment-profile-specific.md) |
| <a id="adr-006"></a>`ADR-006` | Dual assurance and disclosure boundaries | [definition](../adr/ADR-006-dual-assurance-disclosure-boundaries.md) |
| <a id="adr-007"></a>`ADR-007` | Attestation schema sets both boundaries | [definition](../adr/ADR-007-attestation-schema-sets-both-boundaries.md) |
| <a id="adr-008"></a>`ADR-008` | Three-part claim parameterization | [definition](../adr/ADR-008-claim-parameterization.md) |
| <a id="adr-009"></a>`ADR-009` | Cryptoperiod and assurance horizon | [definition](../adr/ADR-009-cryptoperiod-assurance-horizon.md) |
| <a id="adr-010"></a>`ADR-010` | Mediated proving non-retention | [definition](../adr/ADR-010-mediated-proving-non-retention.md) |
| <a id="adr-011"></a>`ADR-011` | Canonical threat, harm and control model | [definition](../adr/ADR-011-threat-harm-control-model.md) |
| <a id="adr-012"></a>`ADR-012` | Explicit credential linkage evidence | [definition](../adr/ADR-012-explicit-credential-linkage-evidence.md) |
| <a id="adr-013"></a>`ADR-013` | Task context is not authority | [definition](../adr/ADR-013-task-context-not-authority.md) |
