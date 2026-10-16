# Capability-to-task fit decisions

Use the real task constraints and receiver contract.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Export returns a retrieval token but the receiver has no network | Add a supported local artifact path | Local file handling becomes part of the workflow | Disconnect retrieval and run the actual receiver from the local artifact |
| Existing structured export cannot be consumed by the required line importer | Add an explicit task-format adapter | Adapter must preserve all task-essential fields | Compare source records with parsed receiver records |
| Zero quantities disappear during formatting | Emit valid zero values explicitly | Cannot use a truthiness shortcut for omission | Handoff a zero-quantity record and inspect the received value |
| A source field contains the receiver's unescaped separator | Refuse that case or agree on a supported encoding/receiver change | Some source inputs remain outside task fit | Exercise the exact separator case without silent rewriting |

## Local artifact sketch

Illustrative pseudocode for the supplied line-format contract.

```text
export_for_receiver(rows):
    if any("|" in row.sku or newline_in(row.sku) for row in rows):
        return UnsupportedField
    lines = ["sku|units"]
    for row in rows:
        lines.append(row.sku + "|" + integer_text(row.units))
    return LocalArtifact(join_with_newlines(lines) + final_newline)
```

The fixture supplies integer unit values and a matching receiver.
Do not infer a general escaping rule or encoding standard.
A local artifact is not fit until the named receiver has accepted it.

## Adaptation boundary

Keep receiver replacement and manual re-entry outside the accepted workflow
unless the stakeholder agrees to them.
An adapter changes task fit; it does not prove effectiveness across real users.
