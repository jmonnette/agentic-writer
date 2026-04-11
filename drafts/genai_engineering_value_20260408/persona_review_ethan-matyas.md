# Persona Review: Ethan Matyas
**Draft**: The Metric That Actually Matters: Why CTOs Must Speak Dollars, Not Story Points — FINAL
**Reviewer**: Persona Reviewer Agent
**Date**: 2026-04-11

---

## Persona Profile Summary

**Who I Am**: Chief Delivery Officer at GlobalLogic (Hitachi Group). 30 years building and running software delivery organizations across enterprise services, professional services, and IT leadership. My current mandate is making AI adoption real — not deployed, real — across global engineering programs, with accountability for measurable outcomes.

**What I Care About**: Whether software actually ships. Whether AI tools actually change how teams work, not just what tools they have. Whether the output of an engineering organization can be connected to a business result someone outside engineering cares about. I have seen too many transformation programs that changed everything on the surface and nothing underneath.

**Reading Approach**: Time-constrained, skims for signal density, reads for argument structure, cross-references against experience in real programs. I bail fast on vague claims. I read carefully when something earns my attention.

---

## Initial Impression

**Hook Effectiveness**: Strong. The opening three sentences do exactly what an opening should do — make a specific claim and establish stakes without warming up to make a point. "Your CFO doesn't care about story points. Your CEO doesn't care about velocity." I'm in. That's the right level of directness. The hook earns the read.

**Value Proposition**: Clear for the primary audience. Engineering leaders who are struggling to justify AI spend in executive conversations will recognize themselves immediately.

**First Reaction**: This is a real argument about a real problem. The METR data in the second section is the kind of evidence I actually want to see in a piece like this — a randomized controlled trial, not a vendor survey, showing a result that cuts against the industry narrative. The author is doing the right thing by foregrounding the data that's inconvenient for the optimistic case. That earns credibility with me before we even get to the framework.

---

## Reading Experience

### What Worked

**The METR RCT citation** is the strongest thing in the article. Not because it's dramatic — because it's honest. Most AI productivity articles reach for the 10x claims. Surfacing a study showing experienced developers took 19% longer, with the author's framing that "that 39-point gap between perception and reality is the most important data point in the AI productivity debate," is the kind of intellectual honesty that makes me trust the rest of the argument.

**The source credibility flagging** is genuinely sophisticated and deserves recognition. Noting that Faros AI sells engineering analytics software, that Salesforce sells AI products to CFOs, that LinearB is a productivity measurement vendor — and still using the data while naming the conflict — is exactly right. I don't see that often. Most authors either ignore the source bias or refuse to use tainted sources. This thread-the-needle approach is the mature version.

**The accountability split** (what to build vs. how to build it) in the "Who Is Accountable for What" section is the most operationally useful section in the article. That distinction — product and business stakeholders own which features, engineering owns how it's built — is something I have had to articulate in client conversations for 20 years, and it's stated here more cleanly than I've managed most of the time. The observation that dollar metrics fix the input problem by requiring business stakeholders to go on record about expected return is genuinely sharp. That changes the conversation before a line of code is written. That's not a measurement insight — that's an organizational design insight dressed as a measurement insight.

**The three-column attribution example** (the in-app renewal prompt table) is the right move. Showing an actual row with actual numbers and naming the methodology makes the whole framework real. The observation that it's "directionally honest" and "names the methodology" rather than claiming precision is exactly the right epistemic posture.

**The "What Happens If You Don't" closing** lands cleanly. "Not because AI isn't working, but because their reporting infrastructure is built around story points and DORA metrics" — that is the correct diagnosis. The problem is often not that AI failed. It's that you can't see whether it worked.

**The practitioner sidebar** ("For practitioners at the ceremony level") is a structurally smart addition. Most articles at this altitude ignore the people actually running sprints. Addressing them directly, with a concrete and minimal entry point (add one field to the story template), is respectful of the audience range.

### What Didn't Work

**The capacity math section undercuts itself**. The framework opens with a claim about the METR data showing gains may be near zero or negative for experienced developers — and then immediately uses the LinearB GitHub Copilot 20% figure as an input to a $2–2.5M capacity recovery calculation. The author adds appropriate caveats, but the rhetorical structure creates a problem: you've told me I should be skeptical of optimistic productivity figures, and then you've built a board presentation example using one. A reader who absorbed the METR data is going to feel the tension. The solution isn't to remove the example — it's to anchor the example on a range that reflects METR's findings more directly. A 5–15% realistic case alongside the 20% optimistic case would make this more defensible. The current framing says "apply appropriate skepticism" and then uses the optimistic number for the math. That's doing work the framing can't support.

