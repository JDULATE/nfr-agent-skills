- **accessibility-access-control**: Separates interaction barriers from permission checks when tickets say "keyboard users get stuck", "screen reader skips errors", "stop cross-team edits", or "revoked access still works". Asks which branch. Not for looks (see attractiveness), personal-data lifecycle (see privacy), or threat review (see security-control-and-security).

- **accountability**: Binds initiating and executing actors under a validated identity model when users ask "who approved this change", "which user queued this job", or "shared accounts hide who acted". Not for evidence sufficiency (see auditability), artifact links (see traceability), or hiding identity (see anonymity).

- **adaptability**: Preserves required behavior across changed external conditions when tickets say "the supplier changed its feed", "support changed operating conditions", or "keep importing after the upstream change". Not for built-in alternatives (see flexibility), platform moves (see portability), or applying settings (see reconfigurability).

- **additivity**: Tests whether separate contributions combine as claimed when users ask "do these gains add up", "are we counting the benefit twice", or "both changes together help less". Not for assembly contracts (see composability) or admitting resources (see expandability).

- **adjustability**: Tunes existing controls in a fixed arrangement when tickets say "let admins tweak thresholds", "change the polling interval", or "tune the current batch size". Not for defining options (see configurability) or switching arrangements (see reconfigurability).

- **agility**: Handles reprioritized delivery when users say "the roadmap changed again", "swap in this urgent feature", or "feedback changed what we should ship". Not for progressing one unchanged request (see changeability) or reducing code-edit effort (see modifiability).

- **anonymity**: Assesses identity and linkage exposed to an observer when users ask "can recipients work out who this is", "these fake IDs link back to people", or "repeated exports reveal the same person". Not for data purpose/lifecycle (see privacy), recipient permissions (see confidentiality), or actor attribution (see accountability).

- **atomicity**: Specifies all-or-none visible effects when tickets say "we see half an update", "a failed write leaves partial changes", or "rollback happens after users saw the change". Not for preserving acknowledged writes (see durability), restoring service (see recoverability), or agreement between values (see consistency).

- **attractiveness**: Evaluates visual appeal when users say "this screen looks uninviting", "which visual style looks better", or "make this layout more appealing". Not for feelings after use (see likeability), recognizing characters (see legibility), or completing tasks (see usability).

- **auditability**: Defines evidence for independent review when tickets say "the reviewer cannot reconstruct this approval", "our audit trail leaves gaps", or "an export does not answer the audit question". Not for actor identity (see accountability), artifact links (see traceability), or compliance conclusions (see conformance).

- **augmentability**: Adds a separately accepted supporting capability when users say "add reply suggestions", "put annotations beside reports", or "add a helper without replacing manual work". Not for improving the original capability (see enhanceability) or admitting through an existing hook (see extensibility).

- **availability**: Improves and measures usable service time when tickets say "users get logged out on deploy", "checkout goes down during releases", or "count our downtime". Not for failure-free operation (see reliability) or restoring usable state (see recoverability).

- **changeability**: Traces one request through decision, delivery, and adoption when tickets say "this ticket is stuck after approval", "merged but not rolled out", or "who needs to hand this change over". Not for changing priorities (see agility) or reducing code-edit effort (see modifiability).

- **communicativeness**: Defines timely user feedback when tickets say "notify me when the export is done", "the error arrives too late", or "keep users posted while a job runs". Not for explaining current state and actions (see self-descriptiveness) or clarifying a standalone explanation (see comprehensibility).

- **comprehensibility**: Clarifies a particular explanation when users say "people misunderstand this error", "what does this requirement mean", or "this paragraph leaves the actor unclear". Not for reading flow (see readability), the whole system model (see understandability), or in-context state cues (see self-descriptiveness).

- **comprehensiveness**: Checks topic coverage for an audience when users ask "this guide skips recovery", "are we missing topics for operators", or "our manual only covers the happy path". Not for a fixed inventory (see completeness), unclear passages (see comprehensibility), or the system model (see understandability).

