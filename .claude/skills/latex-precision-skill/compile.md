---
name: latex-compile
description: "Compilation engine and workflow: multi-pass compilation, latexmk, log analysis, Unicode character fixing, and error handling"
---

# LaTeX Compilation Engine and Workflow

## Single-Command Compilation

The basic compilation command for each engine:

```bash
# XeLaTeX (recommended for Chinese/Unicode documents)
xelatex <filename>.tex

# pdfLaTeX (English-only, no Unicode)
pdflatex <filename>.tex

# LuaLaTeX (modern, Unicode + Lua scripting)
lualatex <filename>.tex
```

These produce a PDF directly from the `.tex` source.

## Common Compilation Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-interaction=MODE` | Error handling mode: `nonstopmode`, `scrollmode`, `errorstopmode`, `batchmode` | `-interaction=nonstopmode` |
| `-file-line-error` | Show errors as `file:line:error` format (editor-friendly) | `-file-line-error` |
| `-synctex=N` | SyncTeX for editor-PDF synchronization (`1` = enable) | `-synctex=1` |
| `-shell-escape` | Allow external program calls (use with caution) | `-shell-escape` |
| `-halt-on-error` | Stop immediately at first error (no interactive prompt) | `-halt-on-error` |
| `-output-directory=DIR` | Write output files to a specific directory | `-output-directory=build` |
| `-quiet` | Reduce console output verbosity | `-quiet` |

**Typical compile command:**

```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error <filename>.tex
```

## Multi-Pass Compilation

LaTeX often requires multiple compilation passes to resolve cross-references and other forward-looking elements.

### Why Multiple Passes?

| Pass | What Happens |
|------|-------------|
| 1st | Typesets content, writes `.aux`, `.toc`, `.lof`, `.lot` files |
| 2nd | Reads auxiliary files, resolves `\ref`, `\pageref`, table of contents |
| 3rd | Stabilizes longtable column widths, finalizes cross-references |

### Standard Multi-Pass Commands

```bash
# Basic: 2 passes for cross-references
xelatex <filename>.tex
xelatex <filename>.tex

# With bibliography: 4 passes
xelatex <filename>.tex
bibtex <filename>
xelatex <filename>.tex
xelatex <filename>.tex

# With index: 3 passes
xelatex <filename>.tex
makeindex <filename>
xelatex <filename>.tex

# With glossary: 3+ passes
xelatex <filename>.tex
makeglossaries <filename>
xelatex <filename>.tex
```

### Why Bibliography Needs 4 Passes

1. First `xelatex`: Writes `.aux` file with citation references
2. `bibtex`: Reads `.aux`, matches citations against `.bib`, writes `.bbl`
3. Second `xelatex`: Reads `.bbl`, includes bibliography, writes updated references
4. Third `xelatex`: Resolves all remaining cross-references in bibliography

### Modern Bibliography (biblatex + biber)

```bash
xelatex <filename>.tex
biber <filename>
xelatex <filename>.tex
xelatex <filename>.tex
```

## latexmk Automation

`latexmk` is a Perl script that automates multi-pass compilation. It is included with TeX Live.

### Basic Usage

```bash
latexmk -xelatex <filename>.tex            % XeLaTeX engine
latexmk -pdf <filename>.tex                % pdfLaTeX engine
latexmk -lualatex <filename>.tex           % LuaLaTeX engine
latexmk -pdfdvi <filename>.tex             % LaTeX → DVI → PDF
```

### Useful Flags

| Flag | Purpose |
|------|---------|
| `-xelatex` | Use xelatex engine |
| `-pdf` | Use pdflatex engine |
| `-lualatex` | Use lualatex engine |
| `-pvc` | Continuous preview mode (watches file, recompiles on change) |
| `-cd` | Change to the file's directory first |
| `-silent` | Reduce output verbosity (shows only errors) |
| `-interaction=MODE` | Pass interaction mode to engine |
| `-outdir=DIR` | Set output directory |
| `-C` | Clean all generated files (`.aux`, `.log`, `.pdf`) |
| `-c` | Clean generated files except `.pdf` and `.dvi` |

### Examples

```bash
# Standard compilation with xelatex (auto-detects passes needed)
latexmk -xelatex <filename>.tex

# Compile to build directory, showing only errors
latexmk -xelatex -outdir=build -silent <filename>.tex

# Continuous preview (recompile on every save)
latexmk -xelatex -pvc <filename>.tex

# Clean and rebuild from scratch
latexmk -xelatex -C <filename>.tex
latexmk -xelatex <filename>.tex
```

