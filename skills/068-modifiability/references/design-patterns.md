# Bounding a specific implementation edit

Use the named edit to choose the analysis surface. A generic dependency graph or
small diff cannot establish a bound for unspecified future work.

## Semantic impact map

- **Use when:** Edited logic writes meanings that other components consume. Map
  direct calls, stored outputs, schema consumers, and generated adapters.
- **Trade-off:** A broad map costs investigation effort; an import-only map can
  miss consumers that interpret the changed data without calling the edited code.
- **How to verify:** Reconcile observed consumer behavior and the complete diff with
  the prediction; record newly discovered semantic dependencies as forecast errors.

## Edit seam chosen from fan-out

- **Use when:** Duplicated interpretations make the named change spread. Identify
  the responsibility that owns the rule before introducing a shared seam.
- **Trade-off:** Consolidation can move responsibilities together without reducing
  coordination. More abstraction is not automatically less change work.
- **How to verify:** Trace this edit through the proposed seam and show which
  consumer-specific modifications it actually removes or still requires.

## Work ledger with scope accounting

- **Use when:** Stakeholders need evidence of change cost. Separate owner impact,
  investigation, implementation, verification, migration, coordination, and waits.
- **Trade-off:** Time estimates can conceal incomplete work or inconsistent units.
  Module counts depend on packaging and cannot replace effort observation.
- **How to verify:** Compare predicted and actual tasks, preserve extra owners,
  and reconcile the ledger with artifacts and included work categories.

## Requirement record

Retain edit identity, allowed behavior delta, preserved cases, counted owner and
contract surfaces, full dependency impact, effort convention, exceptions, and evidence.
An illustrative bound is 2 production owner components under an agreed ownership map;
confirm with the user/stakeholder. Disclose non-production, generated, and migration
work even when that particular source count excludes it. Ask the user for actual
scope and effort bounds; a forecast remains a forecast until the work is observed.