**"This is not additional bureaucracy imposed on engineering teams"** is a claim that won't survive contact with reality for most organizations. Requiring every user story to include a business justification field, a predicted metric impact, and a measurement owner is, in practice, a significant process change that most product organizations are not equipped to execute consistently. The article acknowledges that "organizations that lack [product management maturity] need to address that alongside the measurement infrastructure" — but that's mentioned in a single parenthetical in the accountability section and never operationalized. In my experience, this is where the whole framework fails in the first 90 days. Not because the engineering team resists. Because the product organization has no process for generating credible value hypotheses, the business stakeholders have never been asked to make falsifiable predictions about feature value, and the ownership of measurement plans falls into a gap between product and analytics that no one formally owns. The article treats this as a brief caveat. It's actually the implementation problem.

**The Gartner SEI Platform prediction** (5% adoption today, 50% by 2027) is the weakest citation in the article. Gartner adoption predictions are directionally suggestive and frequently wrong on timing. Citing this as though it's a meaningful data point invites exactly the skepticism the author is trying to avoid by flagging other sources' conflicts of interest. Either make this earn its place with more substance or cut it.

### What Confused Me

**The relationship between the "internal team metrics" framework referenced in "A Note on the Metrics You're Already Using"** and the dollar dashboard isn't fully resolved. The author references prior writing that advocates a multidimensional approach — stakeholder satisfaction, exploration speed, team capability range — and says it's "for internal use." But the article doesn't explain how the two frameworks coexist operationally. If I'm a VP of Engineering running both, what's my reporting architecture? Do I maintain one dashboard for my internal team cadence and a separate one for CFO conversations? How do I keep both from becoming theater if I'm producing two versions of the same question? This deserves a sentence or two, not a whole section — but right now it leaves a gap.

---

## Key Concerns and Objections

### Concerns Raised

**1. The adoption problem is absent.**
The article is written as though the barrier is the measurement framework and the reporting language. In my experience, the barrier is almost always the organizational behavior change required to make the framework stick. Getting product managers to produce credible value hypotheses for every story before estimation is a skills and incentive problem, not a template problem. Getting finance to engage seriously with attributed impact estimates rather than dismissing them as engineering theater requires a relationship investment. Getting engineers to connect sprint work to business outcomes requires a governance structure that most organizations don't have. The article tells you what to build. It doesn't tell you how to survive the first six months of trying to build it, when the template goes into the system and nothing actually changes.

**2. The 60–90 day measurement lag is mentioned but not taken seriously enough.**
"Rough signal in 60–90 days, reliable trend data in 6–12 months." If I'm a CTO whose CFO is asking for AI ROI data right now, a 6–12 month measurement runway is not a minor caveat. It's a political problem. The article should address what you bring to the CFO conversation in the interim — how do you maintain credibility and budget while the measurement infrastructure matures? What proxies are defensible in the short term? This is a gap between the framework and the situation the reader is actually in.

**3. The SaaS-centricity is disclosed but not fully resolved.**
The "Adapt the dollar frame for your context" section correctly identifies that the three-column dashboard assumes product engineering with customer-facing features and clean revenue attribution. The alternatives it offers — process cost eliminated, operational throughput gained, risk and downtime avoided — are directionally right. But these alternative framings require fundamentally different attribution methodologies, different data infrastructure, and different conversations with finance. For someone running delivery for a healthcare IT client, a manufacturing integrator, or an enterprise ERP shop, the delta between "revenue generated or protected" and "regulatory penalties avoided" is not just a label change. It's a completely different measurement problem. A brief acknowledgment in one paragraph is not enough to serve that audience.

### Unanswered Questions

- **How do you get buy-in from product leadership to add business justification requirements to the story template?** The article puts the mechanism in the backlog process but the organizational change work to make that stick is unaddressed.
- **What do you do with existing backlog items that predate this framework?** Most engineering organizations don't start clean. The measurement chain section assumes a greenfield process change.
- **How does this framework interact with delivery governance and program management structures?** For organizations running formal PMO or delivery governance models, where does the dollar dashboard live, who maintains it, and how does it connect to existing program reporting?

---

## Missing Elements

**The organizational change layer.** The article is a compelling argument for why the measurement change is necessary and a coherent description of what the new measurement model looks like. It is missing the how-to-make-it-stick layer almost entirely. For a CTO who accepts the argument, the most important questions are about implementation: who has to change their behavior, what resistance will they encounter, what does the 90-day change sequence look like? The article gestures at this with the practitioner sidebar and the "start with one row" advice, but the organizational dynamics of introducing dollar-denominated requirements to product owners and finance stakeholders who have never been asked to operate this way is the actual hard problem.

**The failure mode section.** Every framework has conditions under which it breaks. I read carefully for this in every article. This one doesn't have it. What happens to this framework in an organization with no product analytics infrastructure? In an organization where the product org has no authority to kill features that can't generate a value hypothesis? In a delivery program where the client has contractual requirements that aren't tied to business outcomes? Where does the dollar dashboard fail silently — producing numbers that look good and mean nothing?

---

## Assumptions I Don't Share

