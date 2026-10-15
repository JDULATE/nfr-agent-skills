# Disambiguation map

All boundaries are proposed repository conventions, not standardized definitions.

Read when choosing between sibling skills, writing exclusions, or reviewing a batch.

These are **proposed repository working meanings for human review**, not claims
that a standard defines these terms or distinguishes every pair this way. Ask the
user when their intended meaning differs or the supplied context is insufficient.
Preserve the catalogue's exact names, ids, aliases, and slugs. A shared word in
two aliases does not establish equivalence. Use the canonical slug for routing.

The tables cover all 114 entries once, including the required overlap clusters
and related terms. Each table stays within one batch or two adjacent batches.
Cross-table sibling pointers explain boundaries without moving their targets
into the same authoring batch. Batch membership is authoritative in
`nfr-list.json`; categories are navigation labels and may differ within a batch.
Every batch has 6-8 entries; all remain `todo` until their authorized authoring phase.

Human review priorities: id 1 combines accessibility with access control; ids 41
and 72 share the alias Efficiency; the growth terms, certainty, trustability,
immunity, susceptibility, nomadicity, and distributivity need confirmation of the
intended local meaning. Do not claim these editorial splits are universal.

## Growth — batch 1

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 46 `extendability` | A new capability can be introduced by changing core source or interfaces within an agreed change surface. | Use when adding behavior requires core edits; use `extensibility` when an existing extension contract admits the addition without those edits. |
| 47 `extensibility` | New behavior attaches through an existing extension contract while the core implementation stays unchanged. | Use for plugin or hook contract adequacy; use `extendability` when that contract must first be created or the core must be edited. |
| 44 `expandability` | An installation can gain resources or units through planned capacity additions. | Use for adding capacity to a deployment; use `scalability` for how behavior changes as workload grows. |
| 42 `enhanceability` | An existing capability improves against its existing acceptance criteria without adding a separately accepted capability. | Use when success is a better result from an existing function; use `augmentability` when a separately accepted supporting function is added. |
| 14 `augmentability` | A supplementary capability has its own acceptance criteria while the original capability remains usable in its original role. | Use for adding an assisting function alongside the original; use `enhanceability` for improving the original function's own results. |
| 5 `additivity` | Combined increments preserve their separately measured contributions under an explicitly declared aggregation rule. | Use when acceptance compares combined effects with individual contributions; Ask the user for the aggregation rule, and use `composability` when only assembly contracts matter. |
| 43 `evolvability` | The system can sustain a sequence of changes as needs and constraints develop over time. | Use for a long-term change path; use `extendability` or `enhanceability` for a particular addition or improvement. |

Review the growth distinction using the unit being accepted: core change,
extension contract, deployment capacity, improvement to an existing function,
separately accepted supplementary function, aggregate contribution, or a sequence
of changes. These concerns can coexist in one request; keep their acceptance
questions separate. Ask the user if the request does not establish that unit.

## Change and tailoring — batches 2-3

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 68 `modifiability` | A specified implementation change has a bounded impact and effort. | Use for concrete change impact; use `maintainability` for the continuing maintenance process. |
| 17 `changeability` | A change can move from request through approval, delivery, and adoption. | Use for the change pathway; use `modifiability` for code-level change cost. |
| 6 `adjustability` | A parameter can be tuned within an existing operating arrangement. | Use for tuning an existing control; use `reconfigurability` for changing the arrangement. |
| 4 `adaptability` | The system can accommodate a specified change in its environment. | Use for an environment-driven adjustment; use `flexibility` for choosing among supported alternatives. |
| 50 `flexibility` | The design allows meaningful alternative ways to perform or arrange work. | Use for keeping alternatives available; use `adaptability` for responding to an environmental change. |
| 63 `maintainability` | Ongoing diagnosis, repair, and modification can be performed with sustainable effort. | Use for maintenance across the lifecycle; use `modifiability` for the impact of one change. |
| 79 `reconfigurability` | An established configuration can transition safely to another arrangement. | Use for the transition and its state handling; use `configurability` for the available settings. |
| 100 `tailorability` | A deployment or workflow can be fitted to a stakeholder's particular context. | Use for contextual fitting of supported behavior; use `customizability` for stakeholder-specific extensions. |
| 32 `customizability` | Stakeholders can introduce their own behavior or presentation beyond choosing standard settings. | Use for custom behavior; use `configurability` for selecting built-in options. |
| 27 `configurability` | Supported settings expose explicit, constrained choices without changing source code. | Use for the options and their validity; use `reconfigurability` for applying a configuration transition. |
| 8 `agility` | The delivery process can respond to changed priorities while preserving agreed constraints. | Use for feedback-to-delivery response; use `changeability` for the handling of an individual change. |
| 96 `supportability` | A support provider can investigate and resolve a user's issue using available support artifacts and procedures. | Use for the support encounter; use `maintainability` for maintaining the implementation itself. |

