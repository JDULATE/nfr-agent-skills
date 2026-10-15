# Worked example: an accepted report is not a finished report

Assume a fictional report system with the following implemented-path contract for
this fixture. API submission stores a queued job, enqueues its identity, and returns
`accepted(job-mint)` after that handoff. A worker writes artifact `artifact-mint`,
then changes the job record to ready. Status readers use the job record, not the
API acknowledgement or artifact existence alone, to decide whether the job is ready.

A compact source outline for the example is:

```text
submit: store(job-mint, queued) -> enqueue(job-mint) -> accepted(job-mint)
worker: consume(job-mint) -> write(artifact-mint) -> store(job-mint, ready)
status: read job record -> queued or ready
```

| Carried checkpoint | Existing state | What cannot yet be concluded |
| --- | --- | --- |
| Submission handoff accepted | Job record queued; work handed to queue | Report is not ready merely from accepted(job-mint) |
| Work lost before worker receives it | Job record still queued; no artifact | There is no demonstrated generation or automatic recovery |
| Artifact written, worker stops before ready write | Artifact exists; job record remains queued | Artifact existence alone does not authorize ready in this model |
| Worker stores ready after writing | Job record ready; artifact-mint exists | Only the declared completion path is modeled, not all fault guarantees |

Propose: "Using `{system_path_material}`, `{maintainer_audience}` shall predict
`{acknowledgement_state_and_completion_outcomes}` under `{cross_boundary_cases}`,
checked against `{writer_reader_and_state_key}` with `{confirmed_answer_rule}`."
Illustrative trial only: 3 causal prediction questions with required answers correct;
confirm with the user/stakeholder before adopting the cases or their scope.

| Question | Source-key answer |
| --- | --- |
| Does the API's accepted response prove the report is ready? | No; it follows queued-job handoff, before worker completion |
| Who establishes ready, and where does the reader look? | The worker updates the job record; status reads that record |
| What if the artifact exists but the worker never wrote ready? | The record remains queued; ready cannot be inferred from the artifact alone |

Carry job identity, record phase, handoff, and artifact existence through each
case. A diagram saying API -> worker -> ready without intermediate state teaches
wrong predictions at the missing-handoff and pre-ready-write checkpoints.
These source rules are hypothetical. Actual transaction, queue, and recovery
semantics need project evidence; no production behavior or audience result is asserted.
