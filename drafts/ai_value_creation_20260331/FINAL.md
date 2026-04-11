# Where AI Actually Makes Money
*Final Draft | 2026-04-01 | ~2,550 words*

---

The dominant story about AI and business value has been about cost. Fewer bodies in the org chart. Cheaper code. Automated customer service queues. That story is real — those savings exist, those headcounts are down, those tickets are being resolved without human intervention. For most organizations, it's also entirely the wrong frame for the larger opportunity.

According to BCG's 2024 research, 74% of companies have not shown tangible value from their AI investments. Only 4% are generating substantial value at scale. Yet FTI Consulting's 2025 survey of more than 500 private equity decision-makers found that AI has emerged as their single top strategic priority — and the leading factor in positioning portfolio companies for exit. The gap between those two data points tells the whole story. AI isn't failing most organizations because it doesn't work. It's failing because most organizations are looking for value in the wrong place.

The companies capturing AI value are deploying it where the money is: directly against the activities that generate and protect revenue. They are using AI to personalize experiences that convert more customers, to optimize prices in real time, to accelerate sales pipelines, to prevent revenue leakage before it happens, and to access markets they couldn't profitably serve before. These are not pilot programs. They are production systems with audited financial results — and the EBITDA impact is large enough to move a multiple.

Most of these use cases are not new concepts. Demand forecasting, personalization, dynamic pricing — these disciplines have existed for decades. What changed is who can deploy them.

---

## The Accessibility Shift

The honest version of the AI value story begins with an acknowledgment. The clearest proof points — Amazon's recommendation engine, Visa's fraud network, Walmart's supply chain — were built by organizations with hundreds of data scientists, proprietary petabyte-scale datasets, and years of infrastructure investment. Pointing to them as evidence of what AI can do is accurate. Implying they are a replicable template for a $200 million business is not.

What changed is the access equation. Generative AI is the reason — though not in the way most people assume.

The applications driving revenue in this article are not large language models. Demand forecasting, dynamic pricing, churn prediction, fraud detection, predictive maintenance — these run on purpose-built ML models: gradient boosting, time series algorithms, neural networks trained on structured operational data. What LLMs don't do well is predict next quarter's inventory requirements or flag which customer is about to leave. What they have done is dramatically lower the expertise required to build the systems that do.

For most of the past decade, deploying custom machine learning at production scale required three things most organizations couldn't assemble: data scientists with deep ML expertise, ML engineers to productionize models, and software engineers to build the surrounding data pipelines, training infrastructure, and monitoring systems. All three, working in concert, for months before anything reached production. MIT Sloan's Davenport and Bean described it plainly: producing data science models was an artisanal activity — bespoke, slow, dependent on scarce specialists.

Two forces have broken that dependency.

The first is automated machine learning. AutoML platforms handle what was the most expertise-intensive work in the ML pipeline: feature engineering, model selection, hyperparameter tuning, and validation — the steps that once required a senior data scientist's judgment. What previously took months of manual iteration now takes days. Domain experts with working knowledge of their data and business problem — but without deep ML specialization — can build and validate production-grade prediction models.

The second force is generative AI applied to the surrounding engineering work. The data pipelines, feature stores, deployment scripts, and monitoring infrastructure that wrap any ML system represent substantial engineering effort — often more than the modeling work itself. GitHub's research found that developers completed coding tasks 55% faster with AI coding assistance, with the largest gains on exactly the repetitive infrastructure work that surrounds any ML deployment: pipeline scaffolding, schema transformation, API wiring, monitoring setup. A team of three with the right tools and proprietary operational data now covers ground that would have required a much larger specialist team five years ago.

Consider how this typically unfolds for a company with reasonably clean operational data — a regional specialty distributor, $150 million in revenue, a small IT team, ten years of SKU-level transaction history in its ERP — building a demand forecasting model to reduce inventory carrying costs and eliminate stockouts.

The team that builds it: a data analyst with ten years of distribution operations experience and a generalist engineer. No ML PhD. No dedicated data scientist. What they bring is not ML expertise — it's deep business domain knowledge. They know which suppliers have unreliable lead times, how promotional calendars and seasonal patterns interact, why certain SKU categories behave differently in Q4. That judgment is what no algorithm substitutes for — and what makes the model useful rather than merely accurate on a validation dataset. The tools handle the technical depth.

The pipeline work takes about a week. Airbyte extracts and syncs historical orders, inventory movements, and supplier records from the ERP into a cloud data warehouse. dbt transforms the raw tables into structured training data. GitHub Copilot accelerates the custom scaffolding — the edge cases, the logic for handling clearance SKUs and promotional outliers every distribution business has. Work that previously required a senior engineer to architect from scratch becomes code the analyst reviews and deploys.

