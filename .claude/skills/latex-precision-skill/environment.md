---
name: latex-environment
description: "TeX Live environment and tool chain: installation, engine comparison, font configuration, package management, and testing"
---

# LaTeX Environment and Tool Chain

## TeX Distributions

Two major TeX distributions are available for LaTeX work:

### TeX Live (Recommended)

[TeX Live](https://tug.org/texlive/) is the cross-platform distribution maintained by the TeX User Group (TUG). It runs on Windows, Linux, and macOS.

**Installation methods:**

- **DVD ISO image**: Download from [TUG](https://tug.org/texlive/) or a [CTAN mirror](https://ctan.org/mirrors). On Windows, run `install-tl.bat` from the mounted image.
- **Network install**: Download `install-tl.zip` from a [CTAN mirror](https://ctan.org/mirrors) (e.g., `http://ftp.ctex.org/mirrors/CTAN/systems/texlive/tlnet/`). Extract and run `install-tl.bat`. Use `-repository` to specify a mirror:

```bash
install-tl -repository http://ftp.ctex.org/mirrors/CTAN/systems/texlive/tlnet/
```

- **Advanced install**: Run `install-tl-advanced.bat` for custom scheme selection (basic vs. full), language subsets, and documentation choices.

**Scheme selection:**

- `scheme-full`: Complete installation (several GB, includes all packages, fonts, and documentation)
- `scheme-basic`: Minimal working system (downloads missing packages on demand)
- `scheme-small`: Smaller but self-contained

For most Chinese LaTeX work, install `scheme-full` or `scheme-medium` at minimum to ensure `ctex`, `fontspec`, `xeCJK`, and CJK fonts are available.

**Windows post-installation:**

TeX Live adds itself to the system PATH and provides:
- `TeXworks editor` — bundled LaTeX editor
- `TeX Live command line` — shell with environment variables set
- `TeX Live Manager` — GUI for `tlmgr`
- `TeX Live documentation` — HTML index of all installed documentation

### CTEX套装 (CTeX Suite)

A Windows-only distribution based on MiKTeX, popular among Chinese users. It bundles:

- MiKTeX engine
- **WinEdt** editor
- **SumatraPDF** viewer
- **GhostScript** + **GSview** for PostScript
- CJK Chinese font configuration

CTEX套装 has "basic" and "complete" editions. The complete edition includes all MiKTeX packages. It relies on MiKTeX's online package manager for missing packages.

> **Note**: CTEX套装 is legacy software. For new projects, TeX Live is strongly recommended as it is actively maintained and cross-platform.

## Engine Comparison

Three engines are available for compiling LaTeX documents to PDF:

| Engine | Command | Unicode | System Fonts | Chinese (ctex) | Speed | Best For |
|--------|---------|---------|-------------|----------------|-------|----------|
| **pdfTeX** | `pdflatex` | No (8-bit) | No | Limited (CJK) | Fastest | English documents, legacy packages |
| **XeTeX** | `xelatex` | Yes | Yes (via fontspec) | Excellent (xeCJK) | Fast | Chinese/Unicode docs, system fonts |
| **LuaTeX** | `lualatex` | Yes | Yes (via fontspec) | Good (luatexja) | Slower | Advanced typography, Lua scripting |

### When to Use Each

- **`xelatex`** — Default choice for Chinese documents with `ctex`. Best Unicode support with system fonts. Use for: Chinese datasheets, articles, books; any document needing system fonts via `fontspec`; documents with mixed scripts.

- **`pdflatex`** — Legacy engine, fast but no Unicode. Only use for: English-only documents relying on packages that don't support xelatex; journals that require pdflatex submissions.

- **`lualatex`** — Most modern engine, supports Unicode and system fonts plus Lua scripting. Slightly slower than xelatex. Use for: documents needing Lua-based calculations; advanced OpenType font features; projects already using luatexja for Japanese.

For Chinese datasheet work in this project, always use **`xelatex`** unless otherwise specified.

## TeX Directory Structure (TDS)

TeX Live follows the TDS (TeX Directory Structure) standard:

| Directory | Purpose |
|-----------|---------|
| `texmf-dist/` | System-installed packages (managed by tlmgr, do not modify) |
| `texmf-local/` | Locally-installed packages (site-wide, survives upgrades) |
| `~/texmf/` | User's personal package tree (Linux/macOS, OS dependent on Windows) |

**Path resolution order**: `~/texmf` → `texmf-local` → `texmf-dist` (later trees override earlier ones).

To find where a file lives in the TDS tree:

```bash
kpsewhich <filename>
# Example:
kpsewhich ctexart.cls
kpsewhich simsun.ttc
```

### TDS Tree Structure

Each TDS root follows this structure:
```
<root>/
├── bibtex/       # BibTeX databases and styles
├── doc/          # Documentation
├── fonts/        # Font files (truetype, type1, opentype)
├── metafont/     # Metafont sources
├── scripts/      # Support scripts
├── source/       # Source code
├── tex/          # TeX macros and packages
└── web2c/        # Configuration files
```

## Font Configuration

### System Fonts with XeLaTeX/LuaLaTeX

XeLaTeX and LuaLaTeX can use any font installed in the operating system via the `fontspec` package:

```latex
\usepackage{fontspec}
\setmainfont{Source Han Serif CN}   % Main text font
\setmonofont{Source Code Pro}       % Monospace font
```

### Chinese Fonts with ctex

The `ctex` package/document class automatically detects and configures Chinese fonts:

```latex
\documentclass[UTF8]{ctexart}    % Chinese article
\documentclass[UTF8]{ctexrep}    % Chinese report
\documentclass[UTF8]{ctexbook}   % Chinese book

% Or use ctex package with standard classes:
\usepackage[UTF8]{ctex}
```

**Common Chinese fonts available on Windows:**

| Font | Family Name | Typical Use |
|------|-------------|-------------|
| SimSun (宋体) | SimSun | Body text |
| SimHei (黑体) | SimHei | Headings |
| Fangsong (仿宋) | FangSong | Quotations |
| KaiTi (楷体) | KaiTi | Emphasis |
| Microsoft YaHei (微软雅黑) | Microsoft YaHei | UI-style text |

**Changing fonts with ctex:**

```latex
% Via package options
\documentclass[UTF8, fontset=windows]{ctexart}

% Or manually after preamble:
\setCJKmainfont{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{FangSong}
```

### OSFONTDIR (Linux/macOS)

On Linux, configure the font path so pdfTeX/dvipdfmx can find system fonts. Edit `texmf.cnf`:

```
OSFONTDIR = /usr/share/fonts//;/usr/local/share/fonts//;~/.fonts//
```

On Windows, TeX Live automatically detects system fonts. No manual configuration is needed.

### Font Fallback Chain

For xelatex, a fallback font can be specified for characters not covered by the main font:

```latex
\usepackage{newunicodechar}
\newCJKfontfamily[fallback]\fallbackfont{Source Han Serif CN}
% xeCJK fallback configuration:
\xeCJKDeclareSubCJKBlock{SupplementaryIdeographicPlane}{"20000->"2FFFF}
```

## Package Management

### tlmgr (TeX Live Manager)

`tlmgr` is the command-line package manager for TeX Live.

```bash
# List available packages matching a pattern
tlmgr search <package>

# Install a package
tlmgr install <package-name>

# Remove a package
tlmgr remove <package-name>

# Update all installed packages
tlmgr update --all

# Update just specific packages
tlmgr update <package-name>

# Show package information
tlmgr info <package-name>

# GUI mode
tlmgr gui
```

**Common maintenance tasks:**

```bash
# Refresh the filename database (after manual file installation)
texhash    # or: mktexlsr

# Regenerate format files (after updating engine binaries)
fmtutil-sys --all

# Update font map files (after installing new fonts)
updmap-sys
```

### MiKTeX Package Manager

CTEX套装 (MiKTeX-based) uses a GUI Package Manager:
- Launches from Start Menu > MiKTeX > Maintenance > Package Manager
- Selects a repository and synchronizes
- Installs/removes packages graphically
- Can be configured to install missing packages on-the-fly during compilation

## Documentation

### texdoc

`texdoc` opens installed documentation for LaTeX packages, classes, and tools:

```bash
# Open documentation for a package
texdoc <package-name>

# Examples:
texdoc ctex          % ctex package documentation (Chinese)
texdoc fontspec      % fontspec documentation
texdoc xelatex       % XeTeX reference
texdoc latex2e       % LaTeX2e official reference
texdoc symbols       % symbol table
texdoc tlmgr         % TeX Live Manager manual
```

### TeX Live Documentation

Accessible via Start Menu > TeX Live > TeX Live documentation, or at:

```
<texlive>/2026/texmf-doc/doc/
```

The HTML index page links to thousands of package manuals in PDF and HTML format.

## Testing Your Installation

Create a minimal test file to verify the installation works:

```latex
% test.tex
\documentclass[UTF8]{ctexart}
\begin{document}
你好，\LaTeX！

这是一段中文测试文字。
\end{document}
```

Compile with:

```bash
xelatex -interaction=nonstopmode test.tex
```

The output should be a PDF with Chinese text rendered correctly.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `TEXMFHOME` | User's personal TDS root (default: `~/texmf`) |
| `TEXMFLOCAL` | Local TDS root (system-wide) |
| `OSFONTDIR` | System font search path (Linux) |
| `TEXINPUTS` | Search path for `.tex` files |
| `BIBINPUTS` | Search path for `.bib` files |
| `BSTINPUTS` | Search path for `.bst` style files |
