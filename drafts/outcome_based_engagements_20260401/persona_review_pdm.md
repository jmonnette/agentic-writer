# Persona Review — EPAM Principal Delivery Manager
**Reviewer**: PDM persona (10–18 years delivery, strategic account, scar tissue from scope disputes and fixed-fee overruns)
**Content reviewed**: QBR deck "The Hours Are Over" — East BU, April 2026
**Date**: 2026-04-01

---

## In-Character Review

Okay. I read the whole thing. Here's where I land.

The title grabbed me — "The Hours Are Over" — and I'll admit the AI efficiency trap argument on slide 2 is something I've been quietly thinking for 18 months. The math is real. I've watched us compress a 10-week engagement to 6 weeks and the AM celebrate it like a delivery win while I'm doing the math on what we actually invoiced. So the burning platform is legitimate, and the competitive data on McKinsey and Accenture landing these contracts — okay, I believe it. That part is solid.

Where I started to slow down was around slide 6. The taxonomy — fixed-price, output, capacity, outcome — is genuinely useful. I've been using "outcome-based" as a catch-all and conflating it with fixed-price in my head. The distinction between "output you control directly" and "outcome you only partially control" matters a lot for how I'd write scope. That was a useful frame.

Slide 8, the worked examples. The gain-sharing recommendation engine example — that's the one I want to flag. It mentions an "external event clause." I wrote that down. Where's the rest of that clause? What counts as an external event? Who decides? In my experience, the entire risk conversation for an outcome engagement lives inside that clause. The deck names it once in a worked example and never comes back to it. That's a problem.

Slides 9 and 10 are where I really paid attention, because measurement is my actual daily problem. The story points critique lands. I've been in QBRs where the client literally says "I don't know what story points mean, I just want to know if we're on track." And I've seen teams inflate estimates to hit velocity targets that were promised in a pitch. Four reasons, all true.

Then slide 10 — functional decomposition, DORA, value stream milestones, acceptance-criteria delivery, outcome proxies. Here's where I stopped and asked myself: okay, but what does the SOW section actually look like? The deck gives me names for approaches and one-line descriptions. It doesn't give me an example acceptance criteria block. It doesn't show me what a functional decomposition entry looks like in a contract. "Auth module in production. Payment integration processing transactions." Fine — but what are the acceptance conditions? Who signs off? What's the disputed-acceptance process? The deck acknowledges that milestones need to be crisp to avoid disputes, and then stops exactly there. That's the one thing I need and it's not here.

DORA as a retainer anchor — slide 10 lists this but slide 15 is where it gets expanded a bit. "Provides attribution models and executive dashboards." I work with AI/Run. I've seen the tooling. I believe it can do this. But I have not run an engagement where DORA metrics were the contractual performance SLA. I don't know what the penalty structure looks like. I don't know how we handle a degraded DORA metric when the cause is a client-side infrastructure freeze. The deck treats AI/Run as essentially solved and moves on. I'm not there yet.

The staff aug evolution on slide 11 is the most practically useful framing in the deck. Level 1 through Level 5, one-level-at-a-time — that's the message I needed. I can actually translate that into an account review conversation. I know which of my accounts are Level 1 and which might be Level 2. The checklist on slide 13 (what domain does EPAM de facto own? can that domain produce measurable outputs?) is actionable. I'm going to use that.

Slide 14, objections. I scanned for the one I actually get hit with: "Is EPAM actually set up to manage outcome risk?" The response on that slide says "partially, honestly" — which I appreciate, because it's true and it's the right thing to say. But then it says internal governance for gain-sharing contracts is "still developing." I need to know what that means for me right now. Not generically — specifically. Who do I call when I'm pricing an outcome bonus on a renewal and I need someone to approve the structure? What's the intake process? Is there a pre-defined gain-sharing term sheet I can start from? "Still developing" without a timeline or a contact is frustrating.

The one slide that would make me raise my hand in the room: slide 10. I'd stop the presenter right after the "functional decomposition" row and ask: can we see an example SOW section? Not the concept — the actual contract language. Because everything that follows in this deck — the worked examples, the retainers, the subscriptions — all of it depends on whether we can actually write the definition of done in a way that holds up. That's the unlock. And it's not in this deck.

What's missing that I'd need before I could actually run one of these engagements:

**One**: An example SOW section showing functional decomposition with acceptance criteria. Even one module, two or three criteria, the dispute resolution process. That's the thing I'd need to bring to our legal team and say "this is what we're building toward."

**Two**: Clarity on the internal governance path. Not "governance is developing" — a named process. Who do I involve when I'm proposing an outcome-linked engagement? Is there a deal review? A template? Someone in practice leadership I should be talking to before I'm sitting in front of the client?

**Three**: The external event clause, spelled out. The gain-sharing example on slide 8 mentions it and moves on. The scenario where the client redirects the team mid-quarter, or where the outcome metric is affected by factors outside our control — what does the contract protection actually look like? Client co-responsibility obligations aren't named anywhere in this deck, and that's the thing that will bite me.

