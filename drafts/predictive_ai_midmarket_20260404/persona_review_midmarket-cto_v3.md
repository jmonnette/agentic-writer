# Persona Review: Mid-Market CTO
**Draft**: Predictive AI Is No Longer a Large-Enterprise Game - v3
**Reviewer**: Persona Reviewer Agent
**Date**: 2026-04-04
**Prior Review**: persona_review_midmarket-cto_v2.md
**Review Focus**: Whether the three v2 gaps were resolved; any remaining or new friction

---

## Persona Profile Summary

**Who I Am**: CTO at a PE-backed specialty distributor, $180M revenue. AI is on the board agenda. I have one data analyst, two engineers already committed to the ERP migration, and a PE operating partner expecting a progress update next quarter.

**What I Care About**: Not stalling the initiative. Knowing what to actually do. Making defensible decisions on team capacity, vendor vs. build, and data readiness before I commit resources I don't have.

**Reading Approach**: I read v2 carefully. I flagged three things the article didn't answer. I'm reading v3 to find out if those answers are now in there.

---

## Gap-by-Gap Assessment

### Gap 1: Build vs. Buy — Was It Addressed?

**Status: Partially addressed. The acknowledgment is present; the decision logic is not.**

The v3 addition is this paragraph, appended to the distributor scenario:

> "Two important decisions precede everything in this scenario: whether to build a custom model or buy a purpose-built SaaS solution for your use case, and how to get the operations team to actually use the model's output once it exists. Both deserve serious attention. The first is a strategic and economic decision specific to your business — existing SaaS products cover many common use cases and may be faster and cheaper than a custom build. The second is a change management challenge that determines whether any of this generates value in practice. Neither is in scope here, but both will determine whether your project succeeds."

This is better than nothing. The author now acknowledges the question exists, names the relevant tradeoff, and flags that a SaaS path may be faster and cheaper. That's a meaningful improvement — it at least doesn't steer me silently toward building when buying might be the right call.

What it doesn't do: help me make the decision.

The v2 review asked for a framework — even a rough one. "Build when your data is proprietary enough to create genuine differentiation; buy when a vendor's model is good enough for your use case" was the suggested framing. The v3 paragraph is softer than that. It tells me the question matters and then steps away. For a reader who came here specifically for decision support, "this decision is important and it's not in scope" is only marginally more useful than silence.

The net effect: I no longer feel misled by an article that assumes build without acknowledging alternatives. But I'm still going to have to figure out the actual decision logic somewhere else. That's acceptable — the article's scope is what it is — but the resolution is partial, not complete.

**Improvement from v2**: Real. The absence of the build/buy question was a credibility gap; its presence, even without a framework, closes that gap.

**Remaining friction**: The paragraph is appended to the end of the scenario section in a way that reads like a disclaimer rather than a structural decision point. If the author is serious that these two decisions "precede everything in this scenario," they belong before the scenario plays out — not after. Right now, I read eight weeks of pipeline and modeling detail and then get told at the end that I should have first figured out whether to build at all. The sequencing of the article doesn't match the sequencing of the actual work.

---

### Gap 2: "Assess Your Data" Had No Method — Was It Addressed?

**Status: Not meaningfully advanced. The instruction is still there; the method is still absent.**

The data quality section in v3 is substantively unchanged from v2. The instruction reads:

> "The honest sequence: before evaluating any AI vendor, before writing any RFP, before hiring anyone to build anything — assess what data you actually have, whether it's reliable, and whether it covers the business problem you're trying to solve."

This is the same language as v2. The v2 review flagged specifically: what does this assessment involve? How long does it take? Who runs it — my data analyst, an external consultant? What does "reliable enough" mean? Is there a threshold?

None of those questions are answered in v3. The instruction is correctly prioritized and the surrounding paragraph correctly names the failure modes (confident, plausible, incorrect outputs from a bad model). But the directive "assess your data" remains a call to action without a description of the action.

This matters in a specific way. I read this section and feel validated — the author understands the data problem and isn't minimizing it. But I walk away without knowing what to actually schedule on my calendar as Step One. "Do a data readiness assessment" is a task I can name, but I don't know its scope, its inputs, its outputs, or who should own it. The article tells me it's the prerequisite for everything; it doesn't tell me what it is.

**Improvement from v2**: None detectable. This gap was flagged as a "helpful improvement" in v2, not a critical change. The author may have deprioritized it intentionally. But for a reader whose next action is "figure out if my ERP data is usable," the gap still stops progress.

**Remaining friction**: Unchanged from v2. The data section earns credibility but doesn't generate next steps.

---

### Gap 3: The Analyst + Engineer Staffing Assumption — Was It Addressed?

**Status: Not addressed. This gap was flagged as a critical change in v2 and is still absent in v3.**

The distributor scenario still reads:

> "The team that builds it: a data analyst with ten years of distribution operations experience and a generalist engineer. No ML PhD."

There is no acknowledgment in v3 that these people might not be available. The build vs. buy paragraph added at the end of the scenario does not mention the resource contention problem. The team composition assumption stands unmodified.

This is the gap I feel most acutely as this persona. My analyst and my best engineer are already on the ERP integration. The article still implicitly assumes I have slack capacity to redirect. It doesn't.

The v2 review asked for one of three things: sequencing guidance (phase AI after ERP stabilizes), contracting options (fractional ML help), or a trade-off framing (what do you deprioritize). None of these appear in v3.

