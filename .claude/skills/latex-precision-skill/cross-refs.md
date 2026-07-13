---
name: cross-refs
description: "LaTeX 自动化工具：目录、交叉引用、hyperref、BibTeX文献、索引、词汇表"
---

# 自动化工具

## 目录

### 基本目录

```latex
\tableofcontents   % 目录
\listoffigures     % 插图目录
\listoftables      % 表格目录
```

均需编译2次才能正确生成。

### 目录深度控制

```latex
\setcounter{tocdepth}{2}           % 目录显示到subsection
\setcounter{secnumdepth}{3}        % 编号深度到subsubsection
```

### 手动添加目录项

```latex
\addcontentsline{toc}{section}{特殊章节}
\addcontentsline{toc}{section}{\protect\numberline{}前言}
```

### 定制目录格式（tocloft 宏包）

```latex
\usepackage{tocloft}
\renewcommand{\cftsecfont}{\large\bfseries}  % 章节字体
\renewcommand{\cftsecpagefont}{\bfseries}    % 页码字体
```

## 交叉引用

### label / ref 基础

```latex
\section{介绍}\label{sec:intro}
如图~\ref{fig:chart} 所示，更多细节见第~\ref{sec:detail} 节。
在第~\pageref{sec:intro} 页中...
```

编译需2次：第一次写入 `.aux`，第二次读取。

### 标签命名规范

| 类型 | 前缀 | 示例 |
|:----:|:----:|------|
| 章节 | `sec:` | `\label{sec:intro}` |
| 公式 | `eq:` | `\label{eq:energy}` |
| 图表 | `fig:` | `\label{fig:chart}` |
| 表格 | `tab:` | `\label{tab:data}` |
| 定理 | `thm:` | `\label{thm:main}` |

### cleveref 宏包（推荐）

自动判断引用类型并添加前缀名称：

```latex
\usepackage{cleveref}

\section{介绍}\label{sec:intro}
如图~\cref{fig:chart} 所示，见 \cref{sec:intro,sec:detail}。

% 大写版本
\Cref{fig:chart} 显示了...
```

cleveref 自动生成"图1"、"表2"、"第1节"等中文标记。

### 注意事项

- `cleveref` 应放在 `hyperref` 之后加载
- 所有引用命令只能使用一次，不能嵌套

## 超链接（hyperref 宏包）

```latex
\usepackage{hyperref}

% 配置中文链接
\usepackage[colorlinks=true, linkcolor=black, citecolor=blue]{hyperref}
```

### 常用选项

| 选项 | 说明 |
|------|------|
| `colorlinks=true` | 彩色链接（而非彩色边框） |
| `linkcolor=black` | 内部链接颜色 |
| `citecolor=blue` | 引文链接颜色 |
| `urlcolor=blue` | URL链接颜色 |
| `bookmarks=true` | 生成PDF书签 |
| `bookmarksnumbered=true` | 书签带编号 |
| `pdfauthor={作者}` | PDF属性作者 |
| `pdftitle={标题}` | PDF属性标题 |

### 超链接命令

```latex
\url{https://example.com}          % 显示URL
\href{https://example.com}{文字}   % 链接+显示文字
\hypertarget{key}{目标}            % 锚点目标
\hyperlink{key}{跳转}               % 跳转到锚点
```

## 文献管理

### BibTeX 基础流程

1. 创建 `.bib` 数据库文件
2. 在 `.tex` 中引用
3. 编译：latex → bibtex → latex → latex

### .bib 数据库格式

```bibtex
@article{key2024,
  author  = {张三 and 李四},
  title   = {论文标题},
  journal = {期刊名},
  year    = {2024},
  volume  = {42},
  pages   = {1--10}
}

@book{knuth1984,
  author    = {Knuth, Donald E.},
  title     = {The TeXbook},
  publisher = {Addison-Wesley},
  year      = {1984}
}

@inproceedings{wang2023,
  author    = {王五},
  title     = {会议论文},
  booktitle = {会议论文集},
  year      = {2023}
}
```

### 在文档中引用

```latex
\bibliographystyle{plain}     % 参考文献格式
\bibliography{refs}            % 引用refs.bib

% 文中引用
根据文献~\cite{knuth1984} 的研究...
多个引用~\cite{knuth1984, wang2023}
```

### 常见 BibTeX 样式

| 样式 | 特点 |
|------|------|
| `plain` | 按字母排序，编号 [1] |
| `unsrt` | 按引用顺序排序 |
| `alpha` | 缩写作者+年份标签 [Knu84] |
| `abbrv` | 缩写姓名 |
| `ieeetr` | IEEE格式 |

### natbib 宏包（增强）

```latex
\usepackage{natbib}

\citet{knuth1984}   % 作者-年份：Knuth (1984)
\citep{knuth1984}   % 括号引用：(Knuth, 1984)
\citeauthor{knuth1984}  % 仅作者名
\citeyear{knuth1984}    % 仅年份
```

### biblatex 现代方案

```latex
\usepackage[backend=biber, style=gb7714-2015]{biblatex}
\addbibresource{refs.bib}

\cite{knuth1984}
\printbibliography
```

编译命令：
```bash
xelatex file.tex
biber file      % 注意：biber 不是 bibtex
xelatex file.tex
xelatex file.tex
```

## 索引（makeindex）

### 基本用法

```latex
\usepackage{makeidx}
\makeindex

% 标记索引项
\index{关键词}
\index{LaTeX!命令}    % 子条目

\printindex            % 输出索引
```

编译流程：latex → makeindex → latex

### makeindex 命令行

```bash
makeindex <filename>              % 生成索引
makeindex -s style.ist <filename> % 使用格式文件
```

## 词汇表（glossaries 宏包）

```latex
\usepackage{glossaries}
\makeglossaries

% 定义术语
\newglossaryentry{latex}{
  name={\LaTeX},
  description={一种文档排版系统}
}

\newglossaryentry{tex}{
  name={\TeX},
  description={高德纳开发的排版引擎}
}

% 引用
\gls{latex} 是建立在 \gls{tex} 之上的。
\printglossaries   % 输出词汇表
```

编译流程：
```bash
xelatex file.tex
makeglossaries file
xelatex file.tex
```

## 跨文件引用

- [document-structure.md](document-structure.md) — 文档结构章节命令
- [compile.md](compile.md) — 编译流程与latexmk
- [macros.md](macros.md) — 自定义命令与宏编写