### latexmkrc Configuration

Place a `.latexmkrc` file in the project root for persistent settings:

```perl
#!/usr/bin/env perl
$pdf_mode = 5;                          # 5 = xelatex
$out_dir = "build";                     # Output directory
$silent = 0;                            # Show all output
$pdf_previewer = "start sumatra";       # Windows PDF viewer
@default_files = ("main.tex");          # Default file to compile
```

`$pdf_mode` values:

| Value | Engine |
|-------|--------|
| 1 | `pdflatex` |
| 2 | `ps2pdf` |
| 3 | `dvipdf` |
| 4 | `lualatex` |
| 5 | `xelatex` |

## Reading Log Files

When LaTeX compiles, it produces a `.log` file alongside the PDF.

### Log File Structure

```
This is XeTeX, Version 3.141592653-2.6-0.999996 (TeX Live 2026)
entering extended mode
...
! Undefined control sequence.
l.23 \nonexistentcommand
                        {argument}
?
...
Output written on <filename>.pdf (12 pages).
```

### Finding Errors

Errors in the log start with `! ` at the beginning of a line:

```bash
# Find all errors
grep "^!" <filename>.log

# Count errors
grep -c "^!" <filename>.log

# Show errors with context (5 lines after)
grep -A 5 "^!" <filename>.log
```

### Finding Warnings

```bash
# Missing Unicode characters (common in Chinese docs)
grep "Missing character" <filename>.log

# Overfull/underfull boxes (line/page break issues)
grep -E "(Overfull|Underfull)" <filename>.log

# Count missing characters
grep -c "Missing character" <filename>.log
```

### Common Error Types

| Error Pattern | Meaning |
|---------------|---------|
| `! Undefined control sequence.` | Typo or missing package |
| `! Missing $ inserted.` | Math command used outside math mode |
| `! LaTeX Error: File \`xxx.sty' not found.` | Missing package |
| `! Emergency stop.` | Fatal error, engine stopped |
| `! LaTeX Error: Something's wrong--perhaps a missing \item.` | Environment issue (often lists) |

### Common Warning Types

| Warning | Meaning |
|---------|---------|
| `Overfull \hbox` | Text too wide for page (adjust margins or rephrase) |
| `Underfull \hbox` | Line too loose (warning only, usually acceptable) |
| `Overfull \vbox` | Vertical overflow (page break issue) |
| `Longtable column widths have changed` | Harmless, stabilize after 3rd pass |
| `Citation \`xxx' on page y undefined` | Bibliography not yet processed |
| `There were undefined references` | Cross-references not yet resolved |

## Unicode Character Fix (fix_unicode.py)

When XeLaTeX encounters Unicode characters not present in the default font (Latin Modern Roman), it emits `Missing character` warnings and the PDF shows blank spots. This is common in Chinese datasheets containing characters like ≤, ≥, λ.

### The Script

The `fix_unicode.py` script (located at `scripts/fix_unicode.py` in this skill directory) scans a `.tex` file and inserts `\newunicodechar` mappings to map problematic Unicode characters to LaTeX command equivalents.

**Usage:**

```bash
python3 scripts/fix_unicode.py <filename>.tex
```

This creates a backup (`<filename>.tex.bak`) and inserts mappings for:
- `≤` → `\leq` (less-than-or-equal)
- `≥` → `\geq` (greater-than-or-equal)
- `λ` → `\lambda` (Greek lambda)
- `U+F06C` (bullet) → `\textbullet`

### Manual Unicode Fixes

For additional Unicode characters, manually add `\newunicodechar` declarations in the preamble:

```latex
\usepackage{newunicodechar}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{≥}{\ensuremath{\geq}}
\newunicodechar{λ}{\ensuremath{\lambda}}
\newunicodechar{℃}{\ensuremath{{}^{\circ}\mathrm{C}}}
\newunicodechar{±}{\ensuremath{\pm}}
\newunicodechar{×}{\texttimes}
\newunicodechar{•}{\textbullet}
```

## Error Handling

### Interaction Modes

