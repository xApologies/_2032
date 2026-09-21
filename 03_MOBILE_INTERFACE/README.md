# Mobile interface

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

## Movement-first continuity

Phone ↔ War Room ↔ Air Force One / travel context ↔ conventional workstation must
resume the same decision ID, brief revision, source pointers, open questions, draft
annotations, and task ownership. Travel is a modeled context, not claimed access
to any actual platform. Mobile-first does not mean mobile-only.

## Proposed handoff protocol

Save a versioned context envelope with timestamp and permitted data labels; authenticate
the destination and re-evaluate authorization before revealing content. Acknowledge
the received revision. Surface stale state and concurrent edits; retain both branches
until a human reconciles them. Never silently overwrite a decision.

Offline mode permits explicitly labeled cached reading and draft capture where
policy permits. It cannot represent a pending action as authorized or completed.
Reconnect reconciles versions, rechecks access, and records the outcome. Lost-device
response revokes sessions and follows the approved retention/recovery policy.

Voice summaries offer source recovery, text alternatives, captions, interruption,
and safe pause/resume. Test handoff latency, source recovery, permission revocation,
network loss, conflicting edits, and comprehension while stationary versus moving.
