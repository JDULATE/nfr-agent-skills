# Worked example: admit an export worker

Suppose a fictional export service already has a worker type and placement rules.
Its operator asks to add a worker to the current installation without replacing
the service. The scenario supplies no measured performance or platform guarantee.

## Trace the addition

Read worker admission code, queue assignment, resource credentials, placement
configuration, and the operations guide. Ask which export class must use the added
worker and whether existing exports may pause during reassignment.

Propose: "From `{documented_installation}`, adding `{supported_export_worker}`
shall make `{confirmed_usable_export_capacity}` available under `{placement_rules}`,
with `{accepted_existing_export_interruption}`, evidenced by actual assigned and
completed representative work plus `{failed_admission_cleanup_record}`."

Illustrative scope only: add 1 supported worker; confirm with the user/stakeholder.
Do not infer a proportional throughput gain or a universal worker limit from this scope.

## Challenge the registration-only result

Assume the new worker appears in the registry but the assignment rule still selects
only the previous worker group. That is an admitted resource without demonstrated
usable added capacity. Change only the accepted placement rule and check that the
new worker can receive and finish the intended export class.

For example, name the synthetic new worker `export-blue` and the test job
`fixture-export`. Suppose inspection shows the job selects group `legacy-export`
while the added worker advertises only `extra-export`. Record that placement
mismatch before proposing another worker. After the approved eligibility change,
trace `fixture-export` to `export-blue` and inspect its completed result, not just
the registry entry. These group labels describe the example, not a scheduler API.

| Rehearsal | Evidence |
| --- | --- |
| Valid worker admitted | Registration and credentials match the supported worker contract |
| Representative export assigned | Placement trace and completed result on the added worker |
| Admission interrupted | Clear checkpoint and ownership of any assigned export |
| Existing exports continue | Their results and interruption observations during addition |
| Shared controller reaches its configured ceiling | The actual installation boundary and unresolved expansion choice |

Return the observed capacity delta only after running the rehearsal on the target
installation. If a separate workload sweep is needed to determine scaling, state
that need rather than presenting the resource-addition demonstration as that sweep.
