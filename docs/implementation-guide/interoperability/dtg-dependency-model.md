---
layout: default
title: "DTG Dependency Model"
parent: "DTG Interoperability"
nav_order: 1
---
# DTG dependency model

The ZKP work sits inside a wider governance and protocol system. This model separates what the ZKP layer **consumes**, what it **establishes**, and what remains outside its authority.

| Concern | Authoritative work | ZKP relationship | ZKP may consume | ZKP must not infer |
|---|---|---|---|---|
| Credential semantics | `trustoverip/dtgwg-cred-spec` | upstream semantic dependency | claims, credential status and defined credential relationships | identity equivalence or relationship linkage that the credential model does not evidence |
| Identifier linkage | Credential Spec issue #9 and subsequent resolution | unresolved construction dependency | explicit linkage evidence when defined | that co-possession of P-DID, R-DID or M-DID proves common subject/controller |
| Proof exchange | `trustoverip/dtgwg-trust-tasks-tf` | protocol integration dependency | task identifiers, audience, challenge, constraints and evidence references | that task participation itself authorises the actor |
| Multi-step ceremonies | Trust Ceremonies design work | optional orchestration dependency | ceremony/enactment context needed for transcript binding | that ceremony membership or completion proves authority or artifact validity |
| Delegated agent action | Trust Tasks plus applicable delegation governance | external authority dependency | separately verifiable delegation/mandate evidence | that holder binding, proof possession or successful verification proves delegation |
| Risks and harms | `trustoverip/dtgwg-rahp-tf` | assurance-method dependency | pressure-test method, control-plane disposition and evidence expectations | that RAHP findings alter ZKP normative authority without Task Force action |
| Registry recognition | applicable DTG registry/VTC work | runtime trust-state dependency | issuer/status/recognition evidence required by profile | that cryptographic validity proves current recognition |

## Dependency rule

Every external dependency used by a ZKP profile MUST identify:

1. the external authority that defines the dependent semantic or state;
2. the evidence consumed by the ZKP construction or verifier;
3. the validity and lifecycle assumptions applied to that evidence;
4. any unresolved assumption that could make a proof technically valid but semantically unsafe; and
5. the authority capable of resolving or revoking that dependency.

## Direction of authority

Dependencies flow **into** a ZKP profile as evidence or governed semantics. Verification output flows **out** only as a result about the statement that was actually proved. No dependency edge grants the ZKP repository authority to redefine another specification.

## Portfolio tracking

The register is maintained as a targeted alignment instrument, not as a mirror of the entire DTG portfolio. A repository is added only when a change in that work can alter proof inputs, transcript binding, verifier policy, authority interpretation, privacy properties, or assurance evidence.
