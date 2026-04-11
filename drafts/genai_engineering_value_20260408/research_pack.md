# Research Pack: GenAI Engineering Value — Translating AI Productivity to Dollar Outcomes
**Date**: 2026-04-08
**Researcher**: Researcher Agent
**Search Queries**: 22 queries conducted
**Sources**: 60+ sources evaluated

---

## Executive Summary

The central thesis — that traditional engineering metrics (story points, velocity, lines of code) are obsolete and must be replaced with dollar-denominated business outcomes — is strongly supported by current research. The case is built on three converging forces: (1) the AI productivity paradox, which proves that individual-level AI gains do not translate to company-level results, exposing the inadequacy of developer-centric metrics; (2) a mounting CFO/board crisis, in which 56–61% of executives report no measurable ROI from AI investment, precisely because engineering teams are reporting the wrong numbers; and (3) an emerging but still nascent framework layer from tools like Gartner's business value mapping, LinearB's DORA-to-revenue correlation, and Harness's velocity paradox research — all pointing toward business outcome metrics as the necessary destination.

The research also surfaced a critical complication: IBM's $4.5 billion productivity figure is the strongest concrete dollar-outcome anchor available, but it is a company-wide ops/consulting efficiency number, not a pure engineering-team metric. The Ghostwriter will need to handle this carefully. The clearest direct case studies linking engineering throughput to dollar outcomes are still sparse — this is a real gap in the literature and reinforces the article's argument (the measurement infrastructure to do this doesn't broadly exist yet, which is part of the problem the article should solve).

---

## Research Questions Addressed

1. **What concrete examples exist of companies successfully tying engineering/AI productivity gains to dollar outcomes?**
   IBM is the strongest anchor: $4.5B annual run-rate savings from AI-driven productivity, enabling $12.7B in free cash flow in 2024. GitHub Copilot ROI calculators show positive returns within one quarter for even 10–11% productivity gains at typical enterprise engineer cost. Most other case studies stop at activity metrics (PRs merged, cycle time reduced) and do not complete the translation to dollars — this gap is itself a key argument for the article.

2. **What frameworks exist for translating delivery metrics to business value in dollars?**
   Gartner's Software Engineering Business Value framework, DORA metrics (with LinearB's correlation showing elite DORA teams achieve 2.6x revenue growth and 2.2x higher profitability vs. low performers), Lean/Value Stream Mapping, and the emerging "AI P&L" concept from CFO-side research. No single framework fully automates the delivery-to-dollar translation.

3. **What is the current state of "business value metrics" in software engineering?**
   The field is actively debating the shift. Gartner, DORA/Google, Harness, LinearB, Jellyfish, Faros AI, and GetDX are all publishing research pointing away from activity metrics toward outcome metrics. The tooling is early — Gartner predicts only 5% of orgs use Software Engineering Intelligence Platforms today, rising to 50% by 2027. The shift is underway but not yet the mainstream standard.

4. **How are CTOs currently justifying AI investment to boards/CFOs? What's working?**
   Most aren't doing it well. 56% of CEOs report zero ROI from AI (Forbes/2026). 61% of CEOs face increasing board pressure for returns (Fortune, Dec 2025). The CFOs who are moving toward approval are shifting to broader business outcome metrics — cost savings, risk reduction, and revenue growth — rather than traditional IT ROI metrics. Salesforce research: 61% of CFOs say AI has changed how they evaluate ROI, moving beyond traditional metrics.

5. **What does research say about the limitations of story points and velocity in the AI era?**
   Forbes Tech Council (March 2026): "AI coding tools have made velocity practically free." Faros AI (2025, n=10,000+ developers): High AI adoption teams complete 21% more tasks and merge 98% more PRs, but PR review time increases 91% and there is no correlation between AI adoption and better outcomes at the company level. METR study (July 2025, RCT): Experienced developers using AI took 19% longer to complete tasks they estimated they'd complete 20% faster — a 39-percentage-point gap between perception and reality. Harness (2025): AI accelerates code creation but creates new bottlenecks downstream in testing, security, and deployment.

6. **Are there examples of AI-assisted measurement systems that auto-connect features to business outcomes?**
   This is the most nascent area. Thoughtworks ran a pilot using GenAI to create higher-quality user stories with shorter lead times. AI tools are being used to generate requirements, acceptance criteria, and test cases — but the automation of business outcome measurement (i.e., did this feature actually move revenue?) is largely still a manual/unsolved problem. The closest existing infrastructure is product analytics + A/B testing combined with feature flags — not yet AI-automated.

