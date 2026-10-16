# Environment adaptation decisions

Use explicit profiles rather than assumptions about a real platform.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The source working directory doubles as an output root. | Supply a profile-specific artifact-root resolver. More configuration needs validation. | Change the target working directory and locate the required output. |
| Target-specific branches spread into business calculations. | Move capability resolution behind a platform boundary. An adapter contract must be maintained. | Review the diff and run the same domain fixture through both adapters. |
| The target lacks a required runtime operation. | Provide an accepted equivalent or declare that capability unsupported. Behavior may need a reviewed restriction. | Exercise the operation through the target boundary rather than its platform label. |
| Generated artifacts are copied without checking their target contract. | Rebuild or replace them when the declared target requires it. Extra build work may be needed. | Load and execute the required artifact in the actual target profile. |
| Build and installation pass but outputs differ. | Compare content, side effects, and required artifact location. Verification extends beyond startup. | Run a common input and inspect each required consequence. |

## Platform-boundary sketch

```text
profile = read_confirmed_target_profile()
artifact_root = profile.required_artifact_root
require writable_artifact_capability(artifact_root)
content = unchanged_domain_renderer(input)
write_artifact(artifact_root, "report-elm.csv", content)
```

The sketch does not claim any real host supplies that capability.
Its supported operation must be established for the actual target.

## Adaptation ledger

Record assumption, source behavior, target capability, chosen adaptation, and
preserved observable. Keep any changed domain behavior as a separate decision.

If the target cannot satisfy a required consequence, report that gap.
Do not silently relax the contract so the migration can be called successful.
