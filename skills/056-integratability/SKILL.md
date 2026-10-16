---
name: integratability
description: >-
  Bounds assembly work when asked "reduce adapter glue", "wire agreed message contracts", or "assign integration ownership". Ask the user if wiring effort vs exchanged meaning is unclear. Not for exchange meaning (see interoperability).
---

# Integratability

## Definition and scope

Integratability means separately developed pieces can be assembled into a working
solution within an agreed integration change surface and effort boundary.
Inspect bindings, prerequisites, adapters, and ownership of glue code.
Separate assembly effort from exchange meaning (`interoperability`) and from
setup of a supplied deployment (`installability`).

## Use when / Don't use when

- Apply when components work independently but connection requires unexpected
  wiring, undocumented prerequisites, or edits across unrelated component internals.
- Include repository assembly code, configuration contracts, composition tests,
  and the integration instructions an implementer actually follows.
- Route ambiguous units or response meaning to `interoperability`.
- Route a ready-made deployment's installation procedure to `installability`;
  do not inflate routine setup into component integration redesign.

## Workflow

1. Clarify: Read component interfaces, composition roots, configuration loaders,
   startup dependencies, adapter code, and integration docs before specifying.
   Reconstruct the connection from checked-in artifacts rather than an author's
   remembered setup.
   If the request is merely "connect them," then Ask the user whether assembly
   work, exchange behavior, or deployment setup is failing.

2. Specify: Name supplied components, permitted glue changes, prerequisites,
   integration owner, effort accounting boundary, and a runnable connected result.
   If an effort budget is absent, then propose this labeled illustrative default:
   wire supplied interfaces through the composition layer without editing
   component internals; confirm with the user/stakeholder.
   Count actual tasks, waiting dependencies, and unplanned edits separately.
   For a fix, ask at most three questions covering the desired path, allowed
   change surface, and the supplied prerequisites before moving to design.

3. Design/Implement: Read [assembly decisions](./references/design-guide.md)
   when introducing bindings, prerequisite validation, or an adapter seam.
   If configuration names differ, then map them explicitly at the composition
   boundary rather than teaching each component every neighbor's settings.
   If a required interface is absent, then expose the missing component work
   and seek a revised boundary instead of counting it as invisible glue.

4. Verify: Assemble from a clean declared state, run the connected smoke path,
   and retain the edit/task ledger and missing-prerequisite outcomes.
   If the run relies on manual state not in the supplied setup, then report
   assembly as unreconstructed until that dependency is documented or removed.

5. Report: Deliver the wiring diff, prerequisite list, owner map, connected
   result, effort observations, and deviations from the agreed change surface.
   If smoke execution passes but semantic exchange checks were not performed,
   then state that limitation rather than claiming full interoperability.

## Specification patterns

- **Assembly boundary:** Given `{supplied_components_and_prerequisites}`, an
  integrator shall establish `{connected_path}` by changing only
  `{permitted_glue_surface}`, verified by `{clean_assembly_and_edit_ledger}`.
- **Effort:** Assembly of `{component_set}` shall fit `{confirmed_effort_boundary}`,
  counting `{implementation_configuration_waiting_and_rework_rules}` and
  producing `{runnable_evidence}`.

When no numeric budget exists, use the illustrative change-surface default in
Specify; confirm with the user/stakeholder rather than inventing a duration.

## Rules of thumb

- Keep environment-to-component bindings in the composition boundary; requiring
  each component to know its neighbor's deployment vocabulary expands assembly work.
- Charge a missing adapter or prerequisite to the integration ledger even when
  its implementation belongs to another team; "provided elsewhere" is not supplied.
- Distinguish an adapter using public interfaces from edits to both components'
  internals; the latter changes the declared integration surface.
- Keep the connected smoke path executable from the supplied prerequisites;
  undocumented manual registrations make the claimed assembly unreconstructable.

## Verification

Use clean-workspace assembly, configuration validation, source-diff inspection,
and connected smoke-test categories.
Record attempted tasks, actual edited paths, unresolved dependencies, and observed
results, including failed setup steps. Do not subtract waiting or rework silently.
Check that a missing required input fails with a named prerequisite before
downstream execution.
Inspect whether a test bypasses the real composition root.
Use semantic contract tests separately when the request also includes exchange
meaning; launching both processes is insufficient evidence for either concern.

## Done checklist

- [ ] Enumerate supplied interfaces and prerequisites.
- [ ] Map environment settings to their component bindings.
- [ ] Reconstruct the composition from the declared clean state.
- [ ] Exercise the connected result through actual wiring.
- [ ] Compare edited paths with the permitted change surface.
- [ ] Account for missing prerequisites, waiting, and unplanned component work.
- [ ] Check actionable refusal when a required binding is absent.
- [ ] Separate assembly evidence from untested exchange semantics.

## Failure modes

- Editing private component internals while reporting configuration-only assembly.
- Hiding a required manual registration outside the integration instructions.
- Excluding another team's missing interface from the work needed to connect.
- Testing direct component calls that bypass the shipped composition.

## References

- Read [assembly decisions](./references/design-guide.md) when bounding glue,
  configuration mapping, or prerequisite work.
- Read [worker-binding example](./references/worked-example.md) when comparing a
  clean assembly attempt with the actual edited files and connected result.
