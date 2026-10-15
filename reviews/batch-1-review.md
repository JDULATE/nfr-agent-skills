# Batch 1 review findings

The seven drafts have distinguishable local acceptance questions, but their rule specificity, routing, and verification depth are weaker than the previous self-scores implied. The previous review mixed instructions with findings and used identical provisional scores without evidence of equivalent quality. Those scores have been removed.

All seven use the same six-rule, seven-check, four-failure shape. This was an authoring target, not a demonstrated content need. Low literal similarity does not resolve that structural or semantic repetition.

## 005-additivity

- The definition admits any declared aggregation rule, including union. That makes the boundary with composability and consistency depend heavily on stakeholder terminology rather than an immediately recognizable additive property.
- The worked example tests exact counts; the guide names noise and drift but supplies no concrete repeated-measurement or uncertainty procedure for noisy contribution claims.
- Replay identity, ordering, and metric-accounting rules transfer unchanged to other NFRs. Original wording did not make these rules exclusive to additivity.

## 014-augmentability

- The description and example narrow supplementary capabilities to optional helpers. The definition permits a broader supporting capability, so an independently accepted mandatory supplement is poorly represented.
- The workflow gives a useful absent-helper comparison, but does not decide when an intentional original-output change from adopted helper advice is acceptable versus a failed preservation check.
- Authority labeling, read-only adoption, and dependency isolation transfer to self-descriptiveness, security, and fault tolerance; they do not by themselves establish a separately accepted supporting result.

## 042-enhanceability

- The parser example, paired-corpus checks, and error-reduction default mostly demonstrate better results, not the engineering effort or impact required to make later refinements. This risks turning an -ability skill into an accuracy evaluation.
- The description matches a parser accuracy request even though Use when routes a specified output-error question alone to accuracy. That boundary is unavailable to a router reading descriptions only.
- The trigger "make future quality upgrades easier" overlaps evolvability. Baseline retention, protected-case comparison, and stable public meanings transfer directly to accuracy or compatibility.

## 043-evolvability

- The sequence, retained intermediate state, and retirement gate distinguish the skill well, but the example primarily covers persisted-data migrations rather than other kinds of evolving constraints.
- The cumulative-effort pattern leaves the cost convention as a placeholder. No worked effort ledger shows how transitional upkeep is charged to a later change.
- Roadmap abstraction advice and ownership of speculative work transfer to modifiability or feasibility. The description overlaps a generic request to make future changes easier without establishing a sequence.

## 044-expandability

- Usable capacity and a capacity delta are not operationalized for the worker example: successfully placing work on an added worker proves eligibility, but alone does not demonstrate an increased service-capacity boundary.
- The description trigger "remove the capacity ceiling" also describes a scalability bottleneck. Admission and workload-response acceptance still require clarification.
- Headroom, placement, and shared-controller rules can be reused unchanged in scalability, distributivity, or recoverability. The last rule draws the boundary explicitly; several earlier rules do not.

## 046-extendability

- The definition clearly states the local core-edit convention, but the description cannot disambiguate an added result type until the existing extension surface is inspected.
- The illustrative module-count budget depends on packaging. The guide warns against gaming it, but supplies no worked owner/interface ledger to replace file count as the main acceptance evidence.
- Explicit operation contracts and old-caller preservation transfer directly to compatibility. Hook-creation accounting transfers to extensibility. These rules alone do not demonstrate bounded core-addition effort.

## 047-extensibility

- The description presupposes an existing contract even for "add a plugin". Requests to let people add plugins can instead require creating that contract, so an unqualified plugin trigger can route too early.
- The worked example assumes the very host contract being tested; its negative fixture rejects a result type but does not concretely exercise cleanup after a failed activation or retained-extension interaction.
- Lifecycle obligations and contract revision checks can sit unchanged in extendability or compatibility. The guide identifies authority as a boundary but does not implement or demonstrate enforcement.

## Uncertain claims and evidence limits

The growth definitions are repository conventions, not standardized definitions. No real target application, plugin host, worker installation, or migration was exercised. Scenario values and schemas are fictional. Workflow question limits have not been tested through an independent execution. Ask the user which aggregation policies, capability boundaries, workloads, contract authorities, and roadmap scenarios apply before treating these proposals as requirements.

The detailed audit in [batch-1-audit.md](./batch-1-audit.md) records exact transferable bullets, definition comparisons, counts, guide evidence, and description routing. Passing the structural validator does not establish semantic specificity or routing correctness.
