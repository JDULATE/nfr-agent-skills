- **accessibility-access-control**: Separates interaction barriers from permission checks when tickets say "keyboard users get stuck", "screen reader skips errors", "stop cross-team edits", or "revoked access still works". Asks which branch. Not for looks (see attractiveness), personal-data lifecycle (see privacy), or threat review (see security-control-and-security).

- **accountability**: Binds initiating and executing actors under a validated identity model when users ask "who approved this change", "which user queued this job", or "shared accounts hide who acted". Not for evidence sufficiency (see auditability), artifact links (see traceability), or hiding identity (see anonymity).

- **accuracy**: Reduces error against a reference when tickets say "our sensor readings are off", "the weight is wrong against the scale", or "rounding hides the error". Not for following a specified algorithm (see correctness) or confidence labels (see certainty).

- **adaptability**: Preserves required behavior across external changes when tickets say "the supplier changed its feed", "the importer broke after their update", or "keep importing after the upstream change". Not for built-in alternatives (see flexibility), platform moves (see portability), or applying settings (see reconfigurability).

- **additivity**: Tests whether separate contributions combine as claimed when users ask "do these gains add up", "are we counting the benefit twice", or "both changes together help less". Not for assembly contracts (see composability) or admitting resources (see expandability).

- **adjustability**: Tunes existing controls in a fixed arrangement when tickets say "let admins tweak thresholds", "change the polling interval", or "tune the current batch size". Not for defining options (see configurability) or switching arrangements (see reconfigurability).

- **affordability**: Checks budget fit when tickets say "this export exceeds our spending cap", "include setup and running costs", or "batch requests so this workload fits the budget". Not for delivery under all constraints (see feasibility) or continued value (see viability).

- **agility**: Handles reprioritized delivery when users say "the roadmap changed again", "swap in this urgent feature", or "feedback changed what we should ship". Not for progressing one unchanged request (see changeability) or reducing code-edit effort (see modifiability).

- **analyzability**: Maps system causes and change impact when tickets say "which layer could explain these failures", "what depends on this schema", or "what breaks if we remove this field". Not for localizing one failing execution (see debuggability) or adding runtime signals (see observability).

- **anonymity**: Assesses identity and linkage exposed to an observer when users ask "can recipients work out who this is", "these fake IDs link back to people", or "repeated exports reveal the same person". Not for data purpose/lifecycle (see privacy), recipient permissions (see confidentiality), or actor attribution (see accountability).

- **atomicity**: Specifies all-or-none visible effects when tickets say "we see half an update", "a failed write leaves partial changes", or "rollback happens after users saw the change". Not for preserving acknowledged writes (see durability), restoring service (see recoverability), or agreement between values (see consistency).

- **attractiveness**: Evaluates visual appeal when users say "this screen looks uninviting", "which visual style looks better", or "make this layout more appealing". Not for feelings after use (see likeability), recognizing characters (see legibility), or completing tasks (see usability).

- **auditability**: Defines evidence for independent review when tickets say "the reviewer cannot reconstruct this approval", "our audit trail leaves gaps", or "this export cannot answer the auditor". Not for actor identity (see accountability), artifact links (see traceability), or checking selected rules (see conformance).

- **augmentability**: Adds a separately accepted supporting capability when users say "add reply suggestions", "put annotations beside reports", or "add a helper without replacing manual work". Not for improving the original capability (see enhanceability) or admitting through an existing hook (see extensibility).

- **availability**: Improves and measures usable service time when tickets say "users get logged out on deploy", "checkout goes down during releases", or "count our downtime". Not for failure-free operation (see reliability) or restoring usable state (see recoverability).

- **certainty**: Bounds confidence claims when tickets say "stop calling guesses confirmed", "show when the evidence is missing", or "mark this result as unverified". Not for value error (see accuracy) or formal guarantees (see provability).

- **changeability**: Traces one request through decision, delivery, and adoption when tickets say "this ticket is stuck after approval", "merged but not rolled out", or "who needs to hand this change over". Not for changing priorities (see agility) or reducing code-edit effort (see modifiability).

