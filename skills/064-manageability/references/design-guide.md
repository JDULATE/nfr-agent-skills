# Fleet administration decisions

Apply these decisions to a declared managed inventory.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A rollout is green after message dispatch only. | Track desired and observed revisions per target. More states remain pending. | Compare agent observations, not message receipts, with the assigned policy. |
| One diagnostic override affects every node. | Store exceptions separately with target, owner, and end condition. More precedence logic is needed. | End the exception and verify only its target returns to base policy. |
| Offline agents disappear from the result. | Retain unresolved assignments for reconciliation after reconnect. The fleet may not converge immediately. | Reconnect the target and inspect its adopted revision. |
| A removed node remains pending forever. | Retire its assignment under the new inventory revision while preserving the old result. Historical and current scope must remain distinct. | Remove the node from inventory and verify it is not reported currently compliant or awaiting convergence. |
| A replacement node inherits an unrelated override. | Re-evaluate policy against current stable identity/incarnation. Replacement may require a new assignment. | Replace a target and confirm the former exception is not copied implicitly. |
| Targets derive desired policy from one another. | Calculate effective assignments from the policy hierarchy. Central intent must remain available. | Give a neighbor an exception and verify ordinary targets keep the base policy. |

## Reconciliation sketch

```text
for target in selected_inventory:
  desired = base_policy
  if active_exception(target.identity, target.incarnation):
    desired = apply_target_exception(desired)
  publish_assignment(target, desired.revision, desired.values)
  observed = read_agent_state(target)
  record(target, desired, observed_or_unknown(observed))
```

The sketch is administration logic, not a distributed consistency guarantee.
A real implementation needs a declared observation freshness rule.

## Exception record

Keep target identity, incarnation, owner, reason, affected fields, and end condition.
Do not use absence of an owner as permission to leave an exception permanent.
If the end condition is not available in existing policy, Ask the user.

Publish local exceptions as effective assignments while preserving the base policy
as the source of ordinary-target intent.
