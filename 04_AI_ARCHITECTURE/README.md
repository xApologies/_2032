# AI architecture

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

See [Astraeus](ASTRAEUS.md) and [Vera](VERA.md). These are separable support functions.
Neither approves government action or independently certifies the other's output.

Proposed contract: versioned sources enter retrieval; Astraeus emits claims, explicit
inferences, alternatives, assumptions, and dependencies; Vera returns lineage gaps,
chronology conflicts, uncertainty, and audit findings. Humans resolve material
disagreements. Preserve model/service versions, input references, output artifacts,
review events, and the applicable authorization context.

Treat retrieved documents as evidence, not executable instructions. Isolate retrieval,
model services, audit storage, and authorized action channels. Service failure must
leave source access and a conventional human workflow available. Test common-mode
model errors, prompt injection, invented citations, source deletion, and model drift.
