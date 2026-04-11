# The Hours Are Over: How to Sell and Deliver Outcomes in an AI-Accelerated World

*Final Draft | 2026-04-01 | ~3,710 words*

Your team delivers a 12-week project in 6. Do you celebrate — or quietly panic about the revenue shortfall? A client asks you to prove the ROI of their investment. You open a timesheet. Is that what they're looking for? A competitor just proposed a gain-sharing model on the same opportunity you pitched as T&M. Who wins the deal?

These aren't hypothetical provocations. They're the real conversations happening in client meetings right now — and most of us aren't ready for them.

The time-and-materials model has served this industry well for decades. It is familiar, simple to administer, and requires almost no courage to sell. But AI has exposed its structural flaw: **T&M rewards inefficiency and punishes the teams that actually invest in getting better.** The faster our engineers become — and AI is making them meaningfully faster — the less revenue we earn under the model we've built our business around. That is a perverse incentive, and every account manager and delivery manager at EPAM needs to understand it clearly.

This is a practical guide to doing something about it.

---

## When Efficiency Becomes Your Enemy

Here is the math in its simplest form. A delivery team takes on a 12-week engagement at $150,000. Midway through, they deploy AI-assisted development tooling. They finish in 6 weeks. Under T&M, they've earned $75,000 for delivering identical scope. The client got what they wanted. The team got half the budget.

That is the structural problem AI has introduced into every project-scoped T&M contract in our portfolio.

The billable hour was always flawed — it discouraged the very efficiency clients claimed to want. A consultant who takes 10 hours bills more than one who takes 2 for the same output. When AI can compress delivery cycles by 60–80% on specific workstreams, that tolerance evaporates.

The perverse incentive is clearest in project-scoped engagements. But it doesn't stop there. In staff augmentation and ongoing platform work, the revenue math looks safer — a faster team adds more features, hours stay flat, revenue appears stable. The problem is that clients have noticed. TCS, Infosys, and Wipro are facing selective renegotiations as enterprise clients use AI-driven efficiency arguments to demand lower rates or fewer FTEs. The risk isn't a single project billing short — it is clients systematically reducing headcount on ongoing contracts as AI makes each FTE more productive. The exposure is identical; the timeline is just slower.

The *Wall Street Journal* noted in December 2025 that AI is rendering the traditional billable hour obsolete across professional services — not just in law and consulting, but in IT engineering delivery. CIOs entered 2026 with "budget exhaustion" after years of AI pilots with limited results. They are no longer willing to fund open-ended T&M spend without ROI accountability attached.

EPAM generates 70–80% of its revenue through T&M billing. That baseline is not defensible long term. Our 2026 strategic imperative is converting AI-related demand into higher-margin engagements — which is not possible at scale under an hourly billing model.

The answer is not to panic. The answer is to learn a different commercial language.

---

## Output, Outcome, and Fixed-Price Are Not the Same Thing

Most practitioners conflate three distinct models. That confusion produces bad contracts.

**Fixed-price** is familiar: defined scope, defined price, vendor absorbs overrun risk. The trap is well-known — lowball to win, then fight on change orders when scope drifts. Fixed-price is not an evolution of T&M; it's a different way to bill for inputs.

**Output-based** ties payment to specific deliverables — not hours worked, not business results achieved. Payment per artifact: per API deployed, per regression suite maintained, per microservice shipped. As Infosys BPM frames it: "charging based on number of tickets fixed rather than hours invested." The vendor absorbs production risk; the client still absorbs whether the outputs actually deliver value.

**Outcome-based** goes further. Payment is tied to measurable business results the client achieves because of the work: reduced application downtime, cost savings from process automation, a revenue-linked fee on a commerce platform that converts better. The vendor accepts some share of business risk — not just delivery risk.

| | Output-Based | Outcome-Based |
|---|---|---|
| **Unit of value** | Deliverable produced | Business result achieved |
| **Example** | Data pipeline deployed | 15% reduction in customer churn |
| **Vendor controls** | Directly | Partially |
| **Measurement** | Relatively simple | Requires instrumentation |

