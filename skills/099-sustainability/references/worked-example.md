# Coalesced work and operational energy only

This is a supplied synthetic energy ledger, not meter readings from actual devices.
All numeric values, results and targets are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled boundary and objective

Worker profile energy-slate runs report identities R001 through R100 in a
600-second period on unchanged device device-amber and snapshot dict-mint.
Each output must be exactly its identity followed by :mint.
There are no retries, missing results, remote devices or background jobs.
The local device energy counter is the entire comparison boundary.
The supplied source is fixture-ledger-amber; it attributes the same 0.2 kWh idle
allocation to this run in both plans. No modeled factor converts CPU to energy.
Every report must be correct and complete within the comparison period.

Illustrative objective; confirm with the user/stakeholder:
reduce operational kWh per correct report by 10% against the direct plan.
Acquisition and retirement impact values are explicitly unknown in this ledger;
no hardware replacement occurs and no total-lifecycle conclusion is permitted.

## Before and after coalescing

The direct producer decodes the same revision twice within each report.
The candidate decodes once per report and shares that value with both uses;
the scope ends with that report, with no persistent cache or changed recipient.

| Supplied energy component | Direct kWh | Coalesced kWh |
| --- | ---: | ---: |
| Decode work | 0.4 | 0.2 |
| Render and write complete output | 1.4 | 1.4 |
| Allocated idle | 0.2 | 0.2 |
| Total | 2.0 | 1.8 |

Both ledgers end with all 100 exact outputs and no unfinished work.
The ratios are 0.020 and 0.018 kWh per report: an illustrative 10% reduction;
confirm with the user/stakeholder. The supplied component ledger supports this
modeled operational comparison, not a conversion inferred from less CPU.
A failed shortcut that emits only R001 through R080 fails the cohort contract
regardless of its lower total energy; no consumption estimate is fabricated for it.

## Conclusion boundary

This before/after fixture supports only its local operational-energy objective.
It provides no emissions factor, acquisition data, retirement impact or net
environmental verdict. In a real run, an offloaded decoder would enlarge the
boundary or leave the claimed whole-task saving unknown. No real energy trial ran.
