# Agentic Writing System — Private README

This is the private repo. It contains everything: your articles, drafts, research, private personas, voice profile, and the full framework. The public repo contains only the framework — no personal content.

---

## Two-Repo Strategy

| | Private (this repo) | Public (framework repo) |
|---|---|---|
| **Contains** | Everything | Framework only |
| **Audience** | You | Anyone |
| **Push to** | `origin` | `public` (via `publish.sh`) |

---

## Directory Structure (Full)

```
agentic_writer/
├── .claude/
│   ├── agents/                   # Agent prompt templates (public)
│   ├── personas/
│   │   ├── _TEMPLATE.md          # public
│   │   ├── ai-skeptic.md         # public
│   │   ├── data-scientist.md     # public
│   │   ├── engineering-manager.md # public
│   │   ├── enterprise-cto.md     # public
│   │   ├── health-tech-cfo.md    # public
│   │   ├── lead-developer-tech-purist.md # public
│   │   ├── midmarket-cto.md      # public
│   │   ├── pe-partner.md         # public
│   │   ├── scrum-master-agile-purist.md  # public
│   │   └── private/              # PRIVATE — never published
│   │       ├── amit-soni.md      # real person
│   │       ├── ethan-matyas.md   # real person
│   │       ├── epam-account-manager.md
│   │       ├── epam-bu-head.md
│   │       └── epam-pdm.md
│   ├── scripts/                  # Utility scripts (public)
│   └── skills/
│       └── personal-voice/       # PRIVATE — your voice profile
├── library/                      # PRIVATE — your finished articles
├── external_library/             # PRIVATE — third-party source material
├── drafts/                       # PRIVATE — work in progress
├── public-docs/                  # Source for public-facing docs (see below)
│   ├── README.md                 # → published as root README.md
│   └── CLAUDE.md                 # → published as root CLAUDE.md
├── .gitignore-public             # Controls what publish.sh excludes
├── .gitignore                    # Standard git ignore
├── CLAUDE.md                     # Full system docs (private version)
├── README.md                     # Full README (private version — this system)
├── README.private.md             # This file
├── LIBRARY_INDEX.md              # PRIVATE — your POV/stance index
├── RESEARCH_INDEX.md             # PRIVATE — completed research packs
├── EXTERNAL_LIBRARY_INDEX.md     # PRIVATE — third-party source index
├── TOPICS.md                     # PRIVATE — article idea backlog
├── publish.sh                    # Publish framework to public repo
└── setup.sh                      # New-user initialization (public)
```

---

## Publishing to the Public Repo

### One-time setup
```bash
git remote add public https://github.com/yourname/agentic-writer-framework.git
```

### Publish
```bash
./publish.sh
```

The script:
1. Creates a temporary branch from current state
2. Replaces `README.md` and `CLAUDE.md` with the versions from `public-docs/`
3. Strips everything listed in `.gitignore-public`
4. Force-pushes to `public/main`
5. Deletes the temporary branch and returns you to your working branch

### Normal git workflow
```bash
# Commit personal work to private repo as usual
git add .
git commit -m "..."
git push origin main

# Publish framework updates whenever agents or docs change
./publish.sh
```

---

## Managing Private Content

### Adding a new private persona
1. Create the persona file in `.claude/personas/private/`
2. Done — `private/` is already excluded by `.gitignore-public`

### Adding any other private file or directory
1. Add the path to `.gitignore-public`
2. Done — `publish.sh` reads that file, no script edits needed

---

## Editing the Public Docs

The public repo gets its `README.md` and `CLAUDE.md` from `public-docs/`. **Do not edit the root `README.md` or `CLAUDE.md` for public-facing changes** — those are the private (full) versions.

| File | Purpose |
|---|---|
| `README.md` | Private version — full system, all references |
| `CLAUDE.md` | Private version — full system, all references |
| `public-docs/README.md` | Published to public repo — no private references |
| `public-docs/CLAUDE.md` | Published to public repo — no private references |

When the framework changes in a meaningful way, update both the private root docs and the `public-docs/` versions.

---

## What's Private and Why

| Path | Reason |
|---|---|
| `library/` | Your personal articles |
| `external_library/` | Source material you've collected |
| `drafts/` | Work in progress |
| `LIBRARY_INDEX.md` | Your POV and stances |
| `RESEARCH_INDEX.md` | Research you've commissioned |
| `EXTERNAL_LIBRARY_INDEX.md` | Your source material index |
| `TOPICS.md` | Your article pipeline |
| `.claude/skills/personal-voice/` | Your linguistic voice profile |
| `.claude/personas/private/` | Real people and company-specific personas |
| `public-docs/` | Publishing meta — not part of the framework |
| `README.private.md` | This file |

---

## Brave Search MCP Setup

The Researcher agent requires Brave Search MCP. Add to your Claude Code MCP config (`~/.claude/mcp_settings.json` or via `claude mcp add`):

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Get a Brave Search API key at: https://brave.com/search/api/
