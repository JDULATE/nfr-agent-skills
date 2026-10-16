---
name: distributivity
description: >-
  Defines node placement when asked "assign key ranges", "prevent duplicate shard owners", or "redistribute partitions". Ask the user if placement rules vs observing current ownership is unclear. Not for workload growth curves (see scalability).
---

# Distributivity

## Definition and scope

Distributivity means placing work, state, or responsibility across nodes under
explicit allocation and coordination rules. Use the repository's proposed
meaning; Ask the user if they mean a different distribution property.
Separate node assignment from workload growth (`scalability`) and usable
resource admission (`expandability`).

## Use when / Don't use when

- Apply when keys, shards, or responsibilities have unclear owners or conflicting
  assignments during placement changes.
- Identify whether replicas may read, write, or merely hold a copy.
- Route demand-versus-resource growth to `scalability`.
- Route exchange interpretation between nodes to `interoperability`; correct
  messages alone do not determine who may execute their effects.

## Workflow

1. Clarify: Read routing code, partition maps, worker startup, state stores,
   handoff procedures, and failure reports before proposing placement rules.
   Identify the authoritative assignment source and stale participants.
   If "distribute this" lacks an allocation unit, then Ask the user what work
   or state moves and which effects must have an exclusive owner.

2. Specify: Define the allocation unit, eligible nodes, ownership invariant,
   routing revision, handoff stages, and refusal behavior.
   If these are missing, then propose a labeled illustrative default:
   exclusive effect authority per shard, stale assignments refused, and new
   ownership published only after a checked handoff; confirm with the user/stakeholder.
   Ask at most three grouped questions about allocation, authority, and handoff
   constraints before designing reversible changes.

3. Design/Implement: Read [placement decisions](./references/design-guide.md)
   when selecting routing maps, stale-owner fencing, or movement stages.
   If an old owner can still perform effects, then enforce assignment authority
   at the effect boundary rather than merely refreshing the router.
   If handoff cannot establish the agreed state boundary, then leave the shard
   unassigned or paused according to the confirmed policy instead of guessing.

4. Verify: Exercise current and stale assignment tokens through the effect path,
   and record ownership before, during, and after a move.
   If the authority check is unavailable, then test its actual refusal policy;
   do not infer safety from a controller's desired map.

5. Report: Show the placement map, authoritative revisions, state handoff evidence,
   stale-owner results, and remaining assumptions about coordination.
   If only a centralized model was checked, then limit the conclusion to that
   model and withhold distributed partition or failover guarantees.

## Specification patterns

- **Allocation:** For `{allocation_units}`, `{authority_source}` shall assign
  `{eligible_nodes_and_roles}` under `{placement_rule}`, verified by
  `{map_and_effect_authority_checks}`.
- **Movement:** Moving `{unit}` from `{source}` to `{target}` shall preserve
  `{state_boundary}` and refuse `{stale_effects}` throughout `{handoff_stages}`,
  checked by `{interleaved_owner_and_router_fixture}`.

Use the illustrative ownership proposal in Specify when no target is given;
confirm with the user/stakeholder, including the behavior while no owner can act.

## Rules of thumb

- Distinguish a replica's possession of shard data from authority to apply shard
  effects; copying the data must not silently create another active owner.
- Enforce assignment revision at the effect boundary, not solely in the router;
  a stale worker must not retain authority merely because its message was routed earlier.
- Keep the movement state explicit between source quiescence and target activation;
  an entry in the desired placement map is not proof the target owns complete state.
- Derive placement from declared node eligibility before balancing assignments;
  equal shard counts do not justify placing a restricted shard on an ineligible node.

## Verification

Use allocation-model inspection, interleaved handoff tests, and effect-store
instrumentation. Capture allocation unit, node, assignment revision, decision,
and state boundary for accepted and refused actions.
Retain stale-router requests and unfinished moves in the evidence.
Check missing authority, source refusal to quiesce, target state mismatch,
and attempts by a replica to mutate authoritative state.
Inspect the real effect-store check separately from controller intent.
Do not substitute throughput measurements for ownership evidence.

## Done checklist

- [ ] Name allocation units and eligible node roles.
- [ ] Identify the authority source used by the effect path.
- [ ] Check that replica presence does not confer write authority.
- [ ] Exercise stale-owner and stale-router attempts.
- [ ] Compare transferred state with the source handoff boundary.
- [ ] Observe refusal during an incomplete move.
- [ ] Document authority-loss and untested partition behavior.

## Failure modes

- Updating routing while leaving an old worker authorized to write.
- Treating every copied shard as another writable owner.
- Activating a target before its required state boundary is established.
- Claiming balanced placement proves acceptable workload growth.
- Presenting a sequential controller fixture as a proof under network partitions.

## References

- Read [placement decisions](./references/design-guide.md) when choosing authority
  checks and handoff gates across nodes.
- Read [shard-move example](./references/worked-example.md) when checking stale
  ownership against a fully specified centralized authority fixture.
