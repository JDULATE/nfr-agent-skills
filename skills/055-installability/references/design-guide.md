# Installation lifecycle decisions

Use these decisions for one declared supported target, not a platform migration.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| Setup assumes every target is empty. | Discover installed state and select an explicit upgrade path. More start states need handling. | Run against an existing owned installation and inspect replacement decisions. |
| An interrupted upgrade exposes mixed artifacts. | Stage a complete app-owned set and activate through a coherent entrypoint change. Extra staging space may be needed. | Fail during staging and check that the old installed entrypoint still works. |
| Removal deletes user projects. | Track app ownership separately from user data and remove by that ledger. Uncertain resources may remain. | Add an unowned neighbor file and verify it survives removal. |
| Files are installed but startup is impossible. | Check prerequisites and the actual installed entrypoint before success. Setup may remain incomplete. | Exercise the startup path without developer-tree resources. |
| Failed setup leaves a dangling launcher. | Include startup registration in lifecycle ownership and cleanup. Cleanup itself can fail and must be reported. | Interrupt registration or remove files and inspect the remaining launcher state. |

## Staging sketch

```text
existing = discover_installation()
require supported_start_state(existing)
require target_prerequisites_satisfied()
journal = record_lifecycle_plan(existing, confirmed_resource_ownership)
staged = stage_owned_artifacts(journal)
if not staged.complete:
  return partial_installation(existing.active, staged.owned_resources)
activate_complete_set(staged, journal)
register_installed_entrypoint(journal)
record_activation_and_registration_state(journal)
verify_installed_entrypoint()
```

Activation is an abstract lifecycle operation, not a guarantee supplied by a
particular filesystem. Choose a supported mechanism for the actual target.
Keep resource-creation progress in the journal before declaring startup success;
a failed startup still leaves an installation state to inspect and clean up.

## Removal boundary

Use the recorded app-owned set and current ownership checks.
Preserve user data unless the user explicitly chose another policy.
If ownership changed since installation, report the conflict instead of broadening deletion.

Artifact rollback does not imply that a data migration can be undone.
Keep that decision outside an otherwise reversible staging plan until established.
