---
name: susceptibility
description: >-
  Maps exposure and enabling conditions without presuming exploitation when users ask "does this dependency issue affect us", "can the importer reach that code", or "is the disabled endpoint our only route". Not for mechanism exclusion (see immunity), bounded adverse response (see robustness), or active containment (see defensibility).
---
# Susceptibility

## Definition and scope

Susceptibility means exposure and preconditions explain where a specified adverse
influence can affect the system. Map reachable, blocked and unknown paths;
distinguish excluding a class (`immunity`), controlled response (`robustness`)
and active adversarial intervention (`defensibility`).

## Use when / Don't use when

- Apply when a team needs to know which input, capability, configuration or
  dependency makes a particular adverse effect possible in its actual environment.
- Route a mechanism-backed exclusion claim to `immunity`.
- Route threat/control prioritization beyond the scoped exposure path to
  `security-control-and-security`; exposure evidence is an input, not a complete security verdict.

## Workflow

1. Clarify: Read entrypoint/data-flow code, deployment and permission config,
   dependency docs and adverse-condition evidence before classifying exposure.
   If the influence, affected effect or relevant environment is unknown, then
   Ask the user rather than inferring exposure from a component name alone.

2. Specify: Record influence, entrypoint, required capability, trust crossings,
   configuration, reachable effect, blocked preconditions, uncertainty and evidence.
   If the user requests exposure analysis, then offer this path record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: stated adverse influence and actual repository/deployment context.
   Path: source -> entrypoint -> prerequisites -> affected operation/result.
   States: reachable, blocked by verified condition, or unknown; do not collapse unknown to safe.
   Trial gate: 0 unsupported exposure classifications in the agreed path fixtures.
   Evidence: source/config/permission observations and synthetic precondition challenges.
   Limits: reachability is not evidence of successful exploitation or a universal immunity claim.
   Output: located paths, missing facts and candidate control boundaries, not invented severity scores.
   ```

   Ask at most three groups about influence/effect/environment; capabilities and
   configuration; and classification, validation or control-priority needs.
   Continue to a source-backed path map with unobserved deployment facts marked unknown.
   If no criterion exists, then propose the illustrative classification gate and
   confirm with the user/stakeholder before accepting its fixture/environment scope.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [exposure-path practices](./references/design-patterns.md)
   when distinguishing prerequisites, apparent blockers and actual affected boundaries.
   If a blocker is assumed rather than observed, then retain unknown reachability
   and identify the minimal source/config evidence needed to resolve it.
   If the task includes reducing exposure, then change the confirmed precondition
   or entrypoint and recheck alternate paths rather than assuming the label alone fixes it.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Trace declared paths and challenge relevant capabilities/configurations
   with synthetic fixtures inside the authorized validation boundary.
   If input reaches the operation but the harmful effect is untested, then report
   that distinction instead of labeling the path a demonstrated successful attack.

5. Report: Return the precondition/path map, observed blockers, unknown environment
   facts, scoped changes and unresolved alternative paths.
   If an enabling condition changes, then reopen the classification; an earlier
   blocked path does not establish permanent inapplicability.

## Specification patterns

- **Exposure map:** For `{adverse_influence_and_environment}`, classify
  `{entrypoint_to_effect_path}` under `{capability_and_configuration_preconditions}`
  as `{reachable_blocked_or_unknown}`, supported by `{source_and_challenge_evidence}`.
- **Precondition change:** After `{exposure_reducing_change}`, reassess
  `{affected_and_alternate_paths}`, retaining `{unknowns_and_effect_limits}`
  rather than inferring `{universal_exclusion_or_successful_exploitation}`.

Use the illustrative unsupported-classification gate if no criterion exists;
confirm with the user/stakeholder. Ask the user for missing deployment facts before declaring blocked exposure.

## Rules of thumb

- Do keep unknown separate from blocked; missing configuration evidence cannot
  establish that the adverse influence lacks a route to the affected operation.
- Don't infer exposure solely from a dependency name; the relevant capability,
  configuration and reachable invocation must fit the specified influence.
- Do distinguish reachable operation from demonstrated adverse effect;
  locating an input path does not establish that exploitation actually succeeded.
- Do preserve each blocking precondition and its evidence; changing that condition
  can reopen exposure even when no application source changed.
- Don't promote a blocked current path to permanent class exclusion; alternate
  entrypoints and future configuration changes remain separate evidence obligations.
- Do trace internal and background paths for the declared influence as well as
  public routes; absence from the visible interface does not establish non-exposure.

## Verification

Use source/data-flow review, configuration/permission inspection and synthetic
precondition toggles. Retain source, entrypoint, capabilities, blockers, environment,
affected operation and effect evidence separately. Check alternative invocation
paths within scope. Distinguish static reachability, observed invocation and actual
adverse result; no component inventory or guessed vulnerability label substitutes for that chain.

## Done checklist

- [ ] Define influence, environment and affected operation/result.
- [ ] Trace entrypoints and required capabilities/configurations to that operation.
- [ ] Classify paths as reachable, verified blocked or unknown with evidence.
- [ ] Challenge material preconditions and inspect declared alternative invocations.
- [ ] Separate reachability from observed adverse effects and exploitation claims.
- [ ] Record condition-change triggers and unresolved deployment facts.
- [ ] Verify any requested exposure reduction against affected and alternate paths.

## Failure modes

- Calling a path safe because its configuration was not available to inspect.
- Declaring exposure from a package name without a relevant invocation/precondition path.
- Treating reachable input as proof an adverse outcome occurred.
- Ignoring an internal/background invocation absent from the public interface.
- Leaving a blocked classification unchanged after its prerequisite changes.

## References

- Read [exposure-path practices](./references/design-patterns.md) when choosing
  preconditions, evidence states or a minimal check for unknown reachability.
- Read [import-entrypoint example](./references/worked-example.md) when a disabled
  route, a background importer and unknown deployment config imply different classifications.