**Four**: What does my weekly status report look like? Right now my weekly updates are hours burned, sprint velocity, open issues. Under a milestone or DORA retainer model, what am I reporting? What does the client-facing view look like? What does my internal utilization report look like when the team isn't billing by the hour?

**Five**: The tooling gap acknowledgment. The deck says EPAM's internal reporting is moving toward this. What that means for me today — what do I do in the gap between the commercial model I'm proposing and the internal systems catching up — is not addressed.

I'll say this: the deck is correct about the problem. The market argument is well made. The taxonomy is useful. The level model for staff aug is the most actionable thing in here. But the operational credibility — the thing that would make me feel like EPAM has worked out how to run this, not just why we should — isn't there yet. I can use this deck to have a better conversation with my AM about account strategy. I can't use it to run my first outcome-based engagement. It gives me the vocabulary; I still need the playbook.

---

## Structured Gaps Analysis

### 1. Measurement Section (Slides 9–10): Conceptual, Not Operational

**Assessment**: Partially satisfies. The story points critique is strong and the five alternatives are correctly named. The gap is that no alternative is shown at the contract level.

- Functional decomposition is described with examples ("Auth module in production") but no acceptance criteria template, no dispute process, no sign-off mechanism.
- DORA metrics are listed as a retainer anchor but the penalty/bonus structure and client-side dependency carve-outs are absent.
- The slide tells the PDM *what to use* but not *how to write it into a contract* or *how to track it operationally week-to-week*.

**What's needed**: One worked example of a functional decomposition SOW entry with 2–3 acceptance criteria and a disputed-acceptance resolution clause.

### 2. Story Points Critique — Follow-Through Gap

**Assessment**: The critique lands hard and will resonate. The follow-through is shallow.

- Slide 9 builds conviction that story points fail. Slide 10 provides names of alternatives.
- Missing: transition guidance. If the PDM is currently running a story-point-driven engagement, how do they migrate to functional decomposition mid-contract? What's the change order or amendment language?
- The deck treats the alternatives as self-evidently implementable once named. For a PDM who has never written an acceptance-criteria SOW for commercial purposes, the gap between "use functional decomposition" and "here is what it looks like" is the entire implementation problem.

### 3. Internal Tooling and Governance Gap — Named But Not Resolved

**Assessment**: The deck acknowledges EPAM's governance is "still developing" (slide 14 objection response). This is honest but operationally insufficient.

- No guidance on timesheets and utilization reporting under non-T&M models. The PDM's internal reporting is hour-native. Outcome/subscription models create a reporting translation problem that is unaddressed.
- No internal intake process identified. Who approves an outcome-linked engagement? Is there a deal structure review? A contract template repository?
- No timeline or interim guidance. "Still developing" without a bridge creates a gap between the commercial direction being set in this deck and the PDM's ability to act on it today.

### 4. Client Co-Responsibility Risk — Absent

**Assessment**: This is the most significant unaddressed gap for this persona.

- The gain-sharing example on slide 8 mentions an "external event clause" once and does not define it.
- The scenario where the client changes priorities mid-quarter, fails to deliver timely decisions, redirects the team, or does not provide agreed data access is never addressed.
- Slide 14 answers "what happens when EPAM misses the outcome target?" — it does not answer "what happens when the client's actions cause the miss?"
- The PDM's most cited risk is outcome accountability without client co-responsibility. The deck does not address this at all beyond the one external-event-clause mention.

**What's needed**: A named "client obligations" section in any outcome-based contract, with specific examples of what constitutes a client-side dependency failure, and what the remedy structure looks like (timeline extension, contract renegotiation, partial payment trigger).

### 5. Highest-Friction Slide — Slide 10

The PDM would raise their hand immediately after the functional decomposition row in slide 10. The question: "Can you show us an example SOW section?" This is the precise point where the deck transitions from building conviction to requiring the PDM to do implementation work without support. The follow-up question on DORA as a retainer anchor ("what does the penalty band look like and who adjudicates a contested metric?") is the second most likely interruption.

### 6. What's Missing Before a PDM Could Run One of These Engagements

| Gap | Severity | Current Deck Status |
|-----|----------|---------------------|
| Example SOW section with acceptance criteria | Critical | Absent |
| Internal deal governance process (who approves, what template) | Critical | "Still developing" — no specifics |
| External event clause definition and client co-responsibility obligations | Critical | Named once, not defined |
| Weekly status reporting format under non-T&M models | High | Absent |
| Internal utilization/timesheet bridge during transition | High | Absent |
| DORA retainer penalty/bonus structure example | Medium | Named, not specified |
| Transition guidance from story-point contracts mid-stream | Medium | Absent |

### Summary

The deck succeeds at building urgency and providing a useful commercial taxonomy. For a PDM audience, it falls short of operational credibility on the four issues this persona prioritizes most: what the contract looks like, how internal governance works, what happens when the client doesn't hold up their end, and what delivery operations look like week-to-week under the new models. A follow-on enablement document — or even a single slide addendum with a sample SOW entry and internal governance contact — would substantially close this gap for the delivery leader audience.
