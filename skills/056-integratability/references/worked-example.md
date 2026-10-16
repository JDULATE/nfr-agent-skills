# Worker binding assembly

All components and paths below are synthetic.
The proposed glue-only acceptance boundary is illustrative; confirm with the
user/stakeholder before using it for a project.

## Inputs and supplied state

| Field | Filled value |
| --- | --- |
| Components | queue stub and worker stub |
| Worker interface | make_worker(inbox); poll returns the next queued payload |
| Transport interface | make_transport(address); accepts fixture address queue-local |
| Host config | jobs_address = queue-local |
| Initial queue | [ticket-cedar] |
| Initial worker state | processed = [] |
| Supplied artifacts | queue stub, worker constructor, host config loader |
| Missing glue | composition root uses inbox_address instead of jobs_address |
| Allowed edits | app/compose.py and tests/test_compose.py |
| Integration owner | service assembly maintainer role |
| Connected result | processed = [ticket-cedar], queue empty |
| Effort procedure | record performed tasks and changed paths; no time budget asserted |

## Before: assembly failure

The composition code reads `host_config["inbox_address"]`.
The supplied host config contains only `jobs_address`.
Construction returns `missing:inbox_address`; worker never starts.
Queue remains [ticket-cedar], processed remains [].

Running the worker with a manually injected transport succeeds, but that bypasses
the failed composition and does not accept the integrated solution.

## Change and work ledger

| Task | Supplied dependency | Edited artifact | Owner | Result |
| --- | --- | --- | --- | --- |
| Inspect constructor and loader | worker signature; host config fixture | none | assembly maintainer | name mismatch identified |
| Add explicit mapping and prerequisite check | make_transport; make_worker | app/compose.py | assembly maintainer | jobs_address bound to inbox |
| Exercise clean construction and refusal | queue stub | tests/test_compose.py | assembly maintainer | both paths observed |

No worker or queue internals changed.
No external registration or waiting dependency occurred in this fixture.
Do not convert this task ledger into an unmeasured speed claim.

## After: connected path

Reset queue to [ticket-cedar] and processed to [].
Construct through the corrected composition root with jobs_address=queue-local.
The root creates a queue-local transport, passes it as inbox, and calls poll.

```text
construction = worker-ready
poll result = ticket-cedar
queue = []
processed = [ticket-cedar]
edited paths = [app/compose.py, tests/test_compose.py]
```

The result stays within the proposed glue surface.

## Missing-prerequisite negative

Reset queue to [ticket-cedar], processed to [], and config to {}.
Composition returns `MissingPrerequisite("jobs_address")`.
No transport or worker is created; both state values remain unchanged.
The output names the actual supplied configuration contract.

## Acceptance and limitation

Accept the named connection only after the stakeholder confirms the glue boundary.
The evidence supports reconstruction from the supplied fixture state.
It does not measure calendar effort, real endpoint registration, error-recovery
behavior, or the semantics of a richer message format.
