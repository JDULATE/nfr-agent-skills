# Worked example: preserve a path through successive invoice changes

Assume a fictional invoice service starts with a single currency representation.
The stakeholder names a later currency expansion and then revised rounding rules.
No currency or accounting rule in this example establishes a real financial requirement.

## Inspect state and consumers

Read invoice calculation code, stored amount representation, exported contracts,
consumer records, and the named roadmap. Ask which meanings existing invoices must
retain and who can retire old readers. Do not guess historical rounding behavior.

Propose: "The service shall support `{currency_change_then_rounding_change}`
without reinterpreting `{historical_invoice_meaning}`, using `{staged_data_transition}`
and `{consumer_exit_conditions}`, verified by a sequential migration rehearsal."

Illustrative scope only: rehearse 2 successive changes while retaining earlier
state; confirm with the user/stakeholder. The actual scenario order, horizon,
effort bound, and historical data meaning require stakeholder decisions.

## Rehearse the path

| Stage | Carry forward | Evidence to collect |
| --- | --- | --- |
| Existing service | Original invoices and their consumer-visible meaning | Baseline outputs and active reader inventory |
| Currency expansion | Existing invoices plus newly explicit currency data | Mixed-reader/writer checks and any representation bridge |
| Old-reader retirement | Both invoice populations | Proof that the obsolete reader no longer needs its bridge |
| Rounding-rule change | Historical meanings and the current representation | New-rule results and preservation of the old invoices' interpretation |

If the rounding change only works after rebuilding invoices from empty fixtures,
identify the missing migration. If old readers cannot be retired, record the
additional coexistence obligation and its owner rather than marking the bridge removed.

Track a synthetic record named `invoice-A` with its original amount text and a
`legacy` rule label through every stage. Add `invoice-B` with the new explicit
currency representation. At the later rounding-rule change, compare `invoice-A`
against its retained baseline output rather than rewriting its label to `current`.
Keep `invoice-B` readable under the expanded representation as the new rule is
introduced. Obtain the historical interpretation from the owner, not from these labels.

Return a cumulative ledger of schema changes, consumer transitions, retained
bridges, and retirement evidence. Distinguish measured rehearsal work from any
forecast of future delivery cost. This fictional path is a way to evaluate the
chosen sequence, not proof of support for every possible invoice change.

## Carry bridge costs into later work

Illustrative accounting only, in person-hours; confirm with the user/stakeholder.
These are invented rehearsal entries, not an effort prediction or accepted budget.

| Stage | New change work | Inherited bridge upkeep | Retirement work | Stage total |
| --- | --- | --- | --- | --- |
| Currency expansion | 3 | 1 | 0 | 4 |
| Prepare rounding change and retire old reader | 2 | 2 | 1 | 5 |

The illustrative cumulative total is 4 + 5 = 9 person-hours; confirm with the
user/stakeholder. Charge bridge creation to its introducing change, then charge
mixed-reader checks and fixes to each stage still carrying it. The later stage's
upkeep occurs before its retirement gate. Do not drop it just because retirement
was planned earlier; confirm the exit before recording later upkeep as absent.
Keep task identities so a shared fix is charged once and forecasts stay separate
from measured rehearsal work. Compare the cumulative total with the actual agreed
budget only after the owner chooses the cost unit, scope, and attribution rule.
