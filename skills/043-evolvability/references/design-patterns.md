# Planning an evolution path

Keep a chosen future scenario and its implementation separate. This guide supplies
design decisions to inspect, not predictions that a particular roadmap will occur.

## Change-driver boundary

- **Use when:** A credible external contract or domain rule is expected to change
  repeatedly. Isolate its interpretation behind a named owned boundary.
- **Trade-off:** Premature generality adds upkeep; a boundary should correspond to
  an actual driver and not hide incompatible meanings behind a shared interface.
- **How to verify:** Apply the next named rule change and inspect which consumers,
  stored meanings, and owner modules must move together.

## Staged coexistence

- **Use when:** Old and new consumers need an overlap period while state migrates.
  Describe which combinations of readers, writers, and data forms are supported.
- **Trade-off:** Coexistence retains temporary code and duplicated representation;
  later changes inherit that burden unless an exit decision is exercised.
- **How to verify:** Rehearse intermediate combinations and interrupted migration,
  then carry the resulting state into the next planned change.

## Retirement gate

- **Use when:** A bridge can be removed after named consumers and data are retired.
  Require evidence of their disappearance rather than a release date alone.
- **Trade-off:** Missing consumer ownership can delay removal; preserving old paths
  indefinitely may conflict with other accepted lifecycle obligations.
- **How to verify:** Remove the bridge in a fixture representing the exit condition
  and exercise both the remaining callers and the subsequent scenario.

## Irreversible-decision ledger

- **Use when:** A migration discards state or changes meaning that old code cannot
  reconstruct. Record the decision, evidence, owner, and remaining recovery options.
- **Trade-off:** Waiting preserves options but can delay an accepted improvement;
  the ledger exposes that choice rather than making every transition reversible.
- **How to verify:** Compare old readers with state written after the transition
  and distinguish actual restoration from merely selecting an older executable.

## Sequence acceptance record

Record starting state, horizon, ordered scenarios, retained meanings, compatibility
bridges, effort accounting, exit evidence, and owners. Illustrative rehearsal scope:
2 successive changes with intermediate state retained; confirm with the user/stakeholder.
Ask for a different scope where the roadmap needs a different depth or no ordering.

- Reject evidence that resets the database before every purported future change.
- Flag temporary obligations that no later stage is responsible for removing.
- Keep speculative branches labeled until the stakeholder commits to their trigger.
