# Persona Review: Mid-Market CTO
**Draft**: The Metric That Actually Matters: Why CTOs Must Speak Dollars, Not Story Points — v1
**Reviewer**: Persona Reviewer Agent
**Date**: 2026-04-08

---

## Persona Profile Summary

**Who I Am**: CTO at a PE-backed specialty distributor, $180M in revenue. Team of 14 — eight keeping the lights on, four on the ERP integration, two nominally available. Reports to a CEO who's enthusiastic about AI and a PE operating partner who wants to see it in the quarterly review.

**What I Care About**: Delivering against the commitments in the value creation plan. Not blowing up my credibility with the board over AI metrics I can't defend. Finding a realistic path forward given my actual team capacity.

**Reading Approach**: Scanned the headers first. The title got my attention — "speak dollars" is exactly the language I'm trying to learn. Then I read the opening and the main framework section carefully. Skimmed the evidence sections once I understood where they were going.

---

## Initial Impression

**Hook Effectiveness**: Strong. "Your CFO doesn't care about story points" — yes, this is the exact conversation I just had last month. The opening paragraph names the problem I'm living with. I kept reading.

**Value Proposition**: Partially clear. I came in expecting an article that would teach me what to measure and how to report it. The article does eventually get there. But the value proposition gets muddied — this reads more like an argument for changing engineering culture than a practical guide for someone who needs to walk into a board meeting in six weeks.

**First Reaction**: "Finally, someone is saying what I've been thinking. But who is this actually written for? Because some of this is directed at someone running a 200-person engineering org, not my team of twelve."

---

## Reading Experience

### What Worked

**The opening problem statement**: "Most engineering leaders cannot answer that question. Not because the answer is bad — but because they've been measuring the wrong things and reporting them in the wrong language." This is precise and accurate. I've been in exactly this position. I didn't need to be convinced — but seeing it articulated this cleanly was useful because now I have language to use with my CEO when I explain why I need to change how we report.

**The Faros AI data**: The finding that 21% more tasks completed and 98% more pull requests merged — and zero correlation to business outcomes — is exactly the kind of evidence I need when my CEO asks why we can't just show him the GitHub Copilot productivity numbers. I'm saving that stat.

**The capacity-to-dollars math**: "If your AI investment frees 20% of engineering capacity... and you have 50 engineers, you've recovered $2–2.5M in annual capacity." This is the first concrete number in the article and it's useful as a framework. I can adapt it to my context (I have 14 engineers, not 50, and the math gets less impressive — but at least it's a model I can run).

**The CFO language framing**: "Cost savings. Revenue growth. Dollars." — Three words. This is the kind of distillation I can hand to my data analyst and say "this is what we're trying to build toward."

**The acknowledgment that attribution is hard**: "Attribution is genuinely hard. Engineering rarely ships in isolation; revenue rarely moves from a single feature. Acknowledge this in your reporting — and then show the trend line anyway." This is honest and useful. It gives me permission to start imperfect rather than waiting for a complete system.

### What Didn't Work

**The IBM $4.5 billion example**: This is the wrong scale entirely.
> "IBM achieved $4.5 billion in annual run-rate savings from AI-driven productivity transformation — a number substantial enough to drive $12.7 billion in free cash flow in 2024."

IBM has 250,000+ employees and a decades-long AI transformation program. I have twelve engineers and an ERP that's been causing problems since 2019. Citing this number without a bridge to my reality doesn't motivate me — it makes me feel like the article isn't for me. When I read this, my actual thought was: "OK, what does that mean for a company my size?" The article never answers that.

**The "50 engineers" assumption in the math**: The capacity calculation assumes 50 engineers. I have fourteen, eight of whom are in support mode. I had to mentally re-run the math myself to figure out what this looks like for my situation — and when I did, the number was much less impressive. The article should have anticipated this and run the math for the 15-person org. That's closer to my reality.

**The "Go look at your backlog right now" section**: This is written for someone who owns the engineering process directly — a VP of Engineering who reviews tickets and shapes the backlog. I'm a CTO. My engineers handle the backlog. My job is to change the system, not inspect individual tickets. The voice here shifts to a practitioner audience I'm not fully part of.

**The AI requirements validation layer**: The idea that every user story passes through an AI layer to validate business justification fields is interesting — but it lands as aspirational rather than actionable for where I am. I haven't yet figured out how to instrument our ERP data for analytics. Building an AI validation layer for user stories feels like step 12 and I'm still on step 2.