The modeling work runs in days. The cleaned dataset goes into H2O.ai AutoML or DataRobot. The platform runs feature engineering and model selection autonomously — testing gradient boosting, random forests, and ensemble approaches across hundreds of hyperparameter configurations — and surfaces a validated model with documented accuracy metrics. The analyst doesn't choose the algorithm. The platform proves which one performs best on held-out data.

The operational wrapper takes another two weeks. MLflow manages the model registry and tracks performance as data evolves. A Prefect workflow schedules weekly retraining as new transaction data accumulates. The generalist engineer, working with Copilot, builds the API into the replenishment system and the monitoring dashboard that flags when accuracy degrades — the difference between a model that works at launch and one that keeps working six months later.

For a company starting from a position of data readiness, the full build runs in eight to twelve weeks with a team of two or three and cloud platform costs in the mid-five figures annually. Three years ago, the equivalent build required a data scientist, an ML engineer, and a software engineer working four to six months — not because the demand forecasting problem was harder, but because the tools required that level of specialization to navigate.

This doesn't make implementation trivial. The most common obstacle is not technical skill — it's data quality. Many mid-market companies discover that years of operational history in their ERP is inconsistent, incomplete, or siloed across system migrations, and resolving it is often the longest phase of the build. The organizational changes required to act on AI output are significant too — a point we will return to.

But the moat has inverted. When building AI required large specialist teams and months of bespoke engineering, scale was the advantage — large companies could build what small ones could not. That barrier has largely fallen. The moat is now in the data. The regional distributor with ten years of SKU-level demand history, the specialty manufacturer with a decade of sensor data from its production lines, the B2B services firm with years of customer transaction records — they hold proprietary advantages that cannot be purchased or replicated quickly. The data middle-market companies have accumulated as a byproduct of running their businesses is now the primary input for AI that actually works.

---

## AI as Revenue Accelerator

The most direct form of AI value creation is when AI increases revenue without adding proportional cost — improving unit economics rather than just reducing expenses.

Personalization is the clearest case. Amazon attributes **35% of its total revenue** to AI-powered recommendation systems that continuously learn which products to surface to which customers at which moments. The Amazon number is extreme because Amazon's data and organizational investment are extreme. But the mechanism is available at any scale. McKinsey's research shows personalization drives **5–15% revenue lift** for most companies that execute it well, and leading companies generate 40% more revenue from their personalization efforts than average performers. That gap compounds over time as better-performing models widen the advantage. A business generating $100 million in revenue that closes half the gap between average and leading performance is looking at $10–20 million in incremental top line — without adding a sales rep or a marketing dollar.

Dynamic pricing is AI's most direct revenue lever. In travel and hospitality — where every room and appointment slot is perishable inventory — AI moves pricing decisions from weekly spreadsheets to continuous, real-time optimization. Marriott and Hilton have reported **RevPAR lifts of 5–10%** from AI revenue management systems. The Four Seasons Resort Whistler saw a **28% increase in off-peak revenue** in 2025 by identifying pricing opportunities in periods that historically underperformed. That is not a hospitality story. It is a capacity utilization story, applicable to any business with variable demand and time-sensitive inventory.

The same principle is producing results in industrial and distribution markets. BCG's analysis of AI pricing in retail and distribution found that companies deploying AI for pricing improved **gross profit by 5–10%**. Manufacturers adopting AI dynamic pricing have reported an average **12% revenue uplift within the first year**. For companies where pricing has been driven by cost-plus formulas or salesforce negotiation, AI-informed pricing captures margin that has always existed in the market but was never systematically extracted.

Sales velocity is where AI is generating some of the most measurable results in B2B markets. ZoomInfo's Copilot, deployed across more than 50,000 sales professionals, has produced a **60% increase in demos and meetings booked** and nearly a **90% improvement in email response rates**. McKinsey's analysis of AI in B2B sales finds a **15–25% ROI improvement** and a **30–50% reduction in lead conversion time**. The mechanism is prioritization, not replacement: AI identifies the right accounts, the right timing, and the right message. In well-implemented deployments, the top 20% of leads AI surfaces generate 60% of quarterly revenue. Not more reps. More productive reps.

---

## AI as Cost Shield That Protects Revenue

Some of AI's most auditable value creation looks like cost reduction on the surface but is better understood as revenue protection — preventing erosion that would otherwise occur silently, and expanding the markets a business can profitably serve.

