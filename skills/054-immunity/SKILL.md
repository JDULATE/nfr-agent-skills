---
name: immunity
description: >-
  Checks whether a mechanism excludes a named failure path under assumptions when users ask "can text still reach the command runner", "remove this failure path completely", or "does the old loader bypass the fix". Not for bounded response (see robustness), exposure mapping (see susceptibility), or threat review (see security-control-and-security).
---
# Immunity

## Definition and scope

Immunity means a stated mechanism excludes a specified attack or fault class
within explicit assumptions. Keep this local repository meaning narrow;
distinguish controlled behavior under exposure (`robustness`), locating exposure
(`susceptibility`) and broader threat/control work (`security-control-and-security`).

## Use when / Don't use when

- Apply when the requested claim is that a defined mechanism makes a particular
  class unreachable or inapplicable, rather than merely handling tested examples well.
- Route bounded adverse response to `robustness` and exposure/precondition mapping
  without an exclusion claim to `susceptibility`.
- Reject unbounded immune-to-everything language; Ask the user for the exact
  class, protected boundary, mechanism and assumptions before making that claim.

## Workflow

1. Clarify: Read relevant execution code, alternate entrypoints, configuration,
   dependency docs and proposed exclusion arguments before specifying immunity.
   If the class or reachability boundary is undefined, then narrow the claim
   with the user instead of inferring universal exclusion from a clean test report.

2. Specify: Record excluded class, protected effect, mechanism, assumptions,
   reachable paths, bypass conditions, argument, counterexamples and invalidation triggers.
   If the user requests an exclusion review, then propose this bounded claim:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Class/boundary: exact prohibited interpretation or fault path under review.
   Mechanism: source-backed removal/separation of the enabling path, not a label.
   Assumptions: entrypoints, config, loaders, dependencies and permitted environmental state.
   Trial gate: 0 unresolved counterexamples to the scoped exclusion argument.
   Evidence: reachable-path inspection plus synthetic bypass/config-change tests.
   Invalidation: any new path or changed assumption reopens the claim.
   Status: proposed local exclusion case; finite tests alone never establish universal immunity.
   ```

   Ask at most three groups about exact class/effect; mechanism and assumptions;
   and bypasses, claim criteria or permitted validation. Continue to a bounded path argument.
   If no criterion exists, then offer the illustrative counterexample gate and
   confirm with the user/stakeholder before accepting the exclusion scope.

3. Design/Implement: Read [exclusion-argument practices](./references/design-patterns.md)
   when removing an enabling path or checking the assumptions behind it.
   If another reachable path still enables the class, then repair that path or
   narrow/withdraw the claim; filtering a few inputs cannot establish mechanism exclusion.
   If exclusion depends on configuration, then encode and verify that condition
   and its invalidation rather than describing the property as unconditional.

4. Verify: Challenge the structural argument with alternate entrypoints,
   assumption violations and synthetic counterexamples in the approved boundary.
   If tests pass without evidence covering the enabling paths, then report
   bounded test results and leave the exclusion claim unestablished.

5. Report: Return the exact class, mechanism/argument, assumptions, challenges,
   counterexamples, excluded environments and change triggers.
   If any assumption is unresolved, then keep the claim conditional or unsupported;
   never translate it into a universal security or failure-free guarantee.

## Specification patterns

- **Class exclusion:** Under `{explicit_assumptions}`, `{mechanism}` shall exclude
  `{specified_class_at_boundary}`, supported by `{reachable_path_argument}` and
  `{counterexample_challenges}`, with `{bypasses_and_limits}` explicit.
- **Claim invalidation:** When `{assumption_or_path_change}` occurs, mark
  `{exclusion_claim}` unestablished until `{required_argument_and_check_update}`,
  verified by `{configuration_or_new_entrypoint_challenge}`.

Use the illustrative unresolved-counterexample gate to start a missing criterion;
confirm with the user/stakeholder. Ask the user which assumptions the deployed system can actually enforce.

## Rules of thumb

- Don't call rejected examples class exclusion; a handler that accepts the same
  dangerous interpretation elsewhere defeats the structural claim despite those passes.
- Do name the mechanism that removes the enabling path; retry, timeout or cleanup
  after exposure may bound damage without excluding the class from occurring.
- Do include alternate loaders and entrypoints in the reachability argument;
  removing the normal path is insufficient if another supported path still enables it.
- Don't silently move a configuration assumption into an unconditional claim;
  changing that condition must reopen the stated exclusion argument.
- Do distinguish a conditional exclusion argument from absence of observed failures;
  more clean examples cannot repair an unexamined enabling path.

## Verification

Use structural reachability review, configuration-boundary checks and synthetic
counterexample categories. Inspect the exact operation that enables the class,
all declared entrypoints, bypasses and dependency assumptions. Retain failed
challenges as tests, not proofs by enumeration. Record unsupported environmental
conditions and claim invalidation; do not infer formal proof without a checkable argument and its premises.

## Done checklist

- [ ] Define the exact excluded class and protected boundary.
- [ ] Identify the source-backed mechanism and all assumptions it requires.
- [ ] Inspect normal and alternate enabling paths within the declared scope.
- [ ] Challenge bypasses and changed configuration with synthetic cases.
- [ ] Separate test observations from the structural exclusion argument.
- [ ] Record counterexamples, unsupported environments and claim-invalidation triggers.

## Failure modes

- Claiming universal immunity from a clean test or scanner result.
- Filtering a normal input while an alternate path retains the enabling operation.
- Calling post-exposure recovery or cleanup proof the class was excluded.
- Omitting a configuration condition needed for the mechanism to work.
- Retaining the claim after an entrypoint or assumption changes without re-examination.
- Calling a source sketch a formal proof without a checkable argument and premises.

## References

- Read [exclusion-argument practices](./references/design-patterns.md) when defining
  a narrow mechanism claim, its bypasses and its invalidation conditions.
- Read [fixed-handler example](./references/worked-example.md) when absence of a
  string-interpretation path is proposed and an alternate loader may defeat it.
