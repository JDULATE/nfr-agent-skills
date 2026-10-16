# Project handoff package

This is an illustrative sequential coordinator fixture, not a distributed transfer protocol.
All values and proposed responsibility policies are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled handoff record

| Field | Fixture value |
| --- | --- |
| Unit | project-elm, title North |
| Source owner | team-fern, active responsibility |
| Recipient | team-moss, permitted by the supplied handoff policy |
| Project content | task-ash, text Review plan, assignee user-fir |
| Required asset | attachment-leaf, text plan-note, linked from task-ash |
| Recipient mapping | user-fir's assigned role -> approved recipient user-ivy |
| Canonical values | text unchanged; no numeric or unit conversion |
| Initial recipient state | empty staging, no active project assignment |
| Transfer mode | responsibility handoff; source becomes read-only archive after acceptance |
| Coordinator | single synthetic assignment ledger orders finalization |
| Acceptance | recipient can open project/task/asset and confirms the mapped assignee role |
| Failure policy | no acceptance, source responsibility unchanged |
| Carry | staged content and acceptance receipt remain identifiable by project-elm |

The mapping is an approved fixture responsibility assignment, not a claim that
user-fir and user-ivy are the same person.

## Failing package before remediation

The original export includes project-elm and task-ash but only the source handle
attachment-leaf. It omits the asset content and recipient mapping.
The recipient cannot open the linked plan-note, and no recipient assignee is resolved.
A successful archive write does not satisfy the filled acceptance predicate.

## Remediation and recipient result

Include attachment-leaf with content plan-note and the confirmed mapping record.
Stage the package without activating recipient responsibility.
The recipient inspection yields:
```text
project = project-elm, title North
task = task-ash, text Review plan
assignee_role = user-ivy under approved mapping
linked_asset = attachment-leaf, content plan-note
staging = usable, not yet active owner
```

The recipient emits accepted(project-elm, task-ash, attachment-leaf, mapping-confirmed).
The synthetic coordinator then records team-moss as active owner and team-fern as
read-only archive under the supplied policy.

This sequential ledger is the fixture's authority boundary, not evidence of an
atomic ownership protocol across independently failing services.

## Missing acceptance and mapping probes

Withhold the receipt: team-fern remains responsible and team-moss remains staged.
Remove the mapping: staging returns unmapped-assignee and cannot emit acceptance.
Remove the asset: staging returns unresolved-attachment and cannot emit acceptance.

If final disposition fails after acceptance, report pending disposition rather
than a fully completed handoff. Do not infer a receipt from a successful export.

## Requirement example and limits

The project handoff shall preserve the declared content and references in the
recipient context and apply source responsibility release only under the confirmed
acceptance and disposition policy.

This fixture does not verify real permissions, personal-data sharing authority,
network transport, recipient software compatibility, or crash-consistent distributed
assignment. Those remain explicit project decisions and verification obligations.