The build vs. buy paragraph is adjacent to this problem — one reason to buy a SaaS solution rather than build is precisely that a custom build requires internal capacity I don't have. But the article doesn't connect these ideas. The build vs. buy acknowledgment and the staffing assumption live in separate paragraphs with no bridge between them. A reader has to make that connection independently, and many won't.

**Improvement from v2**: None on this gap specifically. The build vs. buy addition creates a latent opportunity to address resource contention (buying often requires less internal technical labor), but that opportunity is not taken.

**Remaining friction**: This is still the most significant gap for this persona. The article's practical scenario assumes team availability that most PE-backed operators don't have. Without any acknowledgment of resource contention, the article's guidance breaks down at the point where a reader like me tries to apply it.

---

## New Friction Points in v3

### The Build vs. Buy Paragraph Placement

Covered above under Gap 1. The paragraph appears after eight weeks of build scenario detail. If the author is earnest that build vs. buy is a decision that "precedes everything," placing it after the scenario plays out creates a structural contradiction. A reader who was building an internal case for the custom build path during the scenario will reach the paragraph and feel mildly misled — the article just spent considerable space teaching them how to build, and now it tells them they should have asked whether to build first.

This is a new friction in v3 that didn't exist in v2 (where the question wasn't raised at all). It's better to have it there than not — but the placement works against the intent.

### The Change Management Mention Is Still a Placeholder

The build vs. buy paragraph also surfaces the change management problem:

> "The second is a change management challenge that determines whether any of this generates value in practice."

This was flagged in v2 as a secondary concern: the article treats business adoption as a footnote. The v3 treatment acknowledges it exists and then explicitly says it's out of scope. That's a defensible authorial choice. But for a reader who knows from experience that this is where most AI initiatives fail after a technically successful deployment, "out of scope" reads as evasion. The article could afford one sentence on what "not out of scope" looks like — even a directional note that change management deserves its own dedicated treatment — rather than naming the problem and stepping away from it in the same breath.

This isn't new friction, exactly. But the v3 addition draws more attention to the gap than v2 did by explicitly naming both problems and then declining to address either one.

---

## Overall Assessment

**Would I Finish Reading?**: Yes — same conclusion as v2. The distributor scenario, data quality section, and talent cost data remain the strongest elements and are unchanged.

**Did v3 Move the Needle?**

One gap is partially closed (build vs. buy acknowledged), one is unchanged (data readiness method), and one is unchanged (staffing assumption). The v3 revision does real work but it's conservative — it adds a paragraph of acknowledgment without adding the decision logic or operational guidance the v2 review asked for.

The article is meaningfully better than v2 for a reader who was frustrated that build vs. buy was never surfaced. It is not meaningfully better for a reader trying to figure out how to start the data readiness work or how to thread an AI initiative through a team that is already at capacity.

**Rating**: 4 out of 5 for this audience — same as v2. The v3 change was too targeted and too hedged to move the rating.

**What Changed in My Experience**: The build vs. buy paragraph prevents the article from silently steering me toward building when buying might be the right path. That matters. It doesn't help me make the decision, but it stops the article from making it for me without my awareness. That is a genuine improvement.

**What Didn't Change**: I still don't know what a data readiness assessment involves. I still don't have a path forward if my best analyst and engineer are unavailable. I'm still going to have to figure out most of the operational detail on my own.

---

## Recommendations for Final Pass

### Still Critical

1. **Address the resource contention problem.** The staffing assumption is the article's biggest structural weakness for this audience and it was not touched in v3. One paragraph on sequencing vs. contracting vs. deprioritization options — framed for a PE-backed operator with constrained capacity — would close the gap that the article has had since v1.

2. **Move the build vs. buy acknowledgment to before the scenario.** If these decisions truly precede the build, the article should present them before walking through the build. A brief framing paragraph before the scenario section opens — noting that the scenario assumes a custom build path and that readers should evaluate whether a SaaS solution fits their use case before following this path — would eliminate the structural contradiction introduced in v3.

### Still Helpful

- **Add one paragraph on what a data readiness assessment actually involves.** Even a rough description — who runs it, what it looks for, what "clean enough to train on" means in practical terms — converts the directive into an actionable first step.

- **Connect build vs. buy to the staffing assumption.** If the reason a reader might buy rather than build is partly that building requires internal technical capacity they don't have, say so. The two ideas are already adjacent in the article; a single connecting sentence would make the link explicit.

### New in v3

- **Reconsider the "neither is in scope" framing for both buy decision and change management.** Naming two decisive problems and then stepping away from both in the same paragraph draws attention to the gaps rather than managing them. Either treat each briefly (one sentence of directional guidance each) or remove the explicit out-of-scope declaration and let the paragraph stand as a flag rather than an abdication.

---

## Persona Verdict

**Rating**: 4 out of 5 for this audience

**One-Sentence Summary**: The build vs. buy acknowledgment is a real improvement but is placed too late and goes too soft; the staffing assumption and data readiness gaps are unchanged, leaving the article one substantive revision short of being fully actionable for an operator in a constrained organization.

**Quote**: "I can see the author heard the feedback on build vs. buy — it's now in there, which is better than before. But the paragraph lands like a disclaimer at the end of a scenario I've already been following as a build. And I still don't know what to tell my analyst to actually do when she finishes the ERP integration and I hand her this article. 'Assess your data' is not a project plan."
