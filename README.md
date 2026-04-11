# Agentic Writing System

A modular, multi-agent pipeline for generating high-fidelity articles with consistent voice and stance.

## Quick Start

### 1. Build Your Knowledge Base
```bash
# Add your existing writing samples to /library
cp your_articles/* library/

# Run the Archivist to index them
# In Claude Code: "Run the Archivist on the library"
```

### 2. Calibrate Your Voice
```bash
# Run the Stylist to analyze your linguistic patterns
# In Claude Code: "Run the Stylist to update the personal-voice skill"
```

### 3. Write an Article
```bash
# The full chain:
# 1. "Research [topic]" - Researcher agent gathers evidence
# 2. "Generate POV brief for [topic]" - Librarian provides stance guidance
# 3. "Draft article on [topic]" - Ghostwriter creates outline then draft
# 4. "Critique the draft" - Critic audits logic and evidence
# 5. "Revise based on critique" - Ghostwriter addresses issues
# 6. "Edit to final" - Editor polishes to publication quality
```

## System Architecture

### Knowledge Core (Memory)
- **Archivist**: Indexes `/library` content into `LIBRARY_INDEX.md`
- **Librarian**: Generates POV Briefs from the index for consistency
- **Stylist**: Analyzes writing patterns to update `personal-voice` skill

### Production Team (Execution)
- **Researcher**: Deep-dive web research using Brave Search
- **Ghostwriter**: Transforms research + POV into drafts
- **Critic**: Audits logic, evidence, and argument strength
- **Persona Reviewer**: Tests article from audience perspectives
- **Editor**: Polishes for publication (15% brevity rule)

### Persona System (Audience Validation)
- **Persona Generator**: Creates custom audience profiles
- **Persona Reviewer**: Evaluates drafts from specific personas
- **Persona Library**: 3 pre-defined personas + custom ones

## Directory Structure

```
agentic_writer/
├── .claude/
│   ├── agents/              # Agent prompt templates
│   │   ├── archivist.md
│   │   ├── librarian.md
│   │   ├── stylist.md
│   │   ├── researcher.md
│   │   ├── ghostwriter.md
│   │   ├── critic.md
│   │   └── editor.md
│   └── skills/
│       └── personal-voice/  # Linguistic guardrails
│           └── skill.md
├── library/                 # Your reference materials
├── drafts/                  # Work in progress
│   └── [topic]_YYYYMMDD/    # Each article gets a dated subfolder
│       ├── research_pack.md
│       ├── pov_brief.md
│       ├── outline.md
│       ├── v1.md
│       ├── critique.md
│       ├── v2.md
│       └── FINAL.md
├── LIBRARY_INDEX.md         # Semantic index
├── CLAUDE.md               # System documentation
└── README.md               # This file
```

## Workflows

### Full Article Pipeline

**Goal**: Complete article from topic to publication

Each article gets a dated subfolder: `drafts/[topic]_YYYYMMDD/`
Example: `drafts/ai_regulation_20260329/`

1. **Research Phase**
   ```
   "Research [topic] for a [word count] article"
   → Outputs: drafts/[topic]_20260329/research_pack.md
   ```

2. **Briefing Phase**
   ```
   "Generate a POV brief for [topic]"
   → Outputs: drafts/[topic]_20260329/pov_brief.md
   ```

3. **Outline Phase**
   ```
   "Create outline for [topic] article"
   → Outputs: drafts/[topic]_20260329/outline.md
   ```

4. **Drafting Phase**
   ```
   "Draft the article based on outline"
   → Outputs: drafts/[topic]_20260329/v1.md
   ```

5. **Critique Phase**
   ```
   "Critique the draft"
   → Outputs: drafts/[topic]_20260329/critique.md
   ```

6. **Revision Phase**
   ```
   "Revise draft based on critique"
   → Outputs: drafts/[topic]_20260329/v2.md
   ```

7. **Editing Phase**
   ```
   "Edit to final"
   → Outputs: drafts/[topic]_20260329/FINAL.md
   ```

### Quick Article (Compressed Pipeline)

For shorter pieces or when time is limited:

```
"Write a [word count] article on [topic] - full pipeline"
```

This invokes all agents in sequence automatically.

### Library Maintenance

**Adding New Content**:
```
1. Place files in /library
2. "Run Archivist on new library content"
3. "Run Stylist" (incremental mode - analyzes only new files)
```

**Stylist Modes**:

*Incremental Mode (Default)*:
```
"Run the Stylist"
→ Analyzes only new/modified files since last run
→ Fast, efficient for 1-3 new articles
→ Merges findings with existing patterns
```

*Full Re-Analysis Mode*:
```
"Run the Stylist in full mode"
→ Re-analyzes entire library from scratch
→ Recalculates all statistics
→ Recommended every 5-10 articles
```

**Checking What Needs Analysis**:
```bash
.claude/scripts/check_library_updates.sh
→ Shows which files have been analyzed
→ Lists modification dates
```

