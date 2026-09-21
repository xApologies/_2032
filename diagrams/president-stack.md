# President Stack

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Conceptual design; arrows do not grant authority or imply deployment.

```mermaid
flowchart TD
    Domains[Executive departments and domain experts] --> Stack[President Stack: persistent domain workspaces]
    Stack --> Astraeus[Astraeus: mapping and synthesis]
    Stack --> Vera[Vera: provenance and audit]
    Astraeus <--> Vera
    Astraeus --> Surface[Decision surface: options, dissent, sources]
    Vera --> Surface
    Advisers[Authorized human advisers] <--> Surface
    Surface --> Human[Human decision authority]
```
