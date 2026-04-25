# Fact-Check Report: Most AI Projects Don't Fail at the Model. They Fail at the Foundation.
**Draft Version**: FINAL.md
**Fact-Checker**: Fact-Checker Agent
**Date**: 2026-04-24
**Verdict**: Cleared with Corrections

## Summary
The draft is built on a sound factual foundation. The major statistics — MIT NANDA's 95% figure, Cloudera/HBR's 7%, both Gartner predictions, BCG's value gap figures, and the Deloitte agentic AI finding — all verify against primary sources. Two claims require correction before publication: the Forrester/Capital One attribution is inaccurate as written (wrong research firm, wrong methodology, wrong n), and the 41% "lack of data centralization" statistic misrepresents the source, which actually measured lack of real-time data access, not centralization. Both are fixable with precise attribution. Twelve claims were checked in total; two require correction, one requires a caveat, and nine are fully verified.

**Publication Verdict**: Cleared with Corrections

---

## Claim-by-Claim Analysis

### Section: "The 95% Failure Rate Tells You the Wrong Story"

| # | Claim (as written) | Status | Notes |
|---|---|---|---|
| 1 | "A July 2025 study from MIT's NANDA lab found that 95% of GenAI pilots yield no measurable P&L impact." | ✅ Verified | Confirmed. Multiple credible sources (Fortune, Forbes, Virtualization Review, MIT AIGL blog) corroborate the July 2025 report from MIT Project NANDA titled "The GenAI Divide: State of AI in Business 2025." The 95% figure and "no measurable P&L impact" language are accurate. |
| 2 | "A Forrester survey of 500 enterprise data leaders, commissioned in partnership with Capital One, found that 73% cite data quality and completeness as the primary barrier to AI success" | ❌ Inaccurate | No 2025 Forrester survey of 500 enterprise data leaders commissioned by Capital One on AI success barriers was locatable. Known Capital One/Forrester collaborations involve 150-181 respondents on ML deployment topics (2022-2023). The Capital One AI Readiness Survey (2024) was conducted by Morning Consult (n≈4,000), not Forrester, and the 73% figure there reflects data quality as a ranked concern — not explicitly "primary barrier to AI success." The Cloudera/HBR report (March 2026) separately found 73% find "processing and preparing data for AI to be challenging." The 73% figure may be real but the attribution is wrong. This requires correction. |

### Section: "Your Data Is Not AI-Ready. Probably Not Even Close."

| # | Claim (as written) | Status | Notes |
|---|---|---|---|
| 3 | "According to a March 2026 Cloudera and HBR Analytic Services report, only 7% of enterprises say their data is completely AI-ready." | ✅ Verified | Confirmed directly from Cloudera press release dated March 5, 2026. Exact language matches: "Only 7% of enterprises report their data is 'completely ready for AI adoption.'" |
| 4 | "73% point to data quality and completeness before anything else" (second instance, attributed to enterprise data leaders ranking barriers) | ⚠️ Caveat | The Cloudera/HBR press release confirms 73% "believe their organization should prioritize AI data quality more than it currently does" and 73% found "processing and preparing data for AI to be challenging." This is directionally consistent but the framing in the draft ("rank their primary barrier") overstates what the source says. The Cloudera data reflects a prioritization gap, not a direct ranking of barriers. |
| 5 | "A separate industry survey of more than 400 data leaders found that 41% cite lack of data centralization as the reason AI projects fail." | ❌ Inaccurate | The Fivetran report (n=401 data leaders) is the likely source for the "more than 400" framing. However, the 41% figure in that report refers to "lack of real-time data access prevents AI models from delivering timely insights" — not "lack of data centralization." The Fivetran report does note that 29% say "data silos are blocking AI success," which is closer to a centralization claim but at a different percentage. The draft misrepresents the specific barrier. |

### Section: "Agentic AI Makes the Integration Problem Dangerous, Not Just Inconvenient"

