# Phase 6 final findings

All 114 NFR skills and the new selector remain draft. No release tag was created. This is a development snapshot, not an assertion that the catalogue is reviewed or that its Workflows are proven.

## Counts and structural checks

- 115 skill folders: 114 NFRs plus 000-nfr-selector. The 114-entry nfr-list.json is unchanged; selector.json records the separate draft selector.
- 115 per-skill eval files; 920 should-trigger/near-miss case occurrences. The blinded prompt/key files contain 510 rows and 507 unique prompt texts, including 12 held-out rows and eight new selector rows. Some selector controls intentionally repeat existing single-quality prompts.
- Every skill body is at most 250 lines and every description at most 350 characters. No skill has fewer than three Rules of thumb bullets.
- Rule-count distribution: 3 bullets: 21 skills, 4 bullets: 35 skills, 5 bullets: 24 skills, 6 bullets: 31 skills, 7 bullets: 3 skills, 8 bullets: 1 skills. These are content counts, not quality scores.
- AGENTS.md and CONTRIBUTING.md were not changed. All existing NFR skill bodies and descriptions were preserved.

## Validator and test output

The repository validator, full test suite, index builder, and lexical checker exited successfully. Output below is from this revision; the index count was checked after correcting an intermediate summary-only count bug.

```text
Checked 115 skill(s); 0 absent todo skill(s); 0 error(s).

python -m unittest discover -s tests -v
test_cli_json_text_warnings_and_errors (test_descriptions.DescriptionTests.test_cli_json_text_warnings_and_errors) ... ok
test_eval_identity_counts_duplicates_and_siblings_are_validated (test_descriptions.DescriptionTests.test_eval_identity_counts_duplicates_and_siblings_are_validated) ... ok
test_known_todo_sibling_is_unscored_not_fabricated (test_descriptions.DescriptionTests.test_known_todo_sibling_is_unscored_not_fabricated) ... ok
test_missing_eval_description_and_insufficient_vague_coverage_fail (test_descriptions.DescriptionTests.test_missing_eval_description_and_insufficient_vague_coverage_fail) ... ok
test_near_miss_outranks_named_sibling (test_descriptions.DescriptionTests.test_near_miss_outranks_named_sibling) ... ok
test_only_keeps_all_authored_competitors_and_is_read_only (test_descriptions.DescriptionTests.test_only_keeps_all_authored_competitors_and_is_read_only) ... ok
test_only_rejects_invalid_unknown_and_todo_ids (test_descriptions.DescriptionTests.test_only_rejects_invalid_unknown_and_todo_ids) ... ok
test_positive_ties_are_preserved_and_zero_signal_is_not_a_winner (test_descriptions.DescriptionTests.test_positive_ties_are_preserved_and_zero_signal_is_not_a_winner) ... ok
test_selector_competes_without_changing_nfr_coverage_contract (test_descriptions.DescriptionTests.test_selector_competes_without_changing_nfr_coverage_contract) ... ok
test_tokenization_and_exact_jaccard (test_descriptions.DescriptionTests.test_tokenization_and_exact_jaccard) ... ok
test_body_line_limit_and_unfinished_tokens (test_foundation.FoundationTests.test_body_line_limit_and_unfinished_tokens) ... ok
test_catalog_has_exact_count_range_and_unique_slugs (test_foundation.FoundationTests.test_catalog_has_exact_count_range_and_unique_slugs) ... ok
test_catalog_rejects_duplicate_ids_slugs_and_wrong_count (test_foundation.FoundationTests.test_catalog_rejects_duplicate_ids_slugs_and_wrong_count) ... ok
test_citations_activate_with_allowlist_and_require_exact_matches (test_foundation.FoundationTests.test_citations_activate_with_allowlist_and_require_exact_matches) ... ok
test_cross_skill_copy_detection_in_batch (test_foundation.FoundationTests.test_cross_skill_copy_detection_in_batch) ... ok
test_description_boundaries (test_foundation.FoundationTests.test_description_boundaries) ... ok
test_empty_scaffold_passes_but_selected_missing_file_fails (test_foundation.FoundationTests.test_empty_scaffold_passes_but_selected_missing_file_fails) ... ok
test_generator_dry_run_and_idempotency (test_foundation.FoundationTests.test_generator_dry_run_and_idempotency) ... ok
test_generator_preserves_both_catalog_and_file_status (test_foundation.FoundationTests.test_generator_preserves_both_catalog_and_file_status) ... ok
test_index_grouping_status_links_and_determinism (test_foundation.FoundationTests.test_index_grouping_status_links_and_determinism) ... ok
test_missing_frontmatter_name_description_and_trigger (test_foundation.FoundationTests.test_missing_frontmatter_name_description_and_trigger) ... ok
test_missing_reordered_and_duplicate_sections (test_foundation.FoundationTests.test_missing_reordered_and_duplicate_sections) ... ok
test_only_rejects_invalid_ids_and_unknown_skill_fails_full_run (test_foundation.FoundationTests.test_only_rejects_invalid_ids_and_unknown_skill_fails_full_run) ... ok
test_optional_selector_is_validated_indexed_and_keeps_catalogue_intact (test_foundation.FoundationTests.test_optional_selector_is_validated_indexed_and_keeps_catalogue_intact) ... ok
test_reference_existence_reference_style_and_one_level_depth (test_foundation.FoundationTests.test_reference_existence_reference_style_and_one_level_depth) ... ok
test_references_check_nested_directories_and_citations (test_foundation.FoundationTests.test_references_check_nested_directories_and_citations) ... ok
test_sibling_slugs_must_exist_in_catalogue (test_foundation.FoundationTests.test_sibling_slugs_must_exist_in_catalogue) ... ok
test_unknown_description_or_reference_sibling_fails_cli (test_foundation.FoundationTests.test_unknown_description_or_reference_sibling_fails_cli) ... ok
test_valid_fixture_and_frontmatter_variants (test_foundation.FoundationTests.test_valid_fixture_and_frontmatter_variants) ... ok
test_validator_cli_exit_codes (test_foundation.FoundationTests.test_validator_cli_exit_codes) ... ok
test_cli_json_text_errors_and_read_only_files (test_score_routing.RoutingScoreTests.test_cli_json_text_errors_and_read_only_files) ... ok
test_empty_group_and_no_mutation (test_score_routing.RoutingScoreTests.test_empty_group_and_no_mutation) ... ok
test_extra_result_fields_do_not_score_runner_up (test_score_routing.RoutingScoreTests.test_extra_result_fields_do_not_score_runner_up) ... ok
test_groups_acceptable_sets_and_exact_choices (test_score_routing.RoutingScoreTests.test_groups_acceptable_sets_and_exact_choices) ... ok
test_held_out_marker_requires_boolean (test_score_routing.RoutingScoreTests.test_held_out_marker_requires_boolean) ... ok
test_held_out_partition_outcomes_and_missing_answers (test_score_routing.RoutingScoreTests.test_held_out_partition_outcomes_and_missing_answers) ... ok
test_key_rejects_conflicting_groups_and_invalid_choices (test_score_routing.RoutingScoreTests.test_key_rejects_conflicting_groups_and_invalid_choices) ... ok
test_legacy_keys_have_no_held_out_cases (test_score_routing.RoutingScoreTests.test_legacy_keys_have_no_held_out_cases) ... ok
test_missing_answers_are_misses_with_full_denominators (test_score_routing.RoutingScoreTests.test_missing_answers_are_misses_with_full_denominators) ... ok
test_results_reject_duplicate_unknown_and_malformed_records (test_score_routing.RoutingScoreTests.test_results_reject_duplicate_unknown_and_malformed_records) ... ok

----------------------------------------------------------------------
Ran 40 tests in 3.181s

OK

python scripts/build_index.py
Built INDEX.md with 115 entries.
```