- **conciseness**: Shortens content while preserving meaning when users say "cut the repeated wording", "make this shorter but keep the exceptions", or "remove duplicated explanations". Not for missing topics (see comprehensiveness), recognizing characters (see legibility), or reading structure (see readability).

- **confidentiality**: Restricts disclosure to authorized recipients when tickets say "the API leaks internal notes", "a cache shows another team's data", or "errors expose private fields". Not for purpose and retention (see privacy), identity linkage (see anonymity), or alteration protection (see integrity).

- **configurability**: Defines supported settings, defaults, and valid combinations when tickets say "which settings do we support", "these config options clash", or "document defaults and overrides". Not for tuning a value (see adjustability), switching state (see reconfigurability), or user-authored behavior (see customizability).

- **customizability**: Supports user-authored behavior or presentation when tickets say "let users write report templates", "customers need their own rules", or "allow custom output layouts". Not for built-in choices (see configurability), fitting a work context (see tailorability), or plugin admission (see extensibility).

- **defensibility**: Designs authorized containment during an attack when tickets say "a revoked token still runs jobs", "give responders a kill switch", or "check that containment actually stopped it". Not for full threat/control design (see security-control-and-security), normal restoration (see recoverability), or passive diagnosis (see observability).

- **dependability**: Combines failure evidence for a scoped reliance decision when users ask "can we rely on this for dispatch", "show the gaps across our failure checks", or "uptime looks fine but dispatch is unsafe". Not for usable time (see availability), failure trials (see reliability), or hazard analysis (see safety).

- **durability**: Preserves acknowledged state through named faults when tickets say "saved edits vanish after restart", "did we acknowledge before saving", or "failover loses confirmed writes". Not for partial visibility (see atomicity), restoration (see recoverability), or continued operation (see fault-failure-tolerance).

- **efficiency-device-efficiency**: Reduces resources per useful result when users say "less CPU for each completed report", "stop sending the same bytes twice", or "less compute per result". Not for operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or resource stewardship (see sustainability).

- **enhanceability**: Designs implementation changes to refine an existing capability when tickets say "make this parser easier to improve", "swap in a better version of this algorithm", or "upgrade this feature without adding a new one". Not for judging output error alone (see accuracy), adding helpers (see augmentability), or staged change paths (see evolvability).

- **evolvability**: Plans successive changes with prior state and obligations carried forward when users say "will this migration block the next release", "plan the next few migrations", or "when can we remove the old bridge". Not for one code edit (see modifiability) or one capability refinement (see enhanceability).

- **expandability**: Admits added resources into an existing installation's usable capacity when tickets say "the new worker never picks up jobs", "bring another storage unit online", or "add usable nodes to this cluster". Not for workload growth curves (see scalability) or adding core functionality (see extendability).

- **extendability**: Plans bounded core changes or builds missing extension hooks when users say "we need a hook before adding plugins", "this format needs core changes", or "add an operation the core cannot handle". Not for using an existing hook (see extensibility) or admitting resources (see expandability).

- **extensibility**: Admits additions through an existing hook without core edits when users say "register a plugin with this hook", "add another provider to this interface", or "test plugin activation and cleanup". Not for building or widening the hook (see extendability) or composing component contracts (see composability).

- **fault-failure-tolerance**: Keeps a defined service working during modeled faults when users say "keep serving when a worker dies", "fail over while requests are running", or "keep writes working during a partition". Not for restoration (see recoverability), uptime accounting (see availability), or adverse input (see robustness).

- **flexibility**: Supports alternative ways to perform the same task when tickets say "offer manual and automatic routes", "let users choose another way through", or "keep both workflows supported". Not for external changes (see adaptability), tuning a control (see adjustability), or switching state (see reconfigurability).

- **immunity**: Assesses exclusion of a named failure mechanism under explicit premises when users ask "can text still reach the command runner", "remove this failure path completely", or "does the old loader bypass the fix". Not for bounded response (see robustness), exposure mapping (see susceptibility), or threat review (see security-control-and-security).

