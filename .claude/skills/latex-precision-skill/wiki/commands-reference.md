---
name: commands-reference
description: "LaTeX 常用命令速查表：按功能分类的命令概览"
---

# 常用命令速查

## 文档结构

| 命令 | 说明 |
|------|------|
| `\documentclass[opt]{cls}` | 文档类 |
| `\usepackage[opt]{pkg}` | 加载宏包 |
| `\begin{document}` | 正文开始 |
| `\end{document}` | 文档结束 |
| `\title{}` | 标题 |
| `\author{}` | 作者 |
| `\date{}` | 日期 |
| `\maketitle` | 生成标题 |

## 章节

| 命令 | 说明 |
|------|------|
| `\part{}` | 部 |
| `\chapter{}` | 章（report/book） |
| `\section{}` | 节 |
| `\subsection{}` | 小节 |
| `\subsubsection{}` | 子小节 |
| `\appendix` | 附录模式 |
| `\tableofcontents` | 目录 |

## 字体

| 命令 | 说明 |
|------|------|
| `\textrm{}` | 罗马体 |
| `\textsf{}` | 无衬线 |
| `\texttt{}` | 等宽 |
| `\textbf{}` | 粗体 |
| `\textit{}` | 斜体 |
| `\textsl{}` | 倾斜 |
| `\textsc{}` | 小型大写 |
| `\emph{}` | 强调 |
| `\tiny` ~ `\Huge` | 10级字号 |

## 列表

| 环境 | 说明 |
|------|------|
| `itemize` | 无编号列表 |
| `enumerate` | 编号列表 |
| `description` | 描述列表 |

## 数学

| 命令 | 说明 |
|------|------|
| `$...$` | 行内公式 |
| `\[...\]` | 行间公式 |
| `\frac{a}{b}` | 分式 |
| `\sqrt{x}` | 根式 |
| `\sum`, `\prod`, `\int` | 求和/乘积/积分 |
| `\alpha`, `\beta`, `\gamma` | 希腊字母 |
| `\sin`, `\cos`, `\log` | 数学算子 |

## 表格

| 命令 | 说明 |
|------|------|
| `\begin{tabular}{cols}` | 表格开始 |
| `&` | 列分隔 |
| `\` | 行结束 |
| `\hline` | 横线 |
| `\multicolumn{n}{c}{}` | 跨列合并 |

## 插图

| 命令 | 说明 |
|------|------|
| `\includegraphics[opts]{f}` | 插入图片 |
| `\graphicspath{{dir/}}` | 图片路径 |
| `\caption{}` | 标题 |

## 引用

| 命令 | 说明 |
|------|------|
| `\label{key}` | 标签 |
| `\ref{key}` | 引用 |
| `\pageref{key}` | 引用页码 |
| `\cite{key}` | 文献引用 |
| `\bibliography{file}` | 文献数据库 |
