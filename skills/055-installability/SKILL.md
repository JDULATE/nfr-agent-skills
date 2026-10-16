---
name: installability
description: >-
  Checks installation state when asked "fix partial upgrades", "start a clean install", or "keep user data on uninstall". Ask the user if setup on one target vs platform adaptation is unclear. Not for moving between execution platforms (see portability) or deployment uptime (see availability).
---

# Installability

## Definition and scope

Installability means an application can be placed, upgraded, or removed in a
specified target environment with its installation state understood. Define
prerequisites, owned resources, activation, and retained user data; distinguish
adapting to another platform (`portability`) and keeping service usable through
deployment (`availability`) from the installation lifecycle itself.

## Use when / Don't use when

- Apply when a supported target cannot complete a clean installation.
- Apply when an upgrade leaves a mixed installation or removal deletes user-owned data.
- Route source-to-target environment adaptation to `portability`.
- Route outage-free deployment as the acceptance question to `availability`.
- Route an ongoing runtime operator procedure to `operability` after installation is settled.

## Workflow

1. Clarify: Read packaging, setup/removal code, service registration, version
   discovery, storage ownership, migration notes, and target prerequisites first.
   Identify clean, existing, partial, and removed installation states.
   If ownership, data retention, or supported upgrade paths are unknown, then
   Ask the user before proposing deletion or rollback behavior.

2. Specify: Record the target prerequisites, starting installation state, owned
   resources, user-owned data, activation predicate, failure result, and removal policy.
   If no lifecycle contract exists, then propose labeled illustrative defaults:
   stage app-owned artifacts before activation, preserve user data, and track owned
   resources for removal; confirm with the user/stakeholder.
   Keep data-schema rollback and service interruption as separate explicit decisions.

3. Design/Implement: Read [installation decisions](./references/design-guide.md)
   when selecting staging, activation, resource ownership, or cleanup behavior.
   If setup cannot establish a prerequisite, then stop before activation and report
   the unresolved dependency. If an upgrade fails while staging, then retain the
   known installed version and expose the partial resources for controlled cleanup.
   If removal encounters an unowned resource, then retain it pending an ownership decision.

4. Verify: Rehearse clean install, supported upgrade, interrupted staging, and
   removal on synthetic or otherwise authorized targets. Inspect registrations and data.
   If files exist but the installed application cannot perform its required startup
   check, then do not report installation success.
   Retain failed steps, unfinished cleanup, and starting-state differences.
   Read [lifecycle example](./references/worked-example.md) for filled before/after cases.

5. Report: Return the supported lifecycle paths, installed/partial state,
   activation evidence, removal results, and retained resources.
   If schema or live-service continuity was not checked, then state those boundaries
   rather than implying that successful setup proves safe deployment or rollback.

## Specification patterns

- **Install:** From `{declared_start_state}` on `{supported_target}`, setup shall
  establish `{owned_artifacts_and_registrations}` and activate only after
  `{prerequisite_and_startup_checks}`.
- **Upgrade:** During `{supported_upgrade_path}`, failure at `{staging_boundary}`
  shall leave `{known_installation_state}` and identify `{partial_owned_resources}`,
  preserving `{confirmed_user_data_policy}`.
- **Removal:** Removal shall delete only `{owned_resource_set}`, retain
  `{user_owned_or_unresolved_resources}`, and verify `{remaining_registration_state}`.

For missing numeric targets, use the illustrative lifecycle predicates in Specify
and confirm with the user/stakeholder. Do not invent an installation-time promise.

## Rules of thumb

- Do discover an existing installation before choosing the upgrade path;
  treating it as an empty target cannot define which older resources are replaced.
- Do remove from an explicit ownership record, not by deleting a convenient
  parent directory that also contains user projects.
- Do activate a coherent staged artifact set; changing the active entrypoint
  after only part of the new installation is present creates a mixed lifecycle state.
- Do tie startup registrations to the installed resource set and its cleanup;
  a failed setup must not leave a launcher pointing at nonexistent app files.

## Verification

Use installation-state fixtures, package inspection, failure injection, and
startup smoke-check categories.
Inspect prerequisites and resource permissions before writing app-owned paths.
Check startup using the installed entrypoint, not a developer working tree.
Interrupt staging before activation and inspect the old active version and partial set.
Remove the app and inspect both startup registration absence and user-data retention.
Retain original failures and cleanup gaps rather than reporting a successful retry
as if the initial attempt left no installation state.
Separate app-artifact rollback from unverified data-schema reversibility.

## Done checklist

- [ ] Identify clean, existing, partial, and removed starting states.
- [ ] Establish supported prerequisites and upgrade paths.
- [ ] Separate app-owned resources from retained user data.
- [ ] Exercise startup through the installed entrypoint.
- [ ] Inspect interruption before activation and the resulting partial state.
- [ ] Verify startup registration matches the active installation.
- [ ] Remove only owned resources and check retained data.
- [ ] Report unsupported rollback and continuity claims explicitly.

## Failure modes

- Declaring success because archive extraction completed.
- Running the fresh-install path over an undiscovered existing installation.
- Activating a partially staged upgrade.
- Removing an entire shared directory instead of the owned resource set.
- Leaving startup registration after its target files were removed.

## References

- Read [installation decisions](./references/design-guide.md) when selecting
  staging, activation, ownership, and removal boundaries.
- Read [lifecycle example](./references/worked-example.md) when checking clean
  installation, interrupted upgrade, retry, and user-data-preserving removal.
