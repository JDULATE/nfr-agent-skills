# Removing a modeled coordination ceiling

This is a synthetic capacity model, not observed production throughput.
Every numeric value, target and model result below is illustrative;
confirm with the user/stakeholder before adopting a growth requirement.

## Filled model and acceptance

Run each point for 60 one-second ticks, resetting backlog and result ledger.
The input source offers the stated work count each tick and supports up to
500 items per tick. Identities are unique by tick and sequence.
Each item has a one-unit payload and key A, B, C or D in cyclic order.
All four keys have independent effects; order must be preserved within each key.
The result ledger must contain one done effect per completed identity.
Retries, rejections, background work and input errors are absent.
Service acceptance: complete offered demand without growing backlog at each tick
and preserve those identity/key-order rules. No latency bound is claimed here.

Each worker can complete 100 items per tick. Before the change, an explicit
global coordination gate allows only 90 completions per tick regardless of workers.
The source/config model supplies that gate: the plateau alone would not diagnose it.
Two workers are the fixed baseline; their allocated cost is 120 worker-seconds.
Four workers cost 240 worker-seconds over the same run. These are allocation
counts, not CPU or monetary measurements.

## Before and after intervention

Before: all keys cross the global gate.
After: independent keys have separate owners and queues, removing that gate.
With two workers, A/C use one and B/D the other; with four, each key has an owner.
These balanced inputs allow the model's full per-worker capacity. No transfer
of ownership occurs during a run; the old-owner/epoch test is a separate requirement.

| Offered per tick | Before, 2 workers: completed / final backlog | After, 2 workers: completed / final backlog | After, 4 workers: completed / final backlog |
| ---: | --- | --- | --- |
| 50 | 3000 / 0 | 3000 / 0 | 3000 / 0 |
| 100 | 5400 / 600 | 6000 / 0 | 6000 / 0 |
| 200 | 5400 / 6600 | 12000 / 0 | 12000 / 0 |
| 400 | 5400 / 18600 | 12000 / 12000 | 24000 / 0 |

Initial backlog is zero at every point; final backlog equals offered total minus
correct completed identities. For example, before at 100 per tick:
6000 - 5400 = 600. That accumulating deficit fails the proposed growth envelope.
The fixed-resource remediation passes through 200 per tick but fails at 400;
the separate added-resource series passes the latter at twice the allocation.

## State and causal verification

Within each tick the model enqueues keys cyclically and applies only the permitted
completion budget; work beyond it stays queued with its original identity.
No item is dropped to manufacture the completion count. At each checkpoint,
verify completed and pending identity sets are disjoint and partition admitted work.
Assert increasing per-key sequence in the completed ledger.

The known gate explains this model's limit because its budget is an explicit
input and the candidate removes it while keeping worker capacity unchanged.
Do not infer that cause from a similar real-world curve without inspecting source,
coordination waits and the generator. Real skew, cross-key transactions and owner
movement are outside this balanced model; partitioning may be invalid there.
No real load generator, capacity purchase or unlimited scaling claim is supplied.
