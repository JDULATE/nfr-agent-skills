# Resource-cost decisions

Choose an intervention for the selected device resource per useful result.
Ask the user for that unit and the required output before choosing a plan.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Identical computation recurs within a report | Coalesce it under the input revision for that report | Reuse requires equivalent computation; retained values consume space | Count actual computations and total scoped resource work; compare output contents |
| A batch shares expensive setup | Choose direct or batch execution from its resource-cost crossover | Setup and retained batches can outweigh marginal savings at small volumes | Exercise volumes on both sides with fill, cleanup and useful results included |
| Equivalent payloads repeat structure on the wire | Pack shared structure once for the approved recipient format | Encoding work and receiver state can rise | Compare transmitted bytes per correct decoded result and separate CPU/deadline limits |
| Storage reads unused fields for each result | Fetch the required projection or coalesce identical reads | Extra narrow calls may cost more than a reusable whole object | Compare actual storage work per result and verify the same permitted content |

## Batch-plan sketch

Pseudocode; inputs are measured in the same selected resource unit.
Include setup, fill and cleanup in setup_cost before using this comparison.

~~~text
choose_plan(volume, direct_per_item, setup_cost, batch_per_item):
    direct = volume * direct_per_item
    batched = setup_cost + volume * batch_per_item
    if batched < direct:
        return batch_plan
    return direct_plan
~~~

This selects only the declared resource objective. Reject either plan if it
violates a separate accepted completion or space constraint. A latency win
does not supply any missing resource cost.

## Accounting needed before selection

Bound the useful-result identity, quality, resource ownership and comparison
horizon. Shared-device allocation is a declared modeling choice, not a free saving.
Include retries, background work, cache fill/expiry and consumption displaced
to another process. Keep resource dimensions distinct; no unsupported conversion
turns CPU or bytes into energy, money or lifecycle benefit.
