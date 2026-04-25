# Agentic Article Orchestration System

## System Overview

This is a modular, multi-agent pipeline designed to generate high-fidelity articles through specialized sub-agents. The system maintains strict separation of concerns to prevent context drift and ensure maximum alignment with the user's established voice and stance.

## Design Philosophy: Separation of Concerns

The system operates on three core separations:

1. **Content vs. Form**: The Archivist handles *what* is said (POV/Facts); the Stylist handles *how* it is said (Linguistic DNA)
2. **Logic vs. Polish**: The Critic audits the "bones" of the argument; the Editor audits the "skin" (grammar/brevity)
3. **Scouting vs. Synthesis**: The Researcher gathers raw data; the Ghostwriter transforms it into prose

## Architecture

### Knowledge Core (Memory Loop)

The Knowledge Core maintains institutional memory across articles:

- **Archivist**: Operates in three modes — (1) **Library Mode**: monitors `/library`, extracts themes and stances, updates `LIBRARY_INDEX.md`; (2) **Research Mode**: triggered automatically by the Researcher after each research task, indexes completed `research_pack.md` files into `RESEARCH_INDEX.md` for future reuse; (3) **External Library Mode**: indexes third-party articles in `/external_library` into `EXTERNAL_LIBRARY_INDEX.md`, always capturing author, publication, and date for attribution
- **Librarian**: Queries the index to provide a "POV Brief" for new topics, ensuring consistency across articles
- **Stylist**: Analyzes linguistic patterns in `/library` to dynamically update the `personal-voice` skill

### Production Team (Execution Pipeline)

The Production Team transforms research into polished articles:

- **Interviewer**: The intake agent. Surfaces relevant POV from the library, conducts a structured 3-round interview with the user to sharpen angle/audience/intent, and saves `interview_brief.md` to the draft subfolder before the pipeline begins
- **Researcher**: Uses Brave Search MCP to perform deep-dive, recursive research. Checks `RESEARCH_INDEX.md` for prior coverage before searching. Outputs `research_pack.md`, then automatically triggers the Archivist (Research Mode) to index the completed research
- **Ghostwriter**: The orchestrator. Uses POV Brief + Research Pack + `personal-voice` skill to draft outlines and manuscripts
- **Critic**: The "Skeptic." Audits for logical fallacies, evidence gaps, and argument strength
- **Fact-Checker**: The "Accuracy Guardian." Verifies factual claims against cited sources, checks statistics and quotes, and flags unsupported or inaccurate assertions before publication. Runs after Critic approves structure
- **Persona Reviewer**: Evaluates drafts from specific audience perspectives to surface blind spots and test resonance
- **Editor**: The "Polisher." Ensures brevity (15% reduction rule), mechanical perfection, and final style alignment
- **Social Media Writer**: Writes platform-specific announcement posts (LinkedIn, X/Twitter) from a finished article. Invoked after `FINAL.md` is complete. Outputs `social_posts.md` to the article's draft subfolder

### Persona System (Audience Validation)

The Persona System helps test how different audiences receive articles:

- **Persona Generator**: Creates realistic audience profiles based on role, industry, and characteristics
- **Persona Reviewer**: Embodies specific personas to provide authentic feedback from their perspective
- **Persona Library**: Collection of pre-defined personas in `.claude/personas/`

## Operational Flow: The Chain

### 1. Ingestion Phase
User adds a file to `/library` → Archivist and Stylist update the Index and Style Skill

### 2. Interview Phase (Optional but Recommended)
**Interviewer** conducts a structured intake session:
- Surfaces a short POV summary from the Librarian for user context
- Runs 3 rounds of focused questions (core idea → audience & stakes → substance)
- Saves `interview_brief.md` to the draft subfolder for use by Researcher and Ghostwriter

### 3. Discovery Phase
- **Researcher** checks `RESEARCH_INDEX.md` for prior coverage, then scouts the web for current information, then **automatically triggers the Archivist** to index the completed research pack into `RESEARCH_INDEX.md`
- **Librarian** scouts the local archive for relevant past stances

