# Batch 1 skeptical audit

## Findings and scope

The seven drafts are structurally valid, but the prior review overstated NFR specificity. Exact word-five-gram originality coexists with transferable advice and an identical item-count shape. Skills, their references, catalogue statuses, index, rubric, and validator code are unchanged by this audit. The batch review now contains findings and per-skill weaknesses rather than instructions or self-scores.

## Per-skill weaknesses

### 005-additivity

- The definition admits any declared aggregation rule, including union. That makes the boundary with composability and consistency depend heavily on stakeholder terminology rather than an immediately recognizable additive property.
- The worked example tests exact counts; the guide names noise and drift but supplies no concrete repeated-measurement or uncertainty procedure for noisy contribution claims.
- Replay identity, ordering, and metric-accounting rules transfer unchanged to other NFRs. Original wording did not make these rules exclusive to additivity.

### 014-augmentability

- The description and example narrow supplementary capabilities to optional helpers. The definition permits a broader supporting capability, so an independently accepted mandatory supplement is poorly represented.
- The workflow gives a useful absent-helper comparison, but does not decide when an intentional original-output change from adopted helper advice is acceptable versus a failed preservation check.
- Authority labeling, read-only adoption, and dependency isolation transfer to self-descriptiveness, security, and fault tolerance; they do not by themselves establish a separately accepted supporting result.

### 042-enhanceability

- The parser example, paired-corpus checks, and error-reduction default mostly demonstrate better results, not the engineering effort or impact required to make later refinements. This risks turning an -ability skill into an accuracy evaluation.
- The description matches a parser accuracy request even though Use when routes a specified output-error question alone to accuracy. That boundary is unavailable to a router reading descriptions only.
- The trigger "make future quality upgrades easier" overlaps evolvability. Baseline retention, protected-case comparison, and stable public meanings transfer directly to accuracy or compatibility.

### 043-evolvability

- The sequence, retained intermediate state, and retirement gate distinguish the skill well, but the example primarily covers persisted-data migrations rather than other kinds of evolving constraints.
- The cumulative-effort pattern leaves the cost convention as a placeholder. No worked effort ledger shows how transitional upkeep is charged to a later change.
- Roadmap abstraction advice and ownership of speculative work transfer to modifiability or feasibility. The description overlaps a generic request to make future changes easier without establishing a sequence.

### 044-expandability

- Usable capacity and a capacity delta are not operationalized for the worker example: successfully placing work on an added worker proves eligibility, but alone does not demonstrate an increased service-capacity boundary.
- The description trigger "remove the capacity ceiling" also describes a scalability bottleneck. Admission and workload-response acceptance still require clarification.
- Headroom, placement, and shared-controller rules can be reused unchanged in scalability, distributivity, or recoverability. The last rule draws the boundary explicitly; several earlier rules do not.

### 046-extendability

- The definition clearly states the local core-edit convention, but the description cannot disambiguate an added result type until the existing extension surface is inspected.
- The illustrative module-count budget depends on packaging. The guide warns against gaming it, but supplies no worked owner/interface ledger to replace file count as the main acceptance evidence.
- Explicit operation contracts and old-caller preservation transfer directly to compatibility. Hook-creation accounting transfers to extensibility. These rules alone do not demonstrate bounded core-addition effort.

### 047-extensibility

- The description presupposes an existing contract even for "add a plugin". Requests to let people add plugins can instead require creating that contract, so an unqualified plugin trigger can route too early.
- The worked example assumes the very host contract being tested; its negative fixture rejects a result type but does not concretely exercise cleanup after a failed activation or retained-extension interaction.
- Lifecycle obligations and contract revision checks can sit unchanged in extendability or compatibility. The guide identifies authority as a boundary but does not implement or demonstrate enforcement.

## Rules that transfer unchanged

These are whole original bullets, quoted with wrapping normalized. A destination is a plausible use under the repository disambiguation map, not a claim that an unauthored sibling already contains this text. Transferability flags a specificity weakness; an inherently shared safeguard is not automatically useless. Narrowing the acceptance reason would matter more than changing nouns. Bullet numbers follow each existing Rules of thumb section. Unlisted bullets have no convincing unchanged-transfer example in this audit; that is not proof of exclusivity.

### additivity

**Bullet 2 -> `completeness`.** Counting a bounded set without duplicating its members applies unchanged when checking required-set coverage.