## Comprehension and user experience — batches 4-5

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 106 `understandability` | An intended reader can form a correct mental model of purpose, behavior, and relationships. | Use for understanding the system as a whole; use `comprehensibility` for interpreting a particular explanation. |
| 23 `comprehensibility` | A particular message, specification, or explanation conveys its intended meaning to its audience. | Use for semantic interpretation of an explanation; use `readability` for effort in reading its representation. |
| 24 `comprehensiveness` | An explanation covers the subject areas its intended audience needs. | Use for breadth of explanation; use `completeness` for missing required items in a defined set. |
| 59 `learnability` | A newcomer can acquire the ability to perform an intended task. | Use for acquisition of skill through use; use `trainability` for the provision and effectiveness of training. |
| 78 `readability` | Text or code presents its meaning in a form the intended reader can follow with reasonable effort. | Use for naming, organization, and reading flow; use `legibility` for visual character recognition. |
| 60 `legibility` | The audience can visually distinguish characters and symbols in the stated display conditions. | Use for physical recognition of text; use `readability` for following its structure and meaning. |
| 90 `self-descriptiveness` | The interface or artifact exposes enough context to explain its current state and available actions. | Use for in-context explanation; use `comprehensibility` for the clarity of a separate explanation. |
| 25 `conciseness` | A representation omits unnecessary material while retaining its intended meaning. | Use for avoidable verbosity; use `comprehensiveness` when needed subject matter is absent. |
| 12 `attractiveness` | The presentation's visual qualities appeal to the intended audience. | Use for aesthetic response; use `likeability` for the broader subjective experience. |
| 18 `communicativeness` | Interaction gives users the information and feedback needed at the appropriate point in a conversation or task. | Use for timing and exchange of messages; use `self-descriptiveness` for context available within a state. |
| 61 `likeability` | Users express a positive subjective response to interacting with the product. | Use for overall preference or sentiment; use `attractiveness` for visual appeal or `usability` for task outcomes. |
| 103 `trainability` | Training materials and exercises enable a target audience to acquire required task skills. | Use for a training intervention; use `learnability` for how readily the product is learned through use. |
| 108 `usability` | The intended audience can complete its tasks in the stated usage context. | Use for overall task interaction outcomes; use `learnability`, `legibility`, or `readability` for a specific obstacle. |

