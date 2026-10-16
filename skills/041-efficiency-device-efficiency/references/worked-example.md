# Coalescing repeated decoding within each report

This is a synthetic resource-cost model, not a profile of actual workers.
All numeric fixture values and targets below are illustrative examples;
confirm with the user/stakeholder before using them as a requirement.

## Filled input and acceptance record

- Inputs: report identities R001 through R100, all offered at the start of a
  60-second run to serial worker profile cpu-slate; no arrivals after that cohort.
- Each report reads immutable dictionary revision dict-amber twice and renders
  its own identity plus the value amber. Expected content is exactly Rnnn:amber.
- Resource boundary: worker process CPU, including all decoding/rendering;
  retries, idle CPU allocation, background work and remote work are all absent.
- Existing service constraint: every offered report completes correctly by run end.
  Peak retained state is 32 MiB in each plan; the space allowance is 40 MiB.
- Objective: CPU-seconds per correct report, with an illustrative 10% reduction
  against the direct plan; confirm with the user/stakeholder.
- End-state oracle: completed identity set and exact content; no attempt is
  counted as a correct report merely because it was admitted.

## Before, failed shortcut and remediation

The model charges 0.02 CPU-seconds per dictionary decode and 0.16 per render.
The direct implementation decodes twice per report. The candidate coalesces
those equal reads inside the report and releases the value on report completion.
It has no cross-report persistent cache, fill job, eviction work or stale revision.

~~~text
render_report(identity, dict_revision):
    decoded = decode_once(dict_revision)
    return render(identity, decoded, decoded)
~~~

| Plan | Decode calls | Render calls | CPU-seconds | Correct reports | CPU per report | End state |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Direct | 200 | 100 | 20 | 100 | 0.20 | All expected identities present |
| Drop R081 through R100 | 160 | 80 | 16 | 80 | 0.20 | Named identities dropped; none pending |
| Coalesce within each report | 100 | 100 | 18 | 100 | 0.18 | All expected identities present |

The dropped cohort fails the output obligation, not just the reduction target.
The coalesced plan reaches the illustrative reduction: (20 - 18) / 20 = 10%;
confirm with the user/stakeholder before accepting such a target in a real project.
Completed work uses 20 or 18 seconds of modeled serial CPU and fits the run window;
the failed shortcut finishes early only because the missing identities were dropped.

## Transferred-byte variant

Illustrative wire fixture; confirm with the user/stakeholder:
the approved recipient needs exactly the ordered pairs A:amber and B:amber.
Before, send the literal payloads {"tag":"amber","id":"A"} and
{"tag":"amber","id":"B"}; after, send {"tag":"amber","ids":["A","B"]}.
With one byte per literal character and no framing in this model, sizes are
24 + 24 = 48 bytes before and 31 after, for the same two decoded results.
Thus bytes per result change from 24 to 15.5. The decoder expands the shared
tag to both identities; omitting B instead would fail the exact output oracle.
The fixture has no encoding cost model, so it supports no CPU-saving claim.

## Interpretation boundary

Compare the exact identity/content oracle and the complete CPU event ledger.
The modeled cause is repeated decode work because the supplied costs and call
counts establish it; lower CPU alone would not diagnose it in a real codebase.
No energy, cost, lifecycle result, profiler run or production saving is inferred.
