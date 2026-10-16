---
name: portability
description: >-
  Moves software between execution environments when tickets say "the app only works on the old host", "move this service to the new runtime", or "keep the same result on the target host". Not for setup on one target (see installability), locale adaptation (see localizability), or user movement (see mobility).
---

# Portability

## Definition and scope

Portability means software can move between specified execution environments
with bounded adaptation while retaining agreed behavior. Identify environment
assumptions and their adaptation surface; distinguish setup on one target
(`installability`), language/locale behavior (`localizability`), and client
movement (`mobility`) from migration of the software's execution environment.

## Use when / Don't use when

- Apply when behavior depends on an old host's implicit paths or runtime assumptions.
- Apply when the target environment needs a bounded adapter or capability mapping.
- Route setup, upgrade, and removal on an already supported target to `installability`.
- Route locale resources and presentation formats to `localizability`.
- Route an independent experiment reconstruction to `replicability`.

## Workflow

1. Clarify: Read build/deployment definitions, runtime interfaces, filesystem and
   process assumptions, configuration, native boundaries, and behavior tests first.
   Record the actual source and target profiles rather than assuming platform facts.
   If a target capability or required behavior is unknown, then Ask the user
   which environment and behavior contract the migration must preserve.

2. Specify: Record source/target capabilities, changed assumptions, allowed
   adaptation modules, preserved behavior, artifact location, and acceptance evidence.
   If no adaptation budget is supplied, then propose labeled illustrative defaults:
   isolate the named environment differences in a platform adapter/configuration
   boundary while keeping the requested behavior fixed; confirm with the user/stakeholder.
   Ask for an effort or elapsed-time limit rather than inventing one.

3. Design/Implement: Read [environment adaptation](./references/design-guide.md)
   when choosing an explicit capability mapping or platform adapter.
   If a working-directory default determines output location, then supply a declared
   target artifact root. If a target lacks a needed capability, then expose an
   alternative with its behavior difference or leave support unverified.
   If adaptation changes domain behavior, then separate that change from the migration claim.

4. Verify: Run preserved behavior fixtures in both declared environment profiles.
   Compare content, side effects, and required artifact locations, not compilation alone.
   If an assumed capability was not exercised, then mark that part of target support
   unverified. Keep failed runs and matched-input evidence in the comparison record.
   Read [report-root example](./references/worked-example.md) when detecting a
   hidden source-directory assumption without claiming real operating-system properties.

5. Report: Return the profile differences, actual adaptation surface, behavior
   comparison, unsupported capabilities, and remaining target assumptions.
   If only a synthetic target profile was tested, then identify that boundary
   rather than reporting the real platform migration complete.

## Specification patterns

- **Preservation:** On `{target_profile}`, `{application_revision}` shall
  preserve `{behavior_and_artifact_contract}` from `{source_profile}`,
  verified with `{shared_input_and_expected_result}`.
- **Bounded adaptation:** Moving between `{source_and_target_profiles}` shall
  require changes only within `{confirmed_adapter_and_configuration_surface}`,
  with `{reviewed_behavior_differences_or_unsupported_capabilities}`.
- **Capability:** Target support for `{required_operation}` shall be established
  through `{capability_mapping_and_exercised_check}`, not inferred from
  `{unexamined_platform_label}`.

Use the illustrative adaptation-surface proposal in Specify when no number is
given and confirm with the user/stakeholder; keep quantitative budgets unresolved.

## Rules of thumb

- Do express target support in required capabilities, not a host brand or label;
  a named target alone does not define the runtime operations this program needs.
- Do keep target-specific resolution inside the declared adaptation boundary;
  edits to domain calculations must be reported as additional migration surface.
- Do resolve required artifact roots explicitly per profile; an inherited working
  directory must not silently decide where the migrated application writes its output.
- Do inspect environment-bound generated artifacts as part of the target profile;
  source-side build success cannot establish that those artifacts are usable there.

## Verification

Use cross-profile behavior fixtures, environment-assumption review, build/package
inspection, and target capability checks.
Inspect both output content and the location/visibility of the resulting artifact.
Hold the requested input and domain contract fixed while recording environment differences.
Check actual runtime construction and required generated artifacts where present.
Preserve wire/data representations unless a separate approved change requires otherwise.
Retain raw results, failures, unfinished runs, and unsupported capability checks.
A successful build or installation is supporting evidence, not the complete
behavior-preservation verdict.

## Done checklist

- [ ] Describe actual source and target capabilities without guessed platform facts.
- [ ] Locate environment assumptions affecting the requested behavior.
- [ ] Confirm the allowed adaptation surface and preserved contract.
- [ ] Supply explicit platform-dependent artifact roots.
- [ ] Compare content and required side effects across the profiles.
- [ ] Exercise required generated artifacts or mark them unverified.
- [ ] Report actual changes, unsupported capabilities, and test boundaries.

## Failure modes

- Calling a successful target build a completed behavior migration.
- Depending on the old host's working directory or private environment defaults.
- Treating installation success as evidence of cross-profile equivalence.
- Hiding changed domain behavior inside a platform adapter.
- Advertising support for a platform capability that was never exercised.

## References

- Read [environment adaptation](./references/design-guide.md) when locating
  source assumptions and selecting bounded target-specific changes.
- Read [report-root example](./references/worked-example.md) when comparing
  behavior and artifact location under explicit synthetic environment profiles.