Fraud prevention and credit risk are the clearest cases in financial services. Visa's AI system analyzed **320 billion transactions** and prevented **more than $40 billion in fraud** — commerce that flowed rather than leaked. JPMorgan Chase reported a **400% ROI in year one** from its fraud detection AI. The economics translate downward. Zest AI, which provides AI-driven underwriting tools to mid-market lenders, has delivered **300% ROI for its clients** through more accurate risk assessment that reduces both defaults and false rejections. The second effect — expanding credit access to previously rejected but creditworthy segments — generates revenue the business wasn't earning before. Better risk models don't just protect the existing book; they expand the addressable market.

Supply chain and inventory management follow the same logic. EisnerAmper documented a regional distribution company that implemented AI demand forecasting, improved inventory turnover by 15%, and saw its EBITDA multiple move from approximately **7x to 9x** at exit. The mechanism: less capital tied up in slow-moving inventory, fewer stockouts costing sales, more reliable fulfillment commanding customer loyalty. AI demand forecasting reduces forecast errors by **20–50%** and stockout incidents by approximately 30%. For a distributor or specialty retailer, a meaningful reduction in stockout rate recovers revenue that disappeared without a trace in traditional reporting.

Predictive maintenance in manufacturing and industrial operations is where the EBITDA improvement is most precisely documented. A peer-reviewed analysis of production deployments found that AI-driven predictive maintenance generates **$1.5–4.2 million in annualized savings per automotive manufacturing line** and **$3.7–8.3 million per semiconductor fabrication facility**. Equipment that doesn't fail unexpectedly produces the revenue it was designed to produce. For an industrial business running multiple facilities, eliminating unplanned downtime is a direct, auditable EBITDA improvement that flows through to valuation.

---

## AI as Market Expander

The most strategically significant form of AI value creation — and the one where the evidence is still accumulating — is when AI enables a company to compete profitably in markets or customer segments that were previously out of reach. Not optimizing existing revenue. Generating revenue the business structurally could not capture before.

Specialty insurance and alternative lending are where this mechanism is most visible today. AI underwriting enables insurers and lenders to evaluate risk in segments that traditional actuarial or credit models either rejected outright or mispriced conservatively enough that the economics didn't work. Early results from AI-enabled underwriting deployments suggest revenue growth in the range of 15% from behavior-based and dynamic pricing products that couldn't be profitably underwritten before. When a specialty insurer can accurately evaluate small business policies or non-standard assets — categories that previously required prohibitively expensive expert review — it expands its addressable market without proportionally expanding its cost structure.

The same logic extends to service businesses sitting on operational data they have never fully monetized. A company with years of customer transaction records, equipment service histories, or usage patterns holds a data asset AI can convert into a differentiated product — analytics capabilities, predictive advisory services, optimization tools that competitors without that data history cannot replicate. PwC's research on AI in PE portfolio companies identifies this as one of the highest-impact plays: deploying AI against proprietary operational data to unlock decisions — market entry, site selection, product expansion — that human analysis couldn't support cost-effectively at scale. The value is not in the AI. It is in the decisions the data makes possible.

A competitor can adopt the same AutoML platform and hire the same generalist engineers. It cannot replicate ten years of your transaction history. The window for establishing a data-based market position is open. It is narrowing.

---

## Why the 4% Win While the 74% Wait

Four mechanisms, multiple documented successes, hard numbers from credible organizations. So why are three-quarters of companies still struggling to show value?

BCG's research points to the answer. Organizations that successfully scale AI value creation follow what BCG calls the 10-20-70 principle: **10% of transformation effort on algorithms**, **20% on data and technology infrastructure**, and **70% on people, processes, and how the business operates**. Companies that follow this distribution achieve 2.1x greater ROI and scale twice as many AI initiatives as those that don't.

Most organizations have it backwards. They fund the technology and assume the value will follow. It doesn't. The hotel that deploys AI pricing software but leaves revenue management decisions to a team that overrides the recommendations every Friday afternoon will not see a 10% RevPAR lift. The distributor that installs AI demand forecasting but doesn't redesign replenishment workflows around it will not see inventory turnover improve 15%. The B2B sales team that buys an AI prospecting tool but doesn't change how it prioritizes its week will book exactly as many demos as it did before.

PE Operational Alpha analysis pegs technology-enabled AI improvements at **4–12% EBITDA uplift with 12–24 month payback periods** when focused on demand forecasting, pricing, lead scoring, and customer analytics. That is a compelling hold-period value creation thesis — but only for companies that make the organizational changes required. According to Bain's 2025 Global Private Equity Report, nearly **20% of PE portfolio companies have now operationalized generative AI use cases and are seeing concrete results** — meaningfully higher than the 4% across the broader enterprise market, reflecting the execution discipline that structured ownership typically imposes.

