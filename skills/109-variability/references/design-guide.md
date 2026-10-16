# Product-family variation decisions

Separate valid feature selection from successful artifact derivation.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Export builds without the audit capability it requires | Encode export implies audit before derivation | Some previously accepted selections refuse | Test export/audit combinations including audit without export |
| Sync is selected with an unsupported local store | Add the declared sync/store dependency | Limits which editions can exist | Enumerate store and sync choices and inspect named refusal |
| Invalid selections leave generated modules behind | Validate the full selection before creating artifacts | Validation must know the relevant constraints first | Start with empty output and inspect it after refusal |
| A valid enabled feature disappears from the build | Map features explicitly to emitted artifacts | Derivation mapping needs maintenance | Compare the selected feature set with actual module manifest |

## Pre-derivation sketch

Illustrative pseudocode for the supplied edition model.

```text
derive(selection):
    if selection.sync and selection.store != "remote":
        return Refused("sync-needs-remote")
    if selection.export and not selection.audit:
        return Refused("export-needs-audit")
    artifacts = [selection.store + "-store"]
    if selection.sync: artifacts.append("sync")
    if selection.audit: artifacts.append("audit")
    if selection.export: artifacts.append("export")
    return artifacts
```

Validate field presence and allowed values before applying this sketch.
Do not treat refusal as permission to disable the requested feature silently.

## Binding boundary

These are build-time choices in this fixture.
If the same fields become live settings, they need their own configuration
validity and transition behavior; this model supplies neither automatically.
