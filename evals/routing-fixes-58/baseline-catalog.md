- **accessibility-access-control**: Separates interaction barriers from permission checks when tickets say "keyboard users get stuck", "screen reader skips errors", "stop cross-team edits", or "revoked access still works". Asks which branch. Not for looks (see attractiveness), personal-data lifecycle (see privacy), or threat review (see security-control-and-security).

- **accountability**: Attributes actions when asked "keep the initiator", "tag delegated jobs", or "link actions to logins". Ask the user if identity vs review evidence is unclear. Not for evidence sufficiency (see auditability), artifact links (see traceability), or hiding identity (see anonymity).

- **accuracy**: Reduces error against a reference when tickets say "our sensor readings are off", "the weight is wrong against the scale", or "rounding hides the error". Not for following a specified algorithm (see correctness) or confidence labels (see certainty).

- **adaptability**: Preserves required behavior across external changes when tickets say "the supplier changed its feed", "the importer broke after their update", or "keep importing after the upstream change". Not for built-in alternatives (see flexibility), platform moves (see portability), or applying settings (see reconfigurability).

- **additivity**: Checks summed gains when asked "compare combined savings", "avoid double-counting", or "measure each contribution". Ask the user if sums vs joined behavior is unclear. Not for assembly contracts (see composability) or admitting resources (see expandability).

- **adjustability**: Tunes existing controls when asked "lower this threshold", "change the polling interval", or "adjust batch size". Ask the user if tuning vs new options is unclear. Not for defining options (see configurability) or switching arrangements (see reconfigurability).

- **affordability**: Checks financial limits when asked "cap running costs", "include setup costs", or "price this workload". Ask the user if budget fit vs delivery feasibility is unclear. Not for delivery under all constraints (see feasibility) or continued value (see viability).

- **agility**: Handles reprioritized delivery when users say "the roadmap changed again", "swap in this urgent feature", or "feedback changed what we should ship". Not for progressing one unchanged request (see changeability) or reducing code-edit effort (see modifiability).

- **analyzability**: Maps system causes and change impact when tickets say "which layer could explain these failures", "what depends on this schema", or "what breaks if we remove this field". Not for localizing one failing execution (see debuggability) or adding runtime signals (see observability).

- **anonymity**: Tests identity linkage when asked "can this export identify people", "check linked fake IDs", or "compare repeated releases". Ask the user which observer and linkage are in scope. Not for data purpose/lifecycle (see privacy), recipient permissions (see confidentiality), or actor attribution (see accountability).

- **atomicity**: Specifies all-or-none visible effects when tickets say "we see half an update", "a failed write leaves partial changes", or "rollback happens after users saw the change". Not for preserving acknowledged writes (see durability), restoring service (see recoverability), or agreement between values (see consistency).

- **attractiveness**: Tests appearance when asked "compare these visual styles", "this layout looks dull", or "review the screen design". Ask the user if looks vs feelings after use is unclear. Not for feelings after use (see likeability), recognizing characters (see legibility), or completing tasks (see usability).

- **auditability**: Prepares review evidence when asked "reconstruct this approval", "explain audit gaps", or "export review records". Ask the user if review evidence vs actor identity is unclear. Not for actor identity (see accountability), artifact links (see traceability), or checking selected rules (see conformance).

- **augmentability**: Adds a separately accepted supporting capability when users say "add reply suggestions", "put annotations beside reports", or "add a helper without replacing manual work". Not for improving the original capability (see enhanceability) or admitting through an existing hook (see extensibility).

- **availability**: Measures usable service time when asked "count checkout downtime", "keep sessions through deploys", or "measure service readiness". Ask the user if outage time vs failure counts is unclear. Not for failure-free operation (see reliability) or restoring usable state (see recoverability).

- **certainty**: Bounds confidence when asked "label missing evidence", "show conflicting sources", or "mark unverified results". Ask the user if confidence vs value error is unclear. Not for value error (see accuracy) or formal guarantees (see provability).

- **changeability**: Traces one request through decision, delivery, and adoption when tickets say "this ticket is stuck after approval", "merged but not rolled out", or "who needs to hand this change over". Not for changing priorities (see agility) or reducing code-edit effort (see modifiability).