| Mode | Behavior |
|------|----------|
| `errorstopmode` | Default. Stops at each error and waits for input |
| `nonstopmode` | Continues past all errors (produces PDF even with errors) |
| `scrollmode` | Stops only for fatal errors |
| `batchmode` | No output at all; errors go only to `.log` |

For automated compilation (scripts, CI), always use:

```bash
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
```

### Exit Codes

- `0` — Success (or only non-fatal warnings)
- `1` — Error occurred (PDF may still be produced with `nonstopmode`)
- ≥ `2` — Fatal system error

### Common Fixes by Symptom

| Symptom | Likely Fix |
|---------|------------|
| `Missing character` warnings | Run `fix_unicode.py` or add `\newunicodechar` declarations |
| `! Undefined control sequence` | Check spelling or install missing package via `tlmgr install <package>` |
| `! LaTeX Error: File not found` | Check file path, install missing package |
| Blank spots in PDF where Chinese chars should be | Missing font — install Source Han Serif CN or configure `\setCJKmainfont` |
| PDF pages all blank | Output engine mismatch — check you're using `xelatex`, not `pdflatex` |
| Overfull `\hbox` warnings | Add `\sloppy` or use `\geometry{margin=...}` to widen margins |

## Build Scripts

### PowerShell Build Script (Windows)

```powershell
# build.ps1
param(
    [string]$File = "main",
    [string]$OutDir = "build"
)

$ErrorActionPreference = "Stop"

# Create output directory
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

# Compile
Write-Host "=== Pass 1: xelatex ==="
xelatex -interaction=nonstopmode -file-line-error `
        -output-directory=$OutDir "$File.tex"

Write-Host "=== Pass 2: xelatex (resolve refs) ==="
xelatex -interaction=nonstopmode -file-line-error `
        -output-directory=$OutDir "$File.tex"

Write-Host "=== Checking log ==="
$logFile = "$OutDir/$File.log"
if (Select-String -Path $logFile -Pattern "^!" -Quiet) {
    Write-Warning "Errors found in log:"
    Select-String -Path $logFile -Pattern "^!" | ForEach-Object { $_.Line }
} else {
    Write-Host "No errors found."
}

Write-Host "=== Output ==="
Get-ChildItem "$OutDir/*.pdf" | ForEach-Object {
    Write-Host "PDF: $($_.FullName)"
}
```

### Bash Build Script

```bash
#!/bin/bash
# build.sh
FILE="${1:-main}"
OUTDIR="${2:-build}"

mkdir -p "$OUTDIR"

echo "=== Pass 1: xelatex ==="
xelatex -interaction=nonstopmode -file-line-error \
        -output-directory="$OUTDIR" "${FILE}.tex"

echo "=== Pass 2: xelatex (resolve refs) ==="
xelatex -interaction=nonstopmode -file-line-error \
        -output-directory="$OUTDIR" "${FILE}.tex"

echo "=== Errors ==="
grep "^!" "$OUTDIR/${FILE}.log" || echo "No errors"

echo "=== PDF ==="
ls -la "$OUTDIR"/*.pdf
```

### Makefile

```makefile
# Makefile for LaTeX compilation
FILE = main
OUTDIR = build
LATEX = xelatex -interaction=nonstopmode -file-line-error -output-directory=$(OUTDIR)

.PHONY: all clean view

all: $(OUTDIR)/$(FILE).pdf

$(OUTDIR)/$(FILE).pdf: $(FILE).tex
	mkdir -p $(OUTDIR)
	$(LATEX) $(FILE).tex
	$(LATEX) $(FILE).tex
	@echo "=== Checking errors ==="
	@grep "^!" $(OUTDIR)/$(FILE).log || echo "No errors"

clean:
	rm -rf $(OUTDIR)

view:
	start $(OUTDIR)/$(FILE).pdf
```

## Simplified Compilation for Chinese Datasheets

For this project's Chinese datasheets, the recommended compilation workflow is:

```bash
# 1. Fix Unicode characters (first time or after significant changes)
python3 scripts/fix_unicode.py <filename>.tex

# 2. Compile with latexmk (3 passes auto-detected)
latexmk -xelatex -interaction=nonstopmode -outdir=build <filename>.tex

# 3. Verify output
echo "Missing chars:" && grep -c "Missing character" build/<filename>.log
echo "Errors:" && grep -c "^!" build/<filename>.log
ls -la build/*.pdf
```

Refer to [environment.md](environment.md) for TeX Live installation, font configuration, and package management details.