- **communicativeness**: Defines timely user feedback when tickets say "notify me when the export is done", "the error arrives too late", or "keep users posted while a job runs". Not for explaining current state and actions (see self-descriptiveness) or clarifying a standalone explanation (see comprehensibility).

- **compatibility**: Protects coexistence when tickets say "these tools overwrite each other", "run both tools side by side", or "installing one breaks the other". Not for exchanging meaningful data (see interoperability).

- **completeness**: Checks bounded coverage when tickets say "the export skips required records", "this export leaves out an item", or "duplicates hide a missing item". Not for breadth of explanations (see comprehensiveness) or wrong computed values (see correctness).

- **complexity-interacting-complexity**: Maps interaction burden when tickets say "these flags change each other", "callbacks trigger a chain reaction", or "how many paths must we reason about". Not for choosing fewer mechanisms (see simplicity) or locating one execution defect (see debuggability).

- **composability**: Preserves behavior when joining components when tickets say "these stages break when chained", "who closes the shared stream", or "the pipeline changes error handling". Not for assembly effort (see integratability) or summed contributions (see additivity).

- **comprehensibility**: Clarifies a particular explanation when users say "people misunderstand this error", "what does this requirement mean", or "this paragraph leaves the actor unclear". Not for reading flow (see readability), the whole system model (see understandability), or in-context state cues (see self-descriptiveness).

- **comprehensiveness**: Checks topic coverage for an audience when users ask "this guide skips recovery", "are we missing topics for operators", or "our manual only covers the happy path". Not for a fixed inventory (see completeness), unclear passages (see comprehensibility), or the system model (see understandability).

- **conciseness**: Shortens content while preserving meaning when users say "cut the repeated wording", "make this shorter but keep the exceptions", or "remove duplicated explanations". Not for missing topics (see comprehensiveness), recognizing characters (see legibility), or reading structure (see readability).

- **confidentiality**: Restricts disclosure to authorized recipients when tickets say "the API leaks internal notes", "a cache shows another team's data", or "errors expose private fields". Not for purpose and retention (see privacy), identity linkage (see anonymity), or alteration protection (see integrity).

- **configurability**: Defines supported settings, defaults, and valid combinations when tickets say "which settings do we support", "these config options clash", or "document defaults and overrides". Not for tuning a value (see adjustability), switching state (see reconfigurability), or user-authored behavior (see customizability).

- **conformance**: Checks selected rules when tickets say "validate this against our schema", "reject names that break the agreed convention", or "show which rule this violates". Not for choosing a convention (see standardizability-standardization-standard).

- **consistency**: Aligns representations when tickets say "the list and detail page disagree", "the cache shows an older status", or "these views conflict at the same revision". Not for external reference error (see accuracy) or unauthorized edits (see integrity).

- **controllability**: Makes runtime state changes controllable when tickets say "pause intake without killing active jobs", "resume only this worker", or "the stop command says OK but work keeps starting". Not for status display (see visibility), fleet policy (see manageability), or whole operator tasks (see operability).

- **correctness**: Matches specified behavior when tickets say "this branch returns the wrong result", "the boundary case breaks the agreed rule", or "the function violates its contract". Not for error against measured truth (see accuracy), missing required members (see completeness), or selected-rule audits (see conformance).

- **customizability**: Supports user-authored behavior or presentation when tickets say "let users write report templates", "customers need their own rules", or "allow custom output layouts". Not for built-in choices (see configurability), fitting a work context (see tailorability), or plugin admission (see extensibility).

- **debuggability**: Localizes a particular execution defect when tickets say "reproduce this parser crash", "show me where this value goes wrong", or "the stack trace does not explain this input". Not for system-wide cause or change-impact analysis (see analyzability) or adding test seams (see testability).

- **decomposability**: Finds separable responsibilities when tickets say "split this without sharing its internals", "these parts cannot run apart", or "extract the renderer from billing". Not for dependency layout alone (see structuredness) or joining components (see composability).

