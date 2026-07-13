# LaTeX Precision Skill

A comprehensive [Claude Code](https://claude.ai/code) skill pack for precise LaTeX typesetting — from quick document authoring to complex multi-pass compilation, covering the full workflow of Chinese and English LaTeX document production.

## Overview

This skill pack turns Claude Code into a LaTeX typesetting assistant. It provides structured knowledge covering the entire lifecycle of a LaTeX project, organized in a progressive-disclosure architecture:

- **Layer 1** — `SKILL.md` (~90 lines): Main entry with routing table and Chinese template
- **Layer 2** — 11 topic files: Each covers one specific area (compile, tables, math, etc.)
- **Layer 3** — `wiki/` and `scripts/`: On-demand reference and automation

### Core capabilities

| Topic | File | Coverage |
|-------|------|----------|
| Environment setup | [environment.md](.claude/skills/latex-precision-skill/environment.md) | TeX Live / MiKTeX installation, engine comparison (pdfTeX / XeTeX / LuaTeX), TDS structure, font configuration, `tlmgr` package management |
| Compilation | [compile.md](.claude/skills/latex-precision-skill/compile.md) | Single/multi-pass compilation, `latexmk` automation, build scripts (PowerShell / Bash / Makefile), log analysis, Unicode character fix |
| Document structure | [document-structure.md](.claude/skills/latex-precision-skill/document-structure.md) | Document classes, `ctex` Chinese classes, preamble setup, sectioning, multi-file projects, page geometry |
| Text formatting | [text-formatting.md](.claude/skills/latex-precision-skill/text-formatting.md) | NFSS font system (encoding/family/series/shape), `fontspec`, Chinese fonts via `ctex`, lists, theorem environments, verbatim, footnotes |
| Math formulas | [math-formulas.md](.claude/skills/latex-precision-skill/math-formulas.md) | Inline/display math, Greek letters, operators, matrices, multi-line equations (align/gather/multline), cases, spacing |
| Tables | [tables.md](.claude/skills/latex-precision-skill/tables.md) | tabular, array, merged cells, tabularx, longtable, booktabs (three-line tables), colortbl |
| Graphics & floats | [graphics.md](.claude/skills/latex-precision-skill/graphics.md) | graphicx, figure/table placement (`[htbp]`, `[H]`), subcaption, wrapfig, xcolor, TikZ basics |
| Cross-references | [cross-refs.md](.claude/skills/latex-precision-skill/cross-refs.md) | `\label`/`\ref`, hyperref, cleveref, BibTeX / biblatex + biber, makeindex, glossaries |
| Custom macros | [macros.md](.claude/skills/latex-precision-skill/macros.md) | `\newcommand`, `\NewDocumentCommand` (xparse), `\newenvironment`, `.sty` / `.cls` authoring, conditionals |
| Troubleshooting | [error.md](.claude/skills/latex-precision-skill/error.md) | 40+ common errors, warnings (overfull/underfull boxes, missing characters), debugging techniques, MWE creation |
| Beamer slides | [beamer.md](.claude/skills/latex-precision-skill/beamer.md) | Frame structure, themes (Madrid, CambridgeUS, etc.), blocks, overlays, columns, Chinese beamer with `ctexbeamer` |

### Reference files (wiki/)

| File | Content |
|------|---------|
| [commands-reference.md](.claude/skills/latex-precision-skill/wiki/commands-reference.md) | Quick lookup of document structure, sectioning, and formatting commands |
| [packages-reference.md](.claude/skills/latex-precision-skill/wiki/packages-reference.md) | Quick lookup of essential packages by category |
| [symbols-reference.md](.claude/skills/latex-precision-skill/wiki/symbols-reference.md) | Greek letters, relational operators, arrows, miscellaneous symbols |
| [font-encoding.md](.claude/skills/latex-precision-skill/wiki/font-encoding.md) | NFSS four-axis font coordinate system reference |
| [ctex-guide.md](.claude/skills/latex-precision-skill/wiki/ctex-guide.md) | ctex document class and package options for Chinese typesetting |

### Scripts

| Script | Purpose |
|--------|---------|
| [fix_unicode.py](.claude/skills/latex-precision-skill/scripts/fix_unicode.py) | Scans `.tex` files and inserts `\newunicodechar` mappings for common Unicode characters (≤, ≥, λ, •) missing in Latin Modern Roman |

### Agent configuration

An optional [latex-writer agent](.claude/agents/latex-writer.md) is included for LaTeX document work. This is a **dedicated sub-agent profile** that defines how Claude operates on `.tex` files, as opposed to the skill files which define what LaTeX knowledge to apply.

**How it differs from the skill:** The skill files (`SKILL.md` + 11 topic files) are a knowledge base — they tell Claude the syntax and best practices of LaTeX. The agent is a behavior specification — it tells Claude how to handle `.tex` documents.

**Core rules enforced by the agent:**

| Rule | Detail |
|------|--------|
| Line-by-line editing | No Python/sed/awk batch processing on `.tex` files — every change must be manual via Read/Write/Edit |
| Backup before edit | Always `cp file.tex file.tex.bak` before modification |
| Context7 integration | Uses MCP to look up package documentation rather than relying on memory |
| Default review mode | Read-only by default; enters edit mode only when explicitly asked |
| Tabularray key order | `hlines`/`vlines` must precede `hline{1,Z}`/`vline{1,Z}` to avoid override |
| Chinese specifics | Fixed XeLaTeX engine, `ctex` document classes, Chinese font commands, `\setstretch` for line spacing |
| Source formatting | Keep lines under 100 chars, one sentence per line for better diffs |

> **Recommendation:** The latex-writer agent is configured to use Context7 MCP for verifying LaTeX syntax, finding the correct package, and understanding best practices. This ensures answers are backed by current documentation rather than training data. The agent will automatically resolve package names and query documentation — no manual setup needed beyond having the Context7 MCP server installed in Claude Code.

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- **Recommended**: [TeX Live](https://tug.org/texlive/) distribution (cross-platform, actively maintained)
- **Alternative**: MiKTeX (Windows-only, legacy CTeX Suite)

For Chinese typesetting, a full or medium TeX Live scheme ensures `ctex`, `fontspec`, `xeCJK`, and CJK fonts are available.

> This skill relies solely on your local TeX distribution — no external services required.

## Quick start

### Install the skill

The repository root already contains `.claude/`, so **do not clone the entire repo into `.claude/skills/`** — that creates a double-nested `.claude/` directory. Instead, use one of these methods:

**Global installation (all projects):**
```bash
# Clone anywhere
git clone https://github.com/MagicMonkey-XK/latex-precision-skill.git
# Symlink the skill directory into ~/.claude/skills/
ln -s "$(pwd)/latex-precision-skill/.claude/skills/latex-precision-skill" ~/.claude/skills/latex-precision-skill
```

**Project-level installation:**
```bash
# Copy only the skill directory into your project
cp -r latex-precision-skill/.claude/skills/latex-precision-skill your-project/.claude/skills/latex-precision-skill
```

Verify the entry point exists at `.claude/skills/latex-precision-skill/SKILL.md`.

### Verify your LaTeX environment

```bash
# Test with a minimal Chinese document
xelatex -interaction=nonstopmode test.tex
```

### Use in Claude Code

Once installed, the skill triggers automatically on LaTeX-related prompts. Common starting points:

```
"Create a Chinese article template with ctex"
"Compile this .tex file and fix errors"
"Build a three-line table with 5 columns and 10 rows"
"Write Maxwell's equations in align environment"
"Turn this article into a Beamer presentation"
```

## Typical compilation workflow

```bash
# Fix Unicode missing characters (first time only)
python3 scripts/fix_unicode.py document.tex

# Compile with latexmk (auto multi-pass)
latexmk -xelatex -interaction=nonstopmode -outdir=build document.tex

# Verify
echo "Missing chars:" && grep -c "Missing character" build/document.log
echo "Errors:" && grep -c "^!" build/document.log
```

## Key features

### First-class Chinese typesetting
- `ctex` document classes — `ctexart`, `ctexrep`, `ctexbook`, `ctexbeamer`
- XeTeX engine optimized for CJK Unicode
- Common Windows Chinese fonts: SimSun (宋体), SimHei (黑体), FangSong (仿宋), KaiTi (楷体)
- `newunicodechar` fix script for missing glyphs

### Multi-engine support
| Engine | Command | Unicode | System fonts | Best for |
|--------|---------|---------|-------------|----------|
| pdfTeX | `pdflatex` | No | No | English, legacy |
| XeTeX | `xelatex` | Yes | Yes | Chinese/Unicode |
| LuaTeX | `lualatex` | Yes | Yes | Advanced typography |

### Compilation automation
- `latexmk` with `-pvc` continuous preview mode
- Standalone build scripts (PowerShell, Bash, Makefile)
- Automated bibliography/index/glossary multi-pass handling

## License

[MIT](LICENSE)
