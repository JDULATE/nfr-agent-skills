# Adjustability repair findings

This repair was tuned on the scratch-project run, using the user-supplied findings. The scratch project itself was not rerun here; this is a targeted workflow correction, not independent held-out behavioral validation.

## Workflow and scope findings

- Both adjustability and configurability now handle an absent runtime setting surface explicitly. The first step starts with configurability design guidance, settles value location and permitted caller, and then uses adjustability for applying the new scalar value.
- Adjustability now requires a consolidated user-visible proposal block before any implementation. It covers domain, units, retained default, application boundary, running-work behavior, interface, persistence, permitted caller, rollback, evidence, trade-offs, and offered extensions.
- Questions are capped at three and limited to unresolved valid-domain/units and running-work semantics not supplied by the user or established by the code. Defaultable choices remain labeled proposals. Unresolved application semantics block implementation; the proposal block does not demand blanket approval for ordinary authorized work.
- The minimum implementation is a validated setting read at its agreed point of use with the existing default. Authentication, persistence, a new server, and response headers are offered extensions requiring the user's yes unless already explicitly authorized.
- The adjustability design reference includes a hardcoded-constant card with observed evidence, intervention, trade-off, verification, and a sequential code sketch. The configurability reference supplies the missing-surface location/caller decisions.
- All three skills distinguish a consumer-applied value readback plus a behavior probe from revision evidence. Readback suffices for an unambiguous synchronous consumer; applied revisions or equivalent identities are needed when asynchronous, overlapping, repeated, or partial changes require correlating a particular application with work. A requested or saved revision is not applied evidence.
- Reconfigurability retains ownership/checkpoint evidence for real arrangement transitions and routes scalar-only changes to adjustability. Configurability's earlier blanket routing of application timing to reconfigurability was narrowed to match this boundary.
- Descriptions, catalogue records, eval prompts, answer keys, scripts, and all other skills are unchanged.

## Verification findings

- Full repository validator: 114 skills checked, zero errors. The final targeted validator on 6,27,79 also passes.
- Full unittest suite: 38 tests passed.
- Supplemental Skill Creator validation: all three skills pass.
- The actual Python sketch was extracted and executed with an injected default, domain predicate, and operation. Default behavior, valid updates, rejection without mutation, rollback, captured running-work values, and the next work unit using the new value all passed.
- No concurrency, durable-store behavior, remote authorization, or asynchronous revision implementation is established by that sequential sketch. Those remain context-dependent design decisions.

| Skill | Body lines | Description characters | Combined entrypoint and references |
| --- | ---: | ---: | ---: |
| 006-adjustability | 151 | 261 | 258 |
| 027-configurability | 132 | 312 | 225 |
| 079-reconfigurability | 131 | 344 | 220 |

Each supporting file remains below 150 lines, and each design reference remains within the 80-line guide limit. Reference counts:
- 006-adjustability: design-patterns.md 62 lines, worked-example.md 40 lines.
- 027-configurability: design-patterns.md 51 lines, worked-example.md 37 lines.
- 079-reconfigurability: design-patterns.md 49 lines, worked-example.md 35 lines.

## Routing findings

The three existing eval files supply 24 case occurrences, deduplicated to 12 unique unchanged blinded prompt IDs. A fresh ephemeral CLI session, with user configuration ignored and no model override, received only the complete current slug/description catalogue and those unlabeled prompts. Neither the answer key nor the changed skill bodies were supplied. The transcript contains no tool calls.

Routing scoring matched 12/12: 6/6 explicit and 6/6 vague, with no misses. No H-prefixed held-out case was included or rerun. Descriptions were unchanged, so this result checks routing compatibility; it does not establish that an agent will execute the repaired workflow correctly.

| Prompt ID | Frozen acceptable choice | Observed choice |
| --- | --- | --- |
| r-3426cfe6d588294e | ask | ask |
| r-5858847318a21069 | configurability | configurability |
| r-591489b007912170 | ask | ask |
| r-5929e4dc4b473e3c | ask | ask |
| r-6509479e01b66713 | adjustability | adjustability |
| r-789b5ac3aa251075 | ask | ask |
| r-7f9059bd6e2f24b0 | reconfigurability | reconfigurability |
| r-829ee8d31c479410 | configurability | configurability |
| r-860bde7ea61265ef | ask | ask |
| r-ab3c6352559e382b | adjustability | adjustability |
| r-ae194021d852b1f9 | ask | ask |
| r-c7490e02d72a00ae | reconfigurability | reconfigurability |

The read-only lexical scorer evaluated 24 cases across the three skills; 12 omit the distinguishing fact. Its overlapping heuristic flags remain: expected_not_top 8; near_pair_no_signal 4; near_target_outranks_sibling 1; no_keyword_signal 3; top_tie 2. These are not semantic routing failures; no description was changed to satisfy the heuristic.

Fresh routing session: 01a1466a-f8e8-7a32-a3d8-96e266af7abd. CLI arguments and neutral instructions were reused from evals/routing-fixes-8/baseline-run.json; CLI model name was not reported. Catalogue SHA-256: 1847f47dca38d2e24bcbcd4dc559d8500c409f72c1db442b0a4320cf809ca9c6. Prompt SHA-256: 03d3e26f542e7b31e67bd807ec653a21827f80ffdec328618b4177e7c67a81d5.

## Remaining uncertainty

The repair reflects the reported scratch-run failure and has not been tested through a fresh end-to-end coding-agent implementation. The sequential sketch and description routing checks do not cover all worker models. Actual valid domains, units, allowed running-work semantics, and extension authorization still depend on the inspected project and user decisions. No new external standards or empirical performance claims were introduced.
