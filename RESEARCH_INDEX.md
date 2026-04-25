# Research Index

**Last Updated**: 2026-04-11
**Maintained By**: Archivist Agent
**Total Entries**: 4

---

## About This Index

This is a living index of all `research_pack.md` files produced by the Researcher agent. The **Archivist** maintains this file automatically after each research task completes. The **Researcher** and **Librarian** can query this index before starting new research to avoid redundant web searches and surface relevant prior findings.

### Index Purpose
- **Research Reuse**: Identify prior research that overlaps with a new topic before running new searches
- **Evidence Library**: Quickly locate specific data points, case studies, or statistics gathered in past work
- **Efficiency**: Avoid re-researching topics already covered; supplement rather than restart
- **Cross-Topic Synthesis**: Surface connections between research done for different articles

### How to Use
- **Before new research**: Search this index for overlapping topics; link relevant past packs in the new research_pack.md
- **Finding evidence**: Use tags and key findings to locate specific data points
- **Researcher agent**: Query this index at the start of each research task to check for prior coverage

---

## Entries

---

## Building an Agentic Writing Pipeline Using Claude Code
**Research Pack**: `drafts/agentic_writer_20260411/research_pack.md`
**Date Researched**: 2026-04-11
**Article Draft**: `drafts/agentic_writer_20260411/`
**Search Queries**: 9
**Sources Evaluated**: 40+

### Topic Summary
How a non-developer knowledge worker can build a sophisticated multi-agent workflow using Claude Code's conversational configuration model — without coding expertise. Covers the competitive landscape of developer-first frameworks (LangGraph, CrewAI, AutoGen), Claude Code's text-first configuration primitives (CLAUDE.md, sub-agents, skills, plugins, MCP, hooks), the no-code/low-code AI agent market trend, and the absence of comparable published first-person accounts of non-developers building similar systems. Core argument: the barrier to building agentic systems is architectural, not just technical — and Claude Code's markdown-based configuration model is structurally different from all major alternatives.

### Key Findings
- **LangGraph**: Steep learning curve; requires understanding of DAG semantics, state propagation, graph design. Enterprise/compliance focused. Not accessible to non-developers.
- **AutoGen (Microsoft Research)**: Requires advanced Python skills. AutoGen Studio provides a UI layer for prototyping, but production use requires Python.
- **CrewAI**: Python-only (3.10–3.13 required). Most accessible of the three frameworks, but "accessible" still means Python installation and developer workflow. Non-technical teams cannot use it without Python developers.
- **Claude Code configuration model**: CLAUDE.md (persistent memory, natural language), sub-agents (markdown files with YAML frontmatter + prose system prompt), skills (SKILL.md procedural instruction files), plugins (bundled collections installable via single command), MCP (.mcp.json connection config), hooks (event-triggered scripts). All text-first, not code-first.
- **AI agents market**: $7.63 billion in 2025; projected $182.97 billion by 2033 at 49.6% CAGR (Grand View Research). No-code/low-code platforms cited as primary adoption accelerant.
- **Developer adoption gap**: 52% of professional developers either don't use agents or use simpler tools; 38% have no plans to adopt (Stack Overflow Dev Survey, Dec 2025). Even technical users find agents non-trivial.
- **No comparable public examples**: No published first-person account of a non-developer building a full multi-agent pipeline conversationally with Claude Code. The subject's 11-agent system is a genuinely novel documented case study.
- **FreeCodeCamp (Claude Code Handbook, 2026)**: "The ability to build software is becoming accessible to a broader range of people — not because the underlying complexity has been eliminated, but because much of the mechanical translation between intent and implementation can now be delegated to an AI agent."
- **Copilot Studio accessibility ceiling**: Microsoft's no-code agent tool is best for templated tasks; $200/month per tenant. Genuine multi-agent pipeline customization is beyond its current capability for non-developers.

### Primary Areas Covered
Multi-agent framework comparison, Claude Code configuration primitives, AI agent market data, no-code/low-code adoption trend, knowledge worker adoption barriers, comparable public examples survey