- **defensibility**: Designs authorized containment during an attack when tickets say "a revoked token still runs jobs", "give responders a kill switch", or "check that containment actually stopped it". Not for full threat/control design (see security-control-and-security), normal restoration (see recoverability), or passive diagnosis (see observability).

- **demonstrability**: Builds inspectable capability demonstrations when tickets say "show reviewers the failed-payment flow", "make the demo runnable again", or "let the audience see the result". Not for proving every possible case (see provability) or designing acceptance evidence (see verifiability).

- **dependability**: Combines failure evidence for a scoped reliance decision when users ask "can we rely on this for dispatch", "show the gaps across our failure checks", or "uptime looks fine but dispatch is unsafe". Not for usable time (see availability), failure trials (see reliability), or hazard analysis (see safety).

- **distributivity**: Defines node allocation when tickets say "which worker owns this key", "spread partitions across nodes", or "two nodes claim the same shard". Not for workload growth curves (see scalability).

- **durability**: Preserves acknowledged state through named faults when tickets say "saved edits vanish after restart", "did we acknowledge before saving", or "failover loses confirmed writes". Not for partial visibility (see atomicity), restoration (see recoverability), or continued operation (see fault-failure-tolerance).

- **effectiveness**: Checks achieved outcomes when tickets say "reviewing discrepancies does not fix stock", "the screen says done but the mismatch remains", or "measure reconciled inventory rather than clicks". Not for capability presence (see functionality) or task fit alone (see suitability).

- **efficiency-device-efficiency**: Reduces resources per useful result when users say "less CPU for each completed report", "stop sending the same bytes twice", or "less compute per result". Not for operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or resource stewardship (see sustainability).

- **enhanceability**: Designs changes that improve an existing capability when tickets say "make this parser easier to improve", "swap in a better algorithm", or "upgrade this feature without adding a new one". Not for judging output error alone (see accuracy), adding helpers (see augmentability), or staged changes (see evolvability).

- **evolvability**: Plans successive changes with prior state and obligations carried forward when users say "will this migration block the next release", "plan the next few migrations", or "when can we remove the old bridge". Not for one code edit (see modifiability) or one capability refinement (see enhanceability).

- **expandability**: Admits added resources into an existing installation's usable capacity when tickets say "the new worker never picks up jobs", "bring another storage unit online", or "add usable nodes to this cluster". Not for workload growth curves (see scalability) or adding core functionality (see extendability).

- **expressiveness**: Adds missing distinctions to a notation when tickets say "this rule cannot say owner only", "we cannot write a deny rule", or "different policies save as the same thing". Not for shortening adequate notation (see conciseness) or setting precision alone (see formality).

- **extendability**: Plans bounded core changes or builds missing extension hooks when users say "we need a hook before adding plugins", "this format needs core changes", or "add an operation the core cannot handle". Not for using an existing hook (see extensibility) or admitting resources (see expandability).

- **extensibility**: Admits additions through an existing hook without core edits when users say "register a plugin with this hook", "add another provider to this interface", or "test plugin activation and cleanup". Not for building or widening the hook (see extendability) or composing component contracts (see composability).

- **fault-failure-tolerance**: Keeps a defined service working during modeled faults when users say "keep serving when a worker dies", "fail over while requests are running", or "keep writes working during a partition". Not for restoration (see recoverability), uptime accounting (see availability), or adverse input (see robustness).

- **feasibility**: Tests whether a design can meet its delivery constraints when tickets say "can we ship this offline", "try the local renderer before we commit", or "the plan needs a service we cannot reach". Not for budget fit alone (see affordability) or ongoing worth (see viability).

- **flexibility**: Supports alternative ways to perform the same task when tickets say "offer manual and automatic routes", "let users choose another way through", or "keep both workflows supported". Not for external changes (see adaptability), tuning a control (see adjustability), or switching state (see reconfigurability).

