# Machine-readable record contracts

Epistemic status: **DESIGN HYPOTHESIS**. Bootstrap date: 2026-09-21.
Source: SRC-0001; generated design elaborations are proposals, not adopted decisions.

Seven JSON Schema draft 2020-12 contracts validate individual records; each matching
PROVENANCE/records file is an array of records. Additional fields are rejected to
expose misspellings. IDs, dates, epistemic status, summary, and source references are
mandatory. Origin timestamps may be null when unknown; receipt dates are separate.

| Contract | Records |
| --- | --- |
| [claims](claims.schema.json) | [examples](../PROVENANCE/records/claims.json) |
| [sources](sources.schema.json) | [examples](../PROVENANCE/records/sources.json) |
| [decisions](decisions.schema.json) | [examples](../PROVENANCE/records/decisions.json) |
| [assumptions](assumptions.schema.json) | [examples](../PROVENANCE/records/assumptions.json) |
| [uncertainties](uncertainties.schema.json) | [examples](../PROVENANCE/records/uncertainties.json) |
| [workstreams](workstreams.schema.json) | [examples](../PROVENANCE/records/workstreams.json) |
| [tests](tests.schema.json) | [examples](../PROVENANCE/records/tests.json) |

Claims contain an explicit inference or null for direct evidence, supporting claim IDs,
and evidence locators. Verified facts require sources, locators, and a verification
record. Sources attribute an actor and locate hashed evidence. Adopted decisions require
an authority and adopted status. Completed tests require results and simulation status.
These constraints check structure, not truth or legitimacy of claimed authority.

The validator additionally checks global ID uniqueness, source and decision references,
acyclic claim/workstream dependencies, local workstream paths, and source hashes.
Artifact versions are preserved by Git; source hashes fix the evidence bytes.
Outcome details are initially prose; richer units, intervals, and run artifacts should
be added only when an evaluation protocol is adopted. Examples are project records
or untested proposals, not manufactured external facts or simulation outcomes.