### 4. Synthesis Phase
**Ghostwriter** creates:
1. Structured outline
2. First draft incorporating POV Brief, Research Pack, and Interview Brief (if available)

### 5. The Gauntlet
**Critic** provides a "Redline Report" identifying:
- Logical fallacies
- Evidence gaps
- Weak arguments
- Inconsistencies

**Ghostwriter** revises based on critique

### 6. Fact-Check
**Fact-Checker** verifies all factual claims in the revised draft:
- Validates statistics, quotes, dates, and named sources against the research pack
- Fetches and spot-checks 3–5 key sources directly
- Flags inaccurate, misrepresented, or unsupported claims
- Outputs `fact_check.md`; corrections produce next vN.md before proceeding

### 7. Persona Validation (Optional)
**Persona Reviewer** evaluates from 2-4 audience perspectives:
- Tests how different stakeholders receive the article
- Surfaces assumptions and blind spots
- Identifies resonance and friction points
- Provides audience-specific improvement suggestions

**Ghostwriter** may revise based on persona feedback if major issues surface

### 8. Final Pass
**Editor** applies final polish:
- 15% brevity reduction target
- Grammar and mechanical perfection
- Style alignment with `personal-voice`

### 9. Distribution (Optional)
**Social Media Writer** generates announcement posts:
- LinkedIn post (150–250 words, primary + alternate)
- X/Twitter post (280 chars, single post + thread option)
- Saved to `social_posts.md` in the article subfolder

## Directory Structure

```
/agentic_writer/
├── .claude/
│   ├── agents/          # Sub-agent prompt templates
│   └── skills/
│       └── personal-voice/  # Linguistic guardrails
├── library/             # The author's own finished articles
├── external_library/    # Third-party articles as source material (must be attributed)
├── drafts/              # Work in progress articles
│   └── [topic]_YYYYMMDD/    # Topic-specific subfolder with date stamp
│       ├── interview_brief.md
│       ├── research_pack.md
│       ├── pov_brief.md
│       ├── outline.md
│       ├── v1.md
│       ├── critique.md
│       ├── v2.md
│       ├── fact_check.md
│       ├── vN.md         # Additional versions as revisions accumulate
│       ├── FINAL.md      # Always the current best version (see versioning protocol)
│       └── social_posts.md  # Platform-specific announcement posts (optional)
├── LIBRARY_INDEX.md          # Semantic index of author's own work (POV/stances)
├── EXTERNAL_LIBRARY_INDEX.md # Index of third-party source material
├── RESEARCH_INDEX.md         # Index of all completed research packs (evidence/data)
├── TOPICS.md                 # Backlog of article ideas with status tracking
└── CLAUDE.md                 # This file
```

### Draft Organization

Each article gets its own subfolder in `/drafts/` using the pattern:
- **Format**: `[topic]_YYYYMMDD/`
- **Example**: `ai_regulation_20260329/`

This structure:
- Groups all files for one article together
- Allows multiple drafts of the same topic (different dates)
- Maintains clear chronological ordering
- Simplifies file management and cleanup

## Usage Patterns

### Starting a New Article

When starting a new article, create a subfolder using today's date:
- **Format**: `/drafts/[topic]_YYYYMMDD/`
- **Example**: `/drafts/ai_regulation_20260329/`

Then follow the pipeline:

1. **Interview** (recommended): Invoke Interviewer agent with topic → `interview_brief.md`
2. **Research**: Invoke Researcher agent with topic + interview brief → `research_pack.md` (Researcher automatically triggers Archivist to index into `RESEARCH_INDEX.md`)
3. **Brief**: Invoke Librarian to get POV Brief → `pov_brief.md`
4. **Outline**: Invoke Ghostwriter to create structure → `outline.md`
5. **Draft**: Invoke Ghostwriter with research, POV, and interview brief → `v1.md`
6. **Critique**: Invoke Critic to review draft → `critique.md`
7. **Revise**: Ghostwriter addresses critique → `v2.md`
8. **Fact-Check**: Invoke Fact-Checker to verify claims → `fact_check.md` (corrections → `v3.md` if needed)
9. **Persona Review** (optional): Test with 2-4 audience perspectives → `persona_review_[name].md`
10. **Polish**: Invoke Editor for final pass → `FINAL.md`
11. **Distribute** (optional): Invoke Social Media Writer → `social_posts.md`

All files for this article stay together in the topic subfolder.

### FINAL.md Versioning Protocol

`FINAL.md` is the canonical, publication-ready artifact for an article. It is always the current best version. When the Editor produces a new final from an existing one:

1. The current `FINAL.md` is saved as the next `vN.md` (preserving the prior state)
2. The new polished draft becomes `v(N+1).md`
3. `FINAL.md` is overwritten with the new content

This ensures `FINAL.md` is always current while the full revision history is preserved in numbered versions. No prior final state is ever lost.

### Using Persona Reviews

**Suggest Personas for Article**:
```
"Suggest personas for my [topic] draft"
```
System analyzes content and suggests 3-5 relevant audience perspectives.

**Review with Specific Persona**:
```
"Review draft from [persona-name] perspective"
```
Examples: `enterprise-cto`, `engineering-manager`, `ai-skeptic`

**Review with Multiple Personas**:
```
"Review draft from enterprise-cto, ai-skeptic, and engineering-manager perspectives"
```

**Generate Custom Persona**:
```
"Generate persona: [description]"
```
Example: `"Generate persona: CFO at manufacturing company, skeptical of tech spending"`

### Managing the Topic Backlog

`TOPICS.md` tracks article ideas in three states: **Backlog**, **In Progress**, and **Published**.

- Add a new idea: Drop it in Backlog with a working angle, audience, and any notes
- Start writing: Move it to In Progress, add the draft subfolder path
- Publish: Move it to Published, add the library filename

**Format for new entries**:
```
### [Working Title]
**Angle**: [The specific argument or frame]
**Audience**: [Who this is for]
**Notes**: [Context, source ideas, or related research]
**Added**: YYYY-MM-DD
```

### Adding to Knowledge Base

**Author's own work**:
1. Place finished article in `/library`
2. Invoke Archivist (Library Mode) to update `LIBRARY_INDEX.md`
3. Invoke Stylist to refresh voice profile

**Third-party source material**:
1. Save the article to `/external_library`
2. Invoke Archivist (External Library Mode) to update `EXTERNAL_LIBRARY_INDEX.md`
3. Archivist will capture author, publication, and date for attribution

The Researcher automatically checks `EXTERNAL_LIBRARY_INDEX.md` for relevant prior material before conducting web research.

## Required Tooling

- **MCP**: `brave-search` for web research
- **Skill**: `personal-voice` for linguistic guardrails
- **Local Files**: `LIBRARY_INDEX.md` for POV/stance indexing; `RESEARCH_INDEX.md` for research reuse; `EXTERNAL_LIBRARY_INDEX.md` for third-party source discovery; `TOPICS.md` for article idea backlog

## Quality Guardrails

1. **POV Consistency**: All drafts must align with stances in `LIBRARY_INDEX.md`
2. **Argument Strength**: Critic must approve logical structure before final edit
3. **Voice Alignment**: Editor must verify adherence to `personal-voice` skill
4. **Brevity Target**: Final draft should be ~15% shorter than first draft
5. **Evidence Standards**: All claims require citation or logical support
6. **Attribution**: Any content drawn from `/external_library` must cite the original author, publication, and date in the article's source references

## Agent Invocation

Agents are stored in `.claude/agents/` and invoked using the Task tool with appropriate sub-agent types. Each agent has specific input requirements and output formats documented in their respective template files.