### Key Sources
- Grand View Research — AI Agents Market Report (2025)
- Stack Overflow Developer Survey (December 2025)
- Latenode Blog — LangGraph vs AutoGen vs CrewAI comparison (2025)
- DataCamp — Multi-agent framework comparison (2025)
- MindStudio — MindStudio vs CrewAI accessibility comparison (2025)
- Anthropic — Claude Code sub-agents, skills, plugins official docs (2025–2026)
- HumanLayer Blog — Writing a good CLAUDE.md (2025)
- FreeCodeCamp — Claude Code Handbook (2026)
- Salesmate — AI agent trends for 2026
- Forbes — Microsoft's Agent Stack Confuses Developers (April 2026)
- McKinsey — Superagency in the Workplace (January 2025)

### Counterarguments Documented
- Initial terminal/CLI setup still requires some comfort beyond a typical GUI user
- Claude Code is Claude-specific (model lock-in), unlike framework alternatives
- No-code tools (Zapier, Copilot Studio) are expanding — accessibility window may narrow
- No published usability data comparing Claude Code vs. CrewAI for non-developer users

### Cross-References
- **Prior Research**: `drafts/ai_champions_guild_20260403/research_pack.md` — AI adoption barriers and McKinsey "employees are ready, leadership is the barrier" framing is relevant context for the accessibility argument.

### Tags
`#claude-code` `#multi-agent` `#agentic-workflow` `#CLAUDE.md` `#sub-agents` `#skills` `#plugins` `#mcp` `#no-code` `#low-code` `#knowledge-workers` `#non-developer` `#crewai` `#langgraph` `#autogen` `#ai-agents-market` `#accessibility` `#personal-productivity` `#writing-pipeline` `#conversational-configuration` `#anthropic`

---

## AI as a Value Creator — Revenue Growth and Profitability
**Research Pack**: `drafts/ai_value_creation_20260331/research_pack.md`
**Date Researched**: 2026-03-31
**Article Draft**: `drafts/ai_value_creation_20260331/`
**Search Queries**: 12
**Sources Evaluated**: 60+

### Topic Summary
How companies are using AI to drive revenue growth and profitability beyond headcount reduction and software automation. Covers five primary value-creation mechanisms with production-scale case studies and hard financial data.

### Key Findings
- **BCG (2024)**: 74% of companies have not shown tangible AI value; only 4% generating substantial value at scale. Organizations following 10-20-70 principle achieve 2.1x greater ROI.
- **Amazon**: 35% of total revenue attributed to AI recommendation systems (widely cited industry consensus)
- **McKinsey**: Personalization drives 5–15% revenue lift; leading companies generate 40% more revenue from personalization than average performers
- **Visa**: AI analyzed 320 billion transactions and prevented $40 billion in fraud
- **JPMorgan**: 400% ROI in year one from fraud detection AI; Zest AI clients: 300% ROI
- **Hotels (Marriott/Hilton)**: 5–10% RevPAR lift from AI revenue management
- **ZoomInfo Copilot**: 60% more demos/meetings booked, 90% email response rate improvement (50,000+ user sample)
- **McKinsey B2B Sales**: 15–25% ROI increase, 30–50% lead conversion time reduction from AI sales tools
- **Walmart**: AI transformed demand forecasting; industry data: 20–50% reduction in forecast errors, 30% fewer stockouts
- **Manufacturing PdM**: Semiconductor fabs $3.7–8.3M annualized savings; automotive lines $1.5–4.2M (ResearchGate peer-reviewed)
- **Insilico Medicine**: AI compressed drug candidate timeline from 4–6 years to 12–18 months across 20+ programs; ISM001-055 in Phase IIa
- **Exelixis**: Acquired AI-discovered drug candidate for $80M (MIT Technology Review, 2024)
- **McKinsey State of AI 2025**: Only 19% of companies see >5% revenue increase from AI; 36% see no change — value concentrated in high performers

### Primary Industries Covered
Retail/E-commerce, Financial Services (banking, insurance), Travel/Hospitality, Manufacturing, Pharma/Biotech, B2B Sales & Marketing

