# Adopting a local task-event vocabulary

All names below belong to a synthetic repository.
This is a proposed local convention, not an external standard.
Treat adoption criteria as illustrative defaults; confirm with the user/stakeholder.

## Filled selection record

| Input | Value |
| --- | --- |
| Candidate A | {event_name: "task.begin", job: "task-cedar"} |
| Candidate B | {kind: "started", task: "task-cedar"} |
| Required concepts | event is task execution started; identity is task-cedar |
| Selected vocabulary | {kind: "task_started", task_key: "task-cedar"} |
| Selection reason | separate event meaning from task identity with explicit local field definitions |
| Decision authority | event-contract maintainer role; approval proposed |
| Adoption scope | runner producer and scheduler producer |
| Legacy consumer | board expects event_name=task.begin and job=task-cedar |
| Initial producer states | runner uses A; scheduler uses B |
| Consumer state | board started_tasks=[] |
| Exception | archive exporter remains on A; owned by archive maintainer role |
| Exception migration condition | archive reader accepts the canonical envelope in a checked fixture |
| Collision rule | task_key denotes an execution identity, not a reusable job definition |

## Before: inconsistent event representation

The board receives candidate A from runner and records:
`started_tasks=[task-cedar]`.

Reset board state to [].
The board receives candidate B directly and returns `unrecognized-event`;
started_tasks remains [].
This demonstrates the filled consumer's response to the two local shapes.
It does not establish that candidate A is universally better than candidate B.

## Remediation and after outputs

Propose the selected vocabulary with both field meanings documented.
Change the runner and scheduler emission boundaries to that vocabulary.
Use the declared board translation while the legacy board remains unchanged.

| Producer | Emitted output after change | Board-bound translated output | Board result from empty state |
| --- | --- | --- | --- |
| runner | {kind: task_started, task_key: task-cedar} | {event_name: task.begin, job: task-cedar} | started_tasks=[task-cedar] |
| scheduler | {kind: task_started, task_key: task-cedar} | {event_name: task.begin, job: task-cedar} | started_tasks=[task-cedar] |

These are separate fixture runs with a reset board, not duplicate-delivery tests.
Both in-scope producers now have demonstrated canonical output.
Archive exporter remains explicitly outside the completed migration claim.

## Failing concept collision

Supply `{kind: task_started, job_definition: template-oak}` with no task_key.
The canonical boundary refuses missing-task-identity.
Board state remains [].
Do not relabel template-oak as task-cedar: they denote different concepts.

## Approval boundary and reporting

The maintainer's decision state remains proposed in this fixture.
Report implemented candidate adoption for runner and scheduler and the explicit
archive exception; do not call it approved across the organization.
The mapping supports the named legacy board outcome only.

This example demonstrates event vocabulary selection, naming, and scoped adoption.
It does not compare every candidate convention, prove organizational consensus,
or establish conformance to any external source.
