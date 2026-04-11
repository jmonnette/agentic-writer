# Critic Report: The AI Champions and Practitioners Guild
**Draft Version**: v1
**Critic**: Critic Agent
**Date**: 2026-04-03
**Overall Assessment**: Persuasive

---

## Executive Summary

This draft is well-researched, structurally sound, and largely aligned with the POV brief. The central argument — that sustained AI adoption requires embedded practitioners rather than governance bodies or training programs — is clear, consistently held, and supported by concrete evidence. The Citi, PwC, BCG, and GitHub data points carry real weight, and the writing hits the pragmatic, post-hype register the author's voice demands.

That said, the draft earns a "Persuasive" rather than "Compelling" rating because it has a significant blind spot: it never genuinely earns its credibility with an audience that has watched communities of practice fail. Enterprise leaders who have tried this before — and most have — will arrive at this article already skeptical. The draft asserts a lot of what this model is ("connective tissue," "cultural infrastructure") without ever confronting the well-documented failure modes that would give that skeptical reader a reason to believe *this time is different*. The research pack has robust failure-mode material that is almost entirely absent from the draft.

Three other issues undercut the argument's rigor: an imprecise causation claim on the Citi adoption number, a "6% vs. 4%" internal inconsistency, and a metrics section missing from the body of the article despite being called out as important in both the outline and POV brief. These are fixable problems in a revision, not structural failures. The argument bones are solid; they need reinforcement in two or three targeted places.

**Recommendation**: Minor to moderate revision needed. No structural rewrite required.

---

## Argument Structure Analysis

### Thesis
- **Clarity**: Strong. "A formal Champions and Practitioners Guild is the organizational infrastructure that converts isolated AI experiments into durable, enterprise-wide adoption" is clearly stated and present in the opening.
- **Placement**: Effective. Opening paragraph establishes the problem, paragraph three delivers the thesis, and the rest of the article substantiates it.
- **Provability**: Partially adequate. The draft proves the Guild *can* drive adoption (PwC, Citi case studies). It does not prove that this model works durably across different organizational sizes, industries, or maturity levels. This is a meaningful gap for an audience that has seen many such programs launch and collapse.

### Logical Flow
- **Overall Coherence**: High. The five sections follow the outline's intended order (definition → membership → leadership → participation → value), and each section sets up the next with appropriate transitions.
- **Section Transitions**: The "Who Belongs → Who Leads It" transition is the weakest. The draft moves from "cross-functional membership" to "here's the two-tier structure" without a connecting sentence that acknowledges why the leadership question is specifically raised by the membership question. It reads slightly abrupt.
- **Progressive Build**: The argument develops well through membership and leadership. The participation section feels slightly like a list rather than a developed argument. The conclusion is appropriately tight but repeats rather than synthesizes.

**Issues**:
1. The "connectors beat coders" section (paragraph 3-4 of "Who Belongs") makes a sharp claim — that technical-heavy programs underperform — but only asserts this from a single trade publication quote (CSO Online). The argument would be materially stronger if it inverted the claim: *why* does a technically fluent inner circle fail to drive broad adoption? The mechanism is missing, and it is what makes the claim convincing, not just asserted.
2. The conclusion (paragraph 3) restates the BCG data already used in Section 1 without adding new synthesis. The closing diagnostic question is the strongest moment; the preceding paragraph is filler that the article does not need.

---

## Evidence Evaluation

### Claim-by-Claim Analysis

- **"Only 4% of companies are generating substantial AI value at scale"** (Opening paragraph)
  - Evidence: BCG AI Adoption Report, October 2024
  - Strength: Robust — properly sourced, high-credibility origin, correctly attributed
  - Issue: None. This is the draft's strongest opening hook.

- **"Organizations following the 10-20-70 principle achieve 2.1x greater ROI and scale twice as many initiatives"** (Section 1, BCG framing)
  - Evidence: BCG, cited in research pack
  - Strength: Adequate
  - Issue: The draft attributes the 2.1x ROI claim to "BCG's research" but the research pack notes this data comes via a *prior* research pack (`ai_value_creation_20260331/research_pack.md`), not directly from the current one. This is a citation traceability issue: the reader has no way to verify the 2.1x claim because it isn't directly linked to the BCG source in either this draft or the current research pack. If the BCG source URL is available, it should be traceable. If not, the claim should be qualified as "BCG research cited in prior coverage."