> Do identify overlapping members before adding set sizes; don't turn a union's shared members into multiple contributions.

**Bullet 3 -> `measurability`.** Defining a valid operation on a metric is equally necessary for a measurement contract.

> Do state the aggregation operation for the actual metric; don't add percentages, elapsed times, or improvements merely because they share a display format.

**Bullet 5 -> `repeatability`.** Replay identity can be checked without any combined-contribution acceptance claim.

> Do exercise repeated increment delivery under its identity policy; don't count a replay as a new contribution when it represents the same increment.

**Bullet 6 -> `consistency`.** Order-sensitive shared-state updates also require an explicit agreement rule.

> Don't assume reversing addition order is harmless when contributions mutate shared state; check order behavior against the declared rule.

### augmentability

**Bullet 1 -> `self-descriptiveness`.** Provenance and decision status are in-context interface explanation.

> Do label helper-derived output separately from the original authoritative result; don't make a suggestion look like a decision the original workflow already made.

**Bullet 3 -> `fault-failure-tolerance`.** An optional helper can be a failing dependency while the original route must continue.

> Do maintain an original-only route through the workflow; don't turn helper initialization into an unexplained prerequisite for completing that route.

**Bullet 4 -> `security-control-and-security`.** Preventing writes across a read-only authority boundary is access control.

> Do distinguish displaying a recommendation from applying it; don't let a helper write through a read-only attachment under the guise of enrichment.

**Bullet 5 -> `maintainability`.** A hidden dependency left after removing a feature is also ongoing maintenance debt.

> Do track helper-owned projections for removal; don't leave an abandoned projection as a hidden dependency of the original feature.

### enhanceability

**Bullet 3 -> `accuracy`.** A paired value-error comparison requires the identical retained baseline.

> Do retain old outputs for paired review; don't overwrite the baseline corpus while using it to demonstrate a candidate's gain.

**Bullet 4 -> `accuracy`.** Reference-error results for required input groups must not disappear into an aggregate.

> Do compare protected case groups alongside aggregate quality; don't hide a degraded existing use case inside a favorable average.

**Bullet 5 -> `compatibility`.** Stable public field meanings are equally a consumer compatibility obligation.

> Do preserve public meaning while changing the internal strategy; don't quietly reinterpret an existing field to make the new result appear better.

**Bullet 6 -> `accuracy`.** Separating scoring changes from computation changes is necessary to attribute an accuracy gain.

> Don't revise both the scoring rule and implementation in the same improvement claim without showing their separate contributions to the reported difference.

### evolvability

**Bullet 1 -> `recoverability`.** A staged restoration or migration rehearsal also needs preceding state, not clean resets.

> Do replay successive changes against the previous stage's data; don't reset fixtures between stages and thereby remove the history that makes change difficult.

**Bullet 3 -> `modifiability`.** Isolating a named change driver is useful for one bounded implementation change too.

> Do isolate the change driver the roadmap actually names; don't substitute a universal abstraction for a concrete decision about likely future variation.

**Bullet 4 -> `recoverability`.** Selecting old code cannot reconstruct a discarded representation in a restoration claim.

> Do mark which later scenario an irreversible representation change forecloses; don't call the evolution path reversible merely because routing can select older code.

**Bullet 5 -> `maintainability`.** Accumulated temporary paths contribute to ongoing modification cost.

> Do include accumulated transitional code in later-change cost; don't price each future release as though previous temporary paths had already disappeared.

**Bullet 6 -> `feasibility`.** Scenario ownership and commitment are delivery-scoping concerns independent of a sequence.

> Don't promote an imagined scenario to a committed requirement without an owner and a trigger for deciding whether it should ever be implemented.

### expandability

**Bullet 1 -> `scalability`.** Allocated resource count alone cannot demonstrate usable capacity in a growth experiment.

> Do count added capacity after representative work can use it; don't equate an allocated or registered unit with a functioning increase in service capacity.

**Bullet 2 -> `scalability`.** Fixed admission/controller limits also bound workload-to-resource growth.

> Do inspect controller, address, partition, and routing ceilings before admitting more units; don't multiply serving capacity while ignoring a fixed admission limit.

**Bullet 3 -> `recoverability`.** A restoration involving data movement also consumes transition headroom.

> Do budget temporary headroom for required data movement; don't spend all spare capacity on new steady-state allocation before the transition can complete.

