# Continuing upkeep patterns

Evaluate recurring work from a declared maintainer context, not merely code size
or a successful demonstration by the original author.

## Reusable diagnosis and retained repair fixtures

- **Use when:** Maintainers repeatedly rediscover a known failure or prerequisite.
  Retain its reproducer, cause evidence, and behavior check with the relevant code.
- **Trade-off:** Fixtures can become stale or overfit one incident; keep their
  supported input meaning visible rather than preserving an obsolete implementation.
- **How to verify:** Start from a fresh checkout/context, diagnose with the recorded
  artifacts, perform a later upkeep task, and replay the retained repair checks.

## Reproducible regeneration

- **Use when:** Maintenance touches generated output. Preserve source inputs and
  the inspected generation procedure along with the corrected consumer result.
- **Trade-off:** Regeneration can expose unrelated drift; a hand patch may be a
  temporary workaround but leaves a recurring obligation until its source is repaired.
- **How to verify:** Regenerate from declared inputs without private edits and
  compare the resulting behavior with the retained repair fixture.

## Residual operator and temporary-path ledger

- **Use when:** A code fix leaves manual invalidation, a compatibility branch, or
  a temporary repair process. Attribute its repeated checks, owner, and exit condition.
- **Trade-off:** Removing scaffolding prematurely can reopen the defect; retaining
  it indefinitely has continuing cost even after the original request is closed.
- **How to verify:** Rehearse the next upkeep task, account for those steps, and
  inspect whether the stated exit condition is actually met before dropping the ledger entry.

For an illustrative trial, use 3 diagnosis/repair/modification tasks with a
30-minute active-work bound per task; confirm with the user/stakeholder.
Record active investigation, implementation, verification, repeated operator work,
and waiting distinctly. Report any excluded coordination instead of making it
disappear from the maintenance picture. Ask the user which contexts and recurring
tasks justify extending a narrow trial into a continuing upkeep claim.