### What Confused Me

**"This is not additional bureaucracy"**: The article claims that requiring every user story to include a business justification field, a predicted metric impact, and a measurement owner is "not additional bureaucracy." That claim will ring hollow to anyone who has tried to change how engineers write stories. My team will see this as overhead. The article asserts it isn't — but doesn't explain how to make that transition without real resistance. I needed more here.

**The audience seems to shift**: The article opens by speaking to me (CTO reporting to a board). Then sections like "Go look at your backlog" and the story-writing framework read like they're speaking to a VP of Engineering or engineering team lead. Then "Your other metrics remain valid. They just don't belong in that room" sounds like it's back to addressing me. The voice oscillates and I found myself losing track of who was supposed to act on what.

---

## Key Concerns & Objections

### Concerns Raised

1. **This is a large-org framework**: The entire measurement architecture described — feature flags, product analytics, A/B testing infrastructure, a dollar-denominated dashboard, automated attribution chains — assumes a modern software company with a dedicated product team, a product analytics stack, and an engineering org that ships software to customers. My company sells specialty industrial parts. We have a website and an ERP. What does "revenue generated by a feature" even mean in my context? The article never addresses this gap.

   - Current treatment: Not addressed. The article assumes SaaS or digital-product context throughout.
   - Recommendation: Even a brief acknowledgment that the framework applies differently in non-SaaS contexts — and a simpler starting point for those environments — would dramatically expand relevance.

2. **The 5% to 50% Gartner stat creates a false sense of timing**: "Gartner estimates that only 5% of organizations currently use Software Engineering Intelligence Platforms capable of tracking metrics at this level — though that number is predicted to reach 50% by 2027." This will be read by my PE sponsor as "we need to be in that 50% by 2027." That creates pressure without a path. The article says "start manual" but doesn't give enough of a roadmap for what manual looks like.

3. **I don't control the story-writing process**: The article's core prescription is to change how user stories are written — requiring business justification and measurement plans. In my organization, I can mandate this. But getting the business stakeholders (operations, sales) to participate in defining the measurement plan is a change management problem, not a technology problem. The article glosses over this.

### Unanswered Questions

- **Where do I actually start?** The "Measurement Chain" section gives me a sequence, but what's the minimum viable first step for a company with no product analytics infrastructure? "Start manual" — but manual what, exactly?
- **How do I handle software that serves internal operations, not external customers?** The dollar-metric framework assumes I can attribute engineering output to revenue or cost. For internal tools and ERP customizations, the causal chain is long and murky. What does the framework look like when I can't use A/B testing or feature flags?
- **What does the dollar-denominated dashboard actually look like?** Three columns are described. But how do I populate the revenue-generated column when my engineering team builds internal tools, not customer-facing features?
- **How long does it take to build this system?** I have a board meeting in six weeks. What can I show by then? What's the 90-day version of this?

---

## Missing Elements

**What I Expected to See**:
- A starter kit: What's the first dashboard I can build with the data I probably already have? Even rough. Something I can put in front of my board in 30–60 days.
- A non-SaaS translation: How does this framework apply to a distributor, a manufacturer, or a B2B services firm where "features" aren't the primary value delivery mechanism?
- A realistic timeline: Not the 2027 Gartner prediction — a realistic 90-day, 6-month, 12-month roadmap for building this measurement capability from scratch.
- Something I can share with my CEO: The action item at the end is good, but I need language to take upward. "We're shifting our reporting from engineer-units to dollar-units" — how do I explain this to a CEO who currently loves the story point dashboard he gets each Monday?

**What Would Make This More Valuable to Me**:
- One mid-market example: Not IBM. A $150M distributor, a $200M manufacturer, a B2B services firm. What does dollar-denominated reporting look like for them? Even one real example at the right scale would make this article three times more useful.
- The change management piece: How do you get engineers — who are proud of velocity metrics because they've been told those matter — to shift to outcome reporting without it feeling like surveillance?

---

## Assumptions I Don't Share

The author seems to assume:

