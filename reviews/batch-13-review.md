# Batch 13 authoring findings

Six catalogue entries are draft: 055 installability, 062 localizability,
067 mobility, 069 nomadicity, 073 portability, and 104 transferability.
All retain the Portability & Interoperability category.
The authoring guide, disambiguation map, allowlist, rubric, and approved pilot
entrypoints were read before authoring. No existing file in reviews/ was read.

Descriptions were written and compared against sibling meanings before bodies.
Each has three developer-style trigger phrases, a clear exclusion, and real
catalogue sibling pointers. Complete trigger phrases are unique across the
current descriptions after case folding. This is a literal uniqueness check,
not semantic routing proof.

## Per-skill findings

### 055 installability

The target's staging/activation capabilities and ownership journal are declared fixture operations. No actual installer, package manager, startup registration, or filesystem activation mechanism was executed. The upgrade has no data-schema change; artifact rollback cannot be generalized to schema rollback. Failed cleanup remains a partial state.

The design sketch records resource creation and activation state in a lifecycle journal before startup success. The examples separately cover fresh installation, interrupted upgrade, retry, and removal with an unowned neighboring project retained.

Post-fix transfer test on every retained bullet: 2 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `portability`, `privacy`, `atomicity`, `operability`.
Data retention can affect removal too; this rule defines uninstall resource ownership, not personal-data purpose. Coherent activation shares all-or-none concerns; here the accepted unit is the installed package set and entrypoint.

### 062 localizability

The resources and date/number conventions are synthetic and deliberately do not represent a real language or region. No qualified translation, glyph, bidirectional-layout, or actual renderer review occurred. The interleaved contexts test selection isolation only, not a particular runtime's locale implementation.

Date-type preservation moved to Verification. A distinct per-audience rendering-context rule and an interleaved plain/alternate/plain probe address locale leakage. The operation labels used by the failing branch are filled explicitly.

Post-fix transfer test on every retained bullet: 2 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `portability`, `interoperability`, `comprehensibility`, `configurability`.
Canonical machine meaning matters to exchange too; this rule prevents display-locale formatting from altering the machine boundary. Choice scoping also matters to settings; here per-audience locale context must reach each rendering path.

### 067 mobility

The example covers an overlapping client-path handoff, not arbitrary movement of every user, device, or service. It has no accepted interruption budget and cannot establish zero interruption. The delayed old acknowledgment names an already committed chunk; loss reconciliation and real distributed fencing remain implementation obligations.

Replacement-readiness and old-route retirement checks moved to Verification because those safeguards also apply to other continuity work. The retained rules distinguish logical task identity, overlap ownership, and active application lifecycle.

Post-fix transfer test on every retained bullet: 2 specific,
1 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `nomadicity`, `nomadicity`, `nomadicity`.
A resumed task may retain identity too; this rule keeps an already active task outside transport reconstruction.

### 069 nomadicity

The local meaning deliberately permits suspension during relocation. Saved context, current binding, and base-revision checks are constructed, not real authentication or concurrency-control evidence. An actual project must confirm saved-data policy and the conflict behavior before applying pending writes.

The fixture covers normal resumption, a changed remote revision, unavailable binding, and revoked current authority. Login and connection success are not accepted as task resumption.

Post-fix transfer test on every retained bullet: 2 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `mobility`, `recoverability`, `portability`, `mobility`.
Saved task context can aid recovery too; the acceptance question here is useful work after relocation. Useful work matters to both, but successful post-move login alone does not establish the promised resumed action.

### 073 portability

Only the working-directory/output-root assumption is worked through in full. Native/generated artifacts, process behavior, and other target capabilities require project-specific checks; none is claimed validated by the path fixture. No real platform migration or quantitative adaptation-effort budget was established.

The adaptation-surface rule was corrected to report additional domain edits rather than assert that scattered checks necessarily make the surface unbounded. Unsupported required output is an explicit failing capability case.

Post-fix transfer test on every retained bullet: 1 specific,
3 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `installability`, `modifiability`, `installability`, `compatibility`.
Target prerequisites also need capabilities; the portability rule defines which profile operations the migrated software must preserve. Change surface matters to edits too; this rule binds target adaptation to the agreed platform boundary. Artifact contracts can constrain coexistence too; here target use must be exercised rather than inferred from the source build.