- **"Citi's 4,200-person AI Accelerators program... drove AI tool adoption above 70%"** (Section 2, "Who Belongs")
  - Evidence: Business Insider / Lead with AI, cited in research pack
  - Strength: Adequate as stated; problematic as implied
  - Issue: This is the draft's most significant evidentiary problem. The sentence implies a causal relationship: the 4,200-person program *drove* adoption to 70%+. But the research pack source (Lead with AI / promptloaded.com) reports the adoption rate as a program outcome metric, not as a controlled causal claim. Citi is a major global bank with substantial IT resources, training infrastructure, and executive mandate. The 70%+ adoption rate may reflect those broader conditions as much as the peer champion model specifically. The draft should hedge the causal claim: "Citi's program, paired with firm-approved tools and data boundaries, coincided with 70%+ adoption" — and note the confounding context. As written, it overstates what the evidence supports for an audience of skeptical enterprise leaders.

- **"54% of PwC's global workforce now uses AI tools weekly, generating 8.7 million Copilot actions in a single month"** (Section 4, participation)
  - Evidence: PwC / Microsoft Copilot case study, October 2025
  - Strength: Robust — high-credibility primary source, specific and quantified
  - Issue: The same causation caution applies here at lower severity: PwC is a Microsoft Copilot deployment partner and the case study is produced in conjunction with Microsoft. The metric reflects Copilot adoption specifically, not AI adoption broadly. This is worth one hedging word ("in the Copilot deployment, 54%...") to be technically accurate.

- **"McKinsey's data shows only 28% of companies have direct CEO involvement in AI governance"** (Section 3, executive sponsorship)
  - Evidence: McKinsey Superagency Report, January 2025
  - Strength: Adequate
  - Issue: The draft uses this statistic as evidence that "most enterprises, champions are operating without that cover." That is a logical leap. CEO non-involvement in AI *governance* does not necessarily mean lack of executive sponsorship for champions programs. Champions programs can have strong VP- or C-1-level sponsors without CEO direct involvement in governance. The inference is plausible but not proven by this specific data point. The statistic is being made to do more work than it actually supports.

- **"71% of leaders are more likely to hire a less experienced candidate with AI skills than a more experienced one without them"** (Section 5, value proposition)
  - Evidence: Microsoft Work Trend Index 2024
  - Strength: Robust — correctly cited, high credibility
  - Issue: None with the statistic itself. However, the research pack notes that the same source also states "77% of leaders say early-career talent will get greater responsibilities with AI" — a complementary data point that is left unused and would strengthen the value-prop section materially.

- **"GitHub's published playbook suggests a time commitment of 30–60 minutes per week"** (Section 3, individual champions)
  - Evidence: GitHub Well-Architected Champion Program
  - Strength: Adequate
  - Issue: The research pack explicitly flags this as a single-source benchmark with no corroboration from actual time studies. The draft presents it without qualification. Given that this is the article's only concrete time commitment figure — and enterprise leaders will use it to assess feasibility — it should be accompanied by one hedging phrase: "GitHub's published benchmark, the most widely cited figure in the practitioner literature."

### Evidence Patterns
- **Strengths**: Evidence density is good. The draft cites named organizations with specific numbers rather than vague claims. The BCG, PwC, and Citi numbers are the strongest anchors.
- **Weaknesses**: Causation is consistently implied where correlation or association is what the source actually establishes. This is the article's systematic evidentiary vulnerability.
- **Gaps**: Three significant data points from the research pack are not used:
  1. The Writer 2025 survey finding that 77% of AI-using employees self-identify as current or potential champions — a powerful enrollment argument for the "Who Belongs" section.
  2. The trivago case study and OKR-structured participation model — cited in the outline but missing from the draft body entirely.
  3. The PwC statistic that 500,000+ hours of capacity were freed via Copilot in one month — stronger proof of business value than the action-count metric.

---

## Logical Fallacies

### Critical Issues (Fix Required)

1. **Post Hoc / Implied Causation** (Section 2, paragraph 4 — Citi claim): The draft states the Citi program "drove AI tool adoption above 70%." The research establishes correlation: a large champion program exists, and a high adoption rate exists. The research pack does not establish that the champion program *caused* the adoption rate, nor does it control for Citi's substantial non-champion investments (IT infrastructure, executive mandate, approved tool lists). For a skeptical enterprise audience, this will read as marketing if uncorrected. A sophisticated reader will immediately ask: "Would Citi have hit 70% adoption anyway given their resources and mandate?" Fix: hedge to "coincided with" or "was associated with," and acknowledge Citi's broader program context (approved tools, executive mandate) as enabling conditions.

