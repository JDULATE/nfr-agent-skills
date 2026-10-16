# Fleet policy exception example

This is an illustrative synthetic fleet, not a production administration result.
All proposed assignments and end conditions are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled fleet record

| Field | Fixture value |
| --- | --- |
| Inventory | inventory-fern: agent-ash/moss, agent-birch/leaf, agent-cedar/root |
| Authority | synthetic fleet operator authorized for that inventory |
| Base desired revision | policy-moss, log_mode compact |
| Initial observed policy | policy-fern, log_mode verbose on every target |
| Exception | agent-birch/leaf only: log_mode verbose |
| Exception owner / end | diagnostics-owner / diagnostics-ended event |
| Exception revision | exception-leaf on top of policy-moss |
| Reachability | ash and birch reachable; cedar offline |
| Observation freshness | observations from this reconciliation pass only |
| Reconnect behavior | cedar obtains its assigned base policy when reachable |
| Carry | desired assignments persist; last observations remain labeled with their pass |

## Failing aggregate before remediation

The dispatcher accepts assignments for all targets and reports "fleet applied".
No per-agent adoption is inspected. Cedar remains offline on policy-fern.
The receipt therefore cannot establish the reported fleet-wide result.

## Remediation

Keep base intent, target exception, and observation separately:
| Target | Effective assignment | Observation this pass | Outcome |
| --- | --- | --- | --- |
| ash/moss | policy-moss, compact | policy-moss, compact | adopted |
| birch/leaf | policy-moss + exception-leaf, verbose | same revision pair, verbose | adopted exception |
| cedar/root | policy-moss, compact | absent | unresolved offline |

The base policy remains compact.
Birch's verbose observation is not a source from which to configure Ash or Cedar.

## Reconnect and exception-end cases

When Cedar reconnects, its new observation is policy-moss, compact.
That resolves its pending assignment without changing the other targets.

When diagnostics-ended occurs, remove exception-leaf.
Birch's next assignment and observation are policy-moss, compact.
The old verbose observation remains in the prior pass, not the current verdict.

## Replacement failure probe

Replace birch/leaf with a new incarnation birch/bud.
The exception names leaf, so bud receives policy-moss, compact unless an explicit
new assignment says otherwise. Copying verbose solely from the display name fails
the fixture's exception-scope rule.

## Requirement example

For a retirement probe, remove cedar/root under a new inventory-sprout containing
only ash/moss and birch/leaf. Mark Cedar's assignment retired in that inventory;
keep its earlier unresolved result in inventory-fern's history. Do not report
the retired target as either currently compliant or awaiting ordinary convergence.

For inventory-fern, administration shall report each target's assigned and observed
policy, preserve the local Birch exception until its declared end, and retain
Cedar as unresolved until its adoption is actually observed.

## Limits

This fixture demonstrates administration decisions, not a distributed rollout
protocol, production authorization, or a numeric convergence deadline.
The example assumes observations are truthful within the synthetic pass.
