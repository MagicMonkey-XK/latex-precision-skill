# latex-precision-skill
Line-by-line LaTeX skill for Claude Code. Edit, compile, and debug documents with surgical precision. Features XeLaTeX, Beamer slides, math formulas, tables, cross-references, bibliographies, and full Chinese typesetting support. All powered by local TeX Live.

<div align="center">

[![Claude Code](https://img.shields.io/badge/Claude%20Code-v2.1%2B-7B3FE4?style=flat-square&logo=anthropic&logoColor=white)](https://code.claude.com/)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-FF6B6B?style=flat-square)](https://agentskills.io)
[![TeX Live](https://img.shields.io/badge/TeX%20Live-2024+-0073CF?style=flat-square&logo=latex&logoColor=white)](https://tug.org/texlive/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**Line-by-line LaTeX typesetting for Claude Code — precision editing from `.tex` to PDF**

</div>

---

## ✨ About

**LaTeX Precision Skill** is a production-grade [Claude Code](https://code.claude.com/) skill that transforms how you write LaTeX. It enables **line-by-line editing, compilation, and debugging** with surgical precision — every character, equation, and table under your control.

No cloud dependencies. No subscription fees. Just your local [TeX Live](https://tug.org/texlive/) and Claude's intelligence working together.

---

## 🎯 What Makes This Different

| Feature | Standard LaTeX Workflow | With This Skill |
|---------|------------------------|-----------------|
| **Editing** | Write, compile, check, repeat | Line-by-line guided refinement |
| **Error fixing** | Manually parse logs | Claude reads logs and fixes instantly |
| **Math formulas** | Remember syntax | Auto-completion and validation |
| **Tables** | Count columns manually | Intelligent structure generation |
| **Beamer slides** | Start from scratch | Template-based slide creation |
| **Chinese typesetting** | Complex engine setup | One-line `ctex` configuration |
| **Cross-references** | Track labels manually | Auto-management of refs |
| **Bibliography** | Multiple BibTeX passes | Automated `biber`/`bibtex` handling |

---

## 📦 What's Included

### Core Capabilities

```text
latex-precision-skill/
├── SKILL.md                 # Smart routing — loads only what you need
├── compile.md               # One-command compilation with latexmk
├── document-structure.md    # Sections, chapters, appendices
├── text-formatting.md       # Fonts, paragraphs, lists, footnotes
├── math-formulas.md         # AMS math, equations, symbols
├── tables.md                # Booktabs, longtables, multi-row/col
├── graphics.md              # Figures, subfigures, float control
├── cross-refs.md            # Labels, citations, indexes
├── macros.md                # Custom commands and packages
├── error.md                 # Automated troubleshooting
├── beamer.md                # Presentation creation
├── environment.md           # TeX Live setup and configuration
├── scripts/
│   └── fix_unicode.py       # Unicode character repair
└── wiki/
    ├── commands-reference.md
    ├── packages-reference.md
    ├── symbols-reference.md
    ├── font-encoding.md
    └── ctex-guide.md
```

### Why This Structure Matters

This skill follows **progressive disclosure** — a design philosophy that keeps your Claude session efficient:

- **Layer 1** (`SKILL.md`): Loads immediately (~60 lines). Contains description and routing table.
- **Layer 2** (`*.md`): Loads only when needed. Each file covers one specific task.
- **Layer 3** (`wiki/`, `scripts/`): Accessed on demand. Never loads unless explicitly required.

**Result**: You get full LaTeX expertise without burning through your context window.

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install TeX Live (macOS/Linux/WSL)
sudo apt-get install texlive-full          # Ubuntu/Debian
brew install texlive                       # macOS
choco install texlive                      # Windows (Chocolatey)

# Or install minimal + required packages
sudo apt-get install texlive-base texlive-latex-recommended \
    texlive-latex-extra texlive-xetex texlive-fonts-recommended \
    texlive-science texlive-lang-chinese
```

### Install the Skill

```bash
# Personal installation (available in all projects)
git clone https://github.com/yourusername/latex-precision-skill.git ~/.claude/skills/latex

# Or project-specific installation
git clone https://github.com/yourusername/latex-precision-skill.git .claude/skills/latex
```

### First Use

Open Claude Code and try:

```text
/latex "Create a Beamer presentation about quantum computing"
```

Or let Claude decide:

```text
"Compile this LaTeX document and fix any errors I'm getting"
```

---

## 💡 Common Workflows

### 1. Write a New Document

```text
/latex "Create a research paper template with abstract, sections, and bibliography"
```

Claude will:
1. Generate a complete `.tex` file with proper structure
2. Include `amsmath`, `graphicx`, `booktabs`, and `hyperref`
3. Set up `biber` for bibliography
4. Show compilation command

### 2. Fix Compilation Errors

```text
/latex "Fix the errors in my document. The PDF won't compile."
```

Claude will:
1. Read the `.log` file
2. Identify missing packages, syntax errors, or undefined commands
3. Make corrections line by line
4. Recompile until clean

### 3. Format a Complex Table

```text
/latex "Create a three-line table with 5 columns, including merged headers"
```

Claude will:
1. Generate a `booktabs` table with proper formatting
2. Handle multi-column and multi-row cells
3. Ensure alignment and spacing are correct
4. Add captions and labels

### 4. Convert to Beamer

```text
/latex "Turn this article into a Beamer presentation with 8 slides"
```

Claude will:
1. Extract sections and key points
2. Create slide frames with proper structure
3. Add transitions and overlays where appropriate

### 5. Fix Chinese Typesetting

```text
/latex "Fix the Chinese fonts in this document. Characters are missing."
```

Claude will:
1. Check if `ctex` is properly configured
2. Run `fix_unicode.py` script
3. Switch to `xelatex` if needed
4. Ensure proper font encoding

---

## 🛠️ Advanced Features

### Pre-Approved Tools

This skill grants Claude access to essential LaTeX tools without interruption:

```yaml
allowed-tools:
  - Bash(latexmk *)      # Smart compilation
  - Bash(xelatex *)      # Unicode/Chinese support
  - Bash(pdflatex *)     # Standard PDF generation
  - Bash(lualatex *)     # Modern engine
  - Bash(tlmgr *)        # Package management
  - Bash(texdoc *)       # Documentation lookup
  - Bash(bibtex *)       # Bibliography
  - Bash(biber *)        # Modern bibliography
  - Bash(makeindex *)    # Index generation
  - Bash(makeglossaries *) # Glossary
```

### Dynamic Context Injection

The skill uses `` !`command` `` to fetch live data before processing:

```markdown
## Current Log Error
!`tail -n 30 *.log 2>/dev/null || echo "No log file found"`
```

This means Claude sees your actual error log without you pasting it.

### Subagent Mode

For complex tasks, the skill can run in an isolated context:

```yaml
context: fork
agent: Explore
```

This ensures:
- No conversation history pollution
- Focused execution on the specific task
- Clean results returned to your main session

---

## 🎨 Example: Line-by-Line Editing Session

Here's what a typical session looks like:

```text
You: "Fix the alignment in this table and add a caption"

Claude reads SKILL.md → routes to tables.md

Claude: "I see the issue. Your table has 4 columns but you defined 3."

[Claude edits the .tex file]

Claude: "I've fixed the column definition and added a proper caption.
         Run: latexmk -xelatex document.tex"

You: "Can you center the table and reduce the font size?"

Claude: [Immediately updates the table environment]

Claude: "Done. Added \centering and \small. Should compile cleanly now."
```

---

## 📖 Documentation

| File | Description |
|------|-------------|
| [environment.md](environment.md) | TeX Live setup and configuration |
| [compile.md](compile.md) | Compilation workflows |
| [document-structure.md](document-structure.md) | Document architecture |
| [text-formatting.md](text-formatting.md) | Fonts, lists, paragraphs |
| [math-formulas.md](math-formulas.md) | Mathematics |
| [tables.md](tables.md) | Tables and tabulars |
| [graphics.md](graphics.md) | Images and floats |
| [cross-refs.md](cross-refs.md) | References and citations |
| [macros.md](macros.md) | Custom commands |
| [error.md](error.md) | Troubleshooting |
| [beamer.md](beamer.md) | Presentations |
| [wiki/](wiki/) | Command, package, and symbol references |

---

## ⚙️ Configuration

### Override Visibility

From your `.claude/settings.local.json`:

```json
{
  "skillOverrides": {
    "latex": "name-only",  // Hide description, keep command visible
    "latex": "off"         // Hide completely
  }
}
```

Or use the `/skills` menu in Claude Code.

### Custom Templates

Add your own templates to the skill directory:

```bash
touch ~/.claude/skills/latex/templates/your-template.tex
```

Then reference them from `SKILL.md`.

---

## 🔍 Troubleshooting

### Skill Doesn't Trigger

- Check `description` matches your natural language
- Try invoking directly: `/latex "your request"`
- Verify the skill is in the correct directory

### YAML Parse Errors

```bash
claude --debug
```

Look for frontmatter validation errors in the output.

### Missing Packages

```bash
# Let Claude handle it automatically
/latex "Install the missing packages for this document"

# Or manually
sudo tlmgr install package-name
```

---

## 🤝 Contributing

Contributions are welcome! This skill follows the [Agent Skills](https://agentskills.io) open standard.

### Development Workflow

1. Fork the repository
2. Make changes to `SKILL.md` or supporting files
3. Test locally: `claude --debug`
4. Submit a PR with clear description of changes

### Adding New Features

```bash
# Add a new reference file
touch ~/.claude/skills/latex/new-feature.md

# Update SKILL.md to reference it
```

### Testing

```bash
# Test YAML parsing
claude --debug

# Test functionality
claude "Compile test.tex and report any warnings"
```

---

## 📚 Related Resources

- [Claude Code Skills Documentation](https://code.claude.com/docs/skills)
- [Agent Skills Open Standard](https://agentskills.io)
- [LaTeX Project Documentation](https://www.latex-project.org/)
- [TeX Live Documentation](https://tug.org/texlive/)
- [CTAN Package Repository](https://ctan.org/)

---

## 📄 License

[MIT](LICENSE) © 2026

---

<div align="center">
  <sub>Built for <strong>Claude Code</strong> · Precision typesetting, line by line</sub>
</div>
```

---

## Optional: Short README Version

If you prefer a more concise README for the GitHub repository:

```markdown
# LaTeX Precision Skill

**Line-by-line LaTeX typesetting for Claude Code.**

## Quick Install

```bash
git clone https://github.com/yourusername/latex-precision-skill.git ~/.claude/skills/latex
```

## Usage

```text
/latex "Create a Beamer presentation"
/latex "Fix this compilation error"
/latex "Format this table with booktabs"
```

## What It Does

- ✅ Compile with latexmk (XeLaTeX/PDFLaTeX/LuaLaTeX)
- ✅ Edit documents line by line
- ✅ Format math formulas and equations
- ✅ Build complex tables
- ✅ Create Beamer presentations
- ✅ Manage cross-references and bibliographies
- ✅ Support Chinese typesetting (ctex)
- ✅ Debug errors automatically
- ✅ Fix Unicode character issues

## Requirements

- Claude Code v2.1+
- TeX Live (local installation)

## License

MIT

---

[Full Documentation](https://github.com/yourusername/latex-precision-skill)
```
