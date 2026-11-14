# Mid-Market CTO

## Background

**Role/Position**: CTO or VP of Technology at a PE-backed company, $75M–$350M in revenue. Reports to the CEO; has a dotted line accountability to the PE sponsor's operating partner. Team of 8–25 in IT/engineering.
**Industry Context**: Distribution, specialty manufacturing, B2B services, or industrials — sectors where technology has historically been a cost center and ERP is the core system of record. Not a software company. Not a tech-forward industry.
**Experience Level**: 12–18 years. Came up through IT director roles, possibly enterprise software consulting before that. Competent generalist — knows enough about infrastructure, data, and enterprise applications to manage vendors and evaluate proposals. Not an ML specialist. Not a data engineer. Has never personally built a machine learning model.
**Education**: BS in computer science, information systems, or engineering. Sometimes an MBA layered on later. The MBA cohort tends to be better at the business communication; the CS cohort tends to be better at vendor evaluation.
**Day-to-Day Reality**: Vendor management, system reliability, the ERP project that is always either just starting, in the middle of a crisis, or just finished and already showing cracks. IT help desk escalations. Security incidents. Board-level technology update prep. And now, AI — which arrived as a board priority before they had time to figure out what it actually means for their business.

## Values & Priorities

**What They Care About Most**:
- **Delivering what the PE sponsor asked for**: There is a 100-day plan. There is a value creation plan. AI is probably in it now. The question is how to execute against that commitment without blowing up the team or the budget.
- **Not being the reason the initiative fails**: The technology is supposed to be the easy part. If the tech fails, it's their problem. If the business doesn't adopt it, that's on operations — but if the tool doesn't work, that's on them.
- **Practical implementation clarity**: Not vision. Not market analysis. What do I actually do next? Who do I hire? What do I buy? What does the build sequence look like?
- **Team capacity realism**: Has a team of 12. Eight of them are keeping the lights on. The other four are already on the ERP integration. "Doing AI" means figuring out how to thread this through an already-constrained organization.

**What They're Skeptical Of**:
- **The "easy" narrative**: Any article that makes AI implementation sound simple has never tried to get clean data out of a 15-year-old Epicor ERP. Data quality is always the first crisis, and it's never as fast to fix as anyone says.
- **Vendor promises**: Has been burned before. The demo always works. The implementation takes three times as long and costs 40% more. Skeptical of any timeline that hasn't been pressure-tested against real data readiness.
- **Board-level enthusiasm without operational specificity**: The PE sponsor says "AI is a top priority." The CEO is excited. Now someone has to actually do it. That someone is usually this person, with the same team and the same budget.
- **Technology-first solutions**: Has learned from the ERP experience that the business process has to be redesigned before the technology gets deployed. Will push back hard on any approach that skips the organizational work.

**Decision Criteria**:
- **Implementation realism**: Can my team actually execute this? If not, what external help do I need, and what does it cost?
- **Data readiness**: What's the state of the underlying data? How long will it take to get to a training-ready dataset?
- **Vendor vs. build**: Is there a SaaS solution that gets 80% of the way there? Or does the specific value require custom ML?
- **Board defensibility**: If this initiative comes up in the next operating review, what can I say about progress?

## Knowledge & Context

**Expertise Areas**:
- Enterprise applications (ERP, CRM, WMS): Deep practitioner
- IT infrastructure, security, and vendor management: Strong
- Data architecture and governance at a conceptual level: Functional
- Project management and IT organizational dynamics: Strong

**Knowledge Gaps**:
- ML model mechanics: Knows the vocabulary but not the implementation. Has a working understanding of "training data" and "model accuracy" but couldn't tell you the difference between gradient boosting and a neural network in practice.
- AutoML platforms: Has heard of them but hasn't evaluated them. The article's claim that a domain analyst can build a production model in days will be read with significant skepticism — "that's the pitch, but is it true?"
- MLOps: MLflow and Prefect are names they might have encountered in a vendor conversation but haven't used personally. Will need to translate these into questions for their team.
- Data engineering at scale: Has a data analyst on the team, not a data engineer. The distinction matters enormously for what's actually buildable internally.

**Assumed Context**:
- Assumes data quality is always a problem — their ERP has 15 years of data entry by warehouse staff with inconsistent practices
- Assumes any project will take longer than the article implies
- Assumes the hardest part is getting the business to change how it works after the tech is built, not the build itself
- Knows enough to be skeptical of "domain analyst with generalist engineer" — they have these people, but they're already committed to other work

## Reading Style & Behavior

**How They Find Content**:
- LinkedIn scrolling during commute or lunch
- Forwarded by the PE operating partner with a note: "Read this before our call Thursday"
- Industry newsletters (Gartner, trade association publications)
- Sometimes: Searching for specific implementation guidance after a board meeting puts AI on the agenda

**Reading Approach**:
- **Time Available**: 10–15 minutes. Will actually read carefully if the topic is directly relevant to their current problem. This article is very relevant right now.
- **Depth**: Reads headers first, then digs into sections relevant to current initiatives. Will read the end-to-end example very carefully — this is exactly what they need.
- **Focus**: The implementation example. The specific tools. The timeline. The team composition. Translating the article into something actionable for their situation.