**1. "This is not additional bureaucracy."**
The author assumes that requiring business justification fields, value hypotheses, and measurement owners on every story is a clean process addition. In practice, this competes with existing planning overhead, creates friction at refinement for stories that are genuinely exploratory or technical, and requires product management maturity that most teams haven't developed. It will be experienced as bureaucracy by the teams it's imposed on, regardless of its intent. The article needs to acknowledge this directly and offer a more graduated adoption path.

**2. Finance will interrogate the methodology honestly.**
The article says "the standard proposed here — honest correlation with named assumptions — requires active interrogation from finance, not passive acceptance." That's true. But in most enterprise environments, finance doesn't have the bandwidth or the domain knowledge to interrogate engineering attribution methodologies rigorously. What usually happens is that the numbers either get accepted uncritically or dismissed as engineering theater. Building a framework that depends on finance engagement to remain honest is a fragile design.

**3. The primary audience has authority to implement this.**
The article is addressed to CTOs and VPs of Engineering. But the measurement framework it's proposing requires buy-in from product leadership, finance, and in many cases the CEO or COO, to actually change how work gets justified and measured. Many of the people reading this have the will but not the cross-functional authority to make it happen. The article doesn't address that political reality.

---

## Overall Assessment

**Would I Finish Reading?**: Yes, absolutely.

**Why**: The argument is coherent, the evidence is handled with more intellectual honesty than most pieces on this topic, and the framework is specific enough to be genuinely useful. This earned my full attention by the end of the second section and didn't lose it.

**What I'd Take Away**:
- The accountability split (what to build vs. how to build it) is the clearest statement of this I've seen. I will use that framing.
- The METR data is something I want to make sure my team knows. We may be measuring adoption when we should be measuring output quality change.
- The requirement to capture capacity gains deliberately — as a deliberate CFO conversation, not an assumed cost savings — is underemphasized elsewhere and important here.

**Would I Share This?**: Yes.

**With Whom**: Delivery leaders on my team who are in AI ROI conversations with clients. Engineering VPs at client organizations who are heading into budget reviews. Probably a few people in my peer network.

**Why**: Not because it's complete — it isn't — but because it's asking the right question and giving a defensible starting framework. Most of what I see on this topic is either pure hype or pure skepticism. This is attempting to be useful, and it mostly succeeds.

**Impact on My Thinking**: The accountability framing gave me something I'll use. The explicit disclosure of source conflicts is a practice I want to apply in my own communications. The METR data point sharpens something I already believed but couldn't cite precisely.

---

## Recommendations for This Audience

### Critical Changes

1. **Extend the implementation section.** The framework is well-argued. The organizational change mechanics are absent. For a CDO or CTO, the argument isn't the hard part — the change management is. Add a section on what the first 90 days actually look like: who you need buy-in from, where the resistance will come from, what minimum viable version you can implement without needing enterprise-wide change. The "start with one row" advice is right as a principle but needs more substance.

2. **Address the product management maturity gap more directly.** The parenthetical that "organizations that lack [product management maturity] need to address that alongside the measurement infrastructure" is doing too much work. This is not a side condition — it's the primary failure mode. Call it out explicitly and tell the reader what to do when they're in that situation, because most of them are.

3. **Revisit the capacity math example.** Either anchor the range on the METR findings more directly (present a realistic-case calculation that uses a much lower productivity improvement assumption) or acknowledge that the $2–2.5M figure is the optimistic ceiling rather than the central estimate. The author has earned trust by being honest about evidence quality elsewhere — this section risks spending that trust.

### Helpful Improvements

- The failure mode section is missing and should be added. Where does the dollar dashboard produce misleading results? What organizational conditions cause it to fail silently?
- Add a clearer bridge for the CTO who accepts the argument but doesn't have cross-functional authority to implement it. What's the strategy for building that coalition?
- The 6–12 month measurement lag deserves a more direct answer: what do you say to the CFO in the interim? What proxies are defensible before the framework is mature?

### Optional Enhancements

- A brief note on how this framework interacts with existing delivery governance and PMO structures would serve the enterprise audience.
- The Scrum Master / practitioner sidebar is good. Consider a parallel one for product owners — they're the people whose behavior needs to change most for this to work, and they're not addressed directly.

---

## Persona Verdict

**Rating**: 4 out of 5 for this audience

**One-Sentence Summary**: The argument is sound, the evidence is handled honestly, and the framework is specific enough to use — but the article stops at the point where the actual hard work begins, and for practitioners trying to implement it in real organizations, that gap is significant.

**Quote**: "This is the right question, and the answer you gave is better than most. The accountability framing is something I'll use directly. But you stopped at the framework level and called it done. The part you didn't write — how to make this stick when the product org hasn't been asked to make falsifiable predictions about feature value before, when finance doesn't have bandwidth to interrogate your attribution methodology, when the client relationship doesn't fit the SaaS model you've been describing — that's where this lives or dies. I'd share this as a starting point. It's not a complete answer. Write the next one."