2. **Hasty Generalization** (Section 2, "Connectors beat coders" claim): The claim that programs recruiting "data scientists and engineers" create a "technically fluent inner circle" that causes the rest of the organization not to show up is stated as a known pattern, but the only support is a single CSO Online assertion. This is a sweeping claim about why an entire category of programs fails, based on one trade publication's framing. The research pack contains richer material on this failure mode — including the CoP research on weak 1:1 connections, the Spotify guild failure, and the "ownership consolidating in too few hands" problem — none of which is technical-exclusivity specific. Fix: either cite a second source, narrow the claim ("one common failure mode"), or name the actual mechanism rather than asserting it.

### Minor Issues (Consider Addressing)

- **Circular Reasoning** (Section 1, definition): The draft argues the Guild is not a governance body because governance bodies cause people to work around them, and then uses the Guild's non-governance nature as evidence that it will be effective. The argument would be stronger if it showed *why* the Guild's specific design prevents the governance-body failure mode, rather than just asserting that it is different by definition.

- **Appeal to Authority** (Section 5, Cambridge Spark quote): "Your expertise in AI will put you above others" is quoted as a career benefit — but this quote comes from a company that sells AI champion training programs, which gives them a direct financial interest in the claim. The quote is from a promotional source and should be treated accordingly, either by acknowledging the source context or replacing it with the Microsoft or GitHub career visibility data.

---

## POV Consistency Check

**Alignment with Established Stances**: High overall. The draft is well-aligned with the author's established positions.

### Deviations
- **On Metrics**: The POV brief is explicit that the author's established view is to avoid activity metrics and measure capability transformation instead. The draft's participation section lists activities (workshops run, prompt libraries shared) but never states what the *right* metrics are for the Guild. The outline called for the trivago OKR model here. The POV brief specifically warns against "measuring activity" and calls for tracking "capability expansion." This is the draft's clearest deviation from established positioning. Fix: add a brief paragraph or sentence in the participation section stating that the Guild's success metrics should track capability growth, not event counts.

- **On Failure Modes**: The POV brief's "recurring themes" section emphasizes post-hype pragmatism and naming dysfunction clearly. The author's established voice does not avoid problems — it names them and provides the solution. The draft is notably silent on why these programs fail, which is inconsistent with the author's pattern of addressing the "this is how it goes wrong" case head-on. The research pack has extensive failure-mode material that would deepen the draft significantly.

- **On Maturity Progression**: The outline called for a "3- or 4-stage maturity model (Seed → Structured → Scaled → Embedded)." The draft does not include one. The POV brief identifies the maturity model framing as a signature argumentative pattern in the author's work. Its absence is a meaningful structural gap — especially for an audience of enterprise leaders who want a progression, not a binary.

### Voice Alignment
- The draft successfully avoids the proscribed vocabulary (governance, compliance, mandates, approval gates) with one exception: the Canada note mentions "governance activities within the Guild" — the only time the word "governance" appears in an un-negated context. This is a minor issue given the sentence's regulatory necessity, but worth reviewing.
- The post-hype register is well-maintained throughout.
- The "slightly impatient" tone is present, particularly in the program lead paragraph ("That's not a leadership failure — it's physics") and the closing diagnostic. These are the draft's strongest voice moments.

---

## Counterargument Handling

### Objections Addressed
- **"This is just a committee"**: Addressed directly and well in Section 1. The "Not a Committee. Cultural Infrastructure." header does rhetorical work.
- **"Why fund a community instead of buying better tools?"**: Adequately addressed via the BCG 10-20-70 framing.
- **"Mandatory participation would be more effective"**: Addressed in the membership section (resentful participants vs. advocates).

### Objections Missing

These are predictable objections from the stated audience (enterprise leaders who have watched CoP programs fail) that the draft does not address:

1. **"We tried this before and it died."** This is the most probable first objection from the target audience. The draft never directly confronts the structural reasons communities of practice fail (no executive mandate, time constraints killing engagement, burnout in the core group, ownership consolidating). The research pack has detailed material on all of these. Readers who have watched a prior CoP quietly expire will not be reassured by a draft that doesn't acknowledge why that happens. A one-paragraph "failure mode" treatment — ideally before the conclusion — would make the argument significantly more durable.

