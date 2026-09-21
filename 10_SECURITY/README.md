# Security

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

## Capability requirements and invariants

| Capability | Invariant and proposed verification |
| --- | --- |
| Authentication | Verify identity at entry and sensitive handoff; test revoked identity. |
| Authorization | Check role, resource, action, and scope; deny unauthorized action. |
| Least privilege | Grant only needed access; test excessive-role and privilege drift. |
| Information separation | Enforce permitted flows across data and service boundaries; test leakage. |
| Provenance and auditing | Record source/action lineage and review events; expose missing or altered records. |
| Records preservation | Apply reviewed retention, correction, and preservation rules; test restoration. |
| Model/service isolation | Separate model inputs, retrieval, audit, and action channels; test injection containment. |
| Human authorization | Require attributable human approval for consequential action; reject AI or ambiguous speech approval. |
| Resilience and continuity | Preserve recoverable state and conventional workflow during outage; test recovery and conflicts. |
| Independent review | Qualified reviewers evaluate threat model and controls before sensitive deployment. |

Access is not authority. No persona, AI, vendor, or individual gains actual U.S.
government clearance from this project. No classified implementation details are
invented here. Public/synthetic prototypes must not ingest classified material.

## Proposed threat and failure model

Include spoofed advisers, malicious source instructions, fabricated citations, replayed
approvals, stale privileges, compromised devices, data exfiltration, audit tampering,
and shared model failure. On uncertain authorization, stop the affected action,
preserve an incident record, and route to a responsible human. Never hide a gap by
claiming a successful audit. Retention, legal obligations, identity systems, recovery
targets, and sensitive deployment boundaries remain unresolved.
