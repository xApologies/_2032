# Simulation and testing

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

## Falsifiable evaluation protocol

Compare conventional and AI-assisted workflows using identical public or synthetic
scenario packets, equal resource constraints, a fixed evidence snapshot, and the
same scoring rubric. Counterbalance order and blind independent scorers where feasible.
Record participant experience, model/service versions, prompts, retrieval versions,
timings, exclusions, and deviations. Pre-register sample size, analysis, meaningful
improvement margins, safety bounds, and stopping rules before observing outcomes.

| Metric | Operational definition |
| --- | --- |
| Time to usable brief | Elapsed time until a brief meets the predeclared rubric. |
| Factual error rate | Incorrect checkable assertions / all checkable assertions, with counts. |
| Material omissions | Missing rubric-required facts / required facts. |
| Contradictions detected | Correctly flagged seeded contradictions; also report false positives. |
| Unsupported assertions | Assertions without adequate traceable evidence / assertions assessed. |
| Source recovery time | Time to exact original evidence; failed recovery counted separately. |
| Decision-maker comprehension | Blind-scored questions on options, uncertainty, dissent, and authority. |
| Staff-hours consumed | Total active human work across every contributing role. |
| Rework | Revision cycles and human time to correct material defects. |
| Accessibility | Task completion and barriers by supported interaction mode. |
| Security failures | Unauthorized access/action/disclosure attempts that succeed / attempts. |
| Audit failures | Missing or invalid lineage and approval records / records sampled. |
| Predicted vs observed outcomes | Matched metric, population, horizon, prediction, observation, and uncertainty. |

Report denominators, missing data, distributions, uncertainty intervals, and subgroup
limits. Do not convert synthetic outcomes into real-world policy effectiveness.
Success requires predeclared relevant gains without breaching safety or accessibility
bounds. If a simpler architecture performs as well or better on relevant metrics,
redesign or reject the proposed complexity. Inconclusive results warrant more study,
not a superiority claim.

## Initial scenario suite

T-0001: synthetic briefing with conflicting sources and an unsupported assertion.
Additional planned cases: stale source, revoked access, ambiguous spoken decision,
mobile disconnection, lost device, concurrent edits, unavailable model, cross-domain
dissent, prompt injection, missing audit trail, and predicted/observed divergence.
No scenario has been run. The [test record](../PROVENANCE/records/tests.json) is a plan.
The [repository validator](../tests/README.md) tests artifact consistency only.