- **communicativeness**: Times user feedback when asked "notify on export completion", "report errors sooner", or "send job updates". Ask the user if notifications vs visible status is unclear. Not for explaining current state and actions (see self-descriptiveness) or clarifying a standalone explanation (see comprehensibility).

- **compatibility**: Protects coexistence when tickets say "these tools overwrite each other", "run both tools side by side", or "installing one breaks the other". Not for exchanging meaningful data (see interoperability).

- **completeness**: Checks required members when asked "find omitted order IDs", "check every attachment", or "duplicates hide missing rows". Ask the user if missing items vs missing topics is unclear. Not for breadth of explanations (see comprehensiveness) or wrong computed values (see correctness).

- **complexity-interacting-complexity**: Maps interaction burden when tickets say "these flags change each other", "callbacks trigger a chain reaction", or "how many paths must we reason about". Not for choosing fewer mechanisms (see simplicity) or locating one execution defect (see debuggability).

- **composability**: Preserves behavior when joining components when tickets say "these stages break when chained", "who closes the shared stream", or "the pipeline changes error handling". Not for assembly effort (see integratability) or summed contributions (see additivity).

- **comprehensibility**: Clarifies meaning when asked "explain this error", "name the actor", or "define this term". Ask the user if unclear concepts, reading flow, or notation rules are the issue. Not for reading flow (see readability), the whole system model (see understandability), or in-context state cues (see self-descriptiveness).

- **comprehensiveness**: Checks topic coverage for an audience when users ask "this guide skips recovery", "are we missing topics for operators", or "our manual only covers the happy path". Not for a fixed inventory (see completeness), unclear passages (see comprehensibility), or the system model (see understandability).

- **conciseness**: Shortens content while preserving meaning when users say "cut the repeated wording", "make this shorter but keep the exceptions", or "remove duplicated explanations". Not for missing topics (see comprehensiveness), recognizing characters (see legibility), or reading structure (see readability).

- **confidentiality**: Restricts disclosure to authorized recipients when tickets say "the API leaks internal notes", "a cache shows another team's data", or "errors expose private fields". Not for purpose and retention (see privacy), identity linkage (see anonymity), or alteration protection (see integrity).

- **configurability**: Defines valid settings when asked "list supported options", "resolve config conflicts", or "show default precedence". Ask the user if options vs tuning vs transitions is unclear. Not for tuning a value (see adjustability), switching state (see reconfigurability), or user-authored behavior (see customizability).

- **conformance**: Checks chosen rules when asked "validate our schema", "reject invalid field names", or "show violated rules". Ask the user whether rules are already selected if unstated. Not for choosing a convention (see standardizability-standardization-standard).

- **consistency**: Aligns representations when tickets say "the list and detail page disagree", "the cache shows an older status", or "these views conflict at the same revision". Not for external reference error (see accuracy) or unauthorized edits (see integrity).

- **controllability**: Makes runtime state changes controllable when tickets say "pause intake without killing active jobs", "resume only this worker", or "the stop command says OK but work keeps starting". Not for status display (see visibility), fleet policy (see manageability), or whole operator tasks (see operability).

- **correctness**: Checks specified behavior when asked "fix this boundary case", "match the decision table", or "reject expired requests". Ask the user if contract failure vs reference error is unclear. Not for error against measured truth (see accuracy), missing required members (see completeness), or selected-rule audits (see conformance).

- **customizability**: Supports user-authored behavior or presentation when tickets say "let users write report templates", "customers need their own rules", or "allow custom output layouts". Not for built-in choices (see configurability), fitting a work context (see tailorability), or plugin admission (see extensibility).

- **debuggability**: Localizes one execution defect when asked "replay this parser crash", "trace this bad value", or "inspect this failing input". Ask the user if one replay vs system analysis is unclear. Not for system-wide cause or change-impact analysis (see analyzability) or adding test seams (see testability).

- **decomposability**: Separates responsibilities when asked "extract billing from rendering", "give this part its own state", or "run the validator alone". Ask the user if splitting duties vs organizing imports is unclear. Not for dependency layout alone (see structuredness) or joining components (see composability).