2. **"Champions become shadow IT vectors without governance infrastructure."** The research pack flags this explicitly as a counterargument. The draft partially addresses it (champions need "something safe to champion," approved tools, clear policies) but buries it in the leadership section without naming the specific failure mode clearly.

3. **"This model scales at Citi and PwC. We have 1,200 employees."** Scale applicability is mentioned indirectly but never stated. At what organizational size does a formal Guild structure make sense? The research pack notes that for organizations under 200 employees, a formal champions program may be unnecessary overhead. Enterprise leaders at mid-size organizations will wonder whether this is designed for them or for the Fortune 50.

4. **"The Spotify guild model — which this borrows from — failed at Spotify itself."** The research pack contains the Jeremiah Lee primary source on this. The draft does not mention the Spotify guild failure at all. For an audience in enterprise technology, the Spotify model is well-known. Not addressing its documented failure looks like the draft is either unaware of it or deliberately omitting it.

### Quality of Responses
Where the draft does engage counterarguments, the responses are adequate but brief. The governance-body concern gets one sentence of mechanism ("people work around it instead of with it") before the draft moves on. The reader is not shown *why* this happens or *what specifically* makes the Guild structurally different.

---

## Gap Analysis

### Logical Gaps
1. **The mechanism of peer adoption is asserted, not explained.** The central claim — that embedded practitioners drive adoption more effectively than training programs or mandates — is stated with supporting examples but never mechanistically explained. *Why* does peer trust create adoption where top-down mandates fail? The research pack has this: employees don't adopt tools because IT tells them to; they adopt when a trusted colleague shows them how it works in their context. One sentence of mechanism would convert an assertion into an argument.

2. **Scale applicability is unexplained.** The article moves from "Citi (182,000 employees)" to "a 2,000-person organization" without addressing what changes at different scales. The 5-10% density target and 1:10-20 ratio are given as universal benchmarks. But the appropriate program design for a 500-person company is different from a 50,000-person company. The draft treats the model as scale-invariant without saying so or justifying it.

3. **"What success looks like" is entirely absent.** The article explains how to build the Guild and what it looks like in operation, but never tells leaders how to know if it's working. What does a healthy Guild produce? Adoption rates? Documented use cases? Capability range expansion? This gap is significant for the target audience, who will be asked to justify headcount and program costs. A single paragraph or even a brief list would address this.

### Missing Context
- The draft introduces the Guild as a "practitioner community layer" and the "field layer of a CoE" without explaining what CoE stands for in the same paragraph. While the audience likely knows the term, the first usage should spell it out, particularly given the article's dual US/Canadian scope and the possibility that CoE structures are not yet in place at many reader organizations.

### Unexplored Implications
- If only 4% of companies are generating substantial AI value at scale, and if the Guild is the organizational infrastructure that drives this — then what does the article's advice imply about the *95% of organizations currently not building this*? The competitive distance argument is present in the conclusion but understated. The draft says the gap "is not academic" but does not land the specific implication: companies that fail to build this infrastructure in the next 18-24 months may be building a competitive gap that is difficult to close.

---

## Section-by-Section Notes

### Opening
- **Hook Effectiveness**: Strong. The temporal-contrast structure ("Here is the pattern most enterprises know by heart") creates immediate recognition. The 4% statistic is well-placed.
- **Context Provided**: Adequate. The "not a technology problem" pivot is well-executed.
- **Thesis Introduction**: Well-handled. Clear and early.
- **Canada Note**: Appropriately brief and non-disruptive. Well-placed.

### Section 1: Not a Committee. Cultural Infrastructure.
- **Main Point Clarity**: Very strong. The header does the work and the body substantiates it.
- **Evidence Strength**: Adequate. BCG 10-20-70 is the right framing device.
- **Logical Issues**: The circular-reasoning note above applies here (see Logical Fallacies). The CoE explanation ("If you don't have a CoE yet, the Guild is often how you build toward one") is the section's strongest line — it answers a reader question proactively.
- **Suggestions**: Consider one sentence acknowledging that governance bodies fail for a structural reason, not just because they're perceived as bureaucratic. This converts assertion into mechanism.