---

## Key Findings

### 1. The AI Productivity Paradox: Individual Gains, No Company Outcomes

#### Summary
Multiple independent studies converge on a finding that directly supports the article's thesis: AI tools improve individual developer output metrics, but these gains do not translate to organizational-level business outcomes. This is the core evidence that developer-centric metrics (story points, velocity, PRs) are measuring the wrong thing.

#### Evidence

- **Faros AI Productivity Paradox Report (2025, n=10,000+ developers)**
  - Source: Faros AI, 2025
  - Link: https://www.faros.ai/blog/ai-software-engineering
  - Credibility: High (primary data, large sample)
  - Key Findings:
    - Developers on high AI adoption teams complete 21% more tasks and merge 98% more pull requests
    - PR review time increases 91% — creating a critical downstream bottleneck
    - Bug rates increased 9% per developer
    - At the company level: no correlation between AI adoption and better outcomes
  - Note: This is the single most important piece of evidence for the article's core argument. More code shipped ≠ better business outcomes.

- **METR Study: Measuring AI Impact on Experienced Developers (July 2025, RCT)**
  - Source: METR.org, published July 10, 2025. Covered by Reuters, Ars Technica, InfoWorld.
  - Link: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - Credibility: Very High (randomized controlled trial, peer-reviewed level rigor)
  - Key Data: 16 experienced developers, 246 tasks, working in codebases they'd maintained for an average of 5 years
  - Finding: Developers using AI tools (including Cursor) took **19% longer** to complete tasks — despite estimating beforehand they'd be **20% faster**. A 39-percentage-point perception-reality gap.
  - Note: This is the sharpest rebuke to velocity-based metrics in the literature. If experienced developers on familiar code are slower with AI, velocity metrics become actively misleading.

- **Harness: The AI Velocity Paradox (2025)**
  - Source: Harness State of AI in Software Engineering, 2025
  - Link: https://www.harness.io/the-state-of-ai-in-software-engineering
  - Credibility: High (survey of engineering leaders and practitioners, n=500)
  - Finding: AI accelerates code creation but creates new bottlenecks downstream in testing, security, and deployment — shifting, not eliminating, the constraint
  - Quote: "The benefits gained in code creation are being throttled by processes further down the software delivery lifecycle"

- **SoftwareSeni / Index.dev synthesis (2025)**
  - Finding: "Developers believe they're working 24% faster with AI, but controlled studies show they're actually 19% slower. That's a 43 percentage point gap between perception and reality."
  - Note: Strong language for use as a pull quote in the article

- **NBER Study (cited Feb 2026 / Fortune)**
  - Source: National Bureau of Economic Research, cited in Fortune (Feb 2026)
  - Finding: 89% of managers saw no change in productivity (measured as sales volume per employee) over three years despite AI adoption rising from 61% to 71% of firms
  - Note: CEO/board-level framing — connects directly to the leadership frustration the article addresses

#### Analysis
This cluster of evidence does two things for the article: (1) it empirically destroys story points and velocity as reliable indicators of value in the AI era, and (2) it explains precisely why engineering leaders are losing credibility with their CFOs. If your velocity is up 40% but your business outcomes are unchanged, reporting velocity is actively misleading your leadership.

---

### 2. The CFO/Board ROI Crisis

#### Summary
Executive leadership is actively demanding dollar-denominated outcomes from AI investments and being denied them. This is the burning platform that makes the article urgent.

#### Evidence

- **Fortune (December 2025): 61% of CEOs face pressure**
  - Source: Fortune, December 2025 (cited by Search Engine Journal, Jan 2026)
  - Link: https://www.searchenginejournal.com/why-cfos-are-cutting-ai-budgets-and-the-3-metrics-that-save-them/564741/
  - Credibility: High (Fortune citation)
  - Finding: 61% of CEOs report increasing pressure from boards to show returns on AI investments

- **Forbes (January 2026): 56% of CEOs see zero ROI**
  - Source: Forbes, January 28, 2026
  - Link: https://www.forbes.com/sites/guneyyildiz/2026/01/28/56-of-ceos-see-zero-roi-from-ai-heres-what-the-12-who-profit-do-differently/
  - Credibility: High
  - Finding: 56% of CEOs report zero ROI from AI. The 12% who profit do so by embedding AI into redesigned processes rather than bolting it onto existing workflows.

- **MIT Study (cited WEF, 2025): 95% of enterprise AI initiatives fail**
  - Source: MIT study, cited by World Economic Forum, October 2025
  - Link: https://www.weforum.org/stories/2025/10/cost-productivity-gains-cfo-ai-investment/
  - Credibility: High
  - Note: Use with attribution caveat — the "95% fail" stat is widely cited but the definition of "fail" in the MIT study may be broad