- **defensibility**: Designs authorized containment during an attack when tickets say "a revoked token still runs jobs", "give responders a kill switch", or "check that containment actually stopped it". Not for full threat/control design (see security-control-and-security), normal restoration (see recoverability), or passive diagnosis (see observability).

- **demonstrability**: Builds inspectable demos when asked "show the payment failure", "replay the approval demo", or "let reviewers inspect the result". Ask the user if demonstration vs acceptance evidence is unclear. Not for proving every possible case (see provability) or designing acceptance evidence (see verifiability).

- **dependability**: Combines failure evidence for a scoped reliance decision when users ask "can we rely on this for dispatch", "show the gaps across our failure checks", or "uptime looks fine but dispatch is unsafe". Not for usable time (see availability), failure trials (see reliability), or hazard analysis (see safety).

- **distributivity**: Defines node placement when asked "assign key ranges", "prevent duplicate shard owners", or "redistribute partitions". Ask the user if placement rules vs observing current ownership is unclear. Not for workload growth curves (see scalability).

- **durability**: Preserves acknowledged state through named faults when tickets say "saved edits vanish after restart", "did we acknowledge before saving", or "failover loses confirmed writes". Not for partial visibility (see atomicity), restoration (see recoverability), or continued operation (see fault-failure-tolerance).

- **effectiveness**: Checks attained outcomes when asked "count resolved issues", "verify stock was reconciled", or "stop counting clicks as success". Ask the user if outcomes vs task fit is unclear. Not for capability presence (see functionality) or task fit alone (see suitability).

- **efficiency-device-efficiency**: Reduces resources per useful result when users say "less CPU for each completed report", "stop sending the same bytes twice", or "less compute per result". Not for operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or resource stewardship (see sustainability).

- **enhanceability**: Refines existing capabilities when asked "improve the current parser", "replace this algorithm with a better one", or "upgrade this feature in place". Ask the user if refinement vs a new helper is unclear. Not for judging output error alone (see accuracy), adding helpers (see augmentability), or staged changes (see evolvability).

- **evolvability**: Plans successive changes with prior state and obligations carried forward when users say "will this migration block the next release", "plan the next few migrations", or "when can we remove the old bridge". Not for one code edit (see modifiability) or one capability refinement (see enhanceability).

- **expandability**: Admits added resources into an existing installation's usable capacity when tickets say "the new worker never picks up jobs", "bring another storage unit online", or "add usable nodes to this cluster". Not for workload growth curves (see scalability) or adding core functionality (see extendability).

- **expressiveness**: Adds missing meanings when asked "express an owner-only rule", "add explicit denial", or "keep distinct policies distinct". Ask the user if missing constructs vs ambiguous wording is unclear. Not for shortening adequate notation (see conciseness) or setting precision alone (see formality).

- **extendability**: Plans bounded core changes or builds missing extension hooks when users say "we need a hook before adding plugins", "this format needs core changes", or "add an operation the core cannot handle". Not for using an existing hook (see extensibility) or admitting resources (see expandability).

- **extensibility**: Checks hooks when asked "plugins without core edits", "customer report plugins", or "register another provider". Ask the user whether core edits are allowed if unstated; inspect the hook before accepting. Not for building or widening the hook (see extendability) or composing component contracts (see composability).

- **fault-failure-tolerance**: Checks service during faults when asked "serve with a dead worker", "write through a partition", or "test failover under load". Ask the user if continued service vs restoration is unclear. Not for restoration (see recoverability), uptime accounting (see availability), or adverse input (see robustness).

- **feasibility**: Tests initial delivery constraints when asked "try the offline renderer", "check dependency access", or "test this design here". Ask the user if build feasibility vs budget or continued worth is unclear. Not for budget fit alone (see affordability) or ongoing worth (see viability).

- **flexibility**: Supports alternative ways to perform the same task when tickets say "offer manual and automatic routes", "let users choose another way through", or "keep both workflows supported". Not for external changes (see adaptability), tuning a control (see adjustability), or switching state (see reconfigurability).

- **formality**: Defines precise notation when asked "define allowed transitions", "give states one meaning", or "specify missing values". Ask the user if notation precision vs explanation clarity is unclear. Not for proving the stated property (see provability) or choosing acceptance evidence (see verifiability).

