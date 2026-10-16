# Comparable-peer alignment decisions

Use a selected convention and a defined peer set.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Equivalent list operations name page size differently | Map each handler to the canonical field and meaning | Existing callers may need aliases | Send the same canonical request to all peers and compare result size |
| Documentation matches but a handler still reads an old field | Change the actual input path and update its contract fixture | A documentation-only fix is insufficient | Exercise the shipped handler rather than a rewritten example |
| Old and canonical names can both be supplied | Define a common conflict refusal or resolution rule | More explicit compatibility handling | Supply conflicting values on each peer |
| A similar-looking parameter controls bytes rather than item count | Keep a semantic exception with distinct naming and explanation | The interface remains intentionally nonidentical | Check the budget's actual effect before including it in the page-size peer set |

## Canonical paging sketch

Illustrative pseudocode for the selected fixture convention.

```text
page_limit(args):
    canonical = args.get("page_limit")
    alias = args.get("pageSize")
    if canonical exists and alias exists and canonical != alias:
        return ConflictingLimit
    return canonical if canonical exists else alias
```

Validate presence and value domain under the actual paging contract.
The fixture supplies a positive limit in every successful case.
Do not invent a default or general precedence rule for other APIs.

## Peer boundary

The same parser can support uniformity, but sharing code alone does not establish
that every handler uses the resulting limit.
Inspect the response and side effects of each comparable operation.