## Reliability and resilience — batches 6-7

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 81 `reliability` | Required behavior continues without failure over a specified operating interval and conditions. | Use for failure-free operation; use `availability` for whether the service is usable when needed. |
| 37 `dependability` | Stakeholders have an evidence-backed basis to rely on the system across their stated failure concerns. | Use for the combined assurance case; use `reliability`, `safety`, or `security-control-and-security` for a specific concern. |
| 15 `availability` | An agreed service is accessible and usable during the times it is required. | Use for service readiness and outages; use `reliability` for continuity without failure. |
| 86 `robustness` | Behavior remains controlled under unexpected inputs, stress, or environmental deviations. | Use for boundary and adverse-condition behavior; use `fault-failure-tolerance` for explicitly modeled component faults. |
| 48 `fault-failure-tolerance` | Required service continues, possibly in an agreed degraded form, despite specified faults or component failures. | Use for operation during a fault; use `recoverability` for restoration after disruption. |
| 80 `recoverability` | Service and state can be restored to an agreed usable condition after disruption. | Use for restoration and lost-work boundaries; use `fault-failure-tolerance` for continuing while the fault exists. |
| 97 `survivability` | Essential mission functions persist through a severe, explicitly scoped disruption. | Use for mission continuity under severe disruption; use `recoverability` for restoring normal operation afterward. |
| 92 `stability` | Behavior avoids unacceptable drift or oscillation within a stated operating envelope. | Use for changes in behavior while conditions are held or varied; use `reliability` for failure occurrence. |
| 65 `maturity` | Evidence from operation and defect handling supports a stated level of readiness for intended use. | Use for demonstrated operational history; use `reliability` for a specified future operating scenario. |
| 39 `durability` | An acknowledged state change remains preserved through the specified subsequent events. | Use for persistence of committed state; use `recoverability` for reconstructing usable state after disruption. |
| 11 `atomicity` | A defined operation exposes all of its state changes together or none of them. | Use for partial-commit prevention; use `durability` for preserving an already acknowledged commit. |
| 87 `safety` | The system controls identified paths to harm in the intended context. | Use for hazards and harmful outcomes; use `security-control-and-security` for adversarial misuse and identify overlaps explicitly. |

For this repository, distinguish a failure event from the duration of unavailable
service: a restart that restores service can end an outage without erasing the
preceding reliability failure. Separate service continued during a modeled fault
(`fault-failure-tolerance`) from service restored afterward (`recoverability`).
Restoring a backup is not by itself evidence that every acknowledged write was
preserved (`durability`). Count degraded operation as available only when it
satisfies the stakeholder's agreed service boundary; Ask the user if that boundary
is missing. Use `dependability` to coordinate the resulting evidence, without
substituting it for these individual acceptance questions.

## Security and privacy — batches 8-9

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 89 `security-control-and-security` | The design addresses an explicit adversary, protected assets, and controls against misuse. | Use for threat and control coordination; use `confidentiality` or `integrity` for a narrower asset property. |
| 26 `confidentiality` | Information is disclosed only to the authorized recipients under the agreed policy. | Use for disclosure boundaries; use `privacy` for purposes and effects of handling personal information. |
| 57 `integrity` | Data or behavior is protected against unauthorized or unintended alteration. | Use for alteration detection and prevention; use `accuracy` for closeness to the correct real-world value. |
| 75 `privacy` | Personal information handling is limited to agreed purposes, subjects, recipients, and lifecycle boundaries. | Use for personal-data handling decisions; use `confidentiality` for unauthorized disclosure alone. |
| 10 `anonymity` | A subject cannot be identified within an explicitly stated observer and linkage model. | Use for identity unlinkability in that model; use `privacy` for the broader handling of personal information. |
| 54 `immunity` | A specified attack or fault class is excluded by a stated mechanism within declared assumptions. | Use for a narrowly bounded exclusion claim; use `robustness` for controlled response or `security-control-and-security` for broader threat handling. |
| 35 `defensibility` | An operator can detect, contain, and contest an active adversarial action using the available controls. | Use for active defensive response; use `security-control-and-security` for the full threat and control design. |
| 98 `susceptibility` | Exposure and preconditions explain where a specified adverse influence can affect the system. | Use for locating exposure paths; use `immunity` for excluding one class or `robustness` for behavior under exposure. |
| 2 `accountability` | Actions can be attributed to an appropriate actor under the agreed identity model. | Use for responsibility and attribution; use `auditability` for evidence suitable for independent examination. |
| 13 `auditability` | A reviewer can examine retained evidence to evaluate actions and controls. | Use for independent examination; use `accountability` for actor attribution or `traceability` for connected artifact history. |
| 102 `traceability` | Relationships connect requirements, decisions, changes, and evidence across their lifecycle. | Use for following those relationships; use `auditability` for assessing whether the evidence supports an audit question. |
| 105 `trustability` | A stakeholder's stated trust decision can be supported by inspectable claims, limits, and evidence. | Use for justified trust in a decision context; use `dependability` for operational reliance across failure concerns. |
| 1 `accessibility-access-control` | The source label contains two distinct concerns: accessible interaction and authorization of access. | Ask the user which branch is intended; address barriers under accessibility and permission decisions under access control, without claiming they are synonyms or treating general `usability` as a substitute. |