- **functionality**: Defines absent capabilities when asked "add export downloads", "add queued-job cancellation", or "list required operations". Ask the user if a missing operation vs broken existing behavior is unclear. Not for wrong existing behavior (see correctness), task fit (see suitability), or achieved outcomes (see effectiveness).

- **generality**: Covers related cases with one abstraction when asked "unify these range checkers", "cover quantities and durations", or "stop field-specific branches". Ask the user which case family and common rule are intended if unstated. Not for different task roles (see versatility) or moving an artifact to another context (see reusability).

- **immunity**: Checks whether a mechanism excludes a named failure path under assumptions when users ask "can text still reach the command runner", "remove this failure path completely", or "does the old loader bypass the fix". Not for bounded response (see robustness), exposure mapping (see susceptibility), or threat review (see security-control-and-security).

- **installability**: Checks installation state when asked "fix partial upgrades", "start a clean install", or "keep user data on uninstall". Ask the user if setup on one target vs platform adaptation is unclear. Not for moving between execution platforms (see portability) or deployment uptime (see availability).

- **integratability**: Bounds assembly work when asked "reduce adapter glue", "wire agreed message contracts", or "assign integration ownership". Ask the user if wiring effort vs exchanged meaning is unclear. Not for exchange meaning (see interoperability).

- **integrity**: Controls unauthorized or unintended alteration when tickets say "stale edits overwrite approved changes", "block updates to protected fields", or "check whether this import was tampered with". Not for factual error (see accuracy), disclosure (see confidentiality), or partial commits (see atomicity).

- **interoperability**: Aligns exchanged meaning when asked "agree on timestamp units", "fix payload interpretation", or "distinguish queued from completed". Ask the user if meaning vs connection setup is unclear. Not for assembly effort (see integratability).

- **learnability**: Checks learning through product use when tickets say "new users never get the hang of it", "people still need help after practicing", or "can beginners do it unaided next time". Not for courses (see trainability), experienced task performance (see usability), or reading flow (see readability).

- **legibility**: Checks character recognition when asked "distinguish I from l", "fix lookalike symbols", or "test this font on the display". Ask the user if characters vs reading flow is unclear. Not for code/text reading flow (see readability), visual appeal (see attractiveness), or broader access barriers (see accessibility-access-control).

- **likeability**: Checks feelings after use when asked "compare workflow preferences", "collect user frustration", or "review session satisfaction". Ask the user if sentiment vs appearance or task success is unclear. Not for visual appeal (see attractiveness), task completion (see usability), or acquiring skill (see learnability).

- **localizability**: Separates locale behavior from business logic when tickets say "add a language without changing the code", "this date is ambiguous after translation", or "the decimal comma breaks our export". Not for platform moves (see portability) or character recognition (see legibility).

- **maintainability**: Reduces recurring upkeep when asked "stop repeated repair work", "help future maintainers", or "review ongoing fix effort". Ask the user if ongoing upkeep vs one edit or support case is unclear. Not for one edit (see modifiability), a support encounter (see supportability), or successive migrations (see evolvability).

- **manageability**: Coordinates fleet policy when asked "reconcile node settings", "find missed fleet updates", or "track local exceptions". Ask the user if fleet policy vs one runtime task is unclear. Not for one runtime task (see operability), one state-changing command (see controllability), or configuration transitions (see reconfigurability).

- **maturity**: Assesses operating history when asked "check use since the fix", "link returning defects", or "review exercised workflows". Ask the user if past experience vs future failure trials is unclear. Not for future failure trials (see reliability), combined assurance (see dependability), or upkeep effort (see maintainability).

- **measurability**: Defines measurements when asked "define queue-delay units", "choose counting boundaries", or "check instrument resolution". Ask the user if measurement vs state inference or acceptance evidence is unclear. Not for inferring hidden runtime state (see observability) or selecting acceptance evidence (see verifiability).

- **mobility**: Preserves active client work through movement when tickets say "keep this upload running as networks change", "switch connections without restarting the task", or "roaming starts the upload again". Not for resuming after a relocation pause (see nomadicity) or moving software platforms (see portability).