Consider two ways to scope the same engagement. *Output*: Build a real-time personalization engine; payment upon deployment. *Outcome*: Reduce customer churn by 15% through a personalization engine; base fee upon deployment, plus gain-sharing for each point of churn reduction below baseline.

The personalization engine in scenario two could work perfectly — and churn might still not drop if the client's pricing is uncompetitive or a market shock intervenes. That is the vendor absorbing business risk beyond their control. It is why most experienced practitioners recommend starting with output-based models and graduating to outcome-based as trust and measurement infrastructure develop.

**A client is ready for outcome-based contracting when they can demonstrate:**

1. A specific, measurable baseline — current churn rate, deployment frequency, processing cost per transaction — not an aspirational target.
2. A data system that already tracks that baseline consistently, without requiring the vendor to build the instrumentation first.
3. An agreed attribution methodology — how will both parties determine that the outcome shifted because of the work, not external factors?
4. A named business owner with authority over the decisions the outcome depends on.
5. An established working relationship that has given both parties confidence in each other's execution and good faith.

If a client cannot meet the first three criteria, output-based is the right model. Use the engagement to build instrumentation and trust. Graduate when the foundation is in place.

Do not use output-based and outcome-based interchangeably. They require different contracts, different governance, and different risk models.

---

## The Measurement Problem: When Units Aren't Discrete

Here is the question every AM and DM runs into the moment they try to move off T&M: *How do you actually measure what you're selling?*

For managed services and high-volume BPO work, the unit is obvious — tickets processed, uptime percentage, claims handled. The problem is that most of EPAM's delivery work isn't that clean. It's product engineering, platform builds, data infrastructure, modernization programs — work where the unit of delivery resists easy discretization.

The default answer in software delivery has been story points. It is the wrong answer. We need to name that honestly before proposing anything to a client.

### Story Points Fail as a Commercial Unit

Story points were designed as an internal planning tool for agile teams. They are team-relative by design — a 5-point story for one team may be a 2 for another, depending on experience, codebase familiarity, and tooling. That relativity is a feature for internal velocity tracking. It is a defect in a commercial contract.

Four problems make story points commercially unworkable:

1. **They measure effort, not value.** A 1-point configuration change that unblocks a $5M revenue stream is not commercially equivalent to an 8-point feature nobody uses.
2. **They're team-relative.** A "5" in one team is a "3" in another. There is no exchange rate. Clients asking "how many story points per sprint will we get?" are asking a question with no stable, cross-contract answer.
3. **They're gameable.** Teams under commercial pressure inflate estimates to demonstrate velocity. Clients have noticed.
4. **They don't translate to business value.** No CFO has ever reported to a board that their platform initiative delivered 847 story points.

If you propose a commercial engagement structured around story point throughput, you're building on sand.

### Practical Alternatives for Non-Discrete Work

There is no perfect commercial unit for complex software delivery. But precise imperfect units beat vague perfect ones — and several approaches are significantly better than hours or points.

**Functional decomposition.** Break the engagement into functional capabilities delivered — not hours, not points, but working software with acceptance criteria. "Authentication module complete and in production." "Payment integration live and processing transactions." Each capability either works or it doesn't. Payment triggers on acceptance. This approach forces the upfront definition work that most engagements skip — and that definition work is where scope risk lives. Investing three days defining acceptance criteria buys weeks of scope argument prevention.

**Throughput metrics as capacity proxies.** For subscription and retainer structures, DORA metrics — deployment frequency, lead time for changes, change failure rate, mean time to restore — provide a team-level picture of delivery capacity that is objective, automatable, and impossible to game without changing actual delivery behavior. A retainer priced around a defined DORA profile ties commercial value to real engineering health, not hour counts.

**Value stream milestones.** Define value milestones up front with the client: "API layer enabling X client integration," "data pipeline processing Y transaction volume," "self-service BI layer live and adopted by Z teams." Tie payment to milestone completion, not time spent. Each milestone should represent a genuine business capability the client can act on — not an arbitrary technical checkpoint.

