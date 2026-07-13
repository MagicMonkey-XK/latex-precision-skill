---
name: macros
description: "LaTeX 自定义命令与宏编写：newcommand、def、条件判断、编写sty/cls"
---

# 自定义命令与宏编写

## 自定义命令

### \newcommand

```latex
\newcommand{\命令名}[参数个数]{定义}
```

**示例：**
```latex
% 无参数
\newcommand{\tn}{\textsuperscript{TM}}

% 1个参数
\newcommand{\abbr}[1]{\textbf{#1}}

% 2个参数
\newcommand{\product}[2]{\textbf{#1}（型号：#2）}

% 使用
\product{光模块}{BH85D04001}
```

### 带默认值的参数

```latex
\newcommand{\chem}[2][C]{\ensuremath{#1_{#2}}}

\chem{H}{2}O    % H₂O
\chem{O}{3}     % C₃（省略可选参数时用默认值C）
```

### \renewcommand（重定义已有命令）

```latex
\renewcommand{\thefootnote}{\fancyfootnote}
```

### 现代方法：\NewDocumentCommand（xparse）

```latex
\usepackage{xparse}   % 或使用 LaTeX2024+（已内置）

\NewDocumentCommand{\product}{ O{标准版} m m }{
  产品：{#3}，型号：{#2}，版本：{#1}
}

% 使用
\product{BH85D04}{光模块A}
\product[增强版]{BH85D08}{光模块B}
```

参数类型：
- `m` — 必选参数
- `o` — 可选参数（默认无值）
- `O{val}` — 可选参数（默认值 val）
- `s` — 星号参数（\cmd* 形式）

## 定义环境

### \newenvironment

```latex
\newenvironment{环境名}[参数个数]{起始代码}{结束代码}

\newenvironment{mycenter}{
  \begin{center}
}{
  \end{center}
}
```

### 带参数的环境

```latex
\newenvironment{note}[1][注意]{
  \textbf{#1：}\par
}{
  \par
}

\begin{note}[提示]
这是一段提示文字。
\end{note}
```

## TeX 底层命令

### \def 与 \edef

```latex
\def\foo{内容}              % 定义命令
\def\foo#1{内容#1}          % 带参数
\edef\foo{内容}             % 展开后定义（内容中的命令会被展开）
```

### \gdef（全局定义）

```latex
\gdef\globalvar{全局值}     % 全局定义（在组外仍有效）
```

### \let（复制定义）

```latex
\let\oldcmd\cmd             % 保存命令原有定义
\renewcommand{\cmd}{新定义\oldcmd}  % 在原有基础上扩展
```

## 条件判断

### \ifnum（数值判断）

```latex
\ifnum\value{page}>10
  第10页之后
\else
  第10页及之前
\fi
```

### \ifdim（尺寸判断）

```latex
\ifdim\textwidth>10cm
  宽版
\else
  窄版
\fi
```

### \ifx（命令/字符判断）

```latex
\ifx\definedcmd\undefined
  命令未定义
\else
  命令已定义
\fi
```

### \if（原始条件）

```latex
\newif\ifdraft     % 创建 \ifdraft
\drafttrue         % 设为真
\draftfalse        % 设为假

\ifdraft
  草稿模式
\else
  正式模式
\fi
```

### etoolbox 宏包（现代条件判断）

```latex
\usepackage{etoolbox}

\ifstrequal{#1}{value}{相等}{不等}
\ifnumcomp{\value{page}}{>}{10}{大于10}{小于等于10}
\ifcsequdef{cmdname}{已定义}{未定义}
```

## 字符串与循环

```latex
\usepackage{xstring}
\StrBefore{filename.tex}{.}[\basename]   % 取前缀

\usepackage{forloop}
\newcounter{mycount}
\forloop{mycount}{1}{\value{mycount}<10}{
  第 \themycount 行\
}
```

## 编写宏包（.sty）

```latex
% mypackage.sty
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{mypackage}[2025/01/01 v1.0 我的宏包]

% 处理选项
\DeclareOption{draft}{\drafttrue}
\DeclareOption{final}{\draftfalse}
\ProcessOptions\relax

% 加载其他宏包
\RequirePackage{graphicx}
\RequirePackage{xcolor}

% 自定义命令
\newcommand{\mycommand}{内容}
\newenvironment{myenv}{开始}{结束}

\endinput
```

### 条件选项处理

```latex
\newcommand{\mycmd}{\textcolor{black}}  % 默认黑色
\DeclareOption{red}{\renewcommand{\mycmd}{\textcolor{red}}}
\DeclareOption{blue}{\renewcommand{\mycmd}{\textcolor{blue}}}
\ProcessOptions\relax
```

## 编写文档类（.cls）

```latex
% myclass.cls
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{myclass}[2025/01/01 v1.0 我的文档类]

% 基于已有文档类
\LoadClass[12pt]{article}

% 自定义选项
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

% 加载宏包
\RequirePackage[margin=2cm]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{ctex}

% 页面格式
\pagestyle{fancy}
\fancyhf{}

\endinput
```

### 使用自定义文档类

```latex
\documentclass{myclass}
\begin{document}
内容...
\end{document}
```

## 注意事项

1. 命令名只能由字母组成（`\foo`），不能包含非字母字符
2. `\newcommand` 检查命令是否已定义（安全性更好）
3. `\def` 直接覆盖已有定义（不检查）
4. 宏包中应使用 `\newcommand` — 如果用户已经定义了同名命令，`\newcommand` 会报错而非静默覆盖
5. 参数个数最多 9 个（`#1` 到 `#9`）
6. 使用 `\makeatletter` / `\makeatother` 可在文档中使用含 `@` 的内部命令

## 跨文件引用

- [cross-refs.md](cross-refs.md) — 交叉引用与自动化工具
- [error.md](error.md) — 常见宏编写错误与调试