- **modifiability**: Bounds one code change and its ripple effects when tickets say "how much code will this edit touch", "changing this rule breaks other modules", or "estimate the work for this code change". Not for recurring upkeep (see maintainability), request progress (see changeability), or successive changes (see evolvability).

- **nomadicity**: Restores useful work after relocation when tickets say "resume my draft after reconnecting elsewhere", "pick up where I left off at the next site", or "reopen saved work after changing networks". Not for uninterrupted activity during movement (see mobility) or outage restoration (see recoverability).

- **observability**: Distinguishes runtime states when asked "join retries to attempts", "separate queued from stuck", or "explain missing results from signals". Ask the user if inference vs status display is unclear. Not for displaying status alone (see visibility), defining units (see measurability), or one defect replay (see debuggability).

- **operability**: Builds operator task paths when asked "handle a partial rerun", "verify the runtime task finished", or "define on-call exit checks". Ask the user if a whole task vs one control or support case is unclear. Not for fleet policy (see manageability), a single control action (see controllability), or a user support case (see supportability).

- **performance-efficiency-time-or-space-bounds**: Sets fixed-load bounds when asked "set an export deadline", "cap operation memory", or "specify completion percentiles". Ask the user if absolute latency vs variation is unclear. Not for run-to-run variation (see predictability), resources per result (see efficiency-device-efficiency), or competing service classes (see quality-of-service).

- **portability**: Moves execution platforms when asked "isolate OS assumptions", "adapt to the target runtime", or "preserve behavior on the new platform". Ask the user if platform differences vs installation alone is unclear. Not for setup on one target (see installability), locale adaptation (see localizability), or user movement (see mobility).

- **predictability**: Bounds run variation when asked "limit completion-time spread", "measure rare pauses", or "compare fast and slow runs". Ask the user if variation vs an absolute deadline is unclear. Not for an absolute tail-latency limit (see performance-efficiency-time-or-space-bounds), control flapping (see stability), or product options (see variability).

- **privacy**: Defines personal-data purpose and lifecycle when tickets say "we keep storing data we never use", "stop sending emails to analytics", or "deleted accounts return after restore". Not for read permissions alone (see confidentiality) or preventing identity linkage (see anonymity). Treats policy labels as supplied constraints.

- **provability**: Proves modeled claims when asked "prove the balance invariant", "check every allowed transition", or "list proof assumptions". Ask the user if proof vs selected test evidence is unclear. Not for testing selected cases (see verifiability) or defining notation alone (see formality).

- **quality-of-service**: Defines service per competing class when tickets say "batch jobs block checkout", "background jobs never get a turn", or "one tenant hogs the workers". Not for one-operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or permissions (see accessibility-access-control).

- **readability**: Improves reading flow when asked "reduce this nesting", "rename confusing locals", or "reorder these sentences". Ask the user if structure vs missing concepts or character recognition is unclear. Not for character recognition (see legibility) or explaining missing concepts (see comprehensibility).

- **reconfigurability**: Controls configuration transitions when asked "preserve queued work on mode switch", "resume a config change", or "check ownership during cutover". Ask the user if a transition vs tuning is unclear. Not for the options menu (see configurability), tuning a value (see adjustability), or supporting alternatives (see flexibility).

- **recoverability**: Restores usable state when asked "restore saved orders", "check restored checkout", or "avoid duplicate replays". Ask the user if restoring service vs preserving writes is unclear. Not for operation during faults (see fault-failure-tolerance), acknowledged-state retention (see durability), or essential mission continuity (see survivability).

- **reliability**: Measures failures over a defined operating profile when tickets say "the worker keeps crashing overnight", "retries hide the original failures", or "run this workload without restarting". Not for usable time (see availability), operating through held faults (see fault-failure-tolerance), or restoration (see recoverability).

- **repeatability**: Checks reruns with held conditions when asked "repeat the same fixture", "keep setup unchanged", or "compare repeated outputs". Ask the user if same setup vs independent reconstruction is unclear. Not for independent reconstruction elsewhere (see replicability) or bounds on service variation (see predictability).

- **replaceability**: Checks substitution when asked "retire the old backend", "preserve callers on replacement", or "migrate provider state". Ask the user if replacement vs coexistence or wrapping is unclear. Not for coexistence alone (see compatibility).