### Section 2: Who Belongs — Connectors, Not Coders
- **Main Point Clarity**: Strong. "Curiosity and willingness to help peers — not technical expertise" is a clear, memorable statement.
- **Evidence Strength**: Adequate for the connector framing; thin for the "technical inner circle fails" claim. The Citi adoption number causation problem applies here.
- **Logical Issues**: Hasty generalization (see above). Missing the Writer survey data point (77% of AI-using employees self-identify as current or potential champions) — this would strengthen the "natural supply" argument and make the 5-10% density target feel achievable rather than aspirational.
- **Suggestions**: Add the Writer survey enrollment statistic. Add one sentence of mechanism for why connectors outperform technical experts in adoption contexts.

### Section 3: Who Leads It — and Is It a Full-Time Job?
- **Main Point Clarity**: Very strong. The "yes for the program lead, no for individual champions" framing is clear and directly answers the question the header poses.
- **Evidence Strength**: Strong on structure; the McKinsey governance-involvement statistic is being used imprecisely (see Evidence Evaluation above).
- **Logical Issues**: The McKinsey 28% misuse is this section's main problem.
- **Suggestions**: Replace or qualify the McKinsey governance-involvement statistic. The point it is trying to make (most champions operate without executive air cover) is real and worth keeping — it just needs a different or more carefully framed supporting data point.

### Section 4: What Participation Looks Like
- **Main Point Clarity**: Strong. "The unit of impact is one workflow changed in one colleague's daily work" is the article's best single sentence.
- **Evidence Strength**: Good on PwC. Missing: trivago OKR model (called for in outline), the 500,000-hours PwC capacity metric, and — most critically — any language about metrics or what healthy participation produces over time.
- **Logical Issues**: The psychological safety paragraph is present but brief. "Members need explicit cover to experiment, including time and permission to fail without consequences" names the design requirement but does not say how to build it. What does "explicit cover" look like in practice? The outline called for "failure budgets" as a specific mechanism — this is missing.
- **Suggestions**: Add the failure-budget concept concretely (designated experimentation time, no-blame failure reporting). Add trivago OKR model or equivalent to connect participation to visible organizational value. Add one line about metrics: what a healthy Guild produces, measured in capability terms not event counts.

### Section 5: What You Get Out of It
- **Main Point Clarity**: Strong.
- **Evidence Strength**: Good. The Microsoft statistic is the strongest anchor.
- **Logical Issues**: The Cambridge Spark quote carries a promotional source problem (see Logical Fallacies). The additional Microsoft data point (77% of leaders say early-career talent will get greater responsibilities with AI) is unused and stronger than what is cited.
- **Suggestions**: Supplement or replace the Cambridge Spark quote with the unused Microsoft data point. Note: "early signs" qualifier is appropriately humble and consistent with the research pack's flagged knowledge gaps.

### Conclusion
- **Synthesis Quality**: Partial. The diagnostic question at the end is excellent — memorable, specific, actionable, and perfectly voiced. The two paragraphs preceding it re-tread earlier points without advancing the argument.
- **New Information**: The conclusion does not introduce new points, which is correct. But it also does not synthesize the parts into a new whole — it recaps.
- **Resonance**: The closing diagnostic ("you don't have a champions program — you have a Slack channel") is the article's single most memorable line. It earns its placement. The rest of the conclusion is weaker than it needs to be to set up that payoff.
- **Suggestions**: Tighten the first two concluding paragraphs. Consider incorporating one sentence about what the competitive distance looks like in 18-24 months for organizations that don't build this infrastructure — this gives the "urgency without FOMO" the outline calls for.

---

## Strengths to Preserve

1. **The "unit of impact" line** ("The unit of impact is one workflow changed in one colleague's daily work. Not a webinar. Not a slide deck.") — precise, voicey, and the clearest statement of the article's practical stakes. Do not dilute.
2. **The program lead "physics" line** ("That's not a leadership failure — it's physics") — sharp and exactly in the author's register. Keep.
3. **The closing diagnostic question** — the best single line in the draft. The entire conclusion should be built to land there.
4. **The CoE relationship treatment in Section 1** — the "If you don't have a CoE yet, the Guild is often how you build toward one" framing answers a real reader question and is one of the draft's most distinctive moments.
5. **The "Connectors, Not Coders" framing** — well-positioned as a section header and reinforced in body. Strong.

---

## Priority Revisions

### Critical (Must Fix)

