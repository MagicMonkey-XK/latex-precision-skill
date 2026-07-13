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

An optional [latex-writer agent](.claude/agents/latex-writer.md) is included for isolated LaTeX document work. It enforces:
- Manual line-by-line editing (no batch scripts on `.tex` files)
- Backup-before-edit safety
- Context7 integration for package documentation lookup
- Tabularray key ordering rules
- Chinese LaTeX best practices

## Prerequisites

- [Claude Code](https://claude.ai/code) installed
- **Recommended**: [TeX Live](https://tug.org/texlive/) distribution (cross-platform, actively maintained)
- **Alternative**: MiKTeX (Windows-only, legacy CTeX Suite)

For Chinese typesetting, a full or medium TeX Live scheme ensures `ctex`, `fontspec`, `xeCJK`, and CJK fonts are available.

> This skill relies solely on your local TeX distribution — no external services required.

## Quick start

### Install the skill

```bash
git clone https://github.com/MagicMonkey-XK/latex-precision-skill.git /path/to/your/project/.claude/skills/latex
```

Or place it under `~/.claude/skills/latex` for cross-project availability.

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