- **formality**: Makes specification notation precise when tickets say "what does this state label mean", "define when this transition is allowed", or "stop interpreting this rule differently". Not for proving the stated property (see provability) or choosing acceptance evidence (see verifiability).

- **functionality**: Defines required capabilities when tickets say "we need an export operation", "there is no way to cancel a queued export", or "list what the export service must do". Not for wrong existing behavior (see correctness), task fit (see suitability), or achieved outcomes (see effectiveness).

- **generality**: Broadens one abstraction across related cases when tickets say "stop adding exceptions to this range checker", "use one range model for quantities and durations", or "every new range field needs another branch". Not for different task roles (see versatility) or moving an artifact to another context (see reusability).

- **immunity**: Checks whether a mechanism excludes a named failure path under assumptions when users ask "can text still reach the command runner", "remove this failure path completely", or "does the old loader bypass the fix". Not for bounded response (see robustness), exposure mapping (see susceptibility), or threat review (see security-control-and-security).

- **installability**: Improves installation lifecycle when tickets say "a clean install will not start", "upgrades leave half-installed files", or "uninstall removes our own data". Not for moving between execution platforms (see portability) or deployment uptime (see availability).

- **integratability**: Bounds assembly work when tickets say "wire these services together", "the components work alone but not together", or "connecting this needs too much glue". Not for exchange meaning (see interoperability).

- **integrity**: Controls unauthorized or unintended alteration when tickets say "stale edits overwrite approved changes", "block updates to protected fields", or "check whether this import was tampered with". Not for factual error (see accuracy), disclosure (see confidentiality), or partial commits (see atomicity).

- **interoperability**: Aligns exchange meaning when tickets say "they disagree on units", "the receiver misreads our payload", or "their success response means something else". Not for assembly effort (see integratability).

- **learnability**: Checks learning through product use when tickets say "new users never get the hang of it", "people still need help after practicing", or "can beginners do it unaided next time". Not for courses (see trainability), experienced task performance (see usability), or reading flow (see readability).

- **legibility**: Checks character and symbol recognition in the viewing context when tickets say "these characters look the same", "users misread the identifier", or "the font is unreadable on this display". Not for code/text reading flow (see readability), visual appeal (see attractiveness), or broader access barriers (see accessibility-access-control).

- **likeability**: Evaluates feelings after use when users say "people hate using this tool", "which workflow do users prefer", or "the app feels frustrating after use". Not for visual appeal (see attractiveness), task completion (see usability), or acquiring skill (see learnability).

- **localizability**: Separates locale behavior from business logic when tickets say "add a language without changing the code", "this date is ambiguous after translation", or "the decimal comma breaks our export". Not for platform moves (see portability) or character recognition (see legibility).

- **maintainability**: Reduces recurring upkeep effort when tickets say "repairs keep taking too long", "future maintainers cannot diagnose this", or "we redo the same maintenance work". Not for one edit (see modifiability), a support encounter (see supportability), or successive migrations (see evolvability).

- **manageability**: Coordinates fleet policy when tickets say "roll out worker settings across nodes", "which nodes missed this setting", or "keep an exception local to one node". Not for one runtime task (see operability), one state-changing command (see controllability), or configuration transitions (see reconfigurability).

- **maturity**: Assesses readiness from operating and defect history when users ask "is this release proven enough", "the same bug came back under a new ticket", or "has anyone used this since the fix". Not for future failure trials (see reliability), combined assurance (see dependability), or upkeep effort (see maintainability).

- **measurability**: Defines a property's measurement procedure when tickets say "what exactly are we counting", "these dashboards use different units", or "how do we measure queue delay". Not for inferring hidden runtime state (see observability) or selecting acceptance evidence (see verifiability).

- **mobility**: Preserves active client work through movement when tickets say "keep this upload running as networks change", "switch connections without restarting the task", or "roaming starts the upload again". Not for resuming after a relocation pause (see nomadicity) or moving software platforms (see portability).

