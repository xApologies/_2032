# Context continuity

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Conceptual design; arrows do not grant authority or imply deployment.

```mermaid
flowchart LR
    Phone[Phone] <--> Context[Versioned context: decision, sources, draft, questions]
    Room[War Room] <--> Context
    Travel[Air Force One or travel context] <--> Context
    Desktop[Conventional workstation] <--> Context
    Context --> Gate[Destination identity and authorization recheck]
    Gate --> Resume[Resume acknowledged revision]
    Context --> Conflict[Offline or concurrent edits: retain and reconcile]
    Conflict --> Gate
```