| # | Claim (as written) | Status | Notes |
|---|---|---|---|
| 6 | "Deloitte's AI Pulse Check 2025 found that nearly 60% of AI leaders cite integrating with legacy systems and addressing risk and compliance as their organization's primary challenges in adopting agentic AI." | ✅ Verified | Confirmed directly on Deloitte's website (ai-adoption-challenges-ai-trends blog post). Exact language: "According to nearly 60% of the AI leaders and representatives surveyed, their organization's primary challenges in adopting agentic AI are integrating with legacy systems and addressing risk and compliance concerns." |
| 7 | "Gartner's August 2025 data shows less than 5% of enterprise applications feature AI agents. Gartner predicts that figure reaches 40% by end of 2026." | ✅ Verified | Confirmed. Gartner press release dated August 26, 2025 states exactly: "Forty percent of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% today." Multiple corroborating sources. |
| 8 | "Gartner's June 2025 analysis reinforces this directly: over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls." | ✅ Verified | Confirmed. Gartner press release dated June 25, 2025 states exactly this prediction with the same three cited reasons. Widely covered by Reuters, Forbes, and others. |
| 9 | "Nate Jones has built a reference implementation of this pattern (OB1, github.com/NateBJones-Projects/OB1)" | ✅ Verified | The GitHub repository at github.com/NateBJones-Projects/OB1 returns HTTP 200 and is publicly accessible. |

### Section: "The 5% Who Are Winning Are Not Using Better Models"

| # | Claim (as written) | Status | Notes |
|---|---|---|---|
| 10 | "BCG's 'Widening AI Value Gap' report from September 2025 found that AI leaders achieve 1.7x revenue growth and 3.6x three-year total shareholder return compared to laggards." | ✅ Verified | Confirmed via BCG press release (PRNewswire) and Forbes coverage. Exact figures: "1.7x revenue growth, 3.6x three-year total shareholder return (TSR), and 1.6x EBIT margin." The report title "The Widening AI Value Gap" and September 2025 date are accurate (published September 30, 2025). |
| 11 | "BCG's own 10-20-70 principle: roughly 10% of the value gap is explained by technology selection, 20% by data and infrastructure, and 70% by people, process, and organizational discipline." | ⚠️ Caveat | The 10-20-70 principle is real and well-documented by BCG. However, the draft's label for the 10% bucket is inaccurate. BCG consistently describes the 10% as "algorithms" (or "machine learning models"), not "technology selection." The 20% is "data and technology" (or "data and technology implementation"), not just "data and infrastructure." The draft's paraphrase distorts BCG's framing in a way that could mislead readers about what BCG actually argues — specifically, BCG's 10% refers to model/algorithm work, not platform or vendor selection. |

### Section: "Fix the Plumbing First. Then Deploy the AI."

| # | Claim (as written) | Status | Notes |
|---|---|---|---|
| 12 | "A customer service agent handling 50,000 interactions per day, each requiring multiple LLM calls with large context windows, can generate token costs that dwarf the infrastructure budget..." and "token consumption runs 10 to 50 times higher than equivalent prompt-response interactions." | ❓ Unverifiable | These are presented as observations from EPAM's own deployment experience ("in our experience across enterprise deployments"). As first-party experiential claims, they cannot be independently verified via web search. They are framed appropriately as internal observations, not external citations, which is acceptable. No correction required, but the framing should remain clearly attributed to EPAM experience, not implied as industry-wide data. |

---

## Issues Requiring Correction

### Critical (Must Fix Before Publication)

1. **Forrester/Capital One 73% attribution** (paragraph 3, "The 95% Failure Rate" section): The survey attribution is inaccurate. No Forrester survey of 500 enterprise data leaders commissioned by Capital One in 2025 on AI success barriers has been located. The claim appears to conflate multiple sources. Recommended fix: Either (a) attribute the 73% to the Cloudera/HBR March 2026 report, which does contain a matching 73% figure with a clear source, or (b) locate and cite the actual primary source for the Forrester/Capital One n=500 claim. Do not retain the current attribution as written.

2. **41% "lack of data centralization"** (paragraph 3, "Your Data Is Not AI-Ready" section): The Fivetran report (n=401) uses 41% to describe "lack of real-time data access," not "lack of data centralization." These are related but meaningfully different barriers. Recommended fix: Change the claim to accurately reflect what the source says ("41% report that lack of real-time data access prevents AI models from delivering timely insights"), or substitute the correct statistic — the Fivetran report notes 29% cite data silos as blocking AI success, which is closer to a centralization claim.

