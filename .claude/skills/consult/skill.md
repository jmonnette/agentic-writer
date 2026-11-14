# Consult Skill

## Purpose

Answer questions about the author's knowledge base — past stances, prior research, voice patterns, topic backlog — without creating a draft or changing any active draft state.

## Trigger

Use when the user wants to:
- Ask what their POV is on a topic
- Check if a topic has been researched before
- Explore whether an argument conflicts with past stances
- Brainstorm angles or ideas
- Query the library, research index, or topic backlog
- Any knowledge-base question that doesn't require starting or continuing a draft

## Execution

Spawn a `general-purpose` agent with the following prompt, substituting `[USER_QUERY]` with the user's actual question:

```
You are a read-only knowledge assistant for an agentic writing system. Your job is to answer questions by consulting the author's knowledge base — no files should be created or modified.

Knowledge base files to consult as relevant:
- /Users/Jeff_Monnette/Documents/code/agentic_writer/LIBRARY_INDEX.md — author's established stances and themes
- /Users/Jeff_Monnette/Documents/code/agentic_writer/RESEARCH_INDEX.md — prior research packs and evidence gathered
- /Users/Jeff_Monnette/Documents/code/agentic_writer/EXTERNAL_LIBRARY_INDEX.md — indexed third-party source material
- /Users/Jeff_Monnette/Documents/code/agentic_writer/TOPICS.md — article idea backlog and status
- /Users/Jeff_Monnette/Documents/code/agentic_writer/.claude/skills/personal-voice/skill.md — author's voice and style profile

Rules:
- Read only. Do not write, edit, or create any files.
- Answer directly and concisely. Cite which index or file you drew from.
- If the answer isn't in the knowledge base, say so clearly rather than speculating.
- If the question involves a potential stance conflict, surface both sides and flag it explicitly.

User's question: [USER_QUERY]
```

## Output

Return the agent's answer directly to the user. No preamble, no file artifacts.
