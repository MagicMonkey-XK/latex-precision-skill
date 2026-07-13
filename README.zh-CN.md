# LaTeX Precision Skill (LaTeX 排版技能包)

面向 [Claude Code](https://claude.ai/code) 的 LaTeX 排版技能包，覆盖从文档编写到复杂多遍编译的完整工作流，同时支持中英文 LaTeX 文档生产。

## 概述

本技能包将 Claude Code 转变为 LaTeX 排版助手。知识体系按**渐进式披露**架构组织：

- **第 1 层** — `SKILL.md`（~90 行）：主入口，含路由表和中文模板
- **第 2 层** — 11 个主题文件：每个覆盖一个具体领域（编译、表格、数学等）
- **第 3 层** — `wiki/` 和 `scripts/`：按需加载的参考文档和自动化脚本

## 核心知识领域

| 主题 | 文件 | 内容 |
|------|------|------|
| 环境配置 | [environment.md](.claude/skills/latex-precision-skill/environment.md) | TeX Live / MiKTeX 安装、引擎对比（pdfTeX/XeTeX/LuaTeX）、TDS 目录结构、字体配置、`tlmgr` 包管理 |
| 编译流程 | [compile.md](.claude/skills/latex-precision-skill/compile.md) | 单次/多次编译、`latexmk` 自动化、构建脚本（PowerShell/Bash/Makefile）、日志分析、Unicode 字符修复 |
| 文档结构 | [document-structure.md](.claude/skills/latex-precision-skill/document-structure.md) | 文档类、ctex 中文文档类、导言区设置、章节命令、多文件编译、页面设置 |
| 文字排版 | [text-formatting.md](.claude/skills/latex-precision-skill/text-formatting.md) | NFSS 字体体系（编码/族/系列/形状）、`fontspec`、ctex 中文字体、列表、定理环境、抄录、脚注 |
| 数学公式 | [math-formulas.md](.claude/skills/latex-precision-skill/math-formulas.md) | 行内/行间模式、希腊字母、运算符、矩阵、多行公式（align/gather/multline）、分段函数、间距 |
| 表格制作 | [tables.md](.claude/skills/latex-precision-skill/tables.md) | tabular、array、单元格合并、tabularx、longtable、booktabs 三线表、彩色表格 |
| 插图与浮动体 | [graphics.md](.claude/skills/latex-precision-skill/graphics.md) | graphicx、浮动体定位（`[htbp]`、`[H]`）、子图、文字绕排、xcolor 彩色、TikZ 绘图基础 |
| 交叉引用 | [cross-refs.md](.claude/skills/latex-precision-skill/cross-refs.md) | `\label`/`\ref`、hyperref、cleveref、BibTeX / biblatex + biber、makeindex 索引、glossaries 词汇表 |
| 自定义宏 | [macros.md](.claude/skills/latex-precision-skill/macros.md) | `\newcommand`、`\NewDocumentCommand`（xparse）、`\newenvironment`、`.sty` / `.cls` 编写、条件判断 |
| 错误排查 | [error.md](.claude/skills/latex-precision-skill/error.md) | 40+ 常见错误、警告分析（Overfull/Underfull boxes、缺失字符）、调试技巧、最小工作示例（MWE） |
| 幻灯片 | [beamer.md](.claude/skills/latex-precision-skill/beamer.md) | 帧结构、主题（Madrid、CambridgeUS 等）、区块、覆盖效果、分栏、中文 beamer（`ctexbeamer`）|

### 速查文档 (wiki/)

| 文件 | 内容 |
|------|------|
| [commands-reference.md](.claude/skills/latex-precision-skill/wiki/commands-reference.md) | 文档结构、章节、格式化命令速查 |
| [packages-reference.md](.claude/skills/latex-precision-skill/wiki/packages-reference.md) | 常用宏包分类速查 |
| [symbols-reference.md](.claude/skills/latex-precision-skill/wiki/symbols-reference.md) | 希腊字母、关系符、箭头等符号速查 |
| [font-encoding.md](.claude/skills/latex-precision-skill/wiki/font-encoding.md) | NFSS 字体四维坐标参考 |
| [ctex-guide.md](.claude/skills/latex-precision-skill/wiki/ctex-guide.md) | ctex 宏包/文档类详细选项 |

### 脚本

| 脚本 | 用途 |
|------|------|
| [fix_unicode.py](.claude/skills/latex-precision-skill/scripts/fix_unicode.py) | 扫描 `.tex` 文件，自动插入 `\newunicodechar` 映射以修复 Latin Modern Roman 中缺失的 Unicode 字符（≤、≥、λ、•）|

### 代理配置

附带 [latex-writer 代理](.claude/agents/latex-writer.md) 配置文件，可用于隔离的 LaTeX 文档处理。其规范包括：
- 逐行手动编辑（禁止对 `.tex` 文件使用批处理脚本）
- 编辑前自动备份
- 通过 Context7 查询宏包文档
- Tabularray 键值顺序规则
- 中文 LaTeX 最佳实践

## 环境要求

- 已安装 [Claude Code](https://claude.ai/code)
- **推荐**：[TeX Live](https://tug.org/texlive/) 发行版（跨平台、持续维护）
- **备选**：MiKTeX（仅 Windows）、CTeX 套装（已停止维护）

如需中文排版，建议安装 `scheme-full` 或 `scheme-medium`，确保 `ctex`、`fontspec`、`xeCJK` 及中文字体可用。

> 本技能仅依赖本地 TeX 发行版，无需外部服务。

## 快速开始

### 安装技能

```bash
# 克隆到项目目录（仅当前项目可用）
git clone https://github.com/MagicMonkey-XK/latex-precision-skill.git .claude/skills/latex

# 或安装到全局目录（所有项目可用）
git clone https://github.com/MagicMonkey-XK/latex-precision-skill.git ~/.claude/skills/latex
```

### 验证 LaTeX 环境

```bash
# 创建最小中文测试文档
echo '\documentclass[UTF8]{ctexart}
\begin{document}
你好，世界！
\end{document}' > test.tex

# 编译
xelatex -interaction=nonstopmode test.tex
```

### 在 Claude Code 中使用

技能安装后会自动响应 LaTeX 相关提示。常用入口：

```
"创建一篇中文文章模板，使用 ctex 和 xelatex"
"编译这个 .tex 文件并修复错误"
"做一个 5 列 10 行的三线表"
"用 align 环境写麦克斯韦方程组"
"把这篇文章转换成 Beamer 幻灯片"
```

## 典型编译工作流

```bash
# 1. 修复 Unicode 缺失字符（首次或大改后）
python3 scripts/fix_unicode.py document.tex

# 2. 使用 latexmk 编译（自动多遍）
latexmk -xelatex -interaction=nonstopmode -outdir=build document.tex

# 3. 验证输出
echo "缺失字符:" && grep -c "Missing character" build/document.log
echo "错误数:" && grep -c "^!" build/document.log
```

## 特色功能

### 中文排版优先支持
- `ctex` 文档类全家桶：`ctexart`、`ctexrep`、`ctexbook`、`ctexbeamer`
- XeTeX 引擎针对 CJK Unicode 优化
- 自动适配 Windows 中文字体：宋体、黑体、仿宋、楷体
- Unicode 缺失字符自动修复脚本

### 多引擎支持
| 引擎 | 命令 | Unicode | 系统字体 | 适用场景 |
|------|------|---------|---------|----------|
| pdfTeX | `pdflatex` | 否 | 否 | 英文文档、传统宏包 |
| XeTeX | `xelatex` | 是 | 是 | 中文/Unicode 文档 |
| LuaTeX | `lualatex` | 是 | 是 | 高级排版、Lua 脚本 |

### 编译自动化
- `latexmk` 自动化编译 + `-pvc` 持续预览模式
- 支持多种构建脚本（PowerShell、Bash、Makefile）
- 自动处理参考文献、索引、词汇表的多遍编译

## 许可

[MIT](LICENSE)
