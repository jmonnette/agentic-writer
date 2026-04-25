# Persona Review: Amit Soni
**Draft**: Most AI Projects Don't Fail at the Model. They Fail at the Foundation. — FINAL
**Reviewer**: Persona Reviewer Agent
**Date**: 2026-04-24

---

## Persona Profile Summary

**Who I Am**: SVP of PE Value Creation at GlobalLogic (Hitachi Group). Nearly 20 years at Wipro before that. I run AI and digital transformation programs inside PE portfolio companies — SaaS and software businesses primarily — and I am accountable to IRR and EBITDA outcomes, not pilot counts or engineering KPIs. I built agentic AI systems from scratch in Python last year because I do not advise on things I have not done.

**What I Care About**: Whether AI creates enterprise value at the business model level, not whether it makes existing workflows faster. Execution that closes in PE timelines — 3 to 5 years, not 10. Frameworks that eliminate political friction structurally. Math that closes.

**Reading Approach**: I skim the structure first. If the opening does not signal a non-obvious perspective, I stop. I read the conclusion early. When I am engaged, I read closely and look for things to steal, challenge, or build on.

---

## Initial Impression

**Hook Effectiveness**: The opening pulls me in. "Pilot purgatory" is the right diagnosis and it is named precisely. I have seen this at nearly every portco I have walked into in the last two years. The framing is correct.

**Value Proposition**: Partially clear. The article promises to explain why AI cannot be operationalized and how to fix it. It delivers on the diagnosis. The prescription is competent but does not deliver the differentiation I was hoping for.

**First Reaction**: This reads like something a capable technology consultant wrote for a general enterprise audience. It is not wrong. The data is solid. The argument is structured. But by section three, I am starting to ask: who specifically is this for, and what are they supposed to do on Monday morning that they could not have figured out from the Gartner press releases cited here? The article gets better toward the end, but it takes too long to earn its specificity.

---

## Reading Experience

### What Worked

**The 95% framing reframe**: The first substantive move — arguing that the 95% GenAI failure stat is misread as a model problem when it is an engineering readiness problem — is the best thing in the article. That is a non-obvious claim that I agree with and can use. That distinction between "chase a better model" versus "fix the plumbing" is operationally useful.
> "If you believe it's a model problem, you chase newer architectures. If you understand it's an engineering problem, you fix your plumbing."

Clean. I would use that in a board conversation.

**The agentic AI failure mode example**: The CRM/ERP/billing rollback scenario is specific and useful. This is the kind of concrete failure case that makes abstract governance arguments land in a room full of operators. I have seen this exact failure mode. The framing of "bad suggestions" versus "bad actions" as a category-of-risk distinction is one I will borrow.
> "A human-in-the-loop system produces bad suggestions. An agentic system produces bad actions. That is a different category of risk."

This is tight and correct.

**The token cost math**: The 10 to 50 times token consumption escalation figure for agentic versus prompt-response workflows is a number I have not seen quantified this clearly. This belongs in a business case conversation. The customer service agent cost example is specific enough to be credible and alarming enough to be memorable.
> "Organizations approve pilots based on demo economics, then hit a production cost wall that was never in the business case."

Yes. I have watched this kill three projects in the last eighteen months.

**The 10-20-70 BCG principle**: The framing that 70% of the AI value gap is explained by people, process, and organizational discipline — not technology — is consistent with what I observe. I am glad it is cited from BCG rather than asserted. This is the kind of claim that needs a source to survive a skeptical GP.

**The closing three questions**: Ending on "if you doubled the number of AI agents running in your environment tomorrow, would your infrastructure hold? Would you know what they were doing? Would you be able to stop them if something went wrong?" is the right stress test. Concrete, auditable, immediately applicable.

---

### What Didn't Work

**The 7% data readiness statistic is treated as a punchline, not a diagnostic tool**: The article drops "only 7% of enterprises say their data is completely AI-ready" and then moves on. This is a powerful number but it is used rhetorically rather than analytically.
> "Seven percent. That means 93 out of 100 organizations attempting to scale AI are building on a foundation they have already admitted is compromised."

That is a valid observation but it does not close the loop. The natural follow-on question from someone running a value creation program is: what is the distribution? What does the 30th percentile look like versus the 70th percentile? What does "partially ready" mean in practice and how long does it take to close that gap? The article raises the alarm without giving me the triage logic I need to prioritize one portco's infrastructure investment over another's.

- **Impact**: The stat lands as a scare tactic for a general audience. For me, it raises more questions than it answers and then leaves them hanging.
- **Suggestion**: Add a maturity model or a 2x2 that maps data readiness against AI ambition level. Even a rough framework for "here is what it takes to move from 20th to 60th percentile readiness" would be more actionable than "93 out of 100 are compromised."