**Acceptance-criteria-based delivery.** Each unit of output is defined by what it must do to be accepted, not how long it took to build. Payment triggers on acceptance. The acceptance criteria become the contract. This shifts the commercial conversation from "how much effort did you spend?" to "does this work as agreed?" — a question clients can evaluate and delivery teams can objectively meet.

**Outcome proxies when attribution is hard.** Sometimes the real outcome — revenue growth, customer retention, cost reduction — is too distal or too influenced by external factors to tie directly to a contract. The answer is not to abandon outcome thinking; it's to agree on leading indicators. "Feature adoption rate exceeds 40% within 30 days of launch." "API call volume reaches X by week eight post-deployment." These proxies are measurable, attributable, and far more meaningful than hours worked.

### The Investment in Clarity

Every one of these approaches requires upfront definition work that T&M contracts skip. Under T&M, work starts Monday and scope gets clarified as you go. Under functional decomposition or acceptance-criteria-based delivery, someone defines "done" before the first line of code is written.

That investment is not overhead. It is scope risk management. Engagements that blow up on T&M — running three times the original estimate, ending in disputes — almost always trace back to insufficient definition at the start. When a client pushes back on the definition work, the honest response is: "We'll spend that time eventually. Either at the front end defining what success looks like, or at the back end arguing about whether we got there." Most clients invest in the front end.

AMs and DMs who walk into a proposal with functional decomposition, DORA-anchored retainers, and acceptance-criteria-based delivery in their toolkit are having a fundamentally different conversation than those who shrug and say "we work in story points."

---

## Five Ways to Price a Project Without Billing the Hour

There is no single outcome-based contract structure. Five proven mechanisms exist — and the right choice depends on engagement type, measurement maturity, and how much delivery risk you're prepared to absorb.

**Milestone payments** are the most accessible entry point. Break the project into phases; release payments upon verification of deliverables at each checkpoint. This aligns payment with delivery risk and eliminates the "paying for effort that produces nothing" problem that plagues T&M in discovery-heavy projects. Output-based, not outcome-based — but a meaningful improvement over hourly billing.

> *In practice:* A global financial services firm migrates a legacy data warehouse to a cloud-native platform. EPAM structures payment in four tranches: 20% on signed architecture ($180K), 30% on decommissioned warehouse with validated data ($270K), 30% on BI layer accepted by three pilot business units ($270K), 20% on 90-day SLA achieved ($180K). The client pays for verified progress. EPAM absorbs delivery risk per phase; the client absorbs scope changes through formal change orders only.

**Gain-sharing** is the purest outcome-based structure. The vendor receives a base fee plus a percentage of quantified savings or revenue gains attributable to their work. Typical splits run 20–40% of documented gains for 12–24 months post-deployment. The critical requirement: a contractually agreed baseline measurement methodology before work begins. Without it, attribution disputes are inevitable.

> *In practice:* A mid-market e-commerce retailer's recommendation-driven revenue is $4.2M annually against a $6M industry benchmark for their traffic volume. EPAM builds a new recommendation engine on a reduced retainer of $180K (versus $280K T&M), earning 20% of documented revenue lift above the $4.2M baseline for 12 months post-launch. Attribution is measured via recommendation-influenced transactions in the client's existing analytics stack, with a contractual "external event" clause. If the engine drives $2M in incremental revenue, EPAM earns $400K in gain-sharing — total engagement value of $580K versus $280K at T&M.

**Subscription retainer** (Capacity-as-a-Service) works well for long-running platform teams and continuous product development. A fixed monthly fee for a defined delivery capability — squad composition, throughput SLAs, quality metrics — with flexible scope within the retainer boundary. No per-hour policing. No change order theater. Predictable cash flow for the vendor; flexible scope for the client.

> *In practice:* A Series C SaaS company engages EPAM at $95K/month: four senior engineers, one staff engineer as technical lead, AI-assisted development tooling. The team operates against the client's product roadmap with a quarterly re-scoping right — the client reprioritizes within the retainer but cannot expand team size mid-quarter. Throughput is tracked via DORA metrics against agreed baselines; sustained underperformance triggers a structured remediation window before any contract adjustment.

