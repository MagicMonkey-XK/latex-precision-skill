---
name: ctex-guide
description: "ctex 宏包/文档类详细选项：中文支持配置、字体设置、标点处理"
---

# ctex 宏包指南

## 概述

ctex 是 LaTeX 的中文支持宏集，支持 xeCJK（xelatex）、luatexja（lualatex）、CJK（pdflatex）三种后端。自动配置中文字体、中文标点、段落缩进等。

## 使用方式

### 文档类方式（推荐）

```latex
\documentclass[UTF8]{ctexart}     % 中文文章
\documentclass[UTF8]{ctexrep}     % 中文报告
\documentclass[UTF8]{ctexbook}    % 中文书籍
\documentclass[UTF8]{ctexbeamer}  % 中文幻灯片
```

### 宏包方式（搭配标准文档类）

```latex
\documentclass{article}
\usepackage[UTF8]{ctex}
```

## 主要选项

### 字体集（fontset）

| 选项 | 说明 | 适用系统 |
|:----:|------|:--------:|
| `fontset=windows` | Windows 系统内建字体（宋体/黑体等） | Windows |
| `fontset=mac` | macOS 系统字体 | macOS |
| `fontset=ubuntu` | Ubuntu 系统字体 | Linux |
| `fontset=adobe` | Adobe 中文字体 | 手动安装 |
| `fontset=fandol` | Fandol 开源字体 | 跨平台（TeX Live自帶） |
| `fontset=none` | 不配置字体（手动设置） | 自定义 |

不指定 `fontset` 时 ctex 自动检测。

### 编码

```latex
UTF8          % UTF-8 编码（推荐，默认）
GBK           % GBK 编码（旧文档兼容）
GB            % GB2312 编码
```

### 其他选项

| 选项 | 说明 |
|------|------|
| `scheme=chinese` | 中文排版（章节名"第X章"） |
| `scheme=plain` | 英文风格（章节名"Chapter X"） |
| `punct=yes` | 中文标点压缩/调整（默认） |
| `punct=no` | 禁用标点压缩 |
| `space=yes` | 允许中英文间空格 |
| `space=auto` | 自动处理中英文间距 |

## 中文字体命令

| 命令 | 字体 | 说明 |
|:----:|:----:|------|
| `\songti` | 宋体 | 正文默认 |
| `\heiti` | 黑体 | 标题常用 |
| `\fangsong` | 仿宋 | |
| `\kaishu` | 楷体 | |
| `\zihao{size}` | 字号设置 | `\zihao{-4}` = 小四 |

## CJK 字体设置宏

```latex
\setCJKmainfont{SimSun}              % CJK 正文字体
\setCJKsansfont{SimHei}              % CJK 无衬线字体
\setCJKmonofont{FangSong}            % CJK 等宽字体

\setCJKfamilyfont{zhyou}{YouYuan}    % 自定义 CJK 字体系列
\newcommand{\youyuan}{\CJKfamily{zhyou}}  % 自定义 CJK 字体命令
```

## 中文字号（\zihao）

| 命令 | 汉字字号 | 对应 pt |
|:----:|:--------:|:-------:|
| `\zihao{0}` | 初号 | 42pt |
| `\zihao{1}` | 一号 | 28pt |
| `\zihao{2}` | 二号 | 22pt |
| `\zihao{3}` | 三号 | 16pt |
| `\zihao{4}` | 四号 | 14pt |
| `\zihao{-4}` | 小四 | 12pt |
| `\zihao{5}` | 五号 | 10.5pt |
| `\zihao{-5}` | 小五 | 9pt |

## 完整示例

```latex
\documentclass[UTF8, fontset=windows, scheme=chinese]{ctexart}
\title{中文文档标题}
\author{作者}
\date{}

\begin{document}
\maketitle
\tableofcontents

\section{引言}
这是一段中文正文内容。

{\heiti 黑体标题}

{\songti 宋体正文：}

\begin{enumerate}
  \item 中文编号列表第一项
  \item 中文编号列表第二项
\end{enumerate}
\end{document}
```

## 跨文件引用

- [environment.md](../environment.md) — TeX Live 环境与字体配置
- [text-formatting.md](../text-formatting.md) — 中文字体使用
