---
name: replicability
description: >-
  Supports independent reconstruction when asked "rebuild this experiment elsewhere", "share the experiment setup", or "remove laptop-only assumptions". Ask the user if reconstruction vs ordinary reruns is unclear. Not for reruns in the original setup (see repeatability) or moving the product to another platform (see portability).
---

# Replicability

## Definition and scope

Replicability means another executor or environment can reconstruct a procedure
and obtain an agreed comparable result. Package the semantic inputs and setup
needed for an independent attempt; distinguish reruns in the original setup
(`repeatability`) and moving a product between platforms (`portability`).

## Use when / Don't use when

- Apply when an experiment depends on an author's laptop settings or private files.
- Apply when another engineer cannot reconstruct the procedure from its handoff.
- Route reruns by the original executor under held conditions to `repeatability`.
- Route adapting deployed software to a different platform to `portability`.
- Ask the user what "replicate" means if the request instead concerns data copies
  or additional running instances.

## Workflow

1. Clarify: Read the procedure, setup code, input fixtures, configuration sources,
   environment assumptions, and handoff docs before promising independent results.
   Identify the independent executor and what they can obtain without author access.
   If that executor or allowed environment difference is unknown, then Ask the user
   which independent reconstruction the claim is intended to cover.

2. Specify: Record source/input revisions, semantic defaults, required capabilities,
   setup steps, allowed differences, comparison rule, and author assistance policy.
   If no package contract exists, then propose labeled illustrative defaults:
   publish the requested procedure's inputs and semantic settings, use a clean
   independent workspace, and compare the required result; confirm with the user/stakeholder.
   Fix the result equivalence rule before either outcome is inspected.

3. Design/Implement: Read [reconstruction design](./references/design-guide.md)
   when eliminating hidden defaults, private resources, or copied results.
   If a laptop setting changes meaning, then make it an explicit input.
   If a package mounts the author's workspace, then replace that dependency with
   declared inputs or limit the independence claim.
   If setup needs assistance, then record the intervention and repair the package
   before claiming an unassisted reconstruction.

4. Verify: Have the independent executor reconstruct from the supplied package
   without the original working directory, then compare the retained actual output.
   If reconstruction fails or needs an undeclared input, then preserve that gap;
   do not substitute a successful run performed in the author's environment.
   Read [independent ledger example](./references/worked-example.md) when
   diagnosing a semantic default that changes the reconstructed result.

5. Report: Return the package, independent execution record, actual comparison,
   environment differences, assistance, and unresolved inputs.
   If no independent attempt occurred, then report the package prepared but
   replicability unverified rather than treating the author's rerun as evidence.

## Specification patterns

- **Independent reconstruction:** `{independent_executor}` shall reconstruct
  `{procedure}` from `{declared_package_and_capabilities}` without
  `{author_private_state}`, producing `{comparable_required_result}`.
- **Handoff closure:** All inputs affecting `{result_semantics}` shall be
  supplied by `{package_or_declared_authorized_source}`; missing inputs and
  assistance shall be recorded in `{independent_attempt_record}`.
- **Comparison:** Compare `{independently_produced_artifact}` with
  `{reference_or_contract}` using `{predeclared_equivalence_rule}`, retaining
  `{allowed_differences_and_failed_reconstruction_steps}`.

Use the illustrative package proposal in Specify for a missing numeric target
and confirm with the user/stakeholder. Do not invent a universal replication success rate.

## Rules of thumb

- Do package semantic defaults as inputs; an author's shell setting must not
  silently determine how an independent executor interprets the fixture.
- Do require a newly produced result from the reconstructed procedure; copying
  the reference artifact establishes transfer, not an independent reconstruction.
- Don't count a different host as independent if it still reads undeclared files
  from the author's mounted workspace.
- Do expose setup assistance as part of the attempt record; private author repairs
  cannot support a claim that the published handoff was sufficient unaided.

## Verification

Use clean-workspace reconstruction, dependency/input inventory, setup validation,
and artifact comparison categories.
Check that the independent executor uses only declared resources and authorized access.
Record actual configuration, environment differences, assistance, raw outputs,
setup failures, and unfinished attempts before comparing outcomes.
Use the predeclared comparison rather than deleting fields that happen to differ.
Separate an environment compatibility issue from a changed semantic default.
An independent fixture attempt supports only its declared reconstruction scope,
not every executor, platform, or future configuration.

## Done checklist

- [ ] Identify the independent executor and authorized input sources.
- [ ] Package the procedure and semantic settings without private defaults.
- [ ] State required capabilities and allowed environment differences.
- [ ] Reconstruct without the author's working directory.
- [ ] Retain the independently produced output and setup record.
- [ ] Apply the comparison rule chosen before observing outcomes.
- [ ] Record missing inputs and any author assistance.
- [ ] Limit the conclusion to the independent attempt actually performed.

## Failure modes

- Calling another host independent while it mounts the original working directory.
- Shipping fixture data but omitting a setting that changes result meaning.
- Returning the reference output instead of executing the reconstructed procedure.
- Repairing setup privately and reporting the unmodified handoff sufficient.
- Treating a rerun by the original author as independent reconstruction evidence.

## References

- Read [reconstruction design](./references/design-guide.md) when packaging
  semantic defaults and removing undeclared author-environment dependencies.
- Read [independent ledger example](./references/worked-example.md) when checking
  that another executor can reconstruct the intended calculation from the package.