**Bullet 4 -> `distributivity`.** Placement and eligibility determine where work can run on an existing node set.

> Do distinguish changing placement rules from physically adding resources; an idle added unit needs a placement explanation, not another allocation.

### extendability

**Bullet 1 -> `structuredness`.** Centralizing dispatch at the owning boundary is also an inspectable responsibility/dependency rule.

> Do place the new operation's dispatch decision with its owning core boundary; don't spread new result-type checks into every unrelated consumer.

**Bullet 2 -> `compatibility`.** Keeping old request modes from changing meaning applies unchanged to consumer compatibility.

> Do make an added operation explicit in its input and result contract; don't overload an existing mode so that old callers unknowingly request new behavior.

**Bullet 3 -> `modifiability`.** Fan-out and affected callers are the impact of a bounded implementation change.

> Do price the new operation's interface fan-out, including old callers it would require to branch; don't equate an owner-local implementation with a narrow addition.

**Bullet 4 -> `compatibility`.** Retaining the old operation contract applies even without an extendability objective.

> Do preserve original-operation cases alongside new ones; don't redefine the old result to avoid implementing a genuinely distinct capability.

**Bullet 5 -> `extensibility`.** The same sentence guards the existing-hook claim from counting hook creation as admission.

> Do separate creating a hook from using it later; don't count the hook-creation core edits as evidence that the first addition required no core change.

**Bullet 6 -> `modifiability`.** Module-count gaming can conceal the semantic impact of any bounded edit.

> Don't merge unrelated responsibilities into a large module to satisfy a module count; keep owner impact and semantic changes visible under the counting rule.

### extensibility

**Bullet 1 -> `extendability`.** A newly created hook needs this same independent fixture to establish its adequacy.

> Do test a separately implemented extension through public contract data; don't let a built-in's access to private host state stand in for a usable hook.

**Bullet 3 -> `extendability`.** Creating a hook requires these same explicit lifecycle and failure obligations.

> Do state lifecycle and failure obligations at the hook; don't require extension authors to discover host cleanup behavior by reading unrelated internals.

**Bullet 4 -> `modifiability`.** An implementation-impact ledger must also count executable edits hidden as configuration.

> Do keep registration data separate from core-source accounting; don't conceal executable host edits in a file that happens to be called configuration.

**Bullet 5 -> `compatibility`.** Old-host support cannot be established using only a modified-host test.

> Do declare which existing contract revision admits an extension; don't claim old-host support from tests run only against a modified host.

**Bullet 6 -> `conformance`.** A component using undocumented privileged access is not evidence of meeting the declared contract.

> Don't grant undocumented built-in access to satisfy an extension's new output; identify the missing host capability as a contract change instead of calling it conformance.

## Definition comparisons

### Extendability / extensibility

**extendability:**

> Extendability means a new capability can be added by changing existing core source
> or interfaces within an agreed change surface. Follow this repository's core-edit
> convention, distinguishing additions through an existing hook (`extensibility`)
> and greater deployment capacity (`expandability`).

**extensibility:**

> Extensibility means new behavior can attach through an existing extension contract
> without changing the core implementation for that addition. Define registration,
> inputs, outputs, lifecycle, and host boundaries; distinguish creating the seam
> through core edits (`extendability`) and general assembly (`composability`).

**One-read verdict: yes, within the repository convention.** Core/interface changes versus a pre-existing contract without per-addition core edits is explicit. A reader can identify the test, but cannot route a concrete addition before inspecting the hook. The distinction does not establish that this terminology is universal.

### Expandability / scalability-adjacent wording

**expandability:**

> Expandability means an installation can gain usable capacity through planned
> resource or deployment-unit additions. Specify the admission, placement, routing,
> and operating transition that make an addition usable; distinguish the growth
> curve under workload (`scalability`) and a new function (`extendability`).

**scalability:** No authored `skills/088-scalability/SKILL.md` exists. Its Definition therefore cannot honestly be quoted. The available counterpart is the exact distinguishing criterion in `references/disambiguation-map.md`:

> Service behavior and resource needs remain acceptable as a specified workload dimension grows.

**One-read verdict: yes for the definition versus the map criterion; no claim of comparing two authored definitions.** Admitting a usable resource is different from preserving acceptable behavior under increasing workload. Operational terms such as capacity, shared ceilings, routing, and headroom occur in both concerns. The description phrase "remove the capacity ceiling" does not preserve the distinction as clearly as the definition.

