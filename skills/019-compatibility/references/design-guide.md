# Coexistence decisions

Use this guide after identifying both components' protected operations.
Choose interventions against an observed collision, not the word "compatible."

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Both tools write the same settings key and one loses its preference | Scope writable keys by component identity; migrate legacy keys with an explicit owner | Extra migration and old-key handling | Set different preferences, start both in each order, inspect independent reads |
| One installer changes a dependency used by the neighbor | Resolve dependencies within separate consumer boundaries, or negotiate an agreed shared revision | Larger deployment surface or narrower supported matrix | Inspect actual resolutions and execute each consumer's protected operation |
| Removing a tool deletes the neighbor's directory | Generate cleanup from owned resources rather than the entire host directory | Ownership metadata needs maintenance | Remove each neighbor and compare survivor paths and results |
| Both components require exclusive use of the same host resource | Allocate distinct resources or state a mutually exclusive combination | Additional resources or an explicit support restriction | Attempt the protected operations together and check the advertised restriction |

## Namespace sketch

Illustrative pseudocode; adapt to the repository's actual settings API.

```text
settings_key(component, field):
    return ("component", component.identity, field)

write(settings_key(report_tool, "theme"), "dark")
write(settings_key(preview_tool, "theme"), "light")
assert read(settings_key(report_tool, "theme")) == "dark"
assert read(settings_key(preview_tool, "theme")) == "light"
```

Do not derive identity from a mutable display name if renaming would orphan keys.
Inspect legacy readers before moving storage; isolation alone does not migrate them.
If either component intentionally reads a shared preference, then retain that
declared contract rather than applying isolation indiscriminately.

## Decision boundary

A payload rejected by a neighbor is an exchange-contract problem.
A neighbor overwriting the sender's settings is coexistence interference.
Both may occur in the same deployment; retain separate evidence.
