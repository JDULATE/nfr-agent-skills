# Context-reuse decisions

Bound adaptation against a concrete consumer rather than hypothetical reuse.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Checker reads rows from an ambient web request | Accept explicit row data and move request decoding to the web adapter | Existing calls need migration | Invoke from CLI with no web context and compare original web outcomes |
| CLI copies the validation branches | Replace the copy with an invocation of the shared checker | Both contexts now depend on its contract | Trace both entrypoints to the same artifact revision |
| Shared checker formats web responses | Return domain findings and let each context present them | Presentation adapters become explicit | Compare common findings with context-specific output envelopes |
| Reuse requires original-context privileges unrelated to checking | Keep consumer authority checks at their own boundaries | Context policies may differ | Exercise validation without granting unrelated web privileges |

## Shared-input sketch

Illustrative pseudocode for an import-row checker.

```text
check_rows(rows):
    return [MissingName(row.id) for row in rows if row.name is empty]

web_check(request):
    findings = check_rows(decode_web_rows(request))
    return web_findings_response(findings)

cli_check(file_rows):
    findings = check_rows(file_rows)
    return cli_findings_output(findings)
```

Do not move decode_web_rows into the shared checker merely to keep an old
signature. The artifact's boundary should describe its actual operation.

## Adaptation ledger

Record shared code edits, consumer adapter edits, dependency setup, and policy
questions separately. Shared reuse does not imply zero adaptation.
If the shared contract must change, compare both consumers before accepting it.
Do not treat matching output from duplicated code as artifact identity evidence.