- **integrity**: Controls unauthorized or unintended alteration when tickets say "stale edits overwrite approved changes", "block updates to protected fields", or "check whether this import was tampered with". Not for factual error (see accuracy), disclosure (see confidentiality), or partial commits (see atomicity).

- **learnability**: Checks learning through product use when tickets say "new users never get the hang of it", "people still need help after practicing", or "can beginners do it unaided next time". Not for courses (see trainability), experienced task performance (see usability), or reading flow (see readability).

- **legibility**: Checks character and symbol recognition in the viewing context when tickets say "these characters look the same", "users misread the identifier", or "the font is unreadable on this display". Not for code/text reading flow (see readability), visual appeal (see attractiveness), or broader access barriers (see accessibility-access-control).

- **likeability**: Evaluates feelings after use when users say "people hate using this tool", "which workflow do users prefer", or "the app feels frustrating after use". Not for visual appeal (see attractiveness), task completion (see usability), or acquiring skill (see learnability).

- **maintainability**: Reduces recurring upkeep effort when tickets say "repairs keep taking too long", "future maintainers cannot diagnose this", or "we redo the same maintenance work". Not for one edit (see modifiability), a support encounter (see supportability), or successive migrations (see evolvability).

- **maturity**: Assesses demonstrated readiness from operating and defect history when users ask "is this release proven enough", "the same bug came back under a new ticket", or "do we have real use after the fix". Not for future failure trials (see reliability), combined assurance (see dependability), or upkeep effort (see maintainability).

- **modifiability**: Bounds one code change and its ripple effects when tickets say "how much code will this edit touch", "changing this rule breaks other modules", or "estimate the work for this code change". Not for recurring upkeep (see maintainability), request progress (see changeability), or successive changes (see evolvability).

- **performance-efficiency-time-or-space-bounds**: Sets fixed-load time, throughput, or space bounds when tickets say "our p95 is too high", "the export takes too long", or "this operation uses too much memory". Not for run-to-run variation (see predictability), resources per result (see efficiency-device-efficiency), or competing service classes (see quality-of-service).

- **predictability**: Bounds variation across comparable runs when tickets say "the same job is fast then slow", "completion times jump around", or "rare pauses keep surprising callers". Not for an absolute tail-latency limit (see performance-efficiency-time-or-space-bounds), control flapping (see stability), or product options (see variability).

- **privacy**: Defines personal-data purpose and lifecycle when tickets say "we keep storing data we never use", "stop sending emails to analytics", or "deleted accounts return after restore". Not for read permissions alone (see confidentiality) or preventing identity linkage (see anonymity). Treats policy labels as supplied constraints.