- Two tests were added for selector validation/indexing and selector participation in description checks while retaining the 114-NFR coverage contract.
- After pre-release cleanup, supplemental Skill Creator validation passes 115/115. All SKILL.md frontmatters contain only name and description; status remains in the catalogue. Runtime host compatibility is still unverified.
- Selector frontmatter is name/description only, its description is 273 characters, and its body is 129 lines.
- The selector has five Rules of thumb, specific to selection coverage, sibling resolution, conflicts, handoff budgets, or bypassing selection for an identified quality.

## Routing and held-out results

| Recorded run | Correct / total | Limits |
| --- | ---: | --- |
| Original full blinded run | 396/490 | Historical catalogue snapshot; 94 misses |
| First targeted routing repair | 205/268 | Adaptive subset; 63 misses including controls; different runner context |
| Subsequent 58-miss repair | 186/195 | Adaptive subset; eight original misses plus one control miss remained |
| Subsequent eight-miss repair | 53/53 | Eight original misses and 45 controls; adaptive testing, not held out |
| Adjustability/configurability/reconfigurability check | 12/12 | Unchanged descriptions; not repaired Workflow execution |
| H001-H012 held-out result | 11/12 | Supplied choices; H006 chose maturity |
| New selector routing check | 8/8 | Four selector cases and four bypass/clarification cases; not held out |