### Enhanceability / evolvability

**enhanceability:**

> Enhanceability means an existing capability can be improved against its existing
> acceptance criteria without becoming a separately accepted capability. Identify
> the refinement surface and the old result being improved; separate a supporting
> function (`augmentability`) and a sequence of future changes (`evolvability`).

**evolvability:**

> Evolvability means the system can accommodate a sequence of changing needs without
> losing a workable path for subsequent changes. Connect design decisions, migrations,
> retirement, and cumulative constraints across that sequence; distinguish the cost
> of a particular edit (`modifiability`) and an isolated addition (`extendability`).

**One-read verdict: yes for the central contrast, partly for boundaries.** Refining one existing capability under retained criteria differs from retaining a workable path through successive changes. The latter can include successive refinements, so these are acceptance scopes rather than mutually exclusive kinds of work. "Make future quality upgrades easier" in enhanceability weakens the otherwise clear distinction.

## Count symmetry and its cause

Counts below are top-level Rules of thumb bullets, Done checklist items, and Failure modes bullets. Verification sections are prose: counting their sentences as checks would be arbitrary. Each has zero verification-list bullets; that says nothing about the number of actions packed into the prose.

| Skill | Rules | Done checks | Failure modes | Same counts as |
| --- | --- | --- | --- | --- |
| additivity | 6 | 7 | 4 | All six other batch-1 skills |
| augmentability | 6 | 7 | 4 | All six other batch-1 skills |
| enhanceability | 6 | 7 | 4 | All six other batch-1 skills |
| evolvability | 6 | 7 | 4 | All six other batch-1 skills |
| expandability | 6 | 7 | 4 | All six other batch-1 skills |
| extendability | 6 | 7 | 4 | All six other batch-1 skills |
| extensibility | 6 | 7 | 4 | All six other batch-1 skills |

**Cause: target shape.** The authoring pass used six rules, seven checks, and four failures for every entry despite allowed ranges of 5-10, 6-10, and 3-6. This is an authoring-process finding, not an inference that matching numbers alone prove filler. There is no content-based justification for these exact equal totals. It produced predictable segmentation: acceptance identity, baseline/boundary, implementation surface, verification, and report recur as checklist slots. Several different checks are compressed into a single item while others restate workflow outputs. Each count should emerge after content selection; changing counts merely to make them different would repeat the problem.

## Design-guide substance and line budgets

Every design guide contains populated Use when / Trade-off / How to verify triads, not empty headings. The practices remain short engineering sketches, not executed implementation recipes. Counts include headings and blank lines, measured from the current files.

| Skill | Concrete practice example | Populated triads | Body | Design guide | Worked example | Body + both refs | Full SKILL + both refs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| additivity | Baseline-relative ledger, overlap identity, residual diagnosis | 3 | 124 | 47 | 42 | 213 | 221 |
| augmentability | Separate result surface, projection, explicit adoption, removal | 4 | 125 | 51 | 48 | 224 | 233 |
| enhanceability | Replaceable strategy, paired evaluation, staged adoption | 3 | 126 | 46 | 54 | 226 | 235 |
| evolvability | Change-driver boundary, coexistence, retirement, irreversible ledger | 4 | 125 | 51 | 44 | 220 | 229 |
| expandability | Admission, placement, shared ceiling, interrupted-addition checkpoint | 4 | 125 | 51 | 45 | 221 | 229 |
| extendability | Owner dispatch, explicit interface, internal seam, change-surface ledger | 4 | 126 | 50 | 52 | 228 | 237 |
| extensibility | Registration, independent fixture, lifecycle, revision/authority | 4 | 127 | 48 | 47 | 222 | 231 |

Against the requested **150-250 total-line guideline**, all seven fit whether total means body plus references or complete SKILL file plus references. Every reference is also below the existing per-file 150-line limit. The existing authoring guide specifies 80-180 body lines and a 250-line hard body cap; it does not previously define a combined 150-250 budget. These are distinct checks. Meeting either budget does not demonstrate adequate depth.

Specific depth gaps are the absent noisy-measurement procedure in additivity, ambiguous accepted helper side effects in augmentability, refinement-effort evidence in enhanceability, worked cost accounting in evolvability, a capacity boundary probe in expandability, an actual owner/interface ledger in extendability, and a failed-activation cleanup example in extensibility. These are findings, not requests to pad guides to a line target.

## Description-only routing test