- **modifiability**: Bounds one code change and its ripple effects when tickets say "how much code will this edit touch", "changing this rule breaks other modules", or "estimate the work for this code change". Not for recurring upkeep (see maintainability), request progress (see changeability), or successive changes (see evolvability).

- **nomadicity**: Restores useful work after relocation when tickets say "resume my draft after reconnecting elsewhere", "pick up where I left off at the next site", or "reopen saved work after changing networks". Not for uninterrupted activity during movement (see mobility) or outage restoration (see recoverability).

- **observability**: Makes runtime state inferable when tickets say "is this job queued or stuck", "we cannot join the retry to its first attempt", or "the logs do not explain the missing result". Not for displaying status alone (see visibility), defining units (see measurability), or one defect replay (see debuggability).

- **operability**: Makes an operator task executable when tickets say "on-call cannot resume this export", "the rerun command leaves us stuck", or "what do we do after a partial export". Not for fleet policy (see manageability), a single control action (see controllability), or a user support case (see supportability).

- **performance-efficiency-time-or-space-bounds**: Sets fixed-load time, throughput, or space bounds when tickets say "our p95 is too high", "the export takes too long", or "this operation uses too much memory". Not for run-to-run variation (see predictability), resources per result (see efficiency-device-efficiency), or competing service classes (see quality-of-service).

- **portability**: Moves software between execution environments when tickets say "the app only works on the old host", "move this service to the new runtime", or "keep the same result on the target host". Not for setup on one target (see installability), locale adaptation (see localizability), or user movement (see mobility).

- **predictability**: Bounds variation across comparable runs when tickets say "the same job is fast then slow", "completion times jump around", or "rare pauses keep surprising callers". Not for an absolute tail-latency limit (see performance-efficiency-time-or-space-bounds), control flapping (see stability), or product options (see variability).

- **privacy**: Defines personal-data purpose and lifecycle when tickets say "we keep storing data we never use", "stop sending emails to analytics", or "deleted accounts return after restore". Not for read permissions alone (see confidentiality) or preventing identity linkage (see anonymity). Treats policy labels as supplied constraints.

- **provability**: Builds checkable arguments from explicit assumptions when tickets say "prove this balance cannot go negative", "which assumptions does this proof need", or "tests do not cover every state". Not for testing selected cases (see verifiability) or defining notation alone (see formality).

- **quality-of-service**: Defines service per competing class when tickets say "batch jobs block checkout", "background jobs never get a turn", or "one tenant hogs the workers". Not for one-operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or permissions (see accessibility-access-control).

- **readability**: Improves code and text reading flow when tickets say "rename these confusing variables", "this function is buried in nesting", or "reorder this paragraph so it flows". Not for character recognition (see legibility) or explaining missing concepts (see comprehensibility).

- **reconfigurability**: Controls transitions between operating configurations when tickets say "switch modes without losing queued jobs", "resume the interrupted config change", or "who owns work during the switch". Not for the options menu (see configurability), tuning a value (see adjustability), or supporting alternatives (see flexibility).

- **recoverability**: Restores usable state after disruption when tickets say "prove we can restore this backup", "the process is up but orders still fail", or "resume work without replaying orders twice". Not for operation during faults (see fault-failure-tolerance), acknowledged-state retention (see durability), or essential mission continuity (see survivability).

- **reliability**: Measures failures over a defined operating profile when tickets say "the worker keeps crashing overnight", "retries hide the original failures", or "run this workload without restarting". Not for usable time (see availability), operating through held faults (see fault-failure-tolerance), or restoration (see recoverability).

- **repeatability**: Checks repeated runs in the same setup when tickets say "the same fixture gives different answers", "rerun this without changing the setup", or "does this pass twice in a row". Not for independent reconstruction elsewhere (see replicability) or bounds on service variation (see predictability).

- **replaceability**: Preserves surrounding contracts during substitution when tickets say "swap this provider", "remove the old backend", or "keep callers unchanged after replacement". Not for coexistence alone (see compatibility).