The held-out miss was H006, the recurring-bug prompt. Maturity was not in its acceptable set. The user judged the prompt ambiguous and ask the better answer; the score and frozen key remain unchanged. The held-out rows and saved id/choice results were not changed or rerun in Phase 6.

The selector run used a fresh ephemeral CLI session, ignored user configuration, no model override, no tools, and only the current description catalogue plus eight unlabeled prompts. No keys or skill bodies were given to the router. The four non-selector cases did not route to nfr-selector. Raw answers, transcript, score, and portable provenance are in evals/results/selector-1* and evals/selector-routing-*.json.

The current routing catalogue reflects all 115 current descriptions. Its prior snapshot is preserved as evals/history/routing-catalog-before-selector.md. Historical results are not a fresh full-catalogue score for this revision; subset scores cannot be combined into one overall accuracy.

The lexical checker evaluated 920 cases, with 458 omitting the distinguishing fact. Flags: {"expected_not_top": 441, "near_pair_no_signal": 111, "near_pair_tie": 4, "near_target_outranks_sibling": 36, "no_keyword_signal": 51, "top_tie": 75}. It reported 391 ambiguous pairs. These overlapping lexical warnings are not semantic routing verdicts. The half-underspecified coverage check remains applicable to the 114 NFRs; explicit selection requests supply a routing fact and are separate from that coverage constraint.

## Scratch runs and baseline

The user reports a few scratch runs exercising fast paths, including a no-skills baseline that behaved about the same on one task. No timing, effectiveness score, repeat count, or independently retained matched-baseline trace is available here to quantify a benefit. The baseline observation is qualitative and user-supplied.

The retained adjustability repair records tuning based on a reported scratch-project run. Its validation exercised a sequential setting sketch and description routing, not a fresh end-to-end coding-agent implementation. The Phase 6 examples are authored planning fixtures, not real project results. No claim of improved implementation quality over an unassisted baseline is supported.

## Known weaknesses and outstanding uncertainty

- Terminology distinctions are repository conventions. Application-specific interpretation, especially overlapping change, resilience, evidence, and mobility terms, still needs project context.
- Standards edition/version selection, applicability, and actual source obligations remain unresolved. No skill is a compliance conclusion; stakeholder policy and authoritative requirements are still needed.
- Project thresholds, value domains, units, running-work semantics, data-handling authority, ownership, and accepted failure effects cannot be supplied by these synthetic fixtures.
- Operational dependencies, deletion behavior, restore compatibility, audience interpretation, instrument precision, proof/model correspondence, environmental objectives, and continuing business value lack project-level verification.
- Independent audits identify transferable rules and depth gaps in earlier batches. This phase did not repair every audited weakness or perform a new independent full-content audit. Validation cannot establish specificity or factual correctness.
- Some skills have three Rules of thumb while the latest guide recommends four to six; others have seven or eight. No padding or unrelated content repair was performed.
- Availability/design-patterns.md has 102 lines and privacy/design-patterns.md has 92, above the current 80-line design-guide recommendation. Both remain below the per-reference 150-line limit.
- The availability/readability status frontmatter fields were removed for pre-release compatibility. Other-agent discovery and environment-specific Codex installation remain unverified.
- Selector routing passed this small authored set; its full planning/build handoffs, question ceiling, assumption disclosure, and conflict decisions were not independently executed on a real task.