**The "semantic data layer" concept is introduced and not explained**: 
> "A semantic data layer must sit between raw enterprise data and the AI systems consuming it, translating technical schema into business concepts agents can actually interpret."

This is technically correct and architecturally important. But it is introduced once, defined in a single sentence, and never operationalized. What does standing up a semantic layer cost? What is the build timeline? What does a portco need in-house versus what can a services partner deliver? For a reader who is going to be asked by a PE operating partner "okay, what does this actually require," this is the answer that is missing.

- **Impact**: Sounds sophisticated. Is not actionable. A technical reader will nod; an operator will nod and not know what to do.
- **Suggestion**: Either cut the term and keep the concept in plain language, or give it one paragraph of operational substance: what it is, what it replaces, what it costs in time and money.

**The "Fix the Plumbing" section is the right answer presented as a checklist**: The final prescription section is the most important part of the article and it reads like a service brochure. Data readiness audit. Integration design. Engineering discipline. Measurement framework. Technical debt.

These are all correct. None of them are sequenced with enough specificity to be useful under PE time pressure. If I am 18 months into a 4-year hold and my portco has moderate data issues, a fragile integration layer, and an engineering team that is already stretched, which of these do I do first? The article says "start with data readiness" but does not give me the logic for why that sequencing is right or what I trade off by doing so.

- **Impact**: The prescription lands as "do all these things" rather than "here is how to prioritize given your constraints."
- **Suggestion**: Add a sequencing framework with explicit trade-off logic. Even a simple "if you have 90 days, do this; if you have 12 months, do this" would move the article from diagnosis to decision tool.

---

### What Confused Me

**The audience is not clearly established**: This article is co-authored for "The Engineer." The language alternates between engineering-level specificity (idempotent APIs, circuit breakers, semantic data layers) and strategic C-suite framing (BCG value gap, IRR-adjacent language, board conversations). This creates a reader identity problem. Engineers will find the strategic sections too thin. Executives will find the technical sections too specific without enough scaffolding.

- **Background**: I know both registers, so I can follow it. But I am not the average reader.
- **Suggestion**: Pick a seat. Either this is a technical article with business context, or a business article with technical grounding. The blend is workable but it should be intentional and declared.

---

## Key Concerns and Objections

### Concerns Raised

1. **The article treats enterprise and PE-backed companies as interchangeable**: Every data point cited — MIT NANDA, Forrester, Cloudera, Gartner — is drawn from broad enterprise surveys. The article's recommendations assume organizational context and timelines that do not map cleanly to a PE hold period. A Fortune 500 can deprioritize infrastructure for 18 months and survive. A portco on a 4-year hold cannot.
   - Current treatment: The article mentions "organizations projecting aggressive AI roadmaps" but never distinguishes between a large enterprise with a 10-year runway and a portco with a management team facing a recap in 24 months.
   - Recommendation: A single paragraph acknowledging that urgency and sequencing logic differ materially under PE timelines would make this article significantly more useful to the audience I represent.

2. **No talent strategy**: The article correctly identifies that the AI problem is organizational, not technical. But the organizational prescription stays at the systems and process level. There is no mention of who inside the organization executes this. Who owns the data readiness audit? Who owns the integration layer redesign? Who owns AI observability? In my experience, the answer to "why did this not get done" is almost never "they did not know they needed to" — it is "the person who needed to do it either did not exist or did not have the organizational power to do it."
   - Current treatment: The article mentions "someone is accountable for this system after the launch celebration" — which is technically a talent/ownership point — but it is buried in a list and given one sentence.
   - Recommendation: The talent and ownership gap deserves its own beat. What does the organizational design look like for an AI-ready engineering function? Who owns this at the VP or SVP level, and what does their charter look like?

### Unanswered Questions

- **What is the actual cost and timeline to get from "7th percentile" to "deployable" on data readiness?** The article sets up the problem; it does not give operators a rough cost envelope or timeline range.
- **What is the right build versus buy decision for the integration layer and the semantic data layer?** The article implicitly assumes you are building this. Is that right? What does a services engagement model look like versus an internal build?
- **What does "persistent agentic memory" cost to stand up?** The OB1 reference is interesting and I followed it, but pointing to a GitHub repo as the answer to an enterprise architectural challenge is not sufficient for a business audience.

---

## Missing Elements

**What I Expected to See**:
- A maturity model: where are most organizations on a 1 to 5 data readiness scale, what does each level look like, and what is the typical lift to move one level?
- PE-specific urgency framing: the argument that technical debt compounds with AI ambition is exactly right but the article never prices that compounding in terms a PE operating partner would recognize (EBITDA drag, multiple compression, missed exit timeline).
- A talent and ownership map: who inside the organization is accountable for each layer of the AI foundation?

