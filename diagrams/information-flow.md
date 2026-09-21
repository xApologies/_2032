# Information flow

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Conceptual design; arrows do not grant authority or imply deployment.

```mermaid
flowchart TD
    Nation[Nation and government systems] --> Domains[Executive departments and domain experts]
    Domains --> Stack[President Stack]
    Stack --> Layers[Astraeus mapping plus Vera provenance and audit]
    Layers --> Surface[Presidential decision surface]
    Surface --> Human[Human presidential decision]
    Human --> Gate{Authorization verified?}
    Gate -->|Yes| Implementation[Authorized implementation]
    Gate -->|No| Review[Return for human review]
    Implementation --> Telemetry[Outcome telemetry]
    Telemetry --> Feedback[Feedback and model update]
    Feedback --> Domains
```
