# Enterprise Knowledge Skill

## Purpose

Query an internal enterprise knowledge repository (via MCP) to supplement web research with proprietary case studies, project examples, solutions, and institutional knowledge. Saves results to the active draft folder as `presales_supplement.md` for the Researcher and Ghostwriter to use.

## Trigger

Use when the user wants to:
- Enrich a research pack with internal case studies or project examples
- Find real delivery examples that support an article's argument
- Surface relevant internal proposals, solutions, or stories for a given topic
- Run after or alongside the Researcher agent during the Discovery Phase

### User-invocable
```
/enterprise-knowledge [topic or query]
```

### Orchestrator-triggered
During the research phase, if an enterprise knowledge MCP is configured, the orchestrator may invoke this skill before or after the Researcher agent to add internal evidence to the pack.

## Execution

Spawn a `general-purpose` agent with the following prompt, substituting `[QUERY]` with the user's topic and `[DRAFT_PATH]` with the active draft subfolder path:

```
You are an enterprise knowledge researcher. Your job is to query the internal enterprise knowledge repository using the available MCP tools and produce a structured supplement to the web research pack.

Available MCP tool categories to query (use whichever are relevant to the topic):
- Case studies: real client engagement examples and measurable outcomes
- Projects / solutions: delivery projects and packaged solution offerings
- Stories / proposals: sales narratives and proposal content
- Q&A / knowledge base: internal policy and institutional knowledge

Query: [QUERY]

Steps:
1. Run 3-5 searches across the relevant entity types using the MCP tools
2. Evaluate relevance of each result to the query — skip low-relevance items
3. Organize findings by type (case studies, solutions, etc.)
4. Note any confidentiality or attribution constraints
5. Save results to [DRAFT_PATH]/presales_supplement.md using the output format below

Output format for presales_supplement.md:

# Enterprise Knowledge Supplement: [Topic]
**Date**: YYYY-MM-DD
**Source**: [MCP server / repository name]
**Queries run**: [count]

## Case Studies
- **[Title]**: [Brief description of client context, approach, and outcome]
  - Relevance: [Why this supports the article topic]
  - Source: [Internal reference / URL if available]

## Projects & Solutions
- **[Title]**: [Brief description]
  - Relevance: [Why this matters for the topic]

## Stories & Proposals
- **[Title]**: [Key narrative point]
  - Relevance: [Connection to article angle]

## Knowledge Base / Q&A
- **[Topic/Question]**: [Answer or key insight]

## Usage Notes
- [Any constraints on how this material can be referenced externally]
- [Suggestions for the Ghostwriter on which examples to foreground]
```

## Integration with Research Pipeline

- Runs alongside or after the **Researcher** agent
- Output (`presales_supplement.md`) is passed to the **Ghostwriter** alongside `research_pack.md`
- Ghostwriter treats internal examples as supporting evidence, subject to confidentiality constraints
- **Attribution rule**: Internal examples cited in published articles must be cleared per your organization's external communication policy

## Configuration

To enable this skill for your organization:
1. Connect your enterprise knowledge MCP server in Claude Code settings
2. Copy this skill to `.claude/skills/private/[your-org]-presales/skill.md`
3. Replace the generic MCP tool descriptions with your server's specific tool names and parameters
4. Add `.claude/skills/private/` to `.gitignore-public` to keep it out of the public repo