### Key Sources
- BCG AI Adoption Report (Oct 2024) — 74%/4%/10-20-70
- McKinsey State of AI (March 2025)
- ZoomInfo State of AI Sales & Marketing (2025)
- MIT Technology Review — Exelixis $80M deal (March 2024)
- ResearchGate — AI PdM in manufacturing (2024, peer-reviewed)
- Wharton/GBK Gen AI Enterprise Report (Oct 2025)
- Insilico Medicine IPO materials (2025)

### Counterarguments Documented
- BCG: 74% have not captured value; only 4% at scale
- McKinsey: 36% of companies see no revenue change; 39% see EBIT improvement of any kind
- Value concentration problem: Amazon/Visa/JPMorgan have proprietary data advantages most cannot replicate
- High performers compound; laggards stall — the gap is widening

### Tags
`#ai-roi` `#revenue-growth` `#personalization` `#dynamic-pricing` `#fraud-detection` `#supply-chain` `#demand-forecasting` `#predictive-maintenance` `#drug-discovery` `#b2b-sales` `#bcg-10-20-70` `#value-creation` `#enterprise-ai` `#mckinsey` `#bcg` `#jpmorgan` `#visa` `#amazon` `#walmart` `#insilico`

---

## AI Champions and Practitioners Guilds in Enterprise Organizations
**Research Pack**: `drafts/ai_champions_guild_20260403/research_pack.md`
**Date Researched**: 2026-04-03
**Article Draft**: `drafts/ai_champions_guild_20260403/`
**Search Queries**: 28
**Sources Evaluated**: 60+

### Topic Summary
How enterprise organizations in the US and Canada are structuring internal AI Champions networks, Practitioners Guilds, and Communities of Practice (CoPs) to bridge the gap between top-down AI governance and ground-level adoption. Covers the hub-and-spoke structural model, membership design, leadership and time commitment, participation formats, and the benefits participants receive. Includes major case studies: Citi (4,200 volunteer AI Accelerators, 70%+ adoption), PwC (3,200 AI Champions, 54% weekly AI usage), trivago AI Ambassadors (2+ years, OKR-driven), and the Spotify guild model (original design and documented failures).

### Key Findings
- **Perception Gap (Writer 2025, n=1,600)**: 75% of C-suite believe their org has successfully adopted AI; only 45% of employees agree. 77% of AI-using employees self-identify as current or potential champions.
- **Citi AI Accelerators**: 4,200 volunteers across 182,000 employees in 84 countries. Achieved 70%+ adoption of firm-approved AI tools. Staff from operations, risk, and customer support — not only data scientists. Program pairs peer network with firm-approved tools, explicit data boundaries, and clear use cases.
- **PwC AI Champions**: 3,200 champions embedded in each line of service. 54% of global workforce using AI tools weekly. 8.7 million Copilot actions in one month, freeing 500,000+ hours of capacity. Champions coach teams on tool use; drive peer-led learning ("prompting parties").
- **trivago AI Ambassadors**: Two-year-old program (as of Oct 2025). Uses OKRs to structure ambassador activities around agentic piloting, knowledge sharing, and tool governance (AI Radar). Spans Hotel Search, Finance & Legal, Marketing.
- **Hub-and-Spoke Model**: AI CoE as central hub (sets policy, standards, tooling); embedded champions as spokes (local adoption, use case discovery, governance translation).
- **Membership Benchmark**: 5–10% of AI user base as champions; one champion lead per 10–20 champions (CSO Online / Lead with AI). Role is opt-in, part-time (~30–60 min/week per GitHub playbook).
- **Program Leadership**: Champion program requires a dedicated full-time program lead (housed in AI CoE, CTO, or CISO org). Individual champions are part-time volunteers.
- **Champion Benefits**: AI fluency ahead of peers; career visibility; influence without formal authority; early tool access; peer network; internal recognition (badges, callouts, prompt library features). Microsoft Work Trend Index: 71% of leaders prefer less experienced candidates with AI skills over more experienced ones without.
- **Failure Modes**: No executive mandate; time constraints; ownership consolidating in too few hands; weak 1:1 connections between members; no governance infrastructure before launch. Spotify's own guild model was "aspirational and never fully implemented" (Jeremiah Lee, former Spotify PM).
- **IAPP 2025**: 77% of organizations actively developing AI governance programs — creating institutional demand for the champion/liaison role.