**SLA-linked pricing** is the natural model for managed services and operations. Base fee tied to availability, performance, or quality metrics. Deductions for breach; bonuses for sustained outperformance.

> *In practice:* A healthcare technology company engages EPAM for platform operations on a patient-facing HIPAA application. Base fee: $65K/month. Targets: 99.9% uptime, P1 response under 15 minutes, bi-weekly deployments. Penalties: 2% fee reduction per 0.1% below the uptime SLA; $2,500 deduction per P1 breach above 30 minutes. Bonus: 5% quarterly bonus ($9,750) for sustaining 99.95%+ uptime and monthly deployment frequency over six consecutive months. Meaningful but bounded performance risk — with real upside for genuine excellence.

**Per-unit output pricing** works for high-volume, repeatable workstreams where outputs are discrete and automatable: per microservice deployed, per automated test suite maintained, per claim processed. AI automation is most valuable here — compressed per-unit production cost becomes margin. Worth noting: per-unit pricing is most mature at large BPO and managed services firms. For EPAM, it is an aspirational direction in high-volume managed services and AI operations, not a default for project delivery.

The hybrid structure — T&M-equivalent base covering delivery costs, with outcome-linked bonuses layered on top — is the pragmatic on-ramp for most existing relationships. It protects cash flow, limits risk during trust-building, and introduces outcome accountability without abandoning a commercial model clients already know. Wipro is direct: "Most contracts now comprise hybrid pricing structures rather than 100% outcome-based pricing." Start there. Graduate as measurement infrastructure matures.

> *In practice:* A regional bank modernizes a core loan origination system. T&M floor: $420K over 18 months — covers delivery costs with a modest margin, protects cash flow. Outcome bonus: 15% of contract value ($63K) if the modernized system hits targets within 90 days of go-live — transaction processing under 2 seconds at peak load, zero P1 incidents, clean cutover with no data integrity exceptions. Total upside: $483K. Client's downside: market rates for delivered work, no clawbacks. EPAM's downside: standard rates.

**Choosing the right structure.** Three factors drive the decision. *Measurement maturity*: if the client can state and track a baseline, gain-sharing or SLA-linked are viable; if not, start with milestone or subscription. *Relationship stage*: new clients belong in milestone structures; established accounts with a delivery track record are candidates for gain-sharing. *Delivery confidence*: outcome-based structures require high predictability; shifting scope calls for T&M or a subscription retainer. Match the mechanism to what the engagement actually is — not to what sounds most sophisticated.

---

## The Staff Augmentation Problem: Evolving the Model That Pays Most of Our Bills

Everything above assumes a project-shaped engagement — defined scope, defined deliverable, defined end state. Most of EPAM's revenue doesn't look like that. It looks like an AM managing 20 engineers embedded across three client teams, billed individually by rate card, with the client directing work.

Staff augmentation is the hardest model to evolve. And it is the one we most need to address.

The reason it's hard is structural: in pure augmentation, the client controls task assignment, prioritization, and direction. The vendor provides capacity; the client provides intent. That arrangement makes it nearly impossible to commit to outputs, let alone outcomes. You cannot accept delivery risk on work you don't control. You cannot share in business results when the client can redirect your team to a different priority at any time.

But "impossible" and "not yet structured correctly" are different things.

### The Augmentation-to-Ownership Spectrum

The path from pure augmentation to something more valuable runs through a single prerequisite: **EPAM must own a defined domain, not just provide bodies within someone else's domain.** The commercial model cannot evolve until the operating model does.

Consider the spectrum:

**Level 1 — Pure augmentation.** Individual contributors embedded in client teams, client-directed, billed by rate. EPAM's accountability: show up and perform. Revenue risk: client reduces headcount whenever AI productivity improves or budget tightens.

**Level 2 — Embedded squad.** A cohesive EPAM team within the client org — tech lead, engineers, QA — operating as a unit rather than a collection of individuals. Still client-directed on priorities, but with internal ownership of how the work gets done. Commercial improvement: the team is harder to reduce piecemeal; the conversation shifts from "we'll cut two developers" to "we'll descope a capability." This is a retention model, not yet a value model.