**What Would Make This More Valuable to Me**:
- A rough economic model for the "fix the plumbing" investment: order-of-magnitude cost, timeline, expected return on the infrastructure investment before AI value realization begins. Even a range.
- A decision framework for organizations that cannot do everything: given 90 days and a budget constraint, which of the four prescriptions (data, integration, observability, technical debt) has the highest expected return?

---

## Assumptions I Don't Share

The author seems to assume:

1. **That the reader has the organizational authority and timeline to do this work correctly**: The article prescribes a logical sequence — data, integration, observability, then scale — and assumes the reader can implement it. In PE-backed portfolio companies, the sequence may be correct but the organizational will, political alignment, and budget authority to execute it are frequently not present simultaneously. The article does not address how to build the internal case for infrastructure investment before you have the AI results that would justify it.
   - Reality for this persona: At portcos, I am often working with a CTO who knows the infrastructure is broken but cannot get budget because the CEO is promising the board an AI roadmap, not an infrastructure remediation project.
   - Impact: The article gives a technically correct answer to a problem that is frequently blocked by an organizational and political constraint it never acknowledges.

2. **That "observability" is a new concept for the audience**: The article spends meaningful space explaining what observability means in the context of AI. Engineers already know what observability is. The interesting question is what AI-specific observability looks like — what do you instrument that you do not instrument for a conventional service? The article gestures at this but does not deliver it.

3. **That the 15% who are winning got there through disciplined foundation-building from the start**: The BCG "widening AI value gap" finding is real. But many of the companies in the top quartile got there through a combination of early mover advantage, favorable data architecture decisions made years ago for non-AI reasons, and access to talent markets that most organizations cannot replicate. The article implies the path is replicable via discipline. That may be too optimistic about the catch-up potential.
   - Impact: Creates false confidence that the formula is knowable and executable without acknowledging the structural advantages some leaders hold.

---

## Overall Assessment

**Would I Finish Reading?**: Yes
**Why**: The argument is structured, the data is credible, and there are at least three passages I would pull for client conversations. The article earns the read even if it does not fully deliver on the promise of its framing.

**What I'd Take Away**:
- The "bad suggestions versus bad actions" distinction for agentic governance. That framing is immediately usable.
- The token cost multiplication figure (10 to 50 times) for agentic versus prompt-response. I will verify this against our own deployment data and use it if it holds.
- The three stress-test questions at the end. Those belong in a board conversation about AI readiness.

**Would I Share This?**: Maybe
**With Whom**: I would share it with a portco CTO who needs board-level language for an infrastructure investment request. I would not send it to a PE operating partner as a strategic framework — it is not PE-native enough.
**Why/Why Not**: The article is solid practitioner content. It is not differentiated enough in framing or specific enough in prescription to be the piece I would put my name on or send as a signal of my own thinking.

**Impact on My Thinking**: Confirms rather than shifts. The diagnosis is one I share. The article gives me some useful quantification I did not have (token cost multiple, 7% data readiness figure). It does not change my operating model or add a framework I have not already arrived at through direct experience.

---

## Recommendations for This Audience

### Critical Changes
1. **Add PE-specific urgency framing**: One paragraph connecting the compounding technical debt argument to PE timeline economics — EBITDA drag, hold period risk, multiple compression at exit — would make this article a different instrument for a different audience.
2. **Add a sequencing decision framework**: Given resource constraints, what is the priority order and what is the logic? The article tells you to do all four things. It does not tell you which one to do when you can only do one.

### Helpful Improvements
- Address the organizational and political blockers explicitly. The article diagnoses what needs to be built. It does not address why it is not being built — which is almost always a power, incentive, or information asymmetry problem.
- Give the semantic data layer concept operational substance: build time, cost range, in-house versus outsourced decision.
- Add a rough cost envelope for the "fix the plumbing" investment so readers can size the ask before they walk into a budget conversation.

### Optional Enhancements
- A maturity model (even a simple 3-level version) for data readiness would convert a diagnostic article into a triage tool.
- A sharper editorial decision on audience: engineer or executive. The current blend is navigable but neither audience gets a fully native reading experience.

---

## Persona Verdict

**Rating**: 3.5 out of 5 for this audience

**One-Sentence Summary**: The diagnosis is correct and well-evidenced, but the prescription is too generic to be a decision tool for operators working under PE time pressure and organizational constraints.

**Quote**: "I agree with everything in this article and I could not hand it to a GP and say 'here is how we are going to create value in the next 18 months.' The diagnosis is right. The math does not close on the prescription."