### Primary Industries Covered
Financial Services (Citi), Professional Services (PwC), Travel/Tech (trivago), Software/Tech (GitHub, Spotify), Government (US GSA AI CoP)

### Key Sources
- Writer Enterprise AI Adoption Survey 2025 (n=1,600)
- Lead with AI — AI Champion Programs guide (2025)
- GitHub Resources — Activating Internal AI Champions playbook (2025)
- OpenAI Academy — The AI Champion Role (2025)
- Business Insider / promptloaded — Citi AI Accelerators (Dec 2025)
- SiliconANGLE / HR Grapevine — PwC AI Champions (June 2025, April 2025)
- trivago Careers / ZenML LLMOps — AI Ambassadors program (2024–2025)
- ACM Communications — Spotify Guilds research (peer-reviewed, 2019)
- Jeremiah Lee — Spotify's Failed #SquadGoals (2020)
- IAPP AI Governance Profession Report 2025
- McKinsey Superagency in the Workplace (Jan 2025)
- Deloitte State of AI in the Enterprise 2026
- Cambridge Spark — L3 AI Champion Apprenticeship
- GSA AI Community of Practice documentation

### Counterarguments Documented
- Champions programs can accelerate shadow AI without governance infrastructure
- Volunteer programs structurally tax the most capable/busy people
- Recognition (badges) without career substance fails to retain champions after Year 1
- The Spotify guild model was never fully implemented even at Spotify
- Not every organization needs a formal structure (sub-200 employees)
- Deloitte: Only 21% of companies have mature agent governance — champions amplify ungoverned use without proper infrastructure

### Cross-References
- **Prior Research**: `drafts/ai_value_creation_20260331/research_pack.md` — BCG (74% no tangible value, 4% at scale) and McKinsey 10-20-70 principle (70% people/process) directly motivate the champions case.

### Tags
`#ai-champions` `#ai-ambassador` `#practitioners-guild` `#community-of-practice` `#spotify-model` `#enterprise-ai` `#change-management` `#ai-adoption` `#hub-and-spoke` `#ai-coe` `#citi` `#pwc` `#trivago` `#github` `#ai-governance` `#peer-learning` `#knowledge-sharing` `#volunteer-program` `#ai-fluency` `#upskilling` `#career-development`

---

## GenAI Engineering Value — Translating AI Productivity to Dollar Outcomes
**Research Pack**: `drafts/genai_engineering_value_20260408/research_pack.md`
**Date Researched**: 2026-04-08
**Article Draft**: `drafts/genai_engineering_value_20260408/`
**Search Queries**: 22
**Sources Evaluated**: 60+

### Topic Summary
Why traditional engineering metrics (story points, velocity, lines of code) are obsolete in the AI era, and how engineering leaders can translate AI productivity investments into dollar-denominated business outcomes (revenue generated, cost reduced, retention defended) that satisfy CFOs and boards. Covers the AI productivity paradox (individual gains do not compound to company outcomes), the growing CFO/board ROI crisis, frameworks for business-value measurement, and the emerging opportunity for AI-assisted outcome measurement. Audience: CTOs and VPs of Engineering at mid-market and large enterprises.