McKinsey's data confirms the pattern. Companies attributing more than 11% of EBIT to AI consistently deploy it against revenue growth and margin improvement, not process efficiency. They invest in the organizational changes that convert AI output into business outcome. And they compound that advantage while their competitors are still debating which model to use.

This isn't a technology gap. It's a prioritization and execution gap. Both are solvable — but neither is solved by a software purchase.

---

## The Question Worth Asking

The evidence that AI creates business value is no longer speculative. Hotels deploying AI pricing outperform RevPAR benchmarks by 5–10%. B2B sales teams using AI prospecting book 60% more meetings with the same headcount. Manufacturers that deploy predictive maintenance eliminate millions in unplanned downtime per facility. Lenders using AI underwriting extend credit to segments that rule-based models rejected — and earn the revenue those segments represent. A regional distributor improved its inventory turnover by 15% and moved its exit multiple by two full turns.

FTI Consulting found that among PE professionals, AI is now the leading factor in exit readiness. Not revenue growth. Not margin expansion. Not the management team. AI capability — specifically the organizational capability to use AI where it affects financial performance.

The relevant question is not whether AI creates value. It is whether your business has positioned AI where value actually lives — against revenue, against margin, against the customer segments and markets currently out of reach — and whether the organizational changes required to capture that value are actually underway.

Ask yourself: where in your P&L is AI currently touching revenue? Not process efficiency. Not headcount. Revenue and margin. The distance between your honest answer to that question and the case studies above is almost never a technology distance.

---

## Publication Metadata
- **Word Count**: ~2,550
- **Reading Time**: ~11 minutes
- **Target Audience**: Private equity professionals and middle-market operating executives (implicit framing throughout)
- **Key Topics**: AI value creation, revenue acceleration, predictive maintenance, demand forecasting, dynamic pricing, AutoML, MLOps, EBITDA improvement, PE portfolio value creation

## Source References
1. BCG. "AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value." October 2024.
2. BCG. "From Potential to Profit: Closing the AI Impact Gap." 2025.
3. BCG. "Overcoming Retail Complexity with AI-Powered Pricing." 2024.
4. McKinsey. "The State of AI: How Organizations Are Rewiring to Capture Value." March 2025.
5. McKinsey. "Superagency in the Workplace." 2025.
6. McKinsey. "Unlocking Profitable B2B Growth Through Gen AI."
7. FTI Consulting. "2025 Private Equity Value Creation Index." 2025.
8. FTI Consulting. "Four Predictions Private Equity 2026." 2025.
9. Bain & Company. "Global Private Equity Report 2025."
10. EisnerAmper. "How AI Is Shaping the Valuation of Private Companies." 2025.
11. Paperfree / PE Operational Alpha. "Private Equity Operational Alpha in 2025." 2025.
12. PwC. "How Private Equity Survives AI." 2025.
13. MIT Sloan / Davenport & Bean. "Five Key Trends in AI and Data Science for 2024."
14. Snowflake. "What Is AutoML." 2024.
15. GitHub. "Research: Quantifying GitHub Copilot's impact on developer productivity and happiness." 2023.
16. Amazon / Taranker. "AI recommendation engine — 35% of revenue."
17. McKinsey / envive.ai. "Personalization lift 5–15%; leaders 40% advantage."
18. epic-rev.com. "AI Revenue Management — Marriott/Hilton 5–10% RevPAR."
19. revenue-hub.com. "Four Seasons Whistler 28% off-peak revenue." 2025.
20. DRING AI / industry. "Manufacturers AI dynamic pricing — 12% revenue uplift year one."
21. ZoomInfo. "State of AI in Sales & Marketing 2025."
22. McKinsey. "AI B2B sales 15–25% ROI; 30–50% lead conversion improvement."
23. Visa / Begine Fusion. "AI fraud prevention — $40B prevented, 320B transactions analyzed."
24. uitg.co / JPMorgan. "Fraud AI — 400% ROI year one."
25. Zest AI / ai.uitgtech.com. "300% ROI for mid-market lender clients."
26. EisnerAmper. "Distribution company — 7x to 9x EBITDA multiple."
27. articsledge.com. "AI demand forecasting — error reduction 20–50%; stockout reduction 30%."
28. ResearchGate. "AI-Driven Predictive Maintenance: per-facility savings." 2024.
29. ScienceSoft. "AI insurance underwriting — early results, behavior-based pricing revenue growth."
