---
name: beamer
description: "LaTeX 幻灯片（beamer）：帧结构、节与目录、主题、区块、图表、动态展示"
---

# 幻灯片（beamer）

## 基本结构

```latex
\documentclass{beamer}
\usepackage[UTF8]{ctex}

\title{幻灯片标题}
\author{作者姓名}
\date{2025年}

\begin{document}

\maketitle          % 标题页

\begin{frame}{第一页}
内容
\end{frame}

\end{document}
```

## 帧（Frame）

### 基本帧

```latex
\begin{frame}{帧标题}
内容
\end{frame}

\begin{frame}{帧标题}{子标题}
内容
\end{frame}

% 无标题帧
\begin{frame}
内容
\end{frame}
```

### 帧标题与内容控制

```latex
% 隐藏导航栏
\begin{frame}[plain]{无导航栏}
内容
\end{frame}

% 不显示帧编号
\begin{frame}[noframenumbering]{不计入编号}
内容
\end{frame}

% 允许内容超出帧（自动缩小）
\begin{frame}[shrink]{自动缩小}
很多很多内容...
\end{frame}
```

## 文档信息与目录

### 标题页

```latex
\title[短标题]{全标题}
\author[缩写]{作者姓名}
\institute[单位缩写]{单位名称}
\date[短日期]{2025年1月}
\titlegraphic{\includegraphics[width=2cm]{logo.png}}

\begin{frame}
\maketitle
\end{frame}
```

### 节与目录

```latex
\section{引言}
\subsection{背景}

\begin{frame}{目录}
\tableofcontents
\end{frame}

% 每节开始前显示目录（高亮当前节）
\AtBeginSection[]{
  \begin{frame}{目录}
  \tableofcontents[currentsection]
  \end{frame}
}
```

## 主题

### 主题选择

```latex
\usetheme{default}       % 默认（无装饰）
\usetheme{Madrid}        % 蓝底顶部
\usetheme{CambridgeUS}   % 顶部条
\usetheme{Berlin}        % 顶部导航
\usetheme{Boadilla}      % 简洁
\usetheme{Warsaw}        % 经典
\usetheme{Singapore}     % 细条形
\usetheme{Frankfurt}     % 圆点导航
```

### 颜色主题

```latex
\usecolortheme{default}
\usecolortheme{dolphin}
\usecolortheme{beetle}
\usecolortheme{crane}
\usecolortheme{seahorse}
\usecolortheme{whale}
```

### 字体主题

```latex
\usefonttheme{default}
\usefonttheme{serif}          % 衬线字体
\usefonttheme{sansserif}      % 无衬线字体
\usefonttheme{professionalfonts}  % 专业字体
```

### 内部/外部主题

```latex
\useinnertheme{circles}       % 圆形条目
\useinnertheme{rectangles}    % 矩形条目
\useinnertheme{rounded}       % 圆角矩形

\useoutertheme{infolines}     % 顶部/底部信息条
\useoutertheme{miniframes}    % 小帧导航
\useoutertheme{sidebar}       % 侧边栏
```

### 自定义颜色

```latex
\setbeamercolor{结构}{fg=blue!60!black}
\setbeamercolor{标题}{fg=red,bg=yellow!20}
\setbeamercolor{正文}{fg=black}
```

## 区块

### 基本区块

```latex
\begin{block}{区块标题}
区块内容
\end{block}

\begin{alertblock}{警告}
突出显示的内容
\end{alertblock}

\begin{examples}
一个例子
\end{examples}
```

### 定理环境

```latex
\begin{theorem}
定理内容
\end{theorem}

\begin{proof}
证明过程
\end{proof}

\begin{definition}
定义内容
\end{definition}
```

## 列表与文本

```latex
% 逐条显示（默认）
\begin{itemize}[<+-| alert@+>]
\item 第一项
\item 第二项
\item 第三项
\end{itemize}

% 编号列表
\begin{enumerate}
\item 第一步
\item 第二步
\end{enumerate}

% 列
\begin{columns}
\column{0.5\textwidth}
左列内容
\column{0.5\textwidth}
右列内容
\end{columns}
```

## 图表

### 插图

```latex
\begin{frame}{插图}
\begin{figure}
\includegraphics[width=0.8\textwidth]{figure.png}
\caption{标题}
\end{figure}
\end{frame}
```

### 表格

```latex
\begin{frame}{表格}
\begin{table}
\begin{tabular}{lcr}
\toprule
参数 & 值 & 单位 \
\midrule
电压 & 3.3 & V \
电流 & 125 & mA \
\bottomrule
\end{tabular}
\caption{参数表}
\end{table}
\end{frame}
```

## 动态展示

### 覆盖（overlay）

```latex
% 逐步显示（使用 <n-> 语法）
\begin{frame}{逐步显示}
\begin{itemize}
\item<1-> 第一项
\item<2-> 第二项
\item<3-> 第三项
\end{itemize}
\end{frame}

% 更简洁的写法
\begin{itemize}[<+->]
\item 依次出现
\item 前一项消失后出现
\end{itemize}
```

### 覆盖 spec

```latex
\onslide<1>{仅第一页显示}
\onslide<2->{第二页及之后显示}
\onslide<3-4>{第三到第四页显示}

\textbf<2>{仅第二页加粗}
\color<3>{red}{第三页红色}

% 逐步显示
\only<1>{第一步}
\only<2>{第二步}
```

### 动态强调

```latex
\begin{frame}{动态表格}
\begin{tabular}{lcr}
\toprule
\rowcolor<2>{red!20}
参数 & 值 & 单位 \
\midrule
电压 & 3.3 & V\only<2>{（标准）} \
\bottomrule
\end{tabular}
\end{frame}
```

## 多媒体

```latex
\usepackage{multimedia}

\movie[width=4cm,height=3cm]{视频说明}{movie.avi}
\sound[autostart]{声音说明}{sound.wav}
```

## 编译

```latex
% 使用 pdflatex 或 xelatex
pdflatex slide.tex
pdflatex slide.tex   % 需2次编译处理目录

% 或使用 latexmk
latexmk -pdf slide.tex
latexmk -xelatex slide.tex
```

## 中文 beamer 注意事项

1. 需加载 `ctex` 宏包或 `ctexbeamer` 文档类
2. 推荐使用 xelatex 编译
3. 中文下最好使用 `\usefonttheme{professionalfonts}` 避免字体警告
4. 部分主题（如 Berlin）导航条中的中文可能显示异常

```latex
\documentclass[UTF8]{ctexbeamer}   % 中文beamer文档类
\usefonttheme{professionalfonts}
```

## 跨文件引用

- [math-formulas.md](math-formulas.md) — 数学公式
- [tables.md](tables.md) — 表格制作
- [graphics.md](graphics.md) — 插图与浮动体
