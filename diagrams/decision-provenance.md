# Decision and provenance chain

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Conceptual design; arrows do not grant authority or imply deployment.

```mermaid
flowchart LR
    Claim[Claim with epistemic status] --> Inference[Explicit inference or direct-source link]
    Inference --> Source[Versioned source]
    Source --> Actor[Originating actor or organization]
    Actor --> Time[Origin timestamp or explicit unknown]
    Time --> Evidence[Underlying evidence and exact locator]
    Claim --> Decision[Human decision record: rationale and dissent]
    Decision --> Authorization[Scope and human authorization]
    Authorization --> Outcome[Prediction and observed outcome]
    Outcome --> Revision[Preserved history and model revision]
```
