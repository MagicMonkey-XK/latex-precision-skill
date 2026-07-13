---
name: document-structure
description: "LaTeX 文档结构：文档类、导言区、章节标题、多文件编译、附录、页面设置"
---

# 文档结构

## 基本骨架

每个 LaTeX 文档具有以下基本结构：

```latex
\documentclass[options]{class}   % 文档类，必须放在第一行
\usepackage[options]{package}    % 导言区：加载宏包
% ... 其他导言区设置 ...
\begin{document}                  % 正文开始
% ... 正文内容 ...
\end{document}                    % 文档结束
```

## 文档类

### 基本文档类

| 文档类 | 用途 | 支持 \chapter |
|--------|------|:---:|
| `article` | 短文、期刊论文、报告 | ❌ |
| `report` | 长报告、毕业论文 | ✅ |
| `book` | 书籍 | ✅ |
| `letter` | 信件 | ❌ |
| `slide` | 幻灯片（过时，建议用beamer） | ❌ |

### ctex 文档类（中文支持）

```latex
\documentclass[UTF8]{ctexart}    % 中文 article
\documentclass[UTF8]{ctexrep}    % 中文 report
\documentclass[UTF8]{ctexbook}   % 中文 book
```

文档类选项示例：

```latex
\documentclass[12pt, a4paper, twoside]{article}
```

| 选项 | 可选值 | 说明 |
|------|--------|------|
| 字号 | `10pt`, `11pt`, `12pt` | 正文基准字号（默认10pt） |
| 纸张 | `a4paper`, `letterpaper`, `a5paper` | 页面大小 |
| 单双面 | `oneside`, `twoside` | 双面打印时奇偶页不同 |
| 章起始 | `openright`, `openany` | book类中新章起始页 |
| 分栏 | `onecolumn`, `twocolumn` | 单栏/双栏 |
| 草稿 | `draft` | 显示溢出标记 |

## 导言区设置

```latex
\usepackage[UTF8]{ctex}              % 中文支持
\usepackage[margin=2cm]{geometry}    % 页面尺寸
\usepackage{fancyhdr}                % 页眉页脚
\usepackage{amsmath,amssymb}         % 数学公式
\usepackage{graphicx}                % 插图
\usepackage{hyperref}                % 超链接
\usepackage{booktabs}                % 三线表
```

宏包加载顺序注意：hyperref 通常放最后，ctex 在字体相关之前。

## 标题与章节

```latex
\title{文档标题}
\author{作者姓名}
\date{2025年1月1日}
\maketitle
```

章节命令（带星号不编号）：

```latex
\chapter{引言}
\section{背景}
\subsection{相关工作}
\section*{不编号的附录}
\appendix           % 切换到附录模式
\chapter{源码}     % 自动编号为 A
```

## 目录

```latex
\tableofcontents   % 编译2次
\listoffigures     % 插图目录
\listoftables      % 表格目录
```

## 多文件编译

```latex
\input{chapter1}          % 直接插入，不换页
\include{chapter2}        % 新页开始
\includeonly{chapter1}    % 只编译指定章节（调试用）
```

## 页面设置

```latex
\usepackage[margin=2cm, top=2.5cm, bottom=2.5cm]{geometry}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{左页眉}
\rhead{\thepage}
```

## 跨文件引用

- [text-formatting.md](text-formatting.md) — 文字排版
- [compile.md](compile.md) — 编译流程
- [cross-refs.md](cross-refs.md) — 交叉引用
- [environment.md](environment.md) — 环境配置
