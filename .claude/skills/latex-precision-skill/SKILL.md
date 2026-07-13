---
name: latex-precision-skill
description: "LaTeX 排版通用技能。Triggers on: 'LaTeX'、'排版'、'xelatex'、'编译'、'表格'、'数学公式'、'幻灯片'、'beamer'、'论文'、'中文排版'、'错误排查'、'.tex'"
allowed-tools: "Bash(latexmk *), Bash(xelatex *), Bash(pdflatex *), Bash(lualatex *), Bash(tlmgr *), Bash(texdoc *), Bash(bibtex *), Bash(biber *), Bash(makeindex *), Bash(makeglossaries *)"
---

# LaTeX 排版技能

## 概述

本技能提供完整的 LaTeX 排版支持，仅依赖本地 TeX Live 环境。涵盖从环境配置、文档结构、文字排版、数学公式、表格图表、交叉引用、幻灯片到错误排查的完整工作流。

## 技能结构

```
latex/
├── SKILL.md               ← 主入口（本文件）
├── environment.md         ← 环境安装与配置
├── compile.md             ← 编译流程与自动化
├── document-structure.md  ← 文档结构与章节
├── text-formatting.md     ← 文字排版与字体
├── math-formulas.md       ← 数学公式
├── tables.md              ← 表格制作
├── graphics.md            ← 插图与浮动体
├── cross-refs.md          ← 交叉引用与文献
├── macros.md              ← 自定义宏与宏包
├── error.md               ← 错误排查与调试
├── beamer.md              ← 幻灯片演示
├── scripts/
│   └── fix_unicode.py     ← Unicode 字符修补脚本
└── wiki/
    ├── commands-reference.md   ← 命令速查
    ├── packages-reference.md   ← 宏包速查
    ├── symbols-reference.md    ← 符号速查
    ├── font-encoding.md        ← 字体编码
    └── ctex-guide.md           ← 中文支持
```

## 快速路由

| 任务 | 参考文件 |
|------|---------|
| 安装 TeX Live 或配置环境 | [environment.md](environment.md) |
| 编译文档（latexmk/多pass） | [compile.md](compile.md) |
| 编写文档骨架和章节 | [document-structure.md](document-structure.md) |
| 字体、段落、列表、脚注 | [text-formatting.md](text-formatting.md) |
| 数学公式与符号 | [math-formulas.md](math-formulas.md) |
| 制作表格（三线表/长表格） | [tables.md](tables.md) |
| 插图与浮动体控制 | [graphics.md](graphics.md) |
| 交叉引用、文献、索引 | [cross-refs.md](cross-refs.md) |
| 自定义命令与宏包 | [macros.md](macros.md) |
| 错误排查与调试 | [error.md](error.md) |
| 幻灯片演示（beamer） | [beamer.md](beamer.md) |
| 查命令、宏包、符号 | [wiki/](wiki/) 目录下速查文件 |

## 中文排版通用模板

```latex
\documentclass[UTF8, a4paper]{ctexart}
\usepackage[margin=2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}

\title{文档标题}
\author{作者}
\date{}

\begin{document}
\maketitle
\tableofcontents

\section{引言}
正文内容...

\end{document}
```

编译（xelatex 推荐）：
```bash
latexmk -xelatex file.tex
```

## 注意事项

- 本技能仅依赖本地 TeX Live 环境，不依赖外部服务
- 中文文档优先使用 `xelatex` 引擎 + `ctex` 宏包
- 所有脚本位于 `scripts/` 目录，通过 `${CLAUDE_SKILL_DIR}/scripts/` 引用
- `fix_unicode.py` 用于修正 XeLaTeX 的 Unicode 缺失字符问题