**Level 3 — Managed capability.** EPAM takes explicit ownership of a defined domain: "We own the data platform team," "We run QA end-to-end," "We are accountable for the CI/CD pipeline." The client sets the outcomes for that domain; EPAM decides how to staff and deliver them. This is the inflection point — the move from capacity to accountability. The commercial model can now attach SLAs, throughput commitments, and quality metrics to the engagement. Per-unit pricing becomes viable. DORA-anchored retainers become credible.

**Level 4 — Team-as-a-Service.** A subscription retainer for a defined capability, scoped against the client's roadmap, with throughput and quality SLAs. The client buys a capability, not headcount. EPAM manages internally — staffing decisions, tooling, delivery approach — and is accountable for outputs. Rate card billing disappears. Quarterly re-scoping replaces open-ended expansion. The engagement becomes a product.

**Level 5 — Outcome-linked capacity.** A retainer base with gain-sharing on business metrics the team's domain directly influences. This requires Level 3 at minimum — you cannot tie a team's commercial terms to business outcomes the client's other teams also influence. But for a team that owns a well-instrumented domain with clear attribution, it is achievable.

Most EPAM augmentation relationships sit at Level 1 or 2. The goal is not to jump immediately to Level 5. It is to move one level — and to do so deliberately, with a specific conversation, on a specific renewal or expansion.

### What's Actually in It for the Client

Before any of the above conversation happens, an AM needs to answer the harder question: why would a client who is comfortable with staff augmentation want to change?

They have control. They have flexibility. And they have the ability to squeeze us on rates whenever they want. That is a commercially attractive position, and we should not pretend otherwise.

But "comfortable" and "well-served" are not the same thing. Staff augmentation solves the client's capacity problem. It does not solve their delivery problem, their outcome problem, or their cost-of-management problem. And it is worth naming each of those gaps explicitly, because different stakeholders feel them differently.

**The engineering manager** who runs staff aug relationships often doesn't want to change the model — they've built their job around it. They assign tasks, manage priorities, run standups, write tickets. The vendor provides execution; they provide direction. That feels like control. What it actually is: they're spending a significant portion of their working week managing vendor capacity rather than doing the higher-order work their organization needs from them. A managed capability model — where EPAM owns a domain and manages it internally — gives them back that time. The value proposition: "We manage ourselves. You set the outcomes and hold us accountable. You stop spending 30% of your week directing our backlog."

**The CTO or VP of Engineering** sees a different problem. Staff augmentation gives them no accountability structure. If a project delivers late, delivers wrong, or delivers poorly, the vendor's response is "we did what you asked." The client owns the delivery risk entirely. Every bad outcome traces back to a client decision — a priority call, a staffing choice, a scope judgment. Managed capability changes that equation. When EPAM owns a domain, EPAM is accountable for that domain performing. The client gets a counterparty who can be held responsible — which is what leaders actually want from a strategic vendor.

**The CFO** has a simpler concern: predictability and ROI. Staff augmentation creates variable costs that are hard to forecast and harder to justify. Every rate negotiation is a line-item fight. A subscription model with defined throughput and quality commitments gives finance what they actually want: a fixed monthly number tied to a defined capability, with measurable outputs that can be reported upward. The CFO doesn't care about headcount. They care about what the spend produces.

**The procurement team** that loves to squeeze rates is optimizing the wrong variable. Lowering the blended rate 10% on a staff aug engagement saves money on unit cost. It does nothing about the total cost of ownership — the engineering manager hours spent directing the work, the rework from insufficient accountability, the knowledge loss when engineers rotate out. A well-structured managed capability or subscription model often has a higher rate card and a lower total cost. That argument lands with CFOs and CTOs, not procurement. Find the right sponsor before making it.

There is also a more direct threat that is increasingly motivating client-side openness to this conversation: **AI is eroding the value of the control staff augmentation gives them.** What clients are controlling in a staff aug relationship is task assignment to human engineers. As AI takes over more of the execution layer — writing code, running tests, managing deployments — directing individual human capacity becomes less valuable. The clients who have started using AI tools internally are already sensing this. The scarce resource is shifting from people who can execute tasks to people who can own outcomes. A vendor who can commit to outcomes in a defined domain is increasingly more valuable than one who provides extra hands for a client's own team to direct.

