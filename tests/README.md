# Repository validation

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Install the pinned direct dependency from requirements.txt in an isolated environment,
then run `python tests/validate.py` from the repository root. Python 3.11+ is expected.
The validator checks local Markdown paths/heading anchors, seven schema definitions,
all example records, record references and cycles, source hashes, and selected invalid
records. It exits nonzero on failures. External URLs and Mermaid rendering are not
checked. Passing does not constitute an architecture experiment, security audit,
source verification, or evidence of government readiness.
