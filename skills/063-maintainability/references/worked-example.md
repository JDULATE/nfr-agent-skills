# Worked example: retained state across label-service upkeep

Assume a fictional label service treats canonical state as authoritative and
regenerates its lookup artifacts from a declared rule source. Those are example
contracts to check in a real repository, not facts about a database or generator.

Initial rule source maps `queued` to `pending`. A cached parcel `parcel-lilac`
still says `ready` although its canonical label is `pending`. The supported lookup
must return the canonical label under this fixture's agreed freshness contract.

Propose: "The declared maintainer context shall complete `{diagnosis_repair_and_rule_task}`
from `{documented_checkout_and_inputs}`, retaining `{earlier_repair_outcomes}` and
`{regeneration_path}`, within `{confirmed_active_effort_bound}` under `{cost_rule}`."

| Task and carried start | Action / concrete expected result | Retained artifact for later work |
| --- | --- | --- |
| Diagnose lookup: cached `ready`, canonical `pending` | Trace `parcel-lilac` lookup to stale cache; recorded lookup result is wrong | `lookup-stale` fixture with both values and canonical-result oracle |
| Repair from diagnosed state | Lookup returns `pending`; regenerate from rule source and replay with the same result | Corrected source/procedure plus passing `lookup-stale`, not just hand-edited output |
| Modify rules with repaired checkout retained | Add `held -> review`; public lookup of a held parcel returns `review`; queued still returns `pending` | New held-case fixture plus still-passing stale/queued cases |

Illustrative ledger only, in active minutes; confirm with the user/stakeholder.
The values are invented worked arithmetic, not measured team effort or estimates.
The illustrative proposed bound is 30 active minutes per task; confirm with the user/stakeholder.

| Task | Investigation | Implementation | Verification | Active total |
| --- | --- | --- | --- | --- |
| Diagnose | 8 | 0 | 4 | 12 |
| Repair/regenerate | 4 | 8 | 6 | 18 |
| Add held rule | 2 | 3 | 4 | 9 |

The illustrative cumulative active total is 12 + 18 + 9 = 39 minutes;
confirm with the user/stakeholder. Each example task fits the proposed per-task
bound; the cumulative value is not a different hidden per-task requirement.
Record coordination/waits separately and include recurring manual repair in active
work if the agreed convention requires it. No wait duration is invented here.

A repair that returns `pending` only after undocumented cache wiping has not
removed the repeated operator obligation. A held-rule change that reintroduces
`ready` for `parcel-lilac` incurs rework even if its new held case passes.
These carried fixtures distinguish recurring upkeep from unrelated clean-room edits;
no maintainer, generator, or time trial was actually run by this example.