The honest framing for the client conversation is not "you should give up control." It is: "The control staff augmentation gives you is control over activity. We're offering you something more valuable — accountability for outcomes. You define what success looks like. We own getting there. That's a different kind of control, and it's worth more."

Not every client is ready to hear that. The ones who are — who have already started asking "what are we actually getting for this spend?" — are the accounts to start with.

### How to Start the Conversation

The evolution conversation cannot happen during a staffing discussion. It has to happen at a level above the people managing headcount.

The right moment is the QBR, the strategic planning cycle, or a major program kick-off — any conversation where the client is thinking about capability, not just capacity. The question that opens the door: "We've been providing X engineers embedded across your teams. If we structured this differently — where EPAM took ownership of [specific domain] and was accountable for defined outcomes rather than individual hours — what would that look like for you?"

That question does two things. It surfaces whether the client sees EPAM as a strategic delivery partner or a staffing agency. And it forces both parties to name what EPAM actually owns — which is the prerequisite for everything that follows.

If the client's answer is "we just need bodies," that is important information. It means the relationship is not yet at the trust level required for ownership-based models — and the AM's job is to build that trust, not force the commercial evolution before it's earned.

If the client's answer is "we've been thinking about that too" — which is increasingly common as clients watch their own AI tooling compress headcount requirements — the conversation is already half over.

### The AM's Practical Checklist for Existing Augmentation Accounts

For each active staff augmentation engagement, ask:

1. **What does EPAM de facto own?** Even in pure augmentation, some teams have informally taken ownership of a domain. Name it explicitly — that's the foundation of a managed capability proposal.
2. **Is there a natural domain boundary?** Data platform, QA, DevOps, a specific product area. Something the client would recognize as "EPAM's domain" if you named it.
3. **Can that domain produce measurable outputs?** Deployment frequency, defect escape rate, data pipeline uptime, feature throughput. If the answer is yes, SLA-linked or subscription pricing is viable.
4. **Who on the client side would benefit from accountability clarity?** The engineering director who's tired of managing vendor headcount. The CTO who wants fewer vendors with deeper ownership. The CFO who wants predictable spend. Outcome-based evolution solves their problems — find them.
5. **Is the relationship at a trust level that supports a direct conversation?** If not, what needs to happen first?

The accounts where EPAM has been embedded longest, with the highest engineer counts, are the most valuable candidates for this evolution — and the most at risk if the conversation doesn't happen. Those relationships are where clients are most likely to use AI efficiency gains as justification for headcount reductions. The defensive move and the offensive move are the same: shift from headcount billing to capability ownership before the client does the math for you.

---

## McKinsey Moved. Accenture Moved. Wipro Is Moving. We Are Behind.

The transition is already underway at scale.

McKinsey now generates approximately **25% of its global fees from outcome-based contracts**. McKinsey told *Business Insider* directly: "AI is changing both what we offer clients and how we price our services." For the most prestigious hourly-billing firm in professional services to shift a quarter of its revenue to performance-linked structures is not a minor experiment. It is a strategic conviction.

Accenture booked **$1.5 billion in new GenAI contracts in Q3 FY2025 alone**, a significant portion with outcome-linked components. Part of Accenture's fee now ties directly to client KPIs — cost reduction, revenue uplift, service-level improvements. They are proposing this because it is winning deals.

Wipro has publicly stated a target of **50% of sales from risk-sharing models** — structures where they share delivery and business risk with clients seeking cost and outcome certainty.

McKinsey's own research finds that companies using value-based pricing achieve **profit margins 15% higher** than peers using traditional approaches. Outcome-based clients are better clients to have.

EPAM has the engineering excellence and the AI delivery tooling to compete on this ground. The question is whether our account managers know how to propose it.

---

## AI Isn't Just Compressing Delivery — It's Enabling the Model That Should Replace T&M