### Key Findings
- **METR RCT (July 2025, n=16, 246 tasks)**: Experienced developers using AI tools took 19% longer to complete real tasks — despite estimating they'd be 20% faster beforehand. A 39-percentage-point perception-reality gap. Peer-reviewed equivalent rigor.
- **Faros AI Productivity Paradox (2025, n=10,000+ developers)**: AI teams complete 21% more tasks and merge 98% more PRs, but PR review time jumps 91%, bug rates increase 9%, and there is zero company-level correlation between AI adoption and better outcomes.
- **Harness AI Velocity Paradox (2025)**: AI accelerates code creation but shifts bottlenecks downstream into testing, security, and deployment — system-level delivery speed is not improving.
- **Fortune/NBER (Feb 2026)**: 89% of managers see no change in productivity (measured as sales/employee) over three years despite AI adoption rising from 61% to 71% of firms.
- **Forbes (Jan 2026)**: 56% of CEOs see zero ROI from AI.
- **Fortune (Dec 2025)**: 61% of CEOs face increasing board pressure to show AI returns.
- **Salesforce CFO Research (Aug 2025, n=not specified)**: 61% of CFOs say AI has changed how they evaluate ROI — now measuring beyond traditional metrics toward business outcomes. Top CFO AI success metrics: cost savings, revenue growth (tied #1).
- **IBM**: $4.5B annual run-rate AI productivity savings (exiting 2025), driving $12.7B free cash flow in 2024. Best available dollar-denominated AI productivity anchor.
- **LinearB (2024/2025)**: Elite DORA teams show 2.6x higher revenue growth and 2.2x higher profitability vs. low performers — strongest available delivery-to-dollar correlation.
- **Gartner**: Only 5% of orgs currently use Software Engineering Intelligence Platforms; predicted to reach 50% by 2027. By 2028, 90% of enterprise engineers will use AI code assistants.
- **Fully loaded engineer cost**: $200–250K/year in enterprise (salary + benefits + overhead + tooling). GitHub Copilot break-even at 2 hours saved/week/developer.
- **Thoughtworks case study**: AI-generated user stories lead to shorter lead times and higher quality in requirements analysis — closest published analog to AI-assisted business justification of engineering work.

### Primary Industries/Sectors Covered
Software engineering / enterprise technology, applicable cross-industry to mid-market and large enterprise CTOs

### Key Sources
- METR — Measuring AI Impact on Experienced Developer Productivity (RCT, July 2025)
- Faros AI — AI Productivity Paradox Report (2025)
- Harness — State of AI in Software Engineering (2025)
- IBM — Enterprise AI transformation earnings data (2024/2025)
- LinearB — Software Development Metrics Guide (2024/2025)
- Salesforce — CFO AI Research (August 2025)
- Forbes / Gune Yildiz — CEO AI ROI analysis (January 2026)
- Gartner — Software Engineering Business Value framework (2024/2025)
- Gartner — Top Strategic Trends in Software Engineering (July 2025)
- DORA / Google Cloud — State of AI-Assisted Software Development (2025)
- Thoughtworks — AI Requirements Analysis Case Study (2024/2025)
- Search Engine Journal — CFO 3-metrics framework (January 2026)

### Counterarguments Documented
- Attribution from engineering to revenue is genuinely difficult — no widely-adopted methodology exists
- IBM's $4.5B is enterprise-wide ops, not an isolated engineering team metric
- LinearB DORA-to-revenue correlation is from a vendor with commercial interest in DORA measurement
- METR study is small (n=16) — directionally strong but not yet enterprise-representative
- GitHub Copilot can show positive ROI — the argument is not that AI doesn't work, but that you must measure value in dollars
- Translation to dollars requires cross-functional collaboration with product, finance, and sales that engineering leaders may not have

### Cross-References
- **Prior Research**: `drafts/ai_value_creation_20260331/research_pack.md` — JPMorgan 400% ROI fraud AI, BCG 74%/4% value concentration, McKinsey 19% >5% revenue increase are all useful supporting data for the "dollars are the only metric" argument and can supplement this research pack.

### Tags
`#engineering-metrics` `#story-points` `#velocity` `#ai-productivity-paradox` `#business-value` `#dollar-outcomes` `#cto` `#cfo-roi` `#ai-roi` `#dora` `#value-stream-mapping` `#github-copilot` `#developer-productivity` `#ibm` `#metr` `#faros-ai` `#harness` `#linearb` `#gartner` `#salesforce` `#engineering-leadership` `#ai-measurement` `#user-stories` `#outcome-metrics` `#enterprise-ai`

---
