# Replacing a settings backend

This local backend model is synthetic.
Its preservation defaults are illustrative; confirm with the user/stakeholder.

## Filled obligations and state

| Field | Value |
| --- | --- |
| Caller interface | get(key) returns Present(value), Missing, or BackendFault(reason) |
| Old provider | dictionary keyed by text |
| Old initial state | {"theme": "dark"} |
| New provider | lookup(tuple_key) returns found, absent, or fault |
| New persisted state after mapping | {("setting", "theme"): "dark"} |
| Key mapping | text key k becomes ("setting", k) |
| Caller hit input | theme |
| Caller miss input | language |
| Fault fixture | new provider configured to return fault:offline |
| Protected outcomes | Present(dark), Missing, BackendFault(offline), respectively |
| Retirement condition | caller runs with no old provider binding |
| New write scope | disabled in this read-only substitution fixture |
| Owner | settings-service maintainer role |

## Before remediation

The initial replacement adapter forwards lookup's absent outcome
directly to the caller.
With input language, it returns provider-level absent rather than caller-level Missing.
The hit theme still yields Present(dark).
This is a failed preserved contract despite a successful positive example.

An alternative broken adapter converts every non-found outcome to Missing.
That makes the offline fault look like an absent setting and also fails.

## Remediation

Convert the text key and translate only the explicit absent outcome.
Leave real provider faults distinct.
The state converter writes ("setting", "theme") from the old theme entry and
checks that no old keys map to the same destination.

## After: old dependency absent

Remove the old provider binding from the composition.
The corrected adapter produces:

| Input and provider mode | Caller output | Persisted state afterward |
| --- | --- | --- |
| theme, normal | Present(dark) | {("setting", "theme"): "dark"} |
| language, normal | Missing | {("setting", "theme"): "dark"} |
| theme, fault:offline | BackendFault(offline) | {("setting", "theme"): "dark"} |

The caller uses only the replacement; there is no fallback binding.

## State-mapping negative case

A broken migration writes ("legacy", "theme") instead.
Record counts still match, but get(theme) returns Missing.
The existing-key read catches the incomplete substitution.
Restore the declared mapping and repeat the retirement run.

## Reversal boundary

Because this fixture disables writes, its old dictionary snapshot can supply
the old read path after stopping replacement reads.
That observation is confined to the unchanged snapshot.
No post-cutover write format or reverse conversion has been exercised.

Report the named read obligations as preserved under old-dependency removal.
Leave write substitution, concurrent cutover, and rollback after new writes
unverified rather than generalizing from this read-only fixture.