### 104 transferability

The handoff includes a confirmed role reassignment, not identity equivalence between the named users. Recipient usability and final owner change occur in a sequential synthetic coordinator. The example does not establish personal-data sharing authority, actual permissions, or an atomic cross-system responsibility protocol.

Identity/unit mapping safeguards moved to Verification. Package closure, recipient acceptance, and source responsibility release remain the handoff-specific decisions.

Post-fix transfer test on every retained bullet: 1 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `interoperability`, `interoperability`, `portability`.
Reference meaning matters to exchange too; this rule closes the particular unit needed for recipient handoff. Receiver usability is related, but package creation is not completion of this recipient acceptance lifecycle.

All 22 retained bullets received a nearest-sibling verdict. Partly shared
judgments remain visible above; zero judged transferable is the author's assessment,
not an independent audit.

Mobility and Transferability retain three rules after shared safeguards were moved
to Verification. This is below the guide's usual four-to-six range and remains
an explicit human-review exception rather than a padded list. The other skills
retain four rules. No count is treated as a quality score.

## Footprint and evidence findings

| Skill | Description characters | Entrypoint lines | Design guide lines | Worked example lines | Combined lines |
| --- | ---: | ---: | ---: | ---: | ---: |
| `installability` | 260 | 120 | 41 | 79 | 240 |
| `localizability` | 276 | 123 | 35 | 83 | 241 |
| `mobility` | 304 | 122 | 34 | 68 | 224 |
| `nomadicity` | 301 | 120 | 30 | 80 | 230 |
| `portability` | 309 | 120 | 32 | 73 | 225 |
| `transferability` | 319 | 121 | 34 | 72 | 227 |

Combined footprints include frontmatter, blank lines, and both references.
All fit the 200-300 guideline; each reference is below 150 lines and each design
guide is below 80. Tables contain observed evidence, interventions, trade-offs,
and verification, with concrete tool-agnostic sketches rather than headings alone.

The examples fill their inputs and carried state, show failure before remediation
and a defined after result, and keep conclusions inside the fixture scope.
Done items correspond to distinct evidence: installed startup/owned removal,
resource/format/machine-data boundaries, active task/path ownership, useful
post-relocation action/conflict handling, cross-profile artifact preservation,
and recipient acceptance/source disposition. Shared measurement safeguards remain
in Workflow or Verification.

## Description routing findings

The following is a manual author check from before body writing, not an independent
blinded evaluation. Six probes provide the distinguishing fact and six omit it.
The specific probes have distinct primary matches under the repository conventions.

| Prompt | Match or clarification | Boundary / first question |
| --- | --- | --- |
| Install, update, and remove this app on our supported target without deleting user projects. | `installability` | Installation lifecycle on a fixed target, not cross-platform adaptation. |
| Add locale resources and date formatting without changing stored business values. | `localizability` | Language/locale-dependent presentation with canonical data preserved. |
| Keep this active upload progressing as the client changes network path. | `mobility` | Continuity during movement, not an explicit suspend/reconnect cycle. |
| Reopen the saved draft after we disconnect, relocate, and reconnect. | `nomadicity` | Useful operation reestablished after relocation and pause. |
| Preserve this program's report output when its execution environment changes. | `portability` | Software environment migration, not merely installing the current package. |
| Hand the project, its linked assets, and its agreed ownership to the receiving team. | `transferability` | Recipient handoff preserving the defined asset and responsibility. |
| Make deployment easier. | ask; unresolved sibling concerns | Is the concern installation lifecycle, another platform, or interruption of service? |
| Make it work in another country. | ask; unresolved sibling concerns | Do language/locale behavior, execution environment, or user relocation need to change? |
| Support working on the move. | ask; unresolved sibling concerns | Must activity continue during movement, or may it pause and resume afterward? |
| Keep my session working. | ask; unresolved sibling concerns | What moves, and is uninterrupted activity or post-relocation resumption required? |
| Move this somewhere else. | ask; unresolved sibling concerns | Does the software change platforms, the user change location, or an asset change recipient? |
| Make the export usable elsewhere. | ask; unresolved sibling concerns | Is this a recipient handoff, machine exchange contract, locale format, or platform concern? |