**Checking Stances**:
```
"What's my established stance on [topic]?"
→ Librarian searches LIBRARY_INDEX.md
```

## Agent Invocation

### Direct Invocation
```
"Run the [Agent Name] agent on [target]"
```

### Task-Based Invocation
```
"[Task description that matches agent's role]"
→ Claude will invoke appropriate agent(s)
```

### Example Commands
- "Research AI regulation" → Researcher
- "What have I written about crypto?" → Librarian
- "Update the library index" → Archivist
- "Analyze my writing style" → Stylist
- "Draft an article outline" → Ghostwriter
- "Critique this draft" → Critic
- "Review from enterprise-cto perspective" → Persona Reviewer
- "Generate persona: junior developer" → Persona Generator
- "Suggest personas for this article" → Persona System
- "Polish to final" → Editor

## Quality Standards

Every article passes through these filters:

1. **POV Consistency** (Librarian → Ghostwriter)
   - Aligns with established stances in LIBRARY_INDEX.md

2. **Argument Strength** (Critic)
   - Logic is sound
   - Evidence is sufficient
   - Counterarguments addressed

3. **Voice Alignment** (Editor)
   - Matches personal-voice skill
   - Stylistic signatures present

4. **Brevity Target** (Editor)
   - 15% reduction from first draft
   - No loss of substance

5. **Evidence Standards** (Researcher → Critic)
   - All claims supported
   - Sources credible and current

## Tips for Best Results

### Building Your Library
- **Include variety**: Different topics, formats, lengths
- **Quality over quantity**: 10 strong pieces > 50 weak ones
- **Update regularly**: Run Archivist + Stylist after additions
- **Note evolution**: Don't delete old work even if stances change

### Working with Agents

**Researcher**:
- Be specific about what you need to know
- Mention if certain sources or types of evidence are preferred
- Set time constraints if needed ("quick research" vs. "deep dive")

**Ghostwriter**:
- Provide clear word count targets
- Specify audience if not general
- Note any special requirements (e.g., "include personal anecdotes")

**Critic**:
- Trust the process—critiques improve work
- If you disagree with a critique, discuss it
- Multiple rounds are normal for complex pieces

**Editor**:
- Final arbiter of style decisions
- Will hit 15% brevity target unless justified
- Publication-ready means publication-ready

### Maintaining Voice Consistency
- Run Stylist after every 3-5 library additions
- Review personal-voice skill periodically
- Note if your style is evolving intentionally
- Update skill manually for aspirational changes

## Troubleshooting

**"My drafts don't sound like me"**
- Ensure library has sufficient samples (minimum 5-10 pieces)
- Run Stylist to update personal-voice skill
- Check that Ghostwriter is loading the skill correctly
- Consider adding more recent writing samples

**"Critique is too harsh/lenient"**
- Critic focuses on logic and evidence, not perfection
- Adjust expectations: some topics need more rounds
- If consistently off, provide feedback to calibrate

**"Research isn't finding what I need"**
- Try more specific search queries
- Specify source types (academic, news, data)
- Manually supplement if needed
- Check Brave Search is working (network issues)

**"POV Brief shows conflicts"**
- This is valuable feedback—your stances may have evolved
- Update library with more recent takes
- Explicitly address evolution in article if appropriate
- Clarify position if genuinely conflicted

## Advanced Usage

### Parallel Agent Execution
For faster processing, run independent agents in parallel:
```
"Run Archivist and Stylist in parallel on library updates"
```

### Custom Workflows
Create your own agent combinations:
```
"Research [topic A] and [topic B] in parallel, then synthesize findings"
```

### Voice Variants
Maintain multiple voice profiles for different contexts:
```
.claude/skills/personal-voice/
  ├── skill.md          # Default voice
  ├── academic.md       # Formal voice
  └── newsletter.md     # Casual voice
```

### Integration with External Tools
- Export research packs to reference managers
- Import drafts into your CMS
- Version control with git
- Backup library regularly

## Project Philosophy

This system embodies three core separations:

1. **Content vs. Form**: What is said vs. how it's said
2. **Logic vs. Polish**: Bones of argument vs. skin of prose
3. **Scouting vs. Synthesis**: Gathering data vs. crafting narrative

Each agent has a specific mandate to prevent context drift and ensure the highest quality at each stage.

## Getting Help

- **System Documentation**: See `CLAUDE.md`
- **Agent Details**: Check `.claude/agents/[agent-name].md`
- **Voice Guidelines**: Review `.claude/skills/personal-voice/skill.md`
- **Index Structure**: See `LIBRARY_INDEX.md` header

## Next Steps

1. ✅ System is set up
2. ⬜ Add samples to `/library`
3. ⬜ Run Archivist to build index
4. ⬜ Run Stylist to calibrate voice
5. ⬜ Write your first article!

---

**Ready to write? Start with**: `"Research [your topic]"`