1. **That my engineering team ships software products with customer-facing features**: The entire measurement framework — A/B testing, product analytics, behavioral tracking, feature attribution — assumes a software company. I run IT for a specialty distributor. My "engineering" is mostly ERP customization, data integration work, and vendor-managed software. The dollar attribution framework described requires a product context I don't have.
   - Reality for this persona: Most of my engineering work is internal — workflow automation, ERP configuration, integration middleware. "Revenue generated by a feature" is almost never a clean attribution story.
   - Impact: A significant portion of the prescriptive section doesn't apply without heavy translation.

2. **That my team has enough capacity to build a measurement architecture**: The article prescribes feature flags, product analytics, A/B testing infrastructure, dollar dashboards, and AI-assisted story validation. Building all of this requires engineering capacity. I have two engineers who aren't committed to the ERP project. One of them is handling security work.
   - Reality for this persona: I can't build a measurement system right now without deprioritizing something else. The article doesn't acknowledge this trade-off.

3. **That the primary audience for this change is the CFO**: The article repeatedly frames the problem as "what does your CFO need to see?" My PE sponsor is actually the more relevant audience — and PE sponsors have different questions than CFOs. They want to see value creation milestones, not quarterly ROI reports.

---

## Overall Assessment

**Would I Finish Reading?**: Yes.
**Why**: The topic is directly relevant to what I'm dealing with right now. The argument is clear and the evidence is strong. Even with the scale mismatch, there's enough I can use.

**What I'd Take Away**:
- The Faros paradox data — useful for explaining why activity metrics are broken.
- The capacity-to-dollars math — I'll adapt it for my team size and use it with my CEO.
- The three-column dashboard framework — I'll try to build a version of it even if my attribution is rough.
- The phrase "imperfect dollar estimate is more useful to a CFO than a precise velocity number" — this is the permission I needed.

**Would I Share This?**: Yes, selectively.
**With Whom**: My CEO — to set up the conversation about changing our reporting. Possibly the PE operating partner's technology advisor.
**Why**: The core argument is sound and the evidence is credible. I'd preface it with "this is written for software companies but the measurement principle applies to us."

**Impact on My Thinking**: It will push me to start building a dollar-denominated view of our engineering work, even if my attribution is imperfect. It won't change my immediate actions because I still don't have a starting point for a non-SaaS context — but it clarifies what direction to move in.

---

## Recommendations for This Audience

### Critical Changes

1. **Add a non-SaaS translation section**: Even two paragraphs. "If your engineering team builds internal tools rather than customer-facing software, here's how to adapt the framework: [cost-per-process before vs. after], [manual hours eliminated], [error rates reduced]." This is the missing bridge for the audience that most needs this article.

2. **Replace IBM with a mid-market example**: Find or construct a realistic example at the $100–300M company scale. An engineering team of 10–15. A 90-day measurement initiative. Rough numbers. Real context. IBM tells me that measurement matters at enterprise scale. I already knew that. Tell me what it looks like for a company my size.

3. **Give me a 90-day roadmap, not a 2027 prediction**: The Gartner stat about 50% adoption by 2027 is interesting strategically but it doesn't help me decide what to do before my next board meeting. What's the 90-day version? What does "start manual" actually mean — specifically?

### Helpful Improvements

- Tighten the "go look at your backlog" section or redirect it to CTOs explicitly: frame it as "direct your VP of Engineering to..." rather than speaking as if I'm the one reviewing tickets.
- Add a "what to say to your CEO" paragraph: A few sentences of upward communication framing. This article is excellent at explaining the problem; it should also give me language to carry into my next leadership team meeting.
- Acknowledge the change management dimension: Changing how stories are written requires business stakeholders to participate differently. One sentence acknowledging this and pointing toward organizational prerequisites would make the prescription feel more honest.

### Optional Enhancements

- A comparison of available tooling at different price points for the dollar-denominated dashboard — even a brief one — would help me evaluate what's realistic without hiring a consultant.
- A sidebar on how this argument plays differently with PE sponsors vs. CFOs vs. CEOs. The frame shifts depending on the audience and a note acknowledging that would be appreciated.

---

## Persona Verdict

**Rating**: 3.5/5 for this audience

**One-Sentence Summary**: The argument is exactly right and the evidence is credible, but the prescriptive framework was written for a software company, not for the mid-market IT leader who most needs to hear it.

**Quote**: "I agree with every word of this. Now tell me what it looks like for a company that runs on an ERP and doesn't ship features to customers — because that's 60% of the mid-market and we all have the same board problem you just described."