1. **Citi causation claim** (Section 2, paragraph 4): Change "drove AI tool adoption above 70%" to language that reflects the association rather than asserts causation. Add one sentence of context acknowledging Citi's enabling conditions (approved tools, executive mandate, data boundaries). This is the article's most likely credibility vulnerability with a sophisticated audience.

2. **Missing failure-mode content** (no current location — needs new paragraph): Add a focused treatment of why these programs typically fail — time constraints, no executive mandate, burnout in the core group, ownership consolidating. This is the material that tells skeptical "we tried this before" readers that the author knows what they've seen, and that this design addresses those failure modes specifically. It belongs either at the end of Section 3 (as a "here's what kills these programs, and here's how the structure prevents it" move) or as a brief stand-alone block before the conclusion.

3. **Metrics gap** (Section 4): Add language — even a single sentence — about what healthy Guild participation should produce in capability terms, not activity counts. This is a POV brief alignment issue and an audience credibility issue. Enterprise leaders will budget against measurable outcomes.

### Important (Should Fix)

4. **McKinsey statistic misuse** (Section 3, paragraph 4): The 28% CEO governance-involvement figure does not support the specific claim being made about champion program air cover. Either replace it with a more precisely applicable data point or narrow the claim to match what the statistic actually supports.

5. **Unused data points** (Sections 2 and 5): Incorporate the Writer survey enrollment data (77% of AI-using employees self-identify as potential champions) in Section 2, and the additional Microsoft data point (77% of leaders / expanded responsibilities) in Section 5.

6. **Failure-budget mechanism** (Section 4): "Failure budgets" is in the POV brief as a signature concept. Name it explicitly and give it one concrete operational definition (e.g., "designated sprint time for experiments with no-blame reporting on what didn't work"). As written, psychological safety is named as a "structural design choice" without the structural design being specified.

7. **Cambridge Spark quote provenance** (Section 5): Acknowledge the promotional context of this source, or replace it with the Microsoft data point already in the research pack.

### Nice to Have (Consider)

8. **Maturity progression** (missing from draft): The outline and POV brief both called for a maturity model (Seed → Structured → Scaled → Embedded). Its absence means the article ends with "do you have this or not" rather than "here is how to progress toward it." Adding even a brief three-stage model would strengthen the article's utility for leaders at different organizational maturity levels.

9. **Scale qualification**: A single sentence clarifying at what organizational size a formal Guild structure is appropriate (suggested threshold: 1,000+ employees with multiple business units) would preempt the "is this for organizations like mine?" objection from mid-market readers.

10. **Spotify guild failure acknowledgment**: One sentence acknowledging that even the model's origin story (Spotify) documented implementation challenges would inoculate the argument against the predictable "but Spotify's guild model failed" objection from technically literate readers.

11. **CoE spelled out on first use**: Small but worth doing for clarity.

---

## Questions for Ghostwriter

1. Is there a reason the trivago OKR model — called out in the outline — was not included in the participation section? The research material is robust and it would address the metrics gap directly.
2. The POV brief recommends opening with the "6% failed to scale" figure, but the draft uses BCG's 4% figure instead. Both appear in the library/research. Was the 4% chosen deliberately (stronger/more specific) or was the 6% omitted by oversight?
3. The outline called for a maturity progression model (Seed → Structured → Scaled → Embedded). Was this omitted for word count reasons, or is there a case for leaving it out that the Ghostwriter wants to preserve?
4. The draft's Canada note mentions "governance activities within the Guild" — the only un-negated use of "governance" in the article. This seems like a necessary exception, but worth confirming that it aligns with the author's intent given the POV brief's strong avoidance of governance framing.

---

## Verdict

**Logic Rating**: Adequate (strong structure; causation claims need tightening in two places)
**Evidence Rating**: Sufficient (well-sourced; three meaningful data points from the pack are unused; one data point is being used beyond what it supports)
**Argument Strength**: Persuasive

**Ready for Editor**: No

**Estimated Revision Scope**: Moderate revision. The structural bones are sound and the voice is well-calibrated. The revision work is concentrated in four areas: (1) a failure-mode paragraph to address the skeptical reader's prior experience, (2) causation hedging on the Citi claim, (3) a metrics statement in the participation section, and (4) use of the three currently-unused data points from the research pack. No section needs to be rewritten. Total estimated addition: 150-200 words, with corresponding tightening of the conclusion's first two paragraphs.