Id 1 retains its original slash label and aliases. Its single category,
Usability & Comprehension, indexes the accessibility branch only; its batch
placement permits review beside the security branch. This is a navigation
compromise requiring human review, not a merged definition. The author must
make the two branches explicit and ask about missing audience or policy context.

## Performance and resource use — batch 10

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 72 `performance-efficiency-time-or-space-bounds` | An operation meets agreed elapsed-time, throughput, or space bounds for a stated workload. | Use for an operation's performance envelope; use `efficiency-device-efficiency` for useful work relative to consumed resources. |
| 41 `efficiency-device-efficiency` | Useful work is related to the device resources consumed in a stated environment. | Use for resource cost per useful result; use `performance-efficiency-time-or-space-bounds` for response-time or space limits. |
| 88 `scalability` | Service behavior and resource needs remain acceptable as a specified workload dimension grows. | Use for growth curves and bottlenecks; use `expandability` for the ability to add deployment capacity. |
| 77 `quality-of-service` | Explicit service classes receive agreed treatment when sharing constrained resources. | Use for class differentiation, scheduling, and admission behavior; use `performance-efficiency-time-or-space-bounds` for one operation's envelope. |
| 74 `predictability` | Variation in observed behavior stays within an agreed range under stated conditions. | Use for bounds on variability and outliers; use `performance-efficiency-time-or-space-bounds` for a central timing or resource target. |
| 99 `sustainability` | Resource and lifecycle choices address an explicitly chosen environmental or long-term stewardship objective. | Ask the user which objective is intended; use `efficiency-device-efficiency` when the concern is only resource cost per operation. |

Ids 41 and 72 keep the source alias Efficiency. Route by the distinction in the
table and ask the user if the bare word does not identify the intended concern.

## Evidence and operation — batches 11-12

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 110 `verifiability` | A stated requirement has a feasible method and evidence for determining whether it is met. | Use for acceptance evidence design; use `testability` for practical control and observation during testing. |
| 76 `provability` | A formal claim can be established from explicit assumptions by a checkable argument. | Use for proof obligations; use `verifiability` when tests, analysis, or inspection suffice. |
| 101 `testability` | The system can be controlled and observed so tests can exercise and distinguish relevant behaviors. | Use for test seams, controllable state, and test oracles; use `verifiability` for the broader acceptance method. |
| 36 `demonstrability` | A repeatable demonstration makes a claimed capability inspectable by the intended audience. | Use for showing behavior in a defined scenario; use `provability` for a claim established beyond that demonstration. |
| 66 `measurability` | A property can be operationalized with a defined measurement procedure and interpretable units. | Use for defining the metric and collection method; use `observability` for inferring internal state from runtime evidence. |
| 70 `observability` | Runtime evidence lets an operator infer relevant internal state and explain behavior. | Use for diagnostic signals and correlations; use `visibility` for whether a stakeholder can see selected status. |
| 113 `visibility` | The appropriate stakeholder can see selected status or progress at the needed point in a workflow. | Use for exposure of status; use `observability` for interpreting internal runtime behavior. |
| 9 `analyzability` | Available structure and evidence support determining causes, dependencies, or change impact. | Use for systematic diagnosis or impact analysis; use `debuggability` for locating a particular execution defect. |
| 33 `debuggability` | A particular failing execution can be reproduced or inspected to localize its defect. | Use for failure localization; use `analyzability` for broader causal and dependency analysis. |
| 51 `formality` | A specification uses an explicitly defined level of notation and interpretation precision. | Use for selecting and checking precision of representation; use `provability` for a proof of a claim represented that way. |
| 82 `repeatability` | The same procedure produces sufficiently consistent results under held conditions. | Use for repeated execution in the same setup; use `replicability` for reconstruction in another setup. |
| 84 `replicability` | Another executor or environment can reconstruct a procedure and obtain an agreed comparable result. | Use for independent reconstruction; use `repeatability` for runs within the original controlled setup. |
| 30 `controllability` | Authorized operators can drive the system into intended states using explicit control actions. | Use for state-changing controls and their effects; use `observability` for inferring state without changing it. |
| 64 `manageability` | Administrators can coordinate policy and lifecycle actions across the managed system or fleet. | Use for administrative scope and coordination; use `operability` for executing a specific operational task. |
| 71 `operability` | Operators can perform intended runtime tasks and handle their outcomes in context. | Use for an operational task flow; use `manageability` for fleet administration or `supportability` for resolving user issues. |