- **replicability**: Supports independent reconstruction when asked "rebuild this experiment elsewhere", "share the experiment setup", or "remove laptop-only assumptions". Ask the user if reconstruction vs ordinary reruns is unclear. Not for reruns in the original setup (see repeatability) or moving the product to another platform (see portability).

- **reusability**: Reuses a shared artifact when asked "decouple the checker from HTTP", "run one validator in web and CLI", or "remove the copied helper". Ask the user if reuse vs broader cases or joined stages is unclear. Not for broadening an abstraction family (see generality) or joining stage contracts (see composability).

- **robustness**: Bounds bad-input effects when asked "reject oversized requests safely", "release failed reservations", or "avoid partial rejected rows". Ask the user if input stress vs modeled faults is unclear. Not for component faults (see fault-failure-tolerance), threat review (see security-control-and-security), or normal-profile failures (see reliability).

- **safety**: Prevents named harm when tickets say "do not delete records that are on hold", "can stopping this action cause harm", or "the safety check is only in the UI". Not for adversary controls (see security-control-and-security), usable service time (see availability), or generic bad-input handling (see robustness).

- **scalability**: Tests demand growth when asked "plot throughput growth", "find the load plateau", or "compare workers under load". Ask the user if growth vs resource admission is unclear. Not for resource admission (see expandability), fixed-load bounds (see performance-efficiency-time-or-space-bounds), or unit resource cost (see efficiency-device-efficiency).

- **security-control-and-security**: Designs controls against adversary paths when tickets say "how could an attacker abuse this feature", "where should we block this attack", or "the normal route is fixed but retries bypass it". Not for disclosure alone (see confidentiality), alteration alone (see integrity), or incident containment (see defensibility).

- **self-descriptiveness**: Explains context at the action when asked "show why this control is disabled", "explain this action now", or "label the current report". Ask the user if in-context cues vs a separate explanation is unclear. Not for later notifications (see communicativeness), standalone explanations (see comprehensibility), or backend diagnosis (see observability).

- **simplicity**: Removes unjustified mechanisms when asked "remove this unused dispatcher", "drop the fixed-path registry", or "justify this plugin framework". Ask the user if unnecessary machinery vs interaction burden is unclear. Not for mapping interaction burden (see complexity-interacting-complexity) or reading flow alone (see readability).

- **stability**: Controls drift and feedback over time when tickets say "the autoscaler keeps flapping", "the output drifts with steady input", or "our controllers undo each other's changes". Not for failure occurrence (see reliability), run-to-run variation (see predictability), or operation latency (see performance-efficiency-time-or-space-bounds).

- **standardizability-standardization-standard**: Selects common conventions when asked "adopt an event format", "publish naming rules", or "agree on field names". Ask the user whether a convention exists before routing a consistency request. Not for checking already selected rules (see conformance).

- **structuredness**: Enforces dependency organization when tickets say "domain code imports the web layer", "these imports violate our layer rules", or "the package layout hides a cycle". Not for finding separable responsibilities (see decomposability) or matching peer conventions (see uniformity).

- **suitability**: Checks capability fit when asked "feed this offline importer", "match this handoff format", or "compare features for our task". Ask the user if task fit vs achieved outcome is unclear. Not for capability presence alone (see functionality) or achieved outcomes (see effectiveness).

- **supportability**: Supports a specific user case when asked "prepare support diagnostics", "give support an investigation path", or "resolve this export case". Ask the user if support work vs code upkeep is unclear. Not for recurring upkeep (see maintainability), state inference alone (see observability), or delivery handoffs (see changeability).

- **survivability**: Preserves essential mission work when asked "dispatch after site loss", "operate without central login", or "reconcile offline assignments". Ask the user if essential continuity vs restoration is unclear. Not for normal restoration (see recoverability), routine fault handling (see fault-failure-tolerance), or uptime accounting (see availability).

- **susceptibility**: Maps exposure and enabling conditions without presuming exploitation when users ask "does this dependency issue affect us", "can the importer reach that code", or "is the disabled endpoint our only route". Not for mechanism exclusion (see immunity), bounded adverse response (see robustness), or active containment (see defensibility).