The ambiguous prompts do not justify unconditional winners. Deployment can mean
installation, platform adaptation, or service continuity. Movement can concern
active application work, paused post-relocation work, or software runtime migration.
An export may be human locale output, a recipient handoff, or an ongoing exchange
contract. The entrypoints require those meanings to be resolved.

Description promises are illustrated by the lifecycle, locale, active upload,
paused draft, report-root, and project-handoff cases. The Mobility entrypoint
explicitly focuses its worked path on active clients; it does not promise an
implementation for every kind of moving service.

## Validation findings

- Batch validator: six checked, zero errors.
- Full validator: 84 authored skills checked, 30 absent todo skills, zero errors.
- Skill-creator quick validation: all six entrypoints pass.
- Read-only assertions cover the 350-character cap, three-to-five trigger count,
  complete trigger uniqueness, explicit workflow conditionals, and reference budgets.
- Highest word-five-gram body similarity involving this batch:
  0.016861, between `installability` and `localizability`,
  below the unchanged 0.35 validator threshold. This does not prove semantic distinctness.
- Synthetic consistency checks cover lifecycle ownership, locale outputs/context
  isolation, task identity across path change, paused-task revision conflict,
  required report location, and recipient package closure. No real installer,
  network handoff, runtime migration, or recipient transfer was performed.
- Catalogue changes are only the six todo-to-draft transitions. The index was
  regenerated; other skills, prior reviews, tools, tests, and evals are unchanged.

### Test-environment finding

The ordinary `python -m unittest discover -s tests -v` run passed 33 tests and
errored in `test_cli_json_text_errors_and_read_only_files` while writing its
temporary key fixture. The exception was PermissionError under Windows' temp
directory. A rerun changing only the temp root into the workspace met the same
permission error. Both failures are retained as environment findings.

The local Python `tempfile.mkdtemp` implementation requests private directory
mode 0o700. An adapted in-process test harness supplied fixture directories via
ordinary workspace-inheriting directory creation instead of that factory.
All 34 tests then passed. Assertions and repository test files were unchanged;
only the temporary-directory creation helper was substituted during that run.
The exact Windows ACL/sandbox interaction has not been independently diagnosed.

The adapted run's accessible temporary fixtures were cleaned up.
The failed workspace fixture container could not be deleted with current access.
It was moved, without changing permissions, outside the repository to:
`C:\Users\ulate\Desktop\Proyectos Personales\NFR SKILLS\.batch-13-test-temp-residue\tmpppyknw23`.
That generated residue needs cleanup by a process with suitable access.
The first failed external-temp attempt may also have left its inaccessible
`tmpflmbyra_` directory under the Windows temp root; its cleanup is unverified.
The test's write and cleanup attempts failed; no further access or permission
changes were attempted on that external residue.

No Phase 5 evals were added. The earlier blinded catalog/key remains its frozen
63-skill snapshot, and the prepared blinded test was not run. Newly authored
batches therefore still need their own later routing-eval coverage.

## Uncertain claims

The repository meanings of Mobility, Nomadicity, and Transferability remain
proposed conventions. Actual interpretation depends on what moves, which task
must remain continuous or resume, what changes recipient, and which source
responsibility ends. The partly shared transfer judgments need independent review.

Unconfirmed implementation assumptions include target staging/activation,
resource ownership, actual locale wording/conventions, renderer behavior,
path readiness and ordering, saved-state authority/revision checks, target runtime
capabilities, and recipient acceptance/disposition policy. None was inferred as
a real project fact from the synthetic examples.

No external standards, legal obligations, platform specifications, library
versions, tool flags, or empirical performance statistics were asserted.
Numeric fixture values are illustrative and paired with stakeholder confirmation.
No installation time, interruption, resumption, adaptation-effort, or transfer
deadline was invented. The remaining temp-directory cleanup and the environment
specifics behind the default test failure are unresolved operational findings.