This is a manual semantic reading of the seven current descriptions, not a model invocation, measured classifier accuracy, keyword score, or Phase-5 evaluation artifact. Existing code and user intent were deliberately unavailable. Exclusion clauses count as routing evidence.

| Prompt | Best batch-1 description | Why / ambiguity |
| --- | --- | --- |
| "make this extensible" | `extensibility`, provisional | Direct term affinity, but the description requires an existing contract. `extendability` becomes appropriate if a hook must be built. No equal semantic match after reading the exclusions; intent remains unresolved. Ask the user whether a usable hook exists. |
| "let people add plugins" | `extensibility`, provisional | "add a plugin" is an explicit trigger. "Let people" can mean designing a plugin facility, which the same description excludes if core creation is needed. Strongest surface match, conditional rather than a justified final route. Ask the user whether this is host-contract creation or an implementation through an existing contract. |
| "add a new export format" | **Tie: `extendability` / `extensibility`** | An additional result type matches the former; a registered formatter matches the latter. Neither description has enough evidence to choose without inventing architecture. Ask the user whether an existing formatter contract admits the format, then inspect it. |
| "add more workers" | `expandability` | Direct match to "attach more workers" and resource additions. If the real goal is a throughput/workload growth curve, `scalability` is the catalogue sibling outside this batch; this prompt alone requests an addition. |
| "make this easier to change over time" | `evolvability`, provisional | The future-change sequence wording is strongest. `enhanceability` overlaps through "make future quality upgrades easier", but this prompt does not restrict change to one capability's quality, so it is not an equal fit. `maintainability` or `modifiability` outside this batch may fit after clarification. Ask the user for likely changes and whether they form a sequence. |
| "improve the accuracy of this parser" | `enhanceability` among batch-1 descriptions | "refine the current parser" and "improve the existing result" match directly. This is a routing defect: its body routes an output-error question alone to `accuracy`. That sibling is the likely full-catalogue destination if only error against a reference matters. Ask the user whether the acceptance question is value error or the engineering surface for repeatable refinements. |

Only the export-format prompt is an equal description-level fit under this reading. The two plugin prompts remain architecturally unresolved even though extensibility has the stronger lexical fit. The parser prompt exposes a description/body boundary mismatch; a confident batch-local winner can still be the wrong catalogue-wide route.

## Proposed similarity threshold; no validator change

The validator computes Jaccard similarity over sets of lowercased body word five-grams, including headings, and rejects only a score greater than 0.35. It does not compare supporting-reference prose. Recomputing with its actual functions yields a maximum of **0.008767123287671232**, additivity/extensibility, among the **42 authored pairs involving batch 1**. This agrees with the previously reported rounded 0.0088.

**Proposal for review: lower the body rejection threshold to 0.05.** This is a provisional repository tooling policy, not an empirically calibrated optimum or a system requirement target. It leaves current bodies below the proposed cutoff while making substantial exact-phrase reuse easier to flag than 0.35. The observed maximum from ten authored skills is too small a sample to establish a reliable cutoff.

Before adoption, compare intentionally copied passages of different lengths and legitimate shared section headings against the unchanged pilot/batch corpus; inspect false positives and misses. A whole-body set score dilutes short copied passages and ignores repeated occurrences. A lower number cannot detect paraphrased filler, repeated rhetorical structure, or transferable advice, as this audit demonstrates. No threshold, tests, or validator code were changed.

## Uncertain claims and limits

Unchanged-transfer destinations and routing verdicts are reviewer judgments based on the local map, not verified performance of an agent router. Some named siblings exist only in the catalogue. No missing sibling definition has been invented. Ask the user about intended terminology, actual hook availability, capacity measures, and change scenarios before deciding their application. Findings do not establish product behavior, accuracy gains, capacity gains, or future migration feasibility.

## Validation evidence

- `python scripts/validate_skills.py --only 5,14,42,43,44,46,47`: seven checked, zero errors.
- `python scripts/validate_skills.py`: ten checked, 104 absent todo entries, zero errors.
- `git diff --check`: passed.
- A changed-path guard confirmed only this audit, the rewritten batch review, and the authoring guide changed. No skill, reference under a skill, validator, catalogue, or index was edited.

These are structural checks, not evidence against the semantic findings above. No batch 2 authoring was performed. This audit is a documentation-only follow-up, not completion of another production phase; the changes remain uncommitted for review.
