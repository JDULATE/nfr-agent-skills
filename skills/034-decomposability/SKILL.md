---
name: decomposability
description: >-
  Finds separable responsibilities when tickets say "split this without sharing its internals", "these parts cannot run apart", or "extract the renderer from billing". Not for arranging dependencies alone (see structuredness) or joining components (see composability).
---

# Decomposability

## Definition and scope

Decomposability means a whole can be separated into parts with explicit
responsibilities and manageable boundary dependencies. Establish which state and
decisions each part owns and what it needs from its neighbors.
Separate genuine separability from dependency organization (`structuredness`)
and preservation of behavior when parts are assembled (`composability`).

## Use when / Don't use when

- Apply when extracting a responsibility still requires another part's private
  fields, hidden initialization, or mutable internal state.
- Include boundary data, state ownership, and the ability to exercise each
  proposed responsibility without constructing unrelated internals.
- Route package direction rules without a split question to `structuredness`.
- Route validating a particular assembled chain to `composability`.
- Do not equate extra files or processes with separable responsibilities.

## Workflow

1. Clarify: Read candidate modules, shared state, constructors, callers,
   transaction boundaries, and responsibility docs before proposing a split.
   Identify the task each proposed part must perform independently.
   If the requested split has no responsibility or state boundary, then Ask the
   user what must become separable and which decisions must stay together.

2. Specify: Record part responsibilities, owned state, boundary inputs/outputs,
   necessary coordination, and independent exercise criteria.
   If no target is provided, then propose a labeled illustrative default:
   each named part runs its declared task through boundary data without reaching
   into another part's private state; confirm with the user/stakeholder.
   Ask at most three questions about responsibilities, state/coordination,
   and preserved whole behavior before extracting code.

3. Design/Implement: Read [split decisions](./references/design-guide.md)
   when selecting responsibility cuts and removing hidden dependencies.
   If an extracted part still reads another's mutable internals, then move the
   required information into an explicit boundary contract or reconsider the cut.
   If an invariant requires a common state owner, then retain that ownership
   rather than forcing a split across an unestablished coordination mechanism.

4. Verify: Exercise each responsibility using only its declared inputs and
   dependencies, then compare the original whole-path behavior.
   If isolation succeeds only with a fake that reproduces a neighbor's private
   implementation, then treat the boundary as unresolved.

5. Report: Return the responsibility/state map, explicit contracts, independent
   exercise results, and necessary coordination that remains.
   If only source files moved, then report organization work rather than
   claiming the responsibilities became independently executable.

## Specification patterns

- **Independent responsibility:** `{part}` shall perform `{task}` using only
  `{declared_inputs_and_dependencies}` while owning `{state_or_decisions}`,
  verified by `{isolated_task_fixture_without_neighbor_internals}`.
- **Preserved whole:** Separating `{responsibilities}` shall preserve
  `{whole_result_and_invariants}` through `{boundary_contract}`, checked by
  `{before_after_whole_path_and_state_comparison}`.

Use the illustrative explicit-boundary proposal in Specify when no numerical
budget exists; confirm with the user/stakeholder before accepting the split.

## Rules of thumb

- Cut by responsibility and state ownership, not by equal file sizes; a balanced
  file split can leave both halves dependent on the same hidden mutable object.
- Pass the information a responsibility needs through its boundary rather than
  handing it the original object's entire private state.
- Keep an invariant with its actual state owner unless the proposed split supplies
  the coordination needed to preserve it; a new process boundary is not that evidence.
- Challenge a split whose isolated fixture reconstructs the neighbor's internals;
  the test may have copied the coupling rather than removed it.

## Verification

Use isolated responsibility fixtures, private-access inspection, and whole-path
regression comparison. Trace constructor and runtime dependencies separately.
Capture initial state, boundary values, effects, and final owned state.
Check that each part can run without initializing the unrelated responsibility.
Retain the original failure case and any boundary fields added during extraction.
Inspect whether a supposedly inert data object actually carries mutable behavior.
Compare necessary coordination explicitly; do not hide it behind test doubles.

## Done checklist

- [ ] Name responsibilities and their independent tasks.
- [ ] Assign each mutable state element and invariant an owner.
- [ ] Enumerate boundary values and necessary coordination.
- [ ] Run each task without another part's private initialization.
- [ ] Inspect runtime and constructor access across the proposed boundary.
- [ ] Compare preserved whole-path outputs and state.
- [ ] Record coupling that remains instead of claiming complete separation.

## Failure modes

- Moving methods into files while sharing the same mutable internal object.
- Extracting a renderer that still requires billing initialization.
- Recreating private neighbor state inside a supposedly independent test double.
- Splitting a state invariant without an implemented coordination boundary.

## References

- Read [split decisions](./references/design-guide.md) when choosing responsibility
  boundaries and ownership of shared state.
- Read [billing/rendering example](./references/worked-example.md) when checking
  real separation rather than a file-only extraction.