- **replicability**: Enables independent reconstruction when tickets say "another engineer gets a different result", "rerun this experiment on a clean runner", or "the setup depends on your laptop". Not for reruns in the original setup (see repeatability) or moving the product to another platform (see portability).

- **reusability**: Reuses an artifact in a specified new context when tickets say "use the same validator in the CLI", "stop copying the import checker", or "this helper needs the web request". Not for broadening an abstraction family (see generality) or joining stage contracts (see composability).

- **robustness**: Bounds behavior under adverse inputs or conditions when tickets say "bad input leaves jobs running", "huge requests take down healthy work", or "rejected imports leave half-written rows". Not for component faults (see fault-failure-tolerance), threat review (see security-control-and-security), or normal-profile failures (see reliability).

- **safety**: Prevents named harm when tickets say "do not delete records that are on hold", "can stopping this action cause harm", or "the safety check is only in the UI". Not for adversary controls (see security-control-and-security), usable service time (see availability), or generic bad-input handling (see robustness).

- **scalability**: Tests behavior as demand grows when tickets say "handle more users without adding errors", "why does throughput stop rising", or "does another worker help under load". Not for resource admission (see expandability), fixed-load bounds (see performance-efficiency-time-or-space-bounds), or unit resource cost (see efficiency-device-efficiency).

- **security-control-and-security**: Designs controls against adversary paths when tickets say "how could an attacker abuse this feature", "where should we block this attack", or "the normal route is fixed but retries bypass it". Not for disclosure alone (see confidentiality), alteration alone (see integrity), or incident containment (see defensibility).

- **self-descriptiveness**: Makes current state and action effects clear in context when users ask "why is this button disabled", "what will clicking this change", or "which report am I editing right now". Not for later notifications (see communicativeness), standalone explanations (see comprehensibility), or backend diagnosis (see observability).

- **simplicity**: Removes unnecessary mechanisms when tickets say "this fixed export has a plugin framework", "why is there a registry for one formatter", or "use a direct call for this fixed path". Not for mapping interaction burden (see complexity-interacting-complexity) or reading flow alone (see readability).

- **stability**: Controls drift and feedback over time when tickets say "the autoscaler keeps flapping", "the output drifts with steady input", or "our controllers undo each other's changes". Not for failure occurrence (see reliability), run-to-run variation (see predictability), or operation latency (see performance-efficiency-time-or-space-bounds).

- **standardizability-standardization-standard**: Selects and adopts common conventions when tickets say "agree on one event format", "teams invent different field names", or "publish a shared naming convention". Not for checking already selected rules (see conformance).

- **structuredness**: Enforces dependency organization when tickets say "domain code imports the web layer", "these imports violate our layer rules", or "the package layout hides a cycle". Not for finding separable responsibilities (see decomposability) or matching peer conventions (see uniformity).

- **suitability**: Checks capabilities against a particular task when tickets say "the export cannot feed our offline importer", "this format does not fit the receiving tool", or "the feature exists but cannot complete this handoff". Not for capability presence alone (see functionality) or achieved outcomes (see effectiveness).

- **supportability**: Resolves a specific support encounter when tickets say "support cannot explain this failed export", "give support a safe diagnostic bundle", or "we need a runbook for this customer issue". Not for recurring upkeep (see maintainability), state inference alone (see observability), or delivery handoffs (see changeability).

- **survivability**: Preserves essential work through severe disruption when tickets say "keep dispatch running if the site is lost", "what still works without central login", or "reconcile offline assignments when we return". Not for normal restoration (see recoverability), routine fault handling (see fault-failure-tolerance), or uptime accounting (see availability).

- **susceptibility**: Maps exposure and enabling conditions without presuming exploitation when users ask "does this dependency issue affect us", "can the importer reach that code", or "is the disabled endpoint our only route". Not for mechanism exclusion (see immunity), bounded adverse response (see robustness), or active containment (see defensibility).

