# Persona Library

This directory contains persona definitions used by the Persona Reviewer agent to provide audience-specific feedback on draft articles.

## Quick Start

**Test your draft from different perspectives:**
```bash
"Review the draft from enterprise-cto perspective"
"Suggest personas for my AI coding tools article"
"Generate persona: CFO at manufacturing company"
```

## System Overview

The Persona System helps you understand how different audiences will receive your articles by:
- **Testing Resonance**: Does your message land with the target audience?
- **Surfacing Blind Spots**: What assumptions are you making?
- **Identifying Barriers**: Where does jargon or complexity lose readers?
- **Validating Value**: Is the benefit clear for each stakeholder?

### Two Agents

**Persona Reviewer** (`.claude/agents/persona-reviewer.md`)
- Embodies specific audience personas
- Provides authentic feedback from their perspective
- Identifies what works, what confuses, what concerns them
- Outputs detailed review reports

**Persona Generator** (`.claude/agents/persona-generator.md`)
- Creates custom persona definitions on demand
- Builds psychologically realistic profiles
- Can generate from role descriptions or article topics
- Saves personas to this library for reuse

## Available Personas

### Technical Roles
- **ai-skeptic**: Senior engineer skeptical of AI hype, values production reality and engineering rigor
- **engineering-manager**: Team lead balancing delivery, team health, and technical quality

### Leadership Roles
- **enterprise-cto**: C-level technology executive focused on strategy, ROI, and risk management

## Using Personas

### Review a Draft with Specific Persona
```
"Review the draft from [persona-name] perspective"
```
Example: `"Review the draft from enterprise-cto perspective"`

### Suggest Personas for an Article
```
"Suggest personas for my [topic] article"
```
The system will analyze your draft and suggest 3-5 relevant personas based on:
- Article topic and content
- Your established audience (from LIBRARY_INDEX.md)
- Personas likely to have strong opinions or valuable feedback

### Review with Multiple Personas
```
"Review the draft from enterprise-cto, engineering-manager, and ai-skeptic perspectives"
```
You'll receive separate reviews from each persona viewpoint.

## Creating Custom Personas

### Option 1: Generate from Description
```
"Generate a persona: [role description]"
```
Example: `"Generate a persona: CFO at healthcare company, skeptical of technology spending"`

The Persona Generator will create a comprehensive persona definition and save it to this directory.

### Option 2: Generate for Article Topic
```
"Generate personas for my [topic] article"
```
The system will suggest and create relevant personas based on your article content.

### Option 3: Manual Creation
1. Copy `_TEMPLATE.md` to a new file
2. Fill in all sections with realistic details
3. Save as `[persona-name].md` in this directory
4. Use with Persona Reviewer

## Persona Naming Conventions

- Use lowercase with hyphens: `enterprise-cto.md`
- Be descriptive but concise: `junior-developer.md` not `early-career-software-engineer.md`
- Include key characteristic if needed: `ai-skeptic.md` not just `engineer.md`

## Persona Selection Guide

### For Enterprise/Process Articles
Good personas:
- enterprise-cto (strategic business perspective)
- engineering-manager (tactical implementation perspective)

### For AI/ML Technology Articles
Good personas:
- ai-skeptic (technical reality check)
- enterprise-cto (business viability check)
- engineering-manager (adoption practicality check)

### For Developer Productivity Articles
Good personas:
- engineering-manager (team impact perspective)
- junior-developer (early-career perspective)
- ai-skeptic (tool skepticism)

### For Contrarian Perspectives
Always include at least one persona who would:
- Disagree with your thesis
- Have opposite priorities
- Face different constraints

This strengthens arguments by surfacing blind spots.

## Persona Review Workflow

### Integration with Main Pipeline

**Standard Pipeline** (with personas):
1. Research → POV Brief → Outline → Draft v1
2. **Critic** reviews logic and evidence → v2
3. **Persona Reviews** (2-4 perspectives) → identify blind spots
4. Revise if major issues surface → v3 (optional)
5. **Editor** final polish → FINAL

