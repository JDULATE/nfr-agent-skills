# Protected report approval state

This synthetic policy allows editors to revise a draft's body but not write its
approval field. A designated review transition can approve the current version.
These are scenario assumptions, not an actual authorization or concurrency implementation.

## Concrete state and attempted alterations

Report `report-slate` is approved at `version-mint`. An editor holds an old draft
`version-amber`. Imported body content also arrives with a caller-supplied reference;
the actual trusted-origin source must be independently confirmed.

| Input/attempt | Expected alteration decision | Carried state |
| --- | --- | --- |
| Editor sets approval directly | Reject prohibited transition | Existing approval unchanged |
| Old version-amber overwrites version-mint | Apply confirmed stale/conflict rule | No silent replacement of protected newer state |
| Content and untrusted reference modified together | Matching pair does not establish trusted origin | Independent expectation still needed |
| Authorized correction under current policy | Accept permitted change | Current approved transition/result recorded |
| Rejected import after partial work | Inspect actual final state | Error alone is not no-alteration evidence |

## Proposed gate

Illustrative example; confirm with the user/stakeholder:
Allow 0 accepted prohibited alterations in the agreed writer, stale-version,
and untrusted-import cases. Ask for legitimate correction, origin, freshness,
and conflict behavior before accepting the proposed gate.

## Verification boundary

Trace the editor, import, and administrative write paths to their final effect.
Compare before/after protected state, actual version decision, and trust source.
Even intact, origin-checked contents could contain a real-world factual error;
that separate Accuracy question is not established by this integrity result.
No actual report mutation, provenance check, or version-race trial occurred here.
