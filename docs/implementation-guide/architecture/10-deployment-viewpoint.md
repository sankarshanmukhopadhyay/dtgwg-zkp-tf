# Deployment viewpoint

Implementations may deploy proof generation locally, remotely or as a hybrid, but trust boundaries and retained data must remain explicit.

| Zone | Typical components | Principal controls |
|---|---|---|
| Holder device | wallet, secure storage, local proof runtime | consent, key protection, request display |
| Agent runtime | delegated task logic, agent key | scope enforcement and step-up |
| Issuer environment | enrollment, attestation and status services | separation of duties and audit |
| Verifier environment | request, verification and policy engine | policy versioning and decision receipts |
| Registry infrastructure | publication, status and recognition records | signed state, time semantics and availability |
| Assurance operations | monitoring, incident response and redress | evidence preservation and accountable decisions |

Remote proof services create an additional exposure surface because they may observe credentials, requests or timing. Their role, authority and data retention must be documented. Cache entries require source, version, effective time and expiry metadata.