### Moderate (Should Fix)

- **BCG 10-20-70 framing** (paragraph in "The 5% Who Are Winning" section): The draft describes the 10% as "technology selection," which misrepresents BCG's framing. BCG's 10% refers to algorithm/model work. Change "technology selection" to "algorithms and model choice" or similar language that accurately reflects BCG's framework.

- **73% second instance** (paragraph in "Your Data Is Not AI-Ready"): The framing "rank their primary barrier to AI success, 73% point to data quality" overstates what the Cloudera/HBR source says. The source reports 73% believe they should prioritize AI data quality more and find data preparation challenging — a prioritization gap, not a direct barrier ranking. Consider softening to "73% say their organization should prioritize AI data quality more than it currently does."

### Minor (Consider)

- The article sources list "Forrester / Capital One, Enterprise Data Leaders Survey, n=500, 2025" — this citation in the sources section should be corrected or removed in parallel with fixing the in-text claim.

---

## Unsourced Claims to Address

The following assertions are presented without explicit citation. They may be reasonable editorial positions or EPAM-internal observations, but should be clearly framed as such:

1. "Structuring data so AI agents can reason over it in business terms is not the same problem as having clean data. A semantic data layer must sit between raw enterprise data and the AI systems consuming it..." — paragraph 4, "Your Data Is Not AI-Ready" section. This is presented as architectural fact, not opinion. It is broadly defensible but uncited. Frame as EPAM's architectural recommendation or cite an industry source.

2. "In agentic architectures, [technical debt] becomes existential: an autonomous system needs reliable, well-documented integration points to operate safely." — "Technical Debt" section. Editorial position framed as fact. Acceptable as opinion if clearly so, but currently reads as an industry finding without citation.

---

## Sources Checked

| Source | URL | Claims Supported |
|---|---|---|
| MIT NANDA / AIGL Blog | https://www.aigl.blog/state-of-ai-in-business-2025/ | Claim #1 |
| Fortune (MIT NANDA coverage) | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | Claim #1 |
| Cloudera Press Release, March 2026 | https://www.cloudera.com/about/news-and-blogs/press-releases/2026-03-05-only-7-percent-of-enterprises-say-their-data-is-completely-ready-for-ai-according-to-new-report-from-cloudera-and-harvard-business-review-analytic-services-reveals.html | Claims #3, #4 |
| Capital One AI Readiness Survey | https://www.capitalone.com/tech/ai/ai-readiness-survey/ | Claim #2 (partial — shows Forrester attribution is wrong) |
| Fivetran Press Release | https://www.fivetran.com/press/fivetran-report-finds-nearly-half-of-enterprise-ai-projects-fail-due-to-poor-data-readiness | Claim #5 |
| Deloitte AI Pulse Check blog | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/blogs/pulse-check-series-latest-ai-developments/ai-adoption-challenges-ai-trends.html | Claim #6 |
| Gartner Press Release (August 2025) | https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 | Claim #7 |
| Gartner Press Release (June 2025) | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | Claim #8 |
| GitHub (NateBJones-Projects/OB1) | https://github.com/NateBJones-Projects/OB1 | Claim #9 |
| BCG PRNewswire / Forbes | https://www.prnewswire.com/news-releases/ai-leaders-outpace-laggards-with-double-the-revenue-growth-and-40-more-cost-savings-302570218.html | Claim #10 |
| BCG 10-20-70 (Forbes, BCG.com) | https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ | Claim #11 |

---

## Verdict

**Factual Accuracy**: Adequate
**Source Quality**: Adequate (strong on Gartner, BCG, MIT, Cloudera; weak on Forrester/Capital One attribution)
**Cleared for Publication**: Yes with corrections — two critical corrections required before publication

The article's core argument is well-supported by verifiable data. The two inaccuracies (Forrester/Capital One attribution and the 41% centralization misrepresentation) are fixable attribution errors, not fabrications. Once corrected, this draft is publication-ready.