## Workflow execution evidence gap

No retained independent real-project Workflow execution record was found for any of the 115 skills. This is an evidence gap, not proof that they have never been used. User-reported scratch trials are distinct from documented real-task validation. Each following entry is therefore flagged as lacking such retained evidence:

- 000-nfr-selector
- 001-accessibility-access-control
- 002-accountability
- 003-accuracy
- 004-adaptability
- 005-additivity
- 006-adjustability
- 007-affordability
- 008-agility
- 009-analyzability
- 010-anonymity
- 011-atomicity
- 012-attractiveness
- 013-auditability
- 014-augmentability
- 015-availability
- 016-certainty
- 017-changeability
- 018-communicativeness
- 019-compatibility
- 020-completeness
- 021-complexity-interacting-complexity
- 022-composability
- 023-comprehensibility
- 024-comprehensiveness
- 025-conciseness
- 026-confidentiality
- 027-configurability
- 028-conformance
- 029-consistency
- 030-controllability
- 031-correctness
- 032-customizability
- 033-debuggability
- 034-decomposability
- 035-defensibility
- 036-demonstrability
- 037-dependability
- 038-distributivity
- 039-durability
- 040-effectiveness
- 041-efficiency-device-efficiency
- 042-enhanceability
- 043-evolvability
- 044-expandability
- 045-expressiveness
- 046-extendability
- 047-extensibility
- 048-fault-failure-tolerance
- 049-feasibility
- 050-flexibility
- 051-formality
- 052-functionality
- 053-generality
- 054-immunity
- 055-installability
- 056-integratability
- 057-integrity
- 058-interoperability
- 059-learnability
- 060-legibility
- 061-likeability
- 062-localizability
- 063-maintainability
- 064-manageability
- 065-maturity
- 066-measurability
- 067-mobility
- 068-modifiability
- 069-nomadicity
- 070-observability
- 071-operability
- 072-performance-efficiency-time-or-space-bounds
- 073-portability
- 074-predictability
- 075-privacy
- 076-provability
- 077-quality-of-service
- 078-readability
- 079-reconfigurability
- 080-recoverability
- 081-reliability
- 082-repeatability
- 083-replaceability
- 084-replicability
- 085-reusability
- 086-robustness
- 087-safety
- 088-scalability
- 089-security-control-and-security
- 090-self-descriptiveness
- 091-simplicity
- 092-stability
- 093-standardizability-standardization-standard
- 094-structuredness
- 095-suitability
- 096-supportability
- 097-survivability
- 098-susceptibility
- 099-sustainability
- 100-tailorability
- 101-testability
- 102-traceability
- 103-trainability
- 104-transferability
- 105-trustability
- 106-understandability
- 107-uniformity
- 108-usability
- 109-variability
- 110-verifiability
- 111-versatility
- 112-viability
- 113-visibility
- 114-wrappability

## Privacy and distribution findings

Nine existing files were sanitized: one batch review and eight run/failure metadata files. Local invocation paths were replaced by portable run-relative values; JSON records are marked local_paths_redacted. Those metadata files no longer claim byte-identical reproduction of original local command lines. Recorded scores and opaque case IDs were not changed. The initial broad search also matched harmless words and a reserved URL fixture; those were not treated as personal identities.

The text-tree audit excludes Git internals and ignored generated bytecode. It found no remaining configured author-identity or machine-local-path matches in distributable text. Git history, author metadata, and configuration were not rewritten; older commits can retain original information. This work does not assert history-level sanitization.

The user chose to retain reviews as development evidence and exclude them from a future release. The directory remains in the working tree. .gitattributes marks it export-ignore for Git archive exports; other packaging paths still need to honor that decision. No release was tagged or published.

A staged-tree Git archive check confirmed that reviews/ is absent, all 115 SKILL.md files remain present, and the exported file contents contain no configured identity or machine-local-path matches. The check produced an in-memory archive only; no release artifact was published.

## Review-file inventory

The retained directory contains 39 files, including this report:

