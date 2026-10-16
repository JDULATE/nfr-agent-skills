# Reusing an import checker from web and CLI

This synthetic repository fixture uses illustrative reuse boundaries;
confirm with the user/stakeholder before adopting them.

## Filled reuse record

| Input | Value |
| --- | --- |
| Existing artifact | import/check_rows revision amber |
| Original context | web import preview |
| New context | CLI import preflight |
| Row input | [{id:cedar, name:""}, {id:maple, name:"Maple"}] |
| Shared rule | each empty name yields MissingName(id); nonempty names yield no finding |
| Expected common findings | [MissingName(cedar)] |
| Original web envelope | {findings:[{kind:missing-name, id:cedar}]} |
| CLI output | missing-name:cedar |
| Initial persistent state | none; checking is read-only |
| Old ambient dependency | current_web_request.rows |
| Allowed edits | shared signature plus web and CLI adapters; no copied checker |
| Policy scope | existing authorized preview/preflight callers supplied by fixture |
| Owner | import-tool maintainer role |

## Before: reuse blocked

The old artifact obtains rows from current_web_request.
Web preview supplies that context and returns the expected web envelope.
CLI preflight has no web request and fails with MissingWebContext.
It produces no common findings and no persistent mutation.

A CLI copy of the branches could return missing-name:cedar, but that would create
another artifact instead of reusing import/check_rows.

## Remediation and adaptation ledger

Change the shared checker to accept rows directly.
Move web row decoding and presentation into the web adapter.
Make the CLI adapter pass its decoded file rows to the same checker.

| Change | Artifact | Result |
| --- | --- | --- |
| Remove ambient row lookup | import/check_rows revision birch | check_rows(rows) |
| Supply rows and web presentation | web/preview | existing envelope preserved |
| Supply file rows and CLI presentation | cli/preflight | no web setup required |

This is a declared edit boundary, not a measured effort estimate.

## After consumer outputs

For the filled row input:
shared findings=[MissingName(cedar)];
web output={findings:[{kind:missing-name, id:cedar}]};
CLI output=missing-name:cedar.
Both traces identify import/check_rows revision birch.
No web context is constructed for the CLI and no persistent state changes.

For rows=[{id:maple, name:"Maple"}]:
shared findings=[]; web output={findings:[]}; CLI output=ok.
The existing valid-row behavior remains.

## Failing controls

Reconnect CLI preflight to copied cli/check_rows_copy.
Its output still matches, but artifact identity inspection fails shared reuse.

Make revision birch read current_web_request again.
CLI preflight fails MissingWebContext, detecting the reintroduced dependency.

## Limits

The fixture establishes shared validation across the named adapters only.
It does not validate a real framework integration, authorization implementation,
packaging system, or adaptation cost for additional consumers.