- **sustainability**: Checks environmental stewardship when asked "measure report energy", "extend useful device life", or "avoid replacing usable hardware". Ask the user which environmental objective is intended. Not for resources per result (see efficiency-device-efficiency), purchase price (see affordability), or continued business value (see viability).

- **tailorability**: Fits supported workflows when asked "choose night-shift presets", "map team needs to presets", or "fit team schedules". Ask the user if supported choices vs custom behavior is unclear. Not for authored behavior (see customizability), defining settings (see configurability), alternatives (see flexibility), or external changes (see adaptability).

- **testability**: Adds test controls when asked "force the timeout branch", "inject a clock", or "observe which test path ran". Ask the user if missing test seams vs one failing replay is unclear. Not for selecting acceptance evidence (see verifiability) or diagnosing a particular failing execution (see debuggability).

- **traceability**: Links versioned artifacts and change impact when users ask "which tests cover this requirement", "what breaks if we delete this function", or "these links point to an old rule". Not for actor identity (see accountability), review conclusions (see auditability), or test control and observation (see testability).

- **trainability**: Designs instruction and independent skill checks when tickets say "replace the demo with practice exercises", "people finish the course but cannot do the job", or "write training with a separate skills check". Not for learning through use (see learnability), topic coverage (see comprehensiveness), or current task success (see usability).

- **transferability**: Transfers project assets when asked "handoff linked project files", "map recipient owners", or "preserve links on transfer". Ask the user if recipient handoff vs installation or exchange is unclear. Not for moving execution platforms (see portability), ongoing system exchange (see interoperability), or rebuilding an experiment (see replicability).

- **trustability**: Supports scoped trust decisions with evidence and limits when users ask "can this tool publish without my review", "show the limits before I delegate", or "this confidence badge promises too much". Not for operational assurance (see dependability), feelings after use (see likeability), or confidence in one output (see certainty).

- **understandability**: Explains the system model when asked "map component responsibilities", "explain state ownership", or "follow the request across services". Ask the user if whole-system meaning vs one passage is unclear. Not for one unclear explanation (see comprehensibility), reading flow (see readability), or topic breadth (see comprehensiveness).

- **uniformity**: Aligns conventions across comparable peers when tickets say "list routes name the same limit differently", "use the same paging fields on these routes", or "why does only this list take pageSize". Not for selecting a common convention (see standardizability-standardization-standard) or value agreement (see consistency).

- **usability**: Checks whole-task interaction when asked "observe checkout errors", "test unaided task completion", or "measure effort through recovery". Ask the user if task success vs learning or sentiment is unclear. Not for learning (see learnability), feelings after use (see likeability), or visual appeal (see attractiveness).

- **variability**: Defines product-family combinations when asked "reject invalid edition builds", "make export require audit", or "list allowed feature sets". Ask the user if family variants vs instance settings is unclear. Not for settings of one instance (see configurability) or applying a transition (see reconfigurability).

- **verifiability**: Designs acceptance evidence when asked "replace an unworkable check", "tie evidence to this claim", or "define the pass decision". Ask the user if acceptance method vs test seams or proof is unclear. Not for adding test seams (see testability), defining units (see measurability), or constructing proofs (see provability).

- **versatility**: Supports distinct product roles when asked "import and audit stock", "add read-only inventory checking", or "keep audit mode nonmutating". Ask the user if new roles vs related cases or reuse is unclear. Not for one abstraction covering related cases (see generality) or reusing an artifact elsewhere (see reusability).

- **viability**: Checks continued value when asked "review upkeep at renewal", "compare benefits with ongoing obligations", or "plan service retirement". Ask the user if continued worth vs build feasibility or budget is unclear. Not for initial delivery (see feasibility), spending cap alone (see affordability), or environmental objectives (see sustainability).

- **visibility**: Exposes status to its intended audience when tickets say "customers cannot see export progress", "show when this job status was updated", or "the status page shows another team's job". Not for inferring hidden causes (see observability), notifying users (see communicativeness), or permission design (see accessibility-access-control).

- **wrappability**: Wraps retained implementations when asked "keep the engine behind an API", "translate native errors", or "expose the old function unchanged". Ask the user if retention vs substitution is unclear. Not for substituting the engine (see replaceability) or just wiring components (see integratability).
