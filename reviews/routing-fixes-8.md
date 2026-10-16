# Eight remaining routing misses: findings

Seven description fields changed: debuggability, functionality, recoverability, replaceability, reusability, self-descriptiveness, and viability. All remain below 350 characters, contain three quoted developer phrases, and preserve their exact original Not for clauses. No quoted trigger phrase duplicates another catalogue description. All bodies, references, other frontmatter, catalogue records, existing eval files, answer labels, and scripts are unchanged.

## Routing results

The final selected rerun matches all 53 cases: eight historical misses and 45 sibling controls. Controls are existing near-miss prompts either owned by an affected skill or naming one as the intended sibling; deduplicated text maps back to the original blinded IDs. The separate prior formality control miss was not included as an edit target.

| Set | Fresh baseline | Final | Newly matching | Regressions |
| --- | ---: | ---: | ---: | ---: |
| Eight requested historical misses | 3/8 | 8/8 | 5 | 0 |
| Sibling controls | 45/45 | 45/45 | 0 | 0 |
| Explicit subgroup | 26/26 | 26/26 | 0 | 0 |
| Vague subgroup | 22/27 | 27/27 | 5 | 0 |
| Total | 48/53 | 53/53 | 5 | 0 |

Three historical misses already matched in this fresh baseline, so only five improvements are observed in the paired comparison. All eight frozen expected choices are ask. No user-voice prompts occur in this selected subset.

| Requested case | Prompt | Fresh baseline choice | Final choice |
| --- | --- | --- | --- |
| r-212433c508cb6344 | Use the validator in the CLI too. | reusability | ask |
| r-2eec4750902942a8 | Should we keep this product? | viability | ask |
| r-9bc5df77b7002ca8 | Make the screen explain itself. | ask | ask |
| r-dd8b0409043f8049 | Where did this wrong value come from? | ask | ask |
| r-e7f93ec80c7a461b | Is this still worth running? | viability | ask |
| r-ebe06c04252d4ce8 | The export feature is missing. | functionality | ask |
| r-f02044e5b76544fb | Swap this backend. | ask | ask |
| r-f5104ee00e36ed63 | Get the service back. | recoverability | ask |

## Description findings

- Debuggability distinguishes localization of one reproducible execution from analysis of sources and dependencies; a wrong value alone does not establish the boundary.
- Functionality asks whether a missing-feature complaint means an absent action, wrong existing behavior, or task mismatch.
- Recoverability separates usable-state restoration from retained writes and mission continuity for generic service-return requests.
- Replaceability states the positive criterion of substitution while preserving caller contracts. A bare swap still leaves retirement, retained wrapping, and coexistence unresolved.
- Reusability distinguishes sharing the same artifact from broadening an input model or joining stages; using a similarly named operation elsewhere does not alone establish shared artifact identity.
- Self-descriptiveness distinguishes current state/action cues from standalone explanation when a screen is merely asked to explain itself.
- Viability distinguishes continued value, spending fit, and delivery feasibility in bare worth/keep/retire judgments; the continuation question remains grounded in its existing body.

| ID | Slug | Before characters | Final characters |
| ---: | --- | ---: | ---: |
| 033 | debuggability | 327 | 330 |
| 052 | functionality | 349 | 315 |
| 080 | recoverability | 325 | 344 |
| 083 | replaceability | 259 | 289 |
| 085 | reusability | 320 | 314 |
| 090 | self-descriptiveness | 312 | 329 |
| 112 | viability | 302 | 345 |

## Iteration evidence and limits

The baseline and all three post-edit runs used fresh ephemeral Codex CLI sessions with ignored user configuration, identical neutral instructions, catalogue layout and prompt order, and default model settings. Input contained only the full catalogue and the selected unlabeled prompts. No keys, earlier choices, or review findings were supplied. Transcripts show no tool calls. The CLI did not report a model name.

The first post-edit run matched seven of the eight historical misses and all 45 controls. It retained the worth-running viability miss. A refinement expanded the generic continuation question to cover bare worth judgments as well as keep/retire wording.

The second run matched all eight historical misses but asked on the explicit contract-preserving substitution control. Replaceability was then revised to state preserved caller contracts in its positive definition rather than requiring a retirement-versus-wrapping distinction for every substitution request. The final run matches both the vague backend-swap case and this explicit control.

All intermediate catalogues, descriptions, choices, and scores remain under round-1/ and round-2/. This is adaptive development on known cases, not an independent held-out estimate. Results establish the observed selected-run behavior; repeated-run stability and performance on unseen wording remain unmeasured. Some frozen ask labels admit a plausible direct route under ordinary language. Their labels were retained, not independently adjudicated.

## Validation

- Full repository validator: 114 skills checked, zero errors.
- Full test suite: 34 tests passed.
- Supplemental Skill Creator validator: all seven affected skills passed.
- Routing scorer: 53 unique complete answers, zero misses; 26/26 explicit and 27/27 vague.
- Scope checks: all 114 bodies unchanged; other 107 descriptions unchanged; original boundary clauses and non-description frontmatter preserved; selected prompts and labels unchanged.
- Read-only lexical checker: 56 prompts across seven affected eval sets; 28 omit the distinguishing fact; 43 flagged pairs. Counts overlap and do not represent accuracy. Flags: expected_not_top 27; near_pair_no_signal 6; near_target_outranks_sibling 2; no_keyword_signal 1; top_tie 4. No description edits were based on this checker alone.

No selected cases remain unresolved in the final scored run. The earlier independent formality-control disagreement remains outside this revision. No new standards or external factual claims were introduced. Raw evidence is retained in evals/routing-fixes-8/.