## Deployment and exchange — batches 13-14

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 73 `portability` | A system can move between specified execution environments with bounded adaptation. | Use for platform migration; use `installability` for placing it into one environment. |
| 67 `mobility` | A user, device, or running service can move while preserving the agreed continuity of activity. | Ask the user what moves; use `nomadicity` when operation resumes after relocation instead of continuing through it. |
| 69 `nomadicity` | A user or device can reestablish useful operation after moving between environments. | Use for reconnecting and resuming after a move; use `mobility` for continuity during movement. |
| 104 `transferability` | A defined asset, responsibility, or state can be handed to another recipient with its agreed meaning preserved. | Ask the user what is transferred; use `portability` for moving software between execution platforms. |
| 55 `installability` | A deployment can be placed, configured initially, upgraded, or removed in its intended environment. | Use for installation lifecycle operations; use `portability` for differences between environments. |
| 19 `compatibility` | Specified components or versions coexist without unacceptable interference. | Use for coexistence constraints; use `interoperability` when they must exchange and use information. |
| 58 `interoperability` | Systems exchange information and interpret the agreed interaction meaning. | Use for exchange contracts and semantics; use `integratability` for effort to assemble the full solution. |
| 56 `integratability` | Separately developed pieces can be connected into a working solution with bounded integration effort. | Use for assembly work and dependencies; use `interoperability` for the resulting exchange behavior. |
| 83 `replaceability` | One component can substitute for another while preserving specified surrounding obligations. | Use for substitution and migration boundaries; use `compatibility` for coexistence without substitution. |
| 62 `localizability` | Language and locale-dependent behavior can be adapted without reworking unrelated behavior. | Use for locale resources and conventions; use `portability` for execution-platform differences. |
| 38 `distributivity` | Work, state, or responsibility can be placed across nodes under explicit placement and coordination rules. | Use for allocation across nodes; use `scalability` for workload growth or `interoperability` for exchange semantics. |
| 93 `standardizability-standardization-standard` | An artifact or interface can be expressed and maintained against an agreed common convention. | Use for selecting and adopting the convention; use `conformance` for checking an artifact against an already chosen rule. |