AI-assisted scoping tools analyze historical delivery data to produce more accurate estimates. Better estimation means lower proposal risk — the "unknown unknowns" that historically made outcome-based contracts feel dangerous become manageable. Delivery managers can commit to outcomes with confidence when empirical data, not intuition, backs their estimates.

AI automation compresses the cost of producing an output. Under T&M, that efficiency transfers to the client — they pay less because the team works fewer hours. Under output-based pricing, compressed delivery cost becomes margin.

Faster delivery cycles mean outcomes land earlier. A personalization engine that would have taken six months now deploys in ten weeks — the gain-sharing measurement period starts sooner and outcome exposure is time-compressed.

The measurement problem — historically the hardest obstacle to outcome-based contracts — is now directly addressable. EPAM AI/Run links tool and agent usage to delivery velocity, time-to-market gains, and task completion rates. It provides attribution models and executive dashboards that quantify outcomes. This is not a generic analytics platform; it is EPAM's proprietary answer to the question every client asks before signing an outcome-based contract: "How will we know?" When that question comes — and it will — AI/Run is the proof point that makes the commitment credible.

The firms that wait are not avoiding risk. They are ceding ground.

---

## The Objections Are Real. So Are the Mitigations.

**Attribution disputes.** Business outcomes are influenced by factors beyond the vendor's work. Mitigation: define a contractually agreed baseline measurement period before work begins; use control groups or A/B architectures where possible; include "external event" clauses that neutralize attribution if market conditions shift dramatically.

**Scope creep.** Clients accountable for outcomes sometimes treat vendor accountability as unlimited. Prevention: define input scope and outcome target as two separate contract schedules. Concrete example — Input scope: build and deploy three ML models to specification. Outcome target: 15% reduction in claim processing time. If the models are deployed to spec but the client hasn't updated their intake workflow, additional scope is a change order, not an obligation. The destination and the agreed road are not the same thing.

**Measurement infrastructure gaps.** Many clients lack the telemetry needed to measure contracted outcomes. Mitigation: build measurement infrastructure as a contractual deliverable — an output-based phase before the outcome-linked phase. EPAM AI/Run addresses this directly for engineering and AI delivery work.

**Client co-responsibility failures.** Outcomes require client behavior: data quality, stakeholder availability, process adoption. Mitigation: define explicit client obligations in the contract as shared accountability. Include condition precedents: outcome payments are only due if named client obligations were met.

**Cash flow timing.** Outcome payments arrive later than T&M invoices. Structure base fees at T&M-equivalent levels to cover costs and working margin; treat outcome bonuses as incremental upside. In a well-structured hybrid, the base fee is the floor and the bonus is the premium. The downside is "we earn market rates." The upside is "we earn meaningfully above market."

**Three counterarguments your clients and legal teams will raise.**

*"Our procurement team will never sign this."* They will flag it. That is their job. Non-standard contract structures require legal partnership — IP allocation, measurement audit rights, attribution methodology, outcome definition schedules. The answer is standard outcome-contract templates: pre-negotiated positions on common disputes so AMs aren't improvising in front of a procurement team. If those templates don't exist yet, that is the business case to bring to practice leadership.

*"What happens when EPAM misses the outcome target?"* In a well-structured hybrid, EPAM does not receive the outcome bonus — and the client has paid base fees at market rates for work delivered. No clawback. The vendor's downside is "we don't earn the premium." If base fees are at risk on an outcome miss, that is a structuring error, not a feature.

*"Is EPAM actually set up to manage outcome risk?"* The honest answer today is: partially. EPAM has the delivery tooling, engineering capability, and measurement infrastructure to support outcome commitments. What is still developing is internal governance: who owns outcome tracking on a gain-sharing contract, who decides when an external event clause triggers, how delivery managers report against outcome targets rather than burn rates. The internal operating model must match the external commercial model. That is the prerequisite, not a future state.

These are design problems, not reasons to retreat to T&M. Every one is solvable with careful contract architecture.

---

## The Language Shift: From "How Many People?" to "What Does Success Look Like?"

Everything above is context. This is what you do on your next client call.

