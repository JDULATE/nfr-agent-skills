# Worked example: from direct processing to staged processing

Assume a fictional direct arrangement A accepts `step=run`. The target staged
arrangement B uses `step=validate`, then `step=dispatch`, then `done`. Both promise
the same accepted parcel-task result, but A cannot interpret B's intermediate steps.
The example specifies these state meanings; no real queue protocol is asserted.

Illustrative loss bound only: 0 unexplained lost accepted task identities;
confirm with the user/stakeholder before adopting the fixture's ownership rules.
Propose: "Moving `{A_to_B}` shall retain `{accepted_ids_and_results}` through
`{admission_and_checkpoint_rule}`, verified by `{interrupted_carried_state_rehearsal}`
with `{confirmed_interruption_and_duplicate_policy}` kept separate."

| Checkpoint | Concrete retained state | Required observation |
| --- | --- | --- |
| Start | `amber`: A/running/run; `violet`: A/queued/run | Both accepted identities recorded |
| Target B ready | Same A owners; B has no accepted tasks | Readiness has not transferred any work |
| Violet transferred and acknowledged under fixture policy | `amber`: A/running/run; `violet`: B/queued/validate | A no longer claims violet; target record actually owns it |
| Application interrupted | Same retained owners and step meanings | No fixture reset or disappearance of violet |
| Resume | A finishes amber; B advances violet validate -> dispatch -> done | Each result matches its retained task contract |
| Cutover complete | New `slate` admitted by B and finishes its staged steps | Target is processing real work; prior identities reconciled |

Inject a counterexample where A deletes violet before B records ownership. The
missing identity violates the proposed loss bound even though the target file is
valid. Check repeated effects separately under the stakeholder's duplicate policy.

Try restoring selector A while violet is at `validate`: A's declared handler only
understands `run`. That file restore is not state-compatible reversal. Rehearse
forward completion under B or an explicitly approved conversion; do not assert
that either is supported without implementation evidence.

Carry identity, arrangement, phase, and result records into each checkpoint.
Report actual interruption and completion evidence only after executing the target
system's rehearsal. This example supplies states and oracles, not empirical proof
of ownership guarantees or availability during configuration changes.