- **quality-of-service**: Defines service per competing class when tickets say "batch jobs block checkout", "background jobs never get a turn", or "one tenant hogs the workers". Not for one-operation bounds (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or permissions (see accessibility-access-control).

- **readability**: Improves code and text reading flow when tickets say "rename these confusing variables", "this function is buried in nesting", or "reorder this paragraph so it flows". Not for character recognition (see legibility) or explaining missing concepts (see comprehensibility).

- **reconfigurability**: Controls transitions between operating configurations when tickets say "switch modes without losing queued jobs", "resume the interrupted config change", or "who owns work during the switch". Not for the options menu (see configurability), tuning a value (see adjustability), or supporting alternatives (see flexibility).

- **recoverability**: Restores usable state after disruption when tickets say "prove we can restore this backup", "the process is up but orders still fail", or "resume work without replaying orders twice". Not for operation during faults (see fault-failure-tolerance), acknowledged-state retention (see durability), or essential mission continuity (see survivability).

- **reliability**: Measures failures over a defined operating profile when tickets say "the worker keeps crashing overnight", "retries hide the original failures", or "run this workload without restarting". Not for usable time (see availability), operating through held faults (see fault-failure-tolerance), or restoration (see recoverability).

- **robustness**: Bounds behavior under adverse inputs or conditions when tickets say "bad input leaves jobs running", "huge requests take down healthy work", or "rejected imports leave half-written rows". Not for component faults (see fault-failure-tolerance), threat review (see security-control-and-security), or normal-profile failures (see reliability).

- **safety**: Prevents named harm when tickets say "do not delete records that are on hold", "can stopping this action cause harm", or "the safety check is only in the UI". Not for adversary controls (see security-control-and-security), usable service time (see availability), or generic bad-input handling (see robustness).

- **scalability**: Tests behavior as demand grows when tickets say "handle more users without adding errors", "why does throughput stop rising", or "does another worker help under load". Not for resource admission (see expandability), fixed-load bounds (see performance-efficiency-time-or-space-bounds), or unit resource cost (see efficiency-device-efficiency).

- **security-control-and-security**: Designs controls against adversary paths when tickets say "how could an attacker abuse this feature", "where should we block this attack", or "the normal route is fixed but retries bypass it". Not for disclosure alone (see confidentiality), alteration alone (see integrity), or incident containment (see defensibility).

- **self-descriptiveness**: Makes current state and action effects clear in context when users ask "why is this button disabled", "what will clicking this change", or "which report am I editing right now". Not for later notifications (see communicativeness), standalone explanations (see comprehensibility), or backend diagnosis (see observability).

- **stability**: Controls drift and feedback over time when tickets say "the autoscaler keeps flapping", "the output drifts with steady input", or "our controllers undo each other's changes". Not for failure occurrence (see reliability), run-to-run variation (see predictability), or operation latency (see performance-efficiency-time-or-space-bounds).

- **supportability**: Resolves a specific support encounter when tickets say "support cannot explain this failed export", "give support a safe diagnostic bundle", or "we need a runbook for this customer issue". Not for recurring upkeep (see maintainability), state inference alone (see observability), or delivery handoffs (see changeability).

- **survivability**: Preserves essential work through severe disruption when tickets say "keep dispatch running if the site is lost", "what still works without central login", or "reconcile offline assignments when we return". Not for normal restoration (see recoverability), routine fault handling (see fault-failure-tolerance), or uptime accounting (see availability).

- **susceptibility**: Maps exposure and enabling conditions without presuming exploitation when users ask "does this dependency issue affect us", "can the importer reach that code", or "is the disabled endpoint our only route". Not for mechanism exclusion (see immunity), bounded adverse response (see robustness), or active containment (see defensibility).

- **sustainability**: Assesses energy and device-life trade-offs when users ask "can we use less energy for these reports", "can we keep these devices useful", or "do we really need replacement hardware". Not for resources per result (see efficiency-device-efficiency), purchase price (see affordability), or continued business value (see viability).

- **tailorability**: Fits supported behavior to a work context when tickets say "fit the workflow to the night shift", "let departments use different presets", or "our team needs another supported process". Not for authored behavior (see customizability), defining settings (see configurability), alternatives (see flexibility), or external changes (see adaptability).

- **traceability**: Links versioned artifacts and change impact when users ask "which tests cover this requirement", "what breaks if we delete this function", or "these links point to an old rule". Not for actor identity (see accountability), review conclusions (see auditability), or test control and observation (see testability).

- **trainability**: Designs instruction and independent skill checks when tickets say "replace the demo with practice exercises", "people finish the course but cannot do the job", or "write training with a separate skills check". Not for learning through use (see learnability), topic coverage (see comprehensiveness), or current task success (see usability).

- **trustability**: Supports scoped trust decisions with evidence and limits when users ask "can this tool publish without my review", "show the limits before I delegate", or "this confidence badge promises too much". Not for operational assurance (see dependability), feelings after use (see likeability), or confidence in one output (see certainty).

- **understandability**: Explains the whole system model when users ask "how do these components fit together", "who owns state in this flow", or "why does this request cross these services". Not for one unclear explanation (see comprehensibility), reading flow (see readability), or topic breadth (see comprehensiveness).

- **usability**: Improves end-to-end task performance when tickets say "users cannot finish checkout", "people make mistakes in this workflow", or "make the whole task easier to complete". Not for learning (see learnability), feelings after use (see likeability), or visual appeal (see attractiveness).