## Correctness and data quality — batch 15

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 31 `correctness` | Behavior matches the agreed specification for the stated inputs and conditions. | Use for agreement with specified behavior; use `accuracy` for closeness to a real-world reference value. |
| 3 `accuracy` | A reported or stored value is close enough to a defined reference under an explicit error model. | Use for value error and its reference; use `correctness` for following the specified computation or rule. |
| 16 `certainty` | An output states the warranted degree of confidence and the limits of what is known. | Ask the user how confidence is established; use `accuracy` for observed value error or `provability` for formal guarantees. |
| 20 `completeness` | Every required member or case in an explicitly bounded set is represented or handled. | Use for omissions from a defined set; use `comprehensiveness` for breadth of explanatory subject matter. |
| 29 `consistency` | Representations or decisions agree under an explicit equivalence or coordination rule. | Ask the user which agreement model applies; use `integrity` for unauthorized alteration or `accuracy` for an external reference value. |
| 28 `conformance` | An artifact or behavior satisfies a specified rule set selected for the context. | Use for checking against selected rules; use `standardizability-standardization-standard` for adopting the common convention. |

## Design structure and variation — batches 16-17

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 91 `simplicity` | A design avoids unnecessary concepts and mechanisms for its stated purpose. | Use for removing avoidable machinery; use `complexity-interacting-complexity` for analyzing interaction burden. |
| 21 `complexity-interacting-complexity` | Elements and their interactions create an explicitly assessed reasoning or coordination burden. | Use for sources and effects of interaction complexity; use `simplicity` for choosing a less elaborate design. |
| 94 `structuredness` | Elements and dependencies follow an explicit organization that can be inspected. | Use for organization and dependency rules; use `decomposability` for defining separable parts. |
| 34 `decomposability` | A whole can be separated into parts with explicit responsibilities and manageable boundary dependencies. | Use for finding and validating split boundaries; use `composability` for assembling the resulting pieces. |
| 22 `composability` | Components can be assembled using contracts that preserve required combined behavior. | Use for assembly contracts; use `additivity` for whether increments preserve their individual contributions. |
| 85 `reusability` | An artifact can serve a different specified context with bounded adaptation. | Use for reuse across contexts; use `generality` for breadth of cases the abstraction expresses. |
| 114 `wrappability` | An adapter can expose an existing component through a new boundary while preserving required original behavior. | Use for an adapter around an existing implementation; use `replaceability` for substituting the implementation itself. |
| 107 `uniformity` | Comparable elements follow deliberately consistent conventions. | Use for consistency of conventions across peers; use `simplicity` for reducing the number of mechanisms. |
| 53 `generality` | An abstraction represents an explicitly defined family of cases without case-specific redesign. | Use for abstraction coverage; use `versatility` for performing different roles or task types. |
| 111 `versatility` | A product or component serves multiple distinct roles or task types. | Use for diversity of supported roles; use `generality` for a single abstraction's family of cases. |
| 45 `expressiveness` | A notation or interface can state intended distinctions and operations directly. | Use for what can be represented; use `conciseness` for shortening an already adequate representation. |
| 109 `variability` | A product family represents explicit variation points and allowed combinations. | Use for family-level alternatives and constraints; use `configurability` for settings of one instance. |

## Business fitness — batch 18

| Id and canonical slug | Distinguishing criterion | Use this one vs. a sibling |
| --- | --- | --- |
| 7 `affordability` | Acquisition, operation, or change costs fit a stakeholder's stated financial constraints. | Ask the user for the cost boundary; use `feasibility` for whether delivery is achievable within all constraints. |
| 40 `effectiveness` | Use of the system achieves the stakeholder's intended outcome in the stated context. | Use for outcome attainment; use `functionality` for whether the required capability exists. |
| 49 `feasibility` | The proposed solution can be delivered within explicit technical, organizational, and resource constraints. | Use for whether a plan is achievable; use `viability` for whether it can remain worthwhile over time. |
| 52 `functionality` | The system provides the explicitly required operations or capabilities. | Use for capability coverage; use `suitability` for whether those capabilities fit a particular task. |
| 95 `suitability` | Available capabilities fit the intended task and context. | Use for fitness of capabilities to a task; use `effectiveness` for achieved outcomes when people actually use them. |
| 112 `viability` | An offering can continue to deliver stakeholder value under stated ongoing constraints. | Ask the user which continuation horizon and value model apply; use `feasibility` for initial delivery achievability. |
