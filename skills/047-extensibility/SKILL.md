---
name: extensibility
description: >-
  Checks new implementations through an existing hook when users say "add a
  plugin through this hook", "register a report template", or "implement
  another provider against this interface". Requires a pre-existing contract
  that admits the behavior without per-addition core edits. If the hook must
  be built or widened, routes that work to extendability. Not for creating the
  hook (see extendability) or component assembly alone (see composability).
---
# Extensibility

## Definition and scope

Extensibility means new behavior can attach through an existing extension contract
without changing the core implementation for that addition. Define registration,
inputs, outputs, lifecycle, and host boundaries; distinguish creating the seam
through core edits (`extendability`) and general assembly (`composability`).

## Use when / Don't use when

- Apply when a documented hook, provider boundary, or supported registration route
  is supposed to admit a new implementation independently of host source changes.
- Investigate hidden concrete-type switches, undocumented callbacks, and extensions
  that work only after editing the host for each new case.
- Route a missing hook or required core protocol change to `extendability`.
- Route the long-term sequence of extension-contract migrations to `evolvability`.

## Workflow

1. Clarify: Read the host code, hook documentation, registration configuration,
   existing extensions, and contract tests before proposing another implementation.
   Identify which contract actually predates the requested addition and who owns it.
   If no usable contract exists for the new behavior, then Ask the user about a
   core addition and route its implementation to `extendability`.

2. Specify: Record the contract revision, extension obligations, permitted host
   configuration changes, core-source boundary, and loading/removal evidence.
   If the request is to add behavior now, offer this extension agreement:

   ```text
   Illustrative attachment agreement; confirm with the user/stakeholder:
   Extension: the requested provider or handler implementing the existing named contract.
   Host-source target: 0 core source edits per conforming extension in the fixture.
   Registration: documented manifest/configuration route; count it separately from host code.
   Contract: accepted inputs, outputs, failures, lifecycle, and resource/authority boundary.
   Coexistence: retained extensions keep their documented dispatch and behavior.
   Evidence: host-source diff, independent registration, contract cases, removal behavior.
   Open decisions: unsupported contract features, trust model, revisions, and contract owner.
   ```

   Keep questions to three groups: which existing contract fits the new behavior;
   what the extension may access or return; and what registration, lifecycle, or
   compatibility limits apply. Proceed to an adapter design against inspected contracts.
   If the source-edit bound was not given, then propose the illustrative bound
   above and confirm with the user/stakeholder before using it as acceptance evidence.

3. Design/Implement: Read [extension-contract patterns](./references/design-patterns.md)
   when selecting registration, contract adapters, dispatch, and lifecycle boundaries.
   If the host needs a new branch naming the concrete extension, then expose that
   hidden coupling rather than claiming the addition used an unchanged core.
   If an extension requires broader authority or a new contract meaning, then
   obtain that decision and separate it from a conforming implementation change.

4. Verify: Add an independently implemented fixture through the documented route,
   exercise its accepted and rejected contract cases, and compare host source.
   If private host access or new cleanup patches are needed for the fixture, then
   report the existing contract gap instead of certifying unchanged-core admission.

5. Report: Show the contract used, extension-owned changes, host-source comparison,
   registration evidence, retained-extension results, and lifecycle limitations.
   If the contract or host changed during the work, then report that foundational
   change separately and withhold the unchanged-core claim for the original contract.

## Specification patterns

- **Admission:** A conforming `{extension_kind}` shall register through
  `{existing_registration_contract}` and provide `{specified_behavior}` without
  changes outside `{permitted_extension_and_configuration_surface}`, verified by
  `{independent_extension_and_host_diff}`.
- **Contract:** The host shall accept `{conforming_inputs_and_outputs}` and handle
  `{declared_failure_forms}` from `{extension}` according to `{contract_revision}`,
  demonstrated by `{contract_and_dispatch_cases}`.
- **Lifecycle:** Adding or removing `{extension}` shall preserve
  `{retained_extension_and_host_obligations}` under `{documented_lifecycle}`,
  checked by `{coexistence_fixture}`.

Confirm the example core-edit target with the user/stakeholder. Ask the user whether
restarts, registration changes, or persistent extension state are part of the allowed surface.

## Rules of thumb

- Do admit a separately implemented fixture using only the pre-existing public data;
  private built-in access means the claimed existing contract cannot admit that result.
- Do register behavior through the declared route; don't add a host-side switch
  naming each new implementation and call that independent extensibility.
- Do fail activation after acquiring extension resources and exercise the existing
  cleanup contract; host patches needed to undo this fixture defeat per-addition independence.
- Do classify executable registration changes by whether they alter host dispatch;
  hiding a per-provider branch in configuration defeats the unchanged-core admission test.
- Do run the new fixture against the recorded starting host and contract revision;
  passing only after widening that revision proves a new seam, not admission by the old one.

## Verification

Use independent-fixture contract testing, host-diff inspection, registration checks,
and lifecycle exercises. Load a conforming extension and an intentionally rejected
one, inspect dispatch without concrete host branches, and exercise declared failure
and cleanup paths, including the worked failed-activation fixture. Run retained
extensions after failed admission, successful registration, and supported removal.
Compare host and contract revisions with the starting state; distinguish a new
boundary design from evidence that the old boundary already admitted the addition.

## Done checklist

- [ ] Load an independent conforming fixture against the recorded starting host.
- [ ] Inspect host and executable configuration diffs for per-implementation dispatch edits.
- [ ] Reject nonconforming input/output through the documented failure behavior.
- [ ] Fail activation after acquisition and compare resource/registry state after cleanup.
- [ ] Retry activation under the documented lifecycle and inspect duplicate registrations.
- [ ] Run retained extensions after both failed and successful admission attempts.
- [ ] Exercise supported removal and inspect remaining owned resources or state.
- [ ] Trace requested data and authority to public contract provisions; identify
  requested behavior the existing contract cannot admit.

## Failure modes

- Introducing the hook and calling the same change an addition through an existing hook.
- Depending on private host state that an independent implementation cannot access.
- Adding a concrete host branch for each new provider while claiming an unchanged core.
- Treating a plugin name as proof of isolation, compatibility, or unload support.
- Passing activation retry while a failed attempt still owns subscriptions or keys.

## References

- Read [extension-contract patterns](./references/design-patterns.md) when defining
  a registration route, independent contract fixture, or lifecycle evidence.
- Read [formatter-hook example](./references/worked-example.md) when checking whether
  admission through the existing hook and cleanup after a failed activation.
