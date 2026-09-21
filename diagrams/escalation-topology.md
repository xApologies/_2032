# Escalation topology

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Conceptual design; arrows do not grant authority or imply deployment.

```mermaid
flowchart TD
    Intake[Question and deadline] --> Owner[Responsible domain human owner]
    Owner --> Complete{Evidence and authority sufficient?}
    Complete -->|Yes within scope| DomainAction[Authorized domain disposition]
    Complete -->|Missing evidence| Return[Return with specific evidence request]
    Return --> Owner
    Complete -->|Cross-domain conflict| Coordinator[Human coordinator: preserve dissent]
    Coordinator --> Need{Presidential authority required?}
    Need -->|No| Owner
    Need -->|Yes or unresolved| Surface[Decision surface with authority question]
    Surface --> Human[Human review and scoped decision]
    Owner -->|Acknowledgment overdue| Coordinator
```