- **CFO.com: Few CFOs see substantial ROI**
  - Source: CFO.com, 2025/2026
  - Link: https://www.cfo.com/news/so-far-few-cfos-see-substantial-roi-from-ai-spending-RPG/808249/
  - Finding: Most finance chiefs expect the AI value equation to change quickly, but currently report minimal tangible returns. "The message for 2026 is clear: CFOs who lead boldly, modernize intentionally, and build the cross-functional muscle for AI adoption will define the next decade."

- **Salesforce CFO Research (August 2025)**
  - Source: Salesforce, August 2025
  - Link: https://www.salesforce.com/news/stories/cfos-invest-ai-for-growth/
  - Credibility: High (primary research)
  - Key Finding: 61% of CFOs say AI agents have changed how they evaluate ROI — moving beyond traditional metrics toward broader business outcomes. Top CFO AI success metrics: cost savings, risk/compliance improvements, and revenue growth (tied #1).
  - Note: This is powerful framing for the article — CFOs are already demanding business outcome metrics, not just tech productivity metrics.

- **CFO Dive (2026): Targeted investments with clear ROI expectations**
  - Source: CFO Dive, 2026
  - Link: https://www.cfodive.com/news/top-5-ai-adoption-challenges-facing-cfos-in-2026/810277/
  - Quote: "CFOs in 2026 will need to direct AI budgets toward 'targeted investments with clear expectations for ROI and value to the business.'"

- **The CFO.io (January 2025): Productivity has overtaken profitability**
  - Source: The CFO.io, January 2025
  - Link: https://the-cfo.io/2025/01/17/the-roi-puzzle-of-ai-investments-in-2025/
  - Finding: Productivity has overtaken profitability as the primary ROI metric for AI initiatives in 2025 — but this is still not a dollar metric. CFOs are asking for productivity to show up as revenue or cost savings.

#### Analysis
The CFO layer is the audience's direct pain point. Engineering leaders are getting pressure from above to produce evidence their AI tools are paying off. The research confirms this pressure is real, widespread, and growing. The prescription — measuring in dollars — is exactly what the CFOs are already asking for.

---

### 3. The Limitations of Traditional Engineering Metrics

#### Summary
The research community has broadly converged on the conclusion that story points, velocity, and lines of code are inadequate — particularly in an AI-augmented environment. Multiple sources provide quotable evidence.

#### Evidence

- **Forbes Tech Council (March 27, 2026): Velocity is now free**
  - Source: Forbes Tech Council
  - Link: https://www.forbes.com/councils/forbestechcouncil/2026/03/27/why-confidence-is-the-new-velocity-in-ai-enabled-software-development/
  - Quote: "AI coding tools have made velocity practically free. An engineer can produce in an afternoon what used to take a sprint."
  - Credibility: High (Forbes contributor, timely)
  - Note: Strong opening-argument quote for the article

- **Swarmia: The Problem with Story Points**
  - Source: Swarmia
  - Link: https://www.swarmia.com/blog/the-problem-with-story-points/
  - Finding: "Velocity becomes a weapon for comparison, teams game the system to protect themselves, and the numbers never answer the questions stakeholders actually care about."
  - Note: The gaming dynamic is a key secondary argument — story points aren't just inadequate, they're actively corrupted by organizational incentives

- **Jellyfish: Skip velocity and story points entirely**
  - Source: Jellyfish
  - Link: https://jellyfish.co/library/ai-in-software-development/measuring-roi-of-code-assistants/
  - Quote: "Skip velocity and story point metrics entirely. They're too easy to manipulate. As one engineering lead confessed on Reddit: [...]"
  - Note: This is a practitioner-level admission; useful for authority

- **GetDX: Activity counts reveal less and less**
  - Source: GetDX
  - Link: https://getdx.com/blog/developer-velocity/
  - Finding: "As AI reshapes engineering workflows, activity counts such as story points or commits reveal less and less about actual effectiveness."

- **Medium: "Story Points Are Dying — Welcome to the Era of Prompt Points" (March 2026)**
  - Source: Amit Kalghatgi, Medium, March 2026
  - Link: https://medium.com/@amitkalghatgi/story-points-are-dying-welcome-to-the-era-of-prompt-points-75d31e44bf9c
  - Note: Trend signal — even practitioners are writing the eulogy for story points

- **Pragmatic Engineer (cited by Augment Code): Three critical failure modes**
  - Source: Augment Code / Pragmatic Engineer research
  - Link: https://www.augmentcode.com/guides/engineering-velocity-metrics-7-ai-enhanced-frameworks
  - Finding: Traditional metrics fail in three modes: (1) they reward output over outcomes, (2) they are gameable under management pressure, and (3) they do not account for AI-augmented work where a single engineer may produce 5x the output of six months ago

#### Analysis
This section gives the Ghostwriter ammunition to make the "story points are obsolete" claim with editorial force and evidential support. The Forbes Tech Council quote ("velocity is now free") is the sharpest formulation available.

---

### 4. What Works: Dollar-Denominated Metrics and Frameworks

#### Summary
The research identifies several frameworks and anchor data points for translating engineering activity to dollar outcomes. These are the building blocks of the article's prescriptive framework.

#### Evidence

- **IBM: $4.5 Billion in AI-Driven Productivity Savings (2025)**
  - Source: IBM Think / IBM CRN earnings call / IBM Q4 2025
  - Link: https://www.ibm.com/think/insights/enterprise-transformation-extreme-productivity-ai
  - Credibility: Very High (public company earnings disclosure)
  - Finding: IBM achieved $4.5 billion annual run-rate savings from AI-driven productivity transformations, helping drive $12.7 billion in free cash flow in 2024. CEO stated: "In 2023, we set out on a goal to achieve $2 billion of productivity savings exiting 2024, and today we are well ahead of that, exiting 2025 with $4.5 billion of annual run rate savings."
  - Caveat: This is a company-wide operations/consulting efficiency figure, not an isolated engineering-team metric. The Ghostwriter should use it as an anchor for "what it looks like when you measure in dollars at scale" rather than an engineering-specific benchmark.

- **LinearB: Elite DORA Teams — 2.6x Revenue, 2.2x Profitability**
  - Source: LinearB Software Development Metrics Guide, 2024/2025
  - Link: https://linearb.io/blog/software-development-metrics-guide
  - Credibility: Medium-High (LinearB's own research; methodology not fully published, but widely cited)
  - Finding: Teams achieving elite DORA performance report 2.6x higher revenue growth and 2.2x higher profitability compared to low performers.
  - Note: This is a correlation, not causation — but it's the strongest published link between delivery metrics and dollar outcomes currently available. Frame it as "the closest proxy available, and even it stops short of full attribution."

- **GitHub Copilot: Positive ROI within one quarter**
  - Source: LinearB Copilot ROI analysis, 2024/2025
  - Link: https://linearb.io/blog/is-github-copilot-worth-it
  - Credibility: High (engineering analytics firm, methodology cited)
  - Finding: "If a developer making $120,000 annually saves just two hours per week through Copilot assistance, that's $2,400 in recovered productivity per year — a 10x return on the Business tier investment."
  - Finding: Most enterprises report positive ROI within 3–6 months
  - Note: This is the clearest developer-cost-to-dollar-savings translation in the literature. The 2-hours-per-week calculation is a useful example for the article's framework section.

- **Fully Loaded Engineer Cost: The Dollar Denominator**
  - Source: Multiple (OSKI, Glen Coyne, VirtualLatinos/BLS)
  - Finding: Benefits and overhead add 25–40% to direct compensation. BLS: wages/salaries = 69.3% of total compensation; benefits = 30.7%. Combined with typical enterprise software tooling costs ($100–300/employee/month) and management overhead, a $150K salary engineer costs $180–225K fully loaded.
  - Note: The article should establish a clear benchmark: in enterprise, a software engineer costs $200–250K fully loaded per year. This becomes the denominator for every "hours saved" calculation.

- **Salesforce: CFOs want cost savings, compliance, and revenue growth (tied #1)**
  - Source: Salesforce CFO Research, August 2025
  - Finding: When CFOs evaluate AI ROI, their top metrics are: cost savings, risk/compliance improvements, and revenue growth (all tied #1). This is the CFO's own language — and it is entirely dollar-denominated.
  - Note: Ghostwriter can use this as "here's what your CFO actually wants to see" — direct from CFO research.

- **Search Engine Journal / "3 Metrics That Save" Framework (January 2026)**
  - Source: Search Engine Journal, citing Fortune Dec 2025
  - Link: https://www.searchenginejournal.com/why-cfos-are-cutting-ai-budgets-and-the-3-metrics-that-save-them/564741/
  - Framework proposed:
    - Leading indicator: Capacity freed (hours × fully loaded cost)
    - Lagging indicator (cost): Cost reduction realized
    - Lagging indicator (growth): New work enabled and revenue impact
  - Note: This three-part structure maps well onto the article's prescriptive framework needs

---

### 5. Emerging Frameworks: Business Value Mapping in Software Engineering

#### Summary
Gartner, DORA, and various tooling vendors are actively developing frameworks to map delivery metrics to business outcomes. The field is moving in the right direction but is early-stage.

#### Evidence

- **Gartner: Software Engineering Business Value Framework**
  - Source: Gartner
  - Link: https://www.gartner.com/en/software-engineering/topics/software-engineering-business-value
  - Finding: Gartner explicitly advocates for "providing teams with visibility into how their work impacts business value by establishing a value framework that maps delivery metrics to business outcomes."
  - Additional Gartner finding: "Even CIOs that map IT spend to business value make the mistake of selecting and tracking metrics that put the technology first, rather than the business outcomes. This happens when CIOs highlight the quantity of technology delivered (for example, number of tickets resolved) or how technology is delivered (for example, number of bugs found in testing)."
  - Credibility: Very High

- **Gartner: Software Engineering Intelligence Platforms (SEI)**
  - Source: Gartner, 2024 report cited by Typo
  - Finding: Only 5% of organizations currently use Software Engineering Intelligence Platforms; Gartner predicts this rises to 50% by 2027. These platforms track metrics like velocity, flow, and quality, with a goal of helping leaders make decisions that drive business value.
  - Note: The tooling gap is real — most orgs don't yet have the infrastructure to measure delivery-to-outcome. This supports the article's argument that AI-assisted measurement is a near-future capability, not a fully deployed one.

- **Gartner: 90% of engineers using AI code assistants by 2028**
  - Source: Gartner press release, July 2025
  - Finding: "By 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024. The role of developers will shift from implementation to orchestration, focusing on problem solving and system design."
  - Note: Sets up urgency — if nearly all engineers will use AI tools, the metrics question becomes critical.

- **DORA 2025: AI Increases Throughput AND Instability**
  - Source: DORA State of AI-Assisted Software Development, Google Cloud, 2025
  - Link: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report
  - Finding (Scrum.org summary): "One of the boldest findings in the report is this: AI increases throughput. It also increases instability. Delivery only matters when it solves a real problem. This model should be required reading for CTOs."
  - Note: DORA itself is moving toward business outcome framing

- **LinearB + DORA Partnership: 36,000 professionals research**
  - Source: LinearB/DORA Accelerate State of DevOps Report
  - Finding: Organizations using elite DORA metrics are 2x more likely to exceed organizational performance goals, 1.8x more likely to report better customer satisfaction

---

### 6. AI-Assisted Measurement: The Gap and the Opportunity

#### Summary
The article's thesis about AI helping bridge the measurement gap (auto-connecting user stories to business outcomes) is directionally supported by research, but concrete deployments of this capability are nascent. The opportunity is real; the infrastructure is not yet built at scale.

#### Evidence

- **Thoughtworks: AI for Requirements Analysis Case Study**
  - Source: Thoughtworks, published 2024/2025
  - Link: https://www.thoughtworks.com/en-us/insights/blog/generative-ai/using-ai-requirements-analysis-case-study
  - Finding: "Leveraging GenAI to create high-quality user stories can lead to shorter lead times and higher quality for requirements analysis." AI-generated user stories with clearer business framing reduced downstream ambiguity.
  - Note: This is the closest published case study for the "AI-assisted user story + business justification" angle. The gap is that it focuses on quality/lead time, not business outcome measurement.

- **InfoWorld: AI bridges communication gaps in requirements**
  - Source: InfoWorld, 2025
  - Link: https://www.infoworld.com/article/3980319/how-to-use-genai-for-requirements-gathering-and-agile-user-stories.html
  - Quote: "The technology excels at translating business needs into technical specifications and vice versa, bridging communication gaps."

- **SAP Business AI: ROI Estimator for AI Projects**
  - Source: SAP Innovation Guide H2 2025
  - Finding: SAP updated its estimator for SAP Business AI to forecast ROI for planned generative AI projects, helping customers deliver tangible business outcomes. This is an AI-assisted ROI measurement tool in production.
  - Note: This is a vendor-specific example, but it points toward the emerging category

- **The Gap: Feature-to-Revenue Automation Not Yet Solved**
  - The research does not surface any production system that automatically traces a shipped feature back to a revenue change or cost reduction at the enterprise level. The tooling chain (feature flags → product analytics → revenue attribution) exists in parts but is not yet AI-automated in any published case.
  - Note: Ghostwriter should acknowledge this gap honestly while positioning it as the opportunity the article's framework is designed to address.

---

## Counterarguments & Complications

- **Attribution is genuinely hard**: Engineering teams rarely ship features in isolation; attribution of revenue change to a specific engineering investment is a real statistical challenge. The article must address this, not dismiss it.
- **IBM's $4.5B is a company-level metric**: It's the best dollar-denominated AI productivity number available, but it's IBM's entire enterprise transformation, not a specific engineering team's output. Use carefully.
- **DORA-to-revenue correlation is LinearB's own research**: The 2.6x revenue / 2.2x profitability figures need to be cited with the caveat that LinearB makes money selling DORA measurement tools. Plausible, but not independently peer-reviewed.
- **The METR study has limits**: 16 developers is a small RCT. The results are directionally significant but the sample is not representative of all enterprise engineering contexts.
- **Some AI productivity gains are real**: GitHub Copilot's positive ROI within 3–6 months is credible. The argument is not that AI provides no value — it's that you must measure that value in dollars, not in story points. Don't overstate the "AI doesn't work" case.
- **Dollars require a business partner**: Translating engineering output to revenue requires collaboration with product, sales, and finance teams that engineering leaders may not have. The article should acknowledge this structural challenge.

---

## Data & Statistics

| Metric | Value | Source | Date |
|--------|-------|--------|------|
| CEOs reporting zero AI ROI | 56% | Forbes | Jan 2026 |
| CEOs facing board pressure for AI returns | 61% | Fortune (cited) | Dec 2025 |
| Enterprise AI initiatives that fail | 95% | MIT study (via WEF) | 2025 |
| CFOs changing how they evaluate ROI for AI | 61% | Salesforce Research | Aug 2025 |
| Faros: AI teams complete more tasks | 21% more tasks | Faros AI | 2025 |
| Faros: AI teams merge more PRs | 98% more PRs | Faros AI | 2025 |
| Faros: PR review time increase | +91% | Faros AI | 2025 |
| Faros: Bug rate increase per developer | +9% | Faros AI | 2025 |
| Faros: Company-level outcome correlation | None (0) | Faros AI | 2025 |
| METR: Experienced developer speed with AI | 19% slower | METR (RCT) | Jul 2025 |
| METR: Developer self-estimate of AI speed | 20% faster | METR (RCT) | Jul 2025 |
| NBER: Managers seeing no productivity change | 89% | NBER (via Fortune) | Feb 2026 |
| IBM annual run-rate AI savings | $4.5B | IBM earnings | Exit 2025 |
| IBM free cash flow 2024 | $12.7B | IBM earnings | 2024 |
| Linear B: Elite DORA revenue premium | 2.6x higher growth | LinearB | 2024/2025 |
| LinearB: Elite DORA profitability premium | 2.2x higher | LinearB | 2024/2025 |
| Gartner: Current SEI platform adoption | 5% of orgs | Gartner | 2024 |
| Gartner: Predicted SEI platform adoption | 50% by 2027 | Gartner | 2024 |
| Gartner: AI code assistant adoption by 2028 | 90% of engineers | Gartner | Jul 2025 |
| Enterprise fully-loaded engineer cost | $200–250K/yr | BLS / OSKI / industry | 2024/2025 |
| GitHub Copilot ROI break-even | 3–6 months | LinearB / Quantumrun | 2025 |
| GitHub Copilot: 2 hrs/wk saved = annualized | $2,400/dev/yr | LinearB | 2025 |
| CFOs: Top AI ROI metrics | Cost savings + revenue growth | Salesforce CFO Research | Aug 2025 |

---

## Expert Voices

### Elaine Marion, CFO of ePlus (via CFO Dive)
- **Stance**: CFOs in 2026 must direct AI budgets toward targeted investments with clear expectations for ROI and value to the business
- **Source**: CFO Dive, 2026

### Scott Rottman, President, Consulting Services (via CFO.com)
- **Key Quote**: "CFOs who lead boldly, modernize intentionally and build the cross-functional muscle for AI adoption will define the next decade of enterprise performance."
- **Source**: CFO.com, 2025/2026

### Marko Bevc, Principal Consultant, Scale Factory (via LeadDev)
- **Stance**: Engineering organizations need to focus on how they are delivering outcomes and then translating those to business impact
- **Source**: LeadDev, 2025

### Gartner (CIO Business Value Research)
- **Key Quote**: "Even CIOs that map IT spend to business value make the mistake of selecting and tracking metrics that put the technology first, rather than the business outcomes."
- **Source**: Gartner CIO Communicate IT Business Value page

### InfoWorld (GenAI requirements)
- **Key Quote**: "The technology excels at translating business needs into technical specifications and vice versa, bridging communication gaps."
- **Source**: InfoWorld, 2025

---

## Historical Context

The story points / velocity measurement model emerged from Extreme Programming (XP) and Scrum in the late 1990s and early 2000s. It was designed as an internal planning tool — a relative complexity estimator to help teams self-organize work within a sprint. It was never designed as a management reporting metric or a business value indicator. The corruption of story points into a performance metric was a gradual organizational dysfunction: once velocity became a KPI reported upward, teams began gaming it, and the signal collapsed.

The DORA metrics (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Recovery) emerged from the 2014–2018 DevOps Research and Assessment program as an improvement over story points — they measure actual delivery system health rather than estimated effort. The 2023 Accelerate book and subsequent DORA reports established these as the current best practice for engineering measurement. But even DORA metrics are delivery-system metrics, not business outcome metrics. The DORA program itself is now acknowledging this limitation (DORA 2025 report).

---

## Recent Developments

- **March 2026**: Forbes Tech Council publishes "Why Confidence Is the New Velocity in AI-Enabled Software Development" — stating AI has made velocity "practically free"
- **February 2026**: Fortune publishes CEO study linking AI adoption with no employment or productivity gains, reviving the "Solow Paradox"
- **January 2026**: Forbes publishes "56% of CEOs see zero ROI from AI" analysis
- **January 2026**: Search Engine Journal synthesizes CFO measurement crisis and proposes 3-metric framework
- **July 2025**: METR publishes RCT showing experienced developers are 19% slower with AI tools
- **August 2025**: Salesforce publishes CFO AI research showing 61% changing how they measure ROI
- **2025**: Faros AI publishes landmark productivity paradox report (n=10,000+ developers)
- **2025**: Harness publishes "AI Velocity Paradox" — gains in code creation offset by downstream bottlenecks
- **2025**: Gartner identifies Software Engineering Business Value mapping as a top strategic trend

---

## Knowledge Gaps

- **Direct engineering-to-revenue case studies**: The literature is thin on companies that have successfully published a complete chain from "engineering AI investment → specific dollar outcome." IBM is the closest but it's enterprise-wide. This gap is itself an argument the article should make.
- **AI-automated outcome measurement**: No published production system automatically traces a feature to a revenue/cost/retention change. The tooling category is nascent.
- **Industry-specific benchmarks**: The article's audience is mid-market and large enterprise. Most data is either startup-level or massive-enterprise (IBM). Mid-market benchmarks are scarce.
- **Attribution methodology**: The research doesn't surface a widely-adopted methodology for statistically attributing engineering work to revenue change. This remains an unsolved problem.

---

## Source Bibliography

1. Faros AI. "The AI Productivity Paradox Research Report." *Faros AI*, 2025. https://www.faros.ai/blog/ai-software-engineering
2. METR. "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity." *METR.org*, July 10, 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
3. Harness. "The State of AI in Software Engineering." *Harness*, 2025. https://www.harness.io/the-state-of-ai-in-software-engineering
4. IBM. "Enterprise transformation and extreme productivity with AI." *IBM Think*, 2025/2026. https://www.ibm.com/think/insights/enterprise-transformation-extreme-productivity-ai
5. LinearB. "Software development metrics guide: Benchmarks & best practices." *LinearB Blog*, 2025. https://linearb.io/blog/software-development-metrics-guide
6. LinearB. "Is GitHub Copilot worth it? ROI & productivity data." *LinearB Blog*, 2025. https://linearb.io/blog/is-github-copilot-worth-it
7. Salesforce. "New Salesforce Research: CFOs Invest in AI for Growth 2025." *Salesforce*, August 2025. https://www.salesforce.com/news/stories/cfos-invest-ai-for-growth/
8. Forbes / Gune Yildiz. "56% of CEOs See Zero ROI From AI: Here's What The 12% Who Profit Do Differently." *Forbes*, January 28, 2026. https://www.forbes.com/sites/guneyyildiz/2026/01/28/56-of-ceos-see-zero-roi-from-ai-heres-what-the-12-who-profit-do-differently/
9. Forbes Tech Council. "Why Confidence Is The New Velocity In AI-Enabled Software Development." *Forbes*, March 27, 2026. https://www.forbes.com/councils/forbestechcouncil/2026/03/27/why-confidence-is-the-new-velocity-in-ai-enabled-software-development/
10. Search Engine Journal. "Why CFOs Are Cutting AI Budgets (And The 3 Metrics That Save Them)." *SEJ*, January 2026. https://www.searchenginejournal.com/why-cfos-are-cutting-ai-budgets-and-the-3-metrics-that-save-them/564741/
11. World Economic Forum. "How CFOs can secure solid ROI from business AI investments." *WEF*, October 2025. https://www.weforum.org/stories/2025/10/cost-productivity-gains-cfo-ai-investment/
12. CFO Dive. "Top 5 AI adoption challenges facing CFOs in 2026." *CFO Dive*, 2026. https://www.cfodive.com/news/top-5-ai-adoption-challenges-facing-cfos-in-2026/810277/
13. CFO.com. "So far, few CFOs see substantial ROI from AI spending." *CFO.com*, 2025/2026. https://www.cfo.com/news/so-far-few-cfos-see-substantial-roi-from-ai-spending-RPG/808249/
14. Fortune / Erin Prater. "Thousands of CEOs just admitted AI had no impact on employment or productivity." *Fortune*, February 17, 2026. https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/
15. Gartner. "Proving the Business Value of Software Engineering." *Gartner*, 2024/2025. https://www.gartner.com/en/software-engineering/topics/software-engineering-business-value
16. Gartner. "Communicate IT Business Value: A Comprehensive Guide." *Gartner*. https://www.gartner.com/en/information-technology/topics/business-value-of-it
17. Gartner. "Gartner Identifies the Top Strategic Trends in Software Engineering for 2025 and Beyond." *Gartner Newsroom*, July 1, 2025. https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond
18. Swarmia. "The problem with story points." *Swarmia Blog*, 2024/2025. https://www.swarmia.com/blog/the-problem-with-story-points/
19. Thoughtworks. "Using AI for requirements analysis: A case study." *Thoughtworks*, 2024/2025. https://www.thoughtworks.com/en-us/insights/blog/generative-ai/using-ai-requirements-analysis-case-study
20. DORA / Google Cloud. "2025 DORA State of AI Assisted Software Development." *Google Cloud*, 2025. https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report
21. LeadDev. "How to measure the impact of engineering in 2025." *LeadDev*, 2025. https://leaddev.com/reporting/how-to-measure-the-impact-of-engineering-in-2025
22. Jellyfish. "How to Measure the ROI of AI Code Assistants." *Jellyfish*, 2025. https://jellyfish.co/library/ai-in-software-development/measuring-roi-of-code-assistants/
23. GetDX. "Beyond story points: how to measure developer velocity the right way." *GetDX Blog*, 2025. https://getdx.com/blog/developer-velocity/
24. SoftwareSeni. "The AI Productivity Paradox in Software Development." *SoftwareSeni*, 2025. https://www.softwareseni.com/the-ai-productivity-paradox-in-software-development-why-developers-feel-faster-but-measure-slower/

---

## Research Notes

- **Prior Research Cross-References**: The `drafts/ai_value_creation_20260331/research_pack.md` entry in the Research Index contains directly relevant data: BCG (74% no tangible AI value, 4% at scale), McKinsey (19% >5% revenue increase), and the IBM/JPMorgan/Visa dollar-denominated case studies. The Ghostwriter should cross-reference that pack for additional dollar-outcome examples, particularly the JPMorgan 400% ROI fraud detection AI case.
- **Strongest evidence for the thesis**: METR study (RCT, 19% slower) + Faros AI (no company-level correlation) + Fortune/NBER (89% of managers see no change) form a triple-confirmation of the productivity paradox.
- **Strongest prescription evidence**: IBM $4.5B + LinearB DORA correlation + Salesforce CFO research + the three-metric framework (capacity freed → cost reduction → revenue enabled).
- **Ghostwriter structural suggestion**: Consider a "The Stack of Lies" section that walks through each layer: story points → velocity → throughput → and why each one fails the CFO test. Then flip to the prescription: the only number that travels up the chain intact is a dollar.
- **Attribution objection**: Must be addressed directly and practically. The research does not solve this fully — the best available guidance is: (1) use control groups where possible (A/B test feature rollouts), (2) use proxy metrics that have known dollar conversion rates (support ticket volume → support cost, conversion rate → revenue), (3) be directionally honest rather than claiming false precision.
- **AI-automated measurement opportunity**: The gap is real and is the most forward-looking part of the thesis. Position it as "where this is going" rather than "what you can do today." Thoughtworks requirements AI is the closest current analog.