- [adjustability-repair.md](adjustability-repair.md)
- [batch-1-audit.md](batch-1-audit.md)
- [batch-1-fixes.md](batch-1-fixes.md)
- [batch-1-review.md](batch-1-review.md)
- [batch-10-audit.md](batch-10-audit.md)
- [batch-10-fixes.md](batch-10-fixes.md)
- [batch-10-review.md](batch-10-review.md)
- [batch-11-review.md](batch-11-review.md)
- [batch-12-review.md](batch-12-review.md)
- [batch-13-review.md](batch-13-review.md)
- [batch-14-review.md](batch-14-review.md)
- [batch-15-review.md](batch-15-review.md)
- [batch-16-review.md](batch-16-review.md)
- [batch-17-review.md](batch-17-review.md)
- [batch-18-review.md](batch-18-review.md)
- [batch-2-audit.md](batch-2-audit.md)
- [batch-2-review.md](batch-2-review.md)
- [batch-3-review.md](batch-3-review.md)
- [batch-4-review.md](batch-4-review.md)
- [batch-5-review.md](batch-5-review.md)
- [batch-6-audit.md](batch-6-audit.md)
- [batch-6-review.md](batch-6-review.md)
- [batch-7-audit.md](batch-7-audit.md)
- [batch-7-review.md](batch-7-review.md)
- [batch-8-audit.md](batch-8-audit.md)
- [batch-8-review.md](batch-8-review.md)
- [batch-9-audit.md](batch-9-audit.md)
- [batch-9-review.md](batch-9-review.md)
- [description-pass.md](description-pass.md)
- [final-report.md](final-report.md)
- [held-out-routing.md](held-out-routing.md)
- [phase5-dry-run.md](phase5-dry-run.md)
- [phase5-full.md](phase5-full.md)
- [pilot-review.md](pilot-review.md)
- [routing-fixes-58.md](routing-fixes-58.md)
- [routing-fixes-8.md](routing-fixes-8.md)
- [routing-fixes.md](routing-fixes.md)
- [routing-misses.md](routing-misses.md)
- [routing-score.json](routing-score.json)

## Release-readiness addendum

v0.1.0 pre-release preparation retains all 115 skills as drafts. No tag, push, or history rewrite was performed.

The audited transferable Rules of thumb bullets in batches 2-9 were not retrofitted. The earlier verification estimate was about 175, as supplied for this prep; that estimate was not independently recounted here. Adding common Workflow guard sentences does not repair those Rules of thumb.

The baseline comparison covered one task. Fast paths were exercised in a few manual scratch runs by the maintainer; the no-skills baseline behaved about the same on that task. Repository validation does not establish that Workflows produce better implementations.

The 21 skills with only three Rules of thumb remain:

- 009-analyzability
- 031-correctness
- 033-debuggability
- 036-demonstrability
- 040-effectiveness
- 045-expressiveness
- 049-feasibility
- 067-mobility
- 070-observability
- 071-operability
- 082-repeatability
- 085-reusability
- 091-simplicity
- 094-structuredness
- 095-suitability
- 101-testability
- 104-transferability
- 107-uniformity
- 109-variability
- 110-verifiability
- 113-visibility

The workflow-update script was run in dry-run mode before application. Specify guards were added to all 115 skills; equivalent Design/Implement guidance was retained in selector, adjustability, and configurability, with the new sentence added to the other 112. A subsequent dry run reports zero changes. Descriptions and sections outside Workflow are unchanged, apart from the two explicitly removed frontmatter status lines.

The full validator reports 115 checked and zero errors; all 43 tests pass; the index builder reports 115 entries; the supplemental Skill Creator checker passes 115/115. No similarity threshold or validator was weakened. Complete command outputs are in [release-prep-validation.txt](release-prep-validation.txt).

The two raw routing result files moved unchanged into evals/results/, and their references were updated. The empty temporary folder was removed. Text normalization uses LF; the existing review export exclusions remain.

The prior review inventory is the Phase 6 snapshot. release-prep-validation.txt is additional development evidence and is excluded from archive exports with the rest of reviews/.

The final tracked-file personal-info scan found 81 matching lines, all substrings
inside unrelated English verbs; no personal data or absolute local paths were
found by the requested searches. Every hit is listed by file and line in
[release-prep-validation.txt](release-prep-validation.txt).
