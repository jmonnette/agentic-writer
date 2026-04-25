# Interview Brief: Building an Agentic Writing System with Claude
**Date**: 2026-04-11
**Topic**: How I built a multi-agent article pipeline using Claude — and what it taught me about agentic workflows
**Draft Subfolder**: /Users/Jeff_Monnette/Documents/code/agentic_writer/drafts/agentic_writer_20260411/

---

## The Core Idea
**Main Argument**: You can build a sophisticated, multi-agent workflow in Claude without deep coding expertise — just describe the workflow you want and iterate. The pattern transfers far beyond writing.
**Angle**: This is a first-person walkthrough of a real, working system — not a theoretical framework. The author built it conversationally, and that's the point.
**Origin**: The author built a personal agentic writing pipeline and realized the system itself was the story. The meta-lesson — that building agentic systems is more accessible than most people assume — is worth sharing.

---

## Audience & Stakes
**Primary Reader**: Knowledge workers, content creators, and professionals curious about AI agents but intimidated by the technical overhead — people who write, think, and publish as part of their work, but who aren't engineers.
**Why Now**: Agentic AI is having a moment, but most coverage is either too abstract ("agents will change everything") or too technical (API calls, orchestration frameworks). There's a gap for a grounded, practical example anyone can follow.
**Desired Outcome**: Readers should feel empowered and curious — the takeaway is "I could do something like this." Not just for writing. The pattern applies anywhere.
**Anticipated Pushback**: "This only works because you're technical enough to set it up." The response: the system was built conversationally through iteration, not engineering. The author's own build process is the counter-argument.

---

## Substance & Signals
**Key Examples/Data**:
- The full system is documented in the project itself: CLAUDE.md describes the architecture, `.claude/agents/` contains each agent, `.claude/skills/` contains the voice profile. The article can reference this structure without exposing private content.
- The build process was conversational: "I told Claude to create agents that support a workflow like: research, draft, critique, edit. Then we iterated to build the stylist and persona-driven review."
- The system includes: Interviewer, Researcher, Ghostwriter, Critic, Editor, Archivist, Librarian, Stylist, Persona Generator, Persona Reviewer, and Social Media Writer agents.
- The persona system is a highlight — readers can create custom personas relevant to their own domain (not just generic audience types).

**Controversial or Bold Claims**:
- The barrier to building agentic systems is lower than the industry makes it seem.
- You don't need to architect this up front — you can describe a workflow and let the model help you build toward it.

**Open Questions for Research**:
- Are there other publicly documented examples of personal agentic pipelines built conversationally (vs. engineered)? What makes this one distinct?
- What existing frameworks (LangGraph, CrewAI, etc.) exist, and how does a Claude-native approach compare in complexity and accessibility?
- Any data or analyst perspective on adoption barriers for agentic tools among non-technical professionals?

---

## Content Constraints
- **Do not expose anything marked private** in the project — this includes any files, configurations, credentials, or content flagged as private.
- The CLAUDE.md architecture documentation, agent prompt files in `.claude/agents/`, and skill files are available for reference when writing, but should be described at the conceptual level in the article — not quoted verbatim unless clearly non-sensitive.
- The system's directory structure and workflow can be described openly. The internal prompts and any personal library content should not be reproduced.

---

## POV Context (from Library)
The author has written extensively on AI adoption, agentic workflows, and the organizational conditions required for AI to succeed. Recurring stances include: AI as augmentation rather than replacement, the importance of probabilistic thinking over deterministic expectations, and a consistent emphasis that cultural readiness matters more than technical sophistication. The author has specifically covered multi-agent systems for software delivery and autonomous coding agents as an emerging theme. This article extends that thread into the personal productivity domain — showing what agentic workflows look like when applied by an individual rather than an enterprise team.

---

## Alignment Notes
**Consistent with past stances**: Yes — this article is a practical instantiation of themes the author has argued abstractly: agentic workflows are accessible, AI amplifies rather than replaces human work, and the barrier is more mindset than technical skill.
**Watch for**: The author's library leans heavily on enterprise and organizational contexts. This article is personal and individual-scale. The Ghostwriter should be careful not to drift into enterprise framing. Keep it first-person and approachable.

---

## Ghostwriter Guidance
- Open with the meta-moment: the author built a writing pipeline and realized the system itself was the story worth telling.
- Structure the piece as a walkthrough, not a manifesto. Show the system, explain how it was built, draw the lesson.
- The build story is important: conversational iteration, not upfront architecture. This is the democratizing insight.
- End with the generalization: this pattern is not about writing. Readers should leave thinking about where they'd apply it in their own work.
- Highlight the persona system as a particularly practical and underrated feature — suggest readers build personas specific to their domain.
- Tone: first-person, grounded, slightly self-aware (the author is writing about their own writing system). Not breathless. Not academic. Practical curiosity.
- Do not frame this as "AI will change everything." Frame it as: here's a thing I built, here's how, here's what I learned, here's why you might try it.
- Reference the project's documented architecture (CLAUDE.md, agent files) as the source of truth for system details, but describe conceptually — do not reproduce private content.

---

## Working Title Options
- "I Built an AI Writing Pipeline. Here's What It Taught Me About Agentic Systems."
- "The Writing System I Built With Claude (And Why the System Is the Story)"
- "How I Turned Claude Into a Multi-Agent Writing Team"
