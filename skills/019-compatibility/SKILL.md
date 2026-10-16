---
name: compatibility
description: >-
  Protects coexistence when tickets say "these tools overwrite each other", "run both tools side by side", or "installing one breaks the other". Not for exchanging meaningful data (see interoperability).
---

# Compatibility

## Definition and scope

Compatibility means specified components can coexist without unacceptable interference.
Identify the shared environment and each component's protected behavior.
Separate coexistence from exchanging meaningful information (`interoperability`)
and from removing one implementation in favor of another (`replaceability`).

## Use when / Don't use when

- Apply when installing, starting, updating, or removing a neighbor damages an
  otherwise working component through shared names, files, dependencies, or settings.
- Require the supported component combinations and shared-host conditions.
- Route payload interpretation to `interoperability`; an exchange can fail even
  when both participants run independently without interference.
- Route a substitution with the old component retired to `replaceability`.

## Workflow

1. Clarify: Inspect manifests, launch configuration, resource paths, dependency
   declarations, setup scripts, and coexistence reports before specifying.
   Run each component alone to identify its existing protected operations.
   If "works together" is the only request, then Ask the user whether it means
   coexistence, information exchange, or replacement.

2. Specify: Record the supported combinations, resource-sharing boundary, operations
   to preserve, lifecycle actions, and allowed interference.
   If no limits are supplied, then propose this labeled illustrative default:
   preserve standalone results during co-residence and neighbor lifecycle actions;
   confirm with the user/stakeholder. Do not invent timing tolerances.
   For a practical fix, present that record and ask at most three questions:
   which combinations, which protected operations, and which shared resources
   or accepted differences? Proceed to reversible design using explicit assumptions.

3. Design/Implement: Read [coexistence decisions](./references/design-guide.md)
   when selecting namespace, dependency, or lifecycle isolation.
   If components collide on a shared name, then separate ownership or negotiate
   that resource before changing either component's protected behavior.
   If shared dependencies cannot satisfy both consumers, then isolate their
   resolution boundary or report the unsupported combination.

4. Verify: Compare each component alone with the supported combinations using
   the same inputs and environment. Include neighbor update and removal.
   If a combination was not exercised, then leave that matrix cell unverified;
   a successful standalone run must not fill it.

5. Report: Return the combination matrix, resource ownership changes, protected
   operation results, and unsupported combinations.
   If a workaround requires exclusive execution, then report a coexistence
   restriction rather than claiming the pair is compatible without qualification.

## Specification patterns

- **Co-residence:** While `{components_and_revisions}` share `{environment}`,
  each shall preserve `{protected_operations_and_results}` during
  `{neighbor_actions}`, verified by `{standalone_and_combined_comparison}`.
- **Lifecycle isolation:** Updating or removing `{neighbor}` shall leave
  `{survivor_resources_and_behavior}` unchanged except for
  `{approved_shared_changes}`, checked by `{resource_diff_and_survivor_test}`.

Use the illustrative preservation default in Specify when targets are absent;
confirm with the user/stakeholder before accepting the combination matrix.

## Rules of thumb

- Give co-resident components separate writable names unless the shared resource
  has an explicit joint-ownership contract; an accidental last writer must not
  determine which component's settings survive.
- Keep a neighbor's uninstall list inside its ownership boundary; a shared-host
  cleanup that removes the survivor's resource violates coexistence even if
  reinstalling the survivor repairs it.
- Check dependency selection from each co-resident consumer's context; validating
  only the host's chosen dependency can hide one neighbor replacing another's needs.
- Treat a lock that forces components to take turns as a restricted combination,
  not evidence that both protected concurrent operations remain available.

## Verification

Use resource-diff inspection, dependency-resolution review, and lifecycle
integration checks. Capture standalone outputs before co-resident runs.
Preserve initial settings and restore the fixture between different action orders.
Check process-level and persistent-resource collisions separately.
Exercise install/start/update/remove order where ownership can change.
Inspect whether environment-wide settings leak into the other consumer.
Keep failed runs and configuration revisions beside the matrix.

## Done checklist

- [ ] List supported component pairs and their actual revisions.
- [ ] Identify writable resource and shared-dependency ownership.
- [ ] Capture each protected operation's standalone output.
- [ ] Compare outputs with both participants present.
- [ ] Check survivor state after neighbor update and removal.
- [ ] Record order-dependent failures and restricted combinations.
- [ ] Mark absent matrix evidence as unverified.

## Failure modes

- Using "both launch" as the only evidence while settings are overwritten.
- Testing one install order and promising all lifecycle orders.
- Removing the neighbor and presenting the repaired standalone run as coexistence.
- Quietly replacing a protected operation with a weaker result to pass the pair.

## References

- Read [coexistence decisions](./references/design-guide.md) when shared names,
  dependencies, or cleanup actions create interference.
- Read [shared-settings example](./references/worked-example.md) when building
  a standalone/co-resident matrix with a concrete survivor check.