**When to Use**:
- ✅ After Critic (logic is sound) but before Editor (final polish)
- ✅ When writing for specific stakeholder groups
- ✅ When testing contrarian/provocative arguments
- ✅ When ensuring message resonates across technical/non-technical divide
- ❌ Skip for purely technical tutorials
- ❌ Skip if just testing structure (use Critic instead)

### Step-by-Step Process

1. **Draft Complete**: Finish v1 or v2 of article
2. **Select/Generate Personas**: Choose 2-4 relevant perspectives
3. **Run Reviews**: Invoke Persona Reviewer for each
4. **Analyze Feedback**: Look for patterns across personas
5. **Revise**: Address major concerns before final edit

### Output Files

Reviews save to your draft folder:
```
drafts/[topic]_YYYYMMDD/
├── v2.md
├── persona_review_enterprise-cto.md
├── persona_review_ai-skeptic.md
├── persona_review_engineering-manager.md
└── FINAL.md
```

Each review includes:
- Initial impression & hook effectiveness
- What worked / didn't work / confused them
- Key concerns and unanswered questions
- Assumptions they don't share
- Would they finish reading? Share it? Act on it?
- Specific recommendations for that audience

## Strategic Use Cases

### Test Business/Technical Balance
```
Review with: enterprise-cto + engineering-manager + ai-skeptic
```
- **enterprise-cto**: Business viability and ROI perspective
- **engineering-manager**: Practical implementation perspective
- **ai-skeptic**: Technical skepticism and reality check

→ See if you're too technical, too business-focused, or well-balanced

### Find Your Blind Spots
Pick personas who would **disagree** with your thesis:
- Writing about AI adoption? Use `ai-skeptic` to stress-test
- Advocating for process change? Use persona resistant to change
- Promoting new tool? Use persona burned by tool churn

→ Strengthens arguments by addressing real objections upfront

### Test Accessibility
Use personas with different expertise levels:
- Technical expert + domain novice
- Practitioner + executive
- Early-career + senior veteran

→ Ensures article reaches intended audience without losing them

### Validate Target Audience Fit
Use personas representing your intended readers:
- Check if value proposition is clear to them
- Verify examples resonate with their context
- Confirm jargon level is appropriate

→ Confirms article will achieve its goal

## Tips for Effective Use

**Don't Overdo It**:
- 2-4 personas per article is usually sufficient
- More personas = more time to process feedback
- Diminishing returns after 4 perspectives

**Choose Deliberately**:
- Pick personas who would actually read this topic
- Include at least one skeptical/challenging perspective
- Consider perspectives you naturally wouldn't think of
- Avoid redundant personas (don't need 3 variants of "engineer")

**Use Reviews Strategically**:
- For technical articles: Include non-technical stakeholder
- For business articles: Include hands-on practitioner
- For contrarian pieces: Include persona who'd disagree
- For adoption/change topics: Include skeptical resister

**Iterate Wisely**:
- If persona feedback reveals major issues, revise and re-review
- Some personas might become irrelevant after revisions
- Don't feel obligated to address every single persona concern
- Look for patterns across personas (multiple flag same issue = fix it)

**Balance Feedback**:
- You can't please everyone - some persona needs conflict
- If enterprise-cto wants more business context and ai-skeptic wants more technical depth, you may need to choose your primary audience
- Use conflicting feedback to sharpen your focus, not dilute your message

## Maintaining the Library

### When to Add Personas
- You're writing for a new audience type
- Existing personas don't capture a valuable perspective
- You want contrarian feedback on a specific topic

### When to Update Personas
- Industry dynamics change (e.g., economic shifts affect CFO priorities)
- New constraints emerge (e.g., regulatory changes)
- Feedback patterns suggest persona isn't realistic

### When to Archive Personas
- No longer writing for that audience
- Persona overlaps too much with existing ones
- Persona wasn't providing valuable distinct perspective

---

**Current Library Size**: 3 personas
**Last Updated**: 2026-03-29