- **sustainability**: Assesses energy and device-life trade-offs when users ask "can we use less energy for these reports", "can we keep these devices useful", or "do we really need replacement hardware". Not for resources per result (see efficiency-device-efficiency), purchase price (see affordability), or continued business value (see viability).

- **tailorability**: Fits supported behavior to a work context when tickets say "fit the workflow to the night shift", "let departments use different presets", or "our team needs another built-in workflow". Not for authored behavior (see customizability), defining settings (see configurability), alternatives (see flexibility), or external changes (see adaptability).

- **testability**: Adds test control and observation seams when tickets say "we cannot force the timeout path", "tests cannot see which branch ran", or "this test depends on the real clock". Not for selecting acceptance evidence (see verifiability) or diagnosing a particular failing execution (see debuggability).

- **traceability**: Links versioned artifacts and change impact when users ask "which tests cover this requirement", "what breaks if we delete this function", or "these links point to an old rule". Not for actor identity (see accountability), review conclusions (see auditability), or test control and observation (see testability).

- **trainability**: Designs instruction and independent skill checks when tickets say "replace the demo with practice exercises", "people finish the course but cannot do the job", or "write training with a separate skills check". Not for learning through use (see learnability), topic coverage (see comprehensiveness), or current task success (see usability).

- **transferability**: Supports project handoffs when tickets say "hand this project to another team", "export these records without losing links", or "the recipient cannot open the package". Not for moving execution platforms (see portability), ongoing system exchange (see interoperability), or rebuilding an experiment (see replicability).

- **trustability**: Supports scoped trust decisions with evidence and limits when users ask "can this tool publish without my review", "show the limits before I delegate", or "this confidence badge promises too much". Not for operational assurance (see dependability), feelings after use (see likeability), or confidence in one output (see certainty).

- **understandability**: Explains the whole system model when users ask "how do these components fit together", "who owns state in this flow", or "why does this request cross these services". Not for one unclear explanation (see comprehensibility), reading flow (see readability), or topic breadth (see comprehensiveness).

- **uniformity**: Aligns conventions across comparable peers when tickets say "list routes name the same limit differently", "use the same paging fields on these routes", or "why does only this list take pageSize". Not for selecting a common convention (see standardizability-standardization-standard) or value agreement (see consistency).

- **usability**: Improves end-to-end task performance when tickets say "users cannot finish checkout", "people make mistakes in this workflow", or "make the whole task easier to complete". Not for learning (see learnability), feelings after use (see likeability), or visual appeal (see attractiveness).

- **variability**: Models allowed product variants when tickets say "which editions can we build", "export must require audit in every edition", or "the build allows a feature combination we do not support". Not for settings of one instance (see configurability) or applying a transition (see reconfigurability).

- **verifiability**: Connects requirements to feasible acceptance evidence when tickets say "how will we know this requirement passed", "this acceptance check cannot be run", or "what evidence would settle this claim". Not for adding test seams (see testability), defining units (see measurability), or constructing proofs (see provability).

- **versatility**: Supports distinct roles in one product when tickets say "use this tool for imports and stock checks", "audit inventory without changing it", or "the import tool also needs a checking mode". Not for one abstraction covering related cases (see generality) or reusing an artifact elsewhere (see reusability).

- **viability**: Checks continued stakeholder value when tickets say "is this report service still worth running", "what if upkeep doubles next cycle", or "when should we retire this service". Not for initial delivery (see feasibility), spending cap alone (see affordability), or environmental objectives (see sustainability).

- **visibility**: Exposes status to its intended audience when tickets say "customers cannot see export progress", "show when this job status was updated", or "the status page shows another team's job". Not for inferring hidden causes (see observability), notifying users (see communicativeness), or permission design (see accessibility-access-control).

- **wrappability**: Adds a boundary around an unchanged implementation when tickets say "put a structured API around this old function", "keep the legacy engine behind a new interface", or "expose a new entrypoint without changing the engine". Not for substituting the engine (see replaceability) or just wiring components (see integratability).