The opening question that changes the conversation is not "How many engineers do you need?" It is: "What business problem are you actually trying to solve — and how will you know when it's solved?"

That question is a diagnostic. A client who can answer it precisely — "We need to reduce deployment lead time from three weeks to three days, and we'll know when change failure rate stays below 2%" — is ready to contract on outcomes. A client who responds with "We just need some developers" hasn't connected the work to the results. Your job is to help them make that connection before the contract is signed.

Move from inputs to baselines. Before proposing any outcome-linked structure, establish what the current state looks like. A client who cannot state their current churn rate cannot buy a churn-reduction engagement. Baseline definition is where the outcome conversation becomes real.

When proposing the structure, lead with the hybrid. "Here is our base engagement — milestone deliverables at market rates. Separately, here is a gain-sharing layer tied to the business outcomes we're both trying to achieve. If we hit the outcomes, we both win. If we don't, you've paid for the work at market rates." That framing is not risky. It is credible. It signals belief in our delivery capability and directly addresses the trust deficit clients carry after years of AI investments that didn't move the business.

One organizational reality deserves direct acknowledgment: EPAM AM KPIs reflect a mix of revenue and margin targets — which means outcome-based deals can score well if structured correctly. A hybrid engagement with a higher-margin outcome bonus improves your numbers, not just the client's. Frame the internal case that way: this is not a revenue sacrifice, it is a margin improvement with a base-fee floor. The accounts that demonstrate this model works are the ones that shift how leadership sets targets for the rest of the portfolio.

For delivery managers: a DM who manages to hours and timesheets internally will struggle to credibly propose outcome accountability externally. If you are already running outcome-oriented sprints — defining success in business result terms, using telemetry to demonstrate progress — you have the practice that makes outcome-based selling authentic. If you haven't, that is where to start.

This is not a pricing experiment. It is a structural realignment of how we define value.

---

## The Question Isn't Whether This Model Works — It's Whether You'll Master It First

The T&M model is not disappearing. For exploratory discovery, rapidly shifting requirements, and early-stage proof-of-concept work — hourly billing remains appropriate. The argument isn't that T&M is always wrong. It's that it should be the exception, not the default we reach for because it requires no courage to propose.

McKinsey has accepted this. Accenture is building its GenAI revenue on it. Wipro has declared a public target. EPAM's 2026 strategic priorities require converting AI delivery capability into higher-margin engagements — which cannot happen as long as our commercial model systematically gives away the value AI creates.

The account managers and delivery managers who learn this model — who can define baselines, structure outcome contracts, propose hybrid gain-sharing, and instrument delivery with AI/Run — will win the deals the rest of the market is still pitching at hourly rates. **43% of enterprise buyers actively prefer vendors willing to share risk through pricing** (PwC). They are waiting for someone to walk in and propose it credibly.

Ask yourself, on your next qualified opportunity: Have you asked the client what success looks like in business terms? Have you defined the baseline? Have you explored a milestone or gain-sharing structure alongside the T&M proposal?

If the answer is no to all three — you've left value on the table. Both yours, and theirs.

The hours are over. The question is what we replace them with.

---

## Publication Metadata
- **Word Count**: ~3,710
- **Reading Time**: ~15 minutes
- **Target Audience**: EPAM account managers and delivery managers
- **Key Topics**: outcome-based pricing, output-based contracts, T&M alternatives, gain-sharing, milestone payments, story points critique, functional decomposition, DORA metrics, acceptance-criteria-based delivery, AI-enabled delivery

## Source References
- *Wall Street Journal*, December 2025 — billable hour obsolescence in professional services
- *Business Insider*, November 2025 — McKinsey outcome-based fee confirmation
- Accenture Q3 FY2025 earnings — $1.5B GenAI contracts
- Wipro investor communications — 50% risk-sharing target
- McKinsey pricing research — 15% margin premium, value-based pricing
- PwC — 43% of enterprise buyers prefer risk-sharing vendors
- Infosys BPM — output-based pricing framing
- TCS/Wipro renegotiation data — augmentation T&M client pressure