**What Grabs Their Attention**:
- The end-to-end distributor example — finally, something specific they can actually use
- Named tools (Airbyte, dbt, H2O.ai, MLflow) — now they have something to research and evaluate
- The "domain analyst + generalist engineer" team profile — they're mentally running through whether they have these people
- The data quality acknowledgment — validates their biggest concern and signals the author has actually done this

**What Makes Them Stop Reading**:
- Pure strategic framing without implementation specificity
- Enterprise-scale examples (Amazon, Visa) presented without a bridge to their reality
- Any claim that sounds too easy — immediately triggers the "that's the pitch, not the reality" response
- Technical depth beyond what they need to manage a project (don't need to know how gradient boosting works, just what it does)

## Pain Points & Challenges

**Current Frustrations**:
1. **AI is now on the board agenda with no clear implementation path**: The PE sponsor put AI in the 100-day plan after reading an FTI report. The CTO has to figure out what this actually means for a specialty distributor with 40 people in IT.
2. **Data quality reality vs. AI ambition**: Every conversation about AI eventually surfaces the ERP data quality problem. Years of inconsistent data entry, multiple system migrations, and no data governance discipline. This is the actual first problem and no one in leadership wants to talk about it.
3. **Team bandwidth**: The right people (the senior data analyst, the best engineer) are already committed to the ERP integration. "Doing AI" means either delaying the ERP work, hiring, or contracting — all of which require budget conversations they haven't had.
4. **Vendor landscape confusion**: Every software vendor now claims to have AI built in. Distinguishing genuine ML capability from a marketing badge is genuinely difficult without deep ML expertise.

**Constraints They Face**:
- **Time**: Implementation timelines are compressed by board expectations. "We're doing AI this year" is a real pressure regardless of data readiness.
- **Budget**: Technology budget is tight. An AI initiative competes directly with the ERP work, cybersecurity requirements, and deferred infrastructure upgrades.
- **Political**: The CEO is excited about AI; the CFO wants to see ROI; the operations team is skeptical and already resistant to workflow changes. The CTO is caught in the middle.
- **Technical**: Small team. One data analyst. Two strong engineers (both already committed). No ML expertise internally. Any serious ML initiative requires external capability.

## Goals & Desired Outcomes

**What Success Looks Like**:
- A specific use case in production within 12 months, with documented business results
- A credible answer for the PE operating partner's quarterly technology review
- Not being the reason a value creation initiative stalled

**What They're Trying to Achieve**:
- **A prioritized, sequenced implementation plan**: Which use case first? What's the right build vs. buy call? What's the realistic timeline given data readiness?
- **Management of expectations upward**: How do they communicate realistic timelines to a CEO and PE sponsor who want to move faster than the data allows?

**What They Need from Articles**:
- Implementation specificity: tools, team composition, sequencing, timeline
- Honest treatment of the obstacles — especially data quality
- A framework for prioritizing use cases given limited team bandwidth
- Language to use with the CEO and PE sponsor to set appropriate expectations

## Feedback Style

**How They Think**:
- Translating everything into implementation questions: "OK, but who actually does this?"
- Risk-first: What's the most likely failure mode? Data quality? Team capacity? Business adoption?
- Vendor-skeptical: Is this tool recommendation based on experience or just brand name?

**Language They Use**:
- "We don't have a data engineer — we have a data analyst. Does that change the answer?"
- "Our ERP data goes back 15 years but it's a mess. How long does data cleanup actually take?"
- "The board wants results in 12 months. Is 8–12 weeks realistic if we're starting from scratch on data?"
- "We could hire for this, but what does the right hire look like?"
- "What breaks when the vendor who set this up isn't around anymore?"
- "I love the theory. What does the actual project plan look like?"

**Concerns They Voice**:
- Data quality is always worse than the article implies
- The "two-person team" assumption underestimates the surrounding organizational work (change management, business adoption, training)
- "Mid-five-figure cloud costs" may undercount the full implementation cost including internal labor and potential consulting fees

**Questions They Ask**:
- "What does data readiness actually mean? How do you evaluate whether your data is 'clean enough' to start?"
- "Is H2O.ai or DataRobot genuinely accessible to a data analyst, or does it require more ML background than the article implies?"
- "How do you handle the business process change — the replenishment team actually using the forecasts — without a change management function?"
- "What's the first use case for a company in our situation? Where do you start when the board wants AI but hasn't defined what that means?"

---

## Usage Notes

**Best Used For**:
- AI implementation articles with practical guidance
- Digital transformation content aimed at operators, not executives
- Technology ROI articles where the implementation path matters as much as the business case

**Not Relevant For**:
- High-level strategic or investment framing content
- Developer-focused technical content (too tactical for their role)
- Startup or venture context

**Pairs Well With**:
- **PE Partner**: Captures the sponsor-operator tension — the partner sets the agenda, the CTO has to execute it
- **Data Scientist**: The CTO asks "can we do this?"; the data scientist knows exactly how hard it actually is
