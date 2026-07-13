---
name: text-formatting
description: "LaTeX 文字排版：特殊符号、NFSS字体、中文字体ctex、段落、列表、定理、抄录、脚注"
---

# 文字排版

## 特殊符号与转义

LaTeX 中以下特殊字符需要转义才能显示：

| 输入 | 输出 | 说明 |
|------|------|------|
| `\#` | # | 井号 |
| `\$` | $ | 美元符号 |
| `\%` | % | 百分号 |
| `\&` | & | and符号 |
| `\_{}` | _ | 下划线 |
| `\^{}` | ˆ | 抑扬符 |
| `\~{}` | ˜ | 波浪符 |
| `\textbackslash` | \ | 反斜线 |
| `\{` `\}` | { } | 花括号 |

### 引号与标点

```latex
``双引号''      % 反引号+单引号组合 → "
`单引号'        % → '
-- 短破折号     % 数字范围：1--10
--- 长破折号    % 语意破折号
\dots 或 \ldots % 省略号 …
$^\circ$C      % 摄氏度 ℃
```

### 连字符与破折号

- `-` 连字符（hyphen）：`well-known`
- `--` 短破折号（en-dash）：`pages 1--10`
- `---` 长破折号（em-dash）：`this is---like---amazing`

### 不可见字符

- 多个连续空格等价于一个空格
- 单个换行等价于空格
- 空行分段（新段落开始）
- `%` 注释：该行 `%` 之后的内容被忽略

## NFSS 字体体系

LaTeX 的 NFSS（New Font Selection Scheme）用四维坐标选择字体。

### 四维坐标

| 维度 | 代码 | 含义 |
|:----:|:----:|------|
| 编码（Encoding） | `T1` | 西文字符编码（8-bit） |
| | `OT1` | 原始 TeX 编码 |
| | `EU1` / `EU2` | Unicode 编码（xelatex/lualatex） |
| 族（Family） | `rm` | 罗马/衬线体 |
| | `sf` | 无衬线体 |
| | `tt` | 等宽体 |
| 系列（Series） | `m` | 中等（常规） |
| | `bx` | 粗体 |
| 形状（Shape） | `n` | 直立（常规） |
| | `it` | 斜体 |
| | `sl` | 倾斜 |
| | `sc` | 小型大写 |

### 字体命令

| 命令 | 声明形式 | 效果 |
|------|---------|------|
| `\textrm{text}` | `{\rmfamily text}` | 罗马体 |
| `\textsf{text}` | `{\sffamily text}` | 无衬线体 |
| `\texttt{text}` | `{\ttfamily text}` | 等宽体 |
| `\textbf{text}` | `{\bfseries text}` | 粗体 |
| `\textit{text}` | `{\itshape text}` | 斜体 |
| `\textsl{text}` | `{\slshape text}` | 倾斜体 |
| `\textsc{text}` | `{\scshape text}` | 小型大写 |
| `\textup{text}` | `{\upshape text}` | 直立（恢复正常） |
| `\emph{text}` | `{\em text}` | 强调（逻辑语义） |

### fontspec 宏包（xelatex/lualatex）

使用系统字体而非 TeX 字体：

```latex
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}
```

### 中文字体（ctex）

ctex 宏包提供了快捷中文字体切换命令：

```latex
\songtip    % 宋体（默认）
\heiti      % 黑体
\fangsong   % 仿宋
\kaishu     % 楷体
```

也可用 fontspec 设置 CJK 主字体：

```latex
\setCJKmainfont{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{FangSong}
```

## 字号

| 命令 | 效果 | 对应大小（12pt基准） |
|------|------|:----:|
| `\tiny` | 极小 | 6pt |
| `\scriptsize` | 脚注大小 | 8pt |
| `\footnotesize` | 脚注 | 9pt |
| `\small` | 小 | 10pt |
| `\normalsize` | 正常 | 12pt（基准） |
| `\large` | 大 | 14pt |
| `\Large` | 更大 | 17pt |
| `\LARGE` | 很大 | 20pt |
| `\huge` | 巨大 | 25pt |
| `\Huge` | 极大 | 30pt |

用法示例：

```latex
{\large 大号文字} \quad {\huge 巨大号文字}
```

## 行距

```latex
\linespread{1}      % 默认
\linespread{1.3}    % 1.5倍行距
\linespread{1.6}    % 双倍行距
```

## 段落格式

### 对齐环境

| 环境 | 效果 |
|------|------|
| `center` | 居中 |
| `flushleft` | 左对齐 |
| `flushright` | 右对齐 |

### 缩进与间距

```latex
\setlength{\parindent}{2em}      % 段落缩进（默认2字符宽）
\setlength{\parskip}{0.5em}      % 段间距
\noindent                         % 当前段不缩进
\indent                           % 强制缩进
```

## 水平间距与盒子

```latex
\quad      % 1 em 间距
\qquad     % 2 em 间距
\,         % 小间距（3/18 em）
\:         % 中间距（4/18 em）
\;         % 大间距（5/18 em）
\hspace{2cm}       % 指定宽度水平间距
\hspace*{2cm}      % 行首也生效
\hfill              % 弹性填充（撑满整行）

\mbox{不换行文本}                % 防止换行的盒子
\makebox[3cm]{居中文本}          % 定宽盒子
\parbox[t]{5cm}{多行文本}        % 段落盒子
\fbox{带框文字}                  % 带边框盒子
\framebox[3cm]{定宽带框}        % 定宽带框
```

## 垂直间距

```latex
\smallskip    % 小间距（约 3pt）
\medskip      % 中间距（约 6pt）
\bigskip      % 大间距（约 12pt）
\vspace{1cm}           % 指定垂直间距
\vspace*{1cm}          % 页面开头也生效
\vfill                  % 弹性垂直填充
\newpage                % 换页
\clearpage              % 换页并清空浮动体
```

## 列表环境

### itemize（无编号列表）

```latex
\begin{itemize}
  \item 第一项
  \item 第二项
  \begin{itemize}
    \item 子项（嵌套）
  \end{itemize}
\end{itemize}
```

### enumerate（编号列表）

```latex
\begin{enumerate}
  \item 第一步
  \item 第二步
\end{enumerate}
```

### description（描述列表）

```latex
\begin{description}
  \item[CPU] 中央处理器
  \item[RAM] 随机存取存储器
\end{description}
```

### 嵌套深度

最多 4 层嵌套。每层有独立的计数器：

| 层级 | 环境 | 计数器 | 默认格式 |
|:----:|:----:|:------:|:--------:|
| 1 | enumi | `enumi` | 1. |
| 2 | enumii | `enumii` | (a) |
| 3 | enumiii | `enumiii` | i. |
| 4 | enumiv | `enumiv` | A. |

### 定制列表编号格式

```latex
\renewcommand{\labelenumi}{\Alph{enumi}}       % A, B, C...
\renewcommand{\labelenumii}{\roman{enumii}}    % i, ii, iii...
\renewcommand{\theenumi}{\Alph{enumi}}         % 引用显示格式
```

编号格式宏：
- `\arabic` — 阿拉伯数字
- `\roman` / `\Roman` — 小写/大写罗马数字
- `\alph` / `\Alph` — 小写/大写字母

## 定理类环境

### 定义新定理

```latex
\usepackage{amsthm}

\newtheorem{theorem}{定理}[section]    % 按章编号
\newtheorem{definition}{定义}
\newtheorem{lemma}{引理}

% 使用
\begin{theorem}
  这是一个定理。
\end{theorem}
```

### proof 环境

```latex
\begin{proof}
  证明过程...
\end{proof}
```

## 抄录环境

### 行内抄录

```latex
\verb|code_here|
\verb*|code here|     % 显示空格
```

注意：`\verb` 不能在命令参数中使用（脆弱命令）。

### 抄录环境

```latex
\begin{verbatim}
原始文本内容
空格  和  制表符  保持原样
\end{verbatim}
```

### listings 宏包（代码展示，推荐）

```latex
\usepackage{listings}
\lstset{
  basicstyle=\ttfamily\small,
  numbers=left,
  numberstyle=\tiny,
  language=Python,
  frame=single,
  breaklines=true
}

\begin{lstlisting}[caption=示例代码]
def hello():
    print("Hello, World!")
\end{lstlisting}
```

从文件读入代码：
```latex
\lstinputlisting[language=C]{source.c}
```

## 脚注

```latex
\footnote{脚注内容}
```

- 脚注自动编号，每页重新计数（或连续计数）
- 注意事项：
  - `\verb` 不能在脚注中使用
  - 脚注中建议不要使用过长内容
- 脚注编号格式定制：
  ```latex
  \renewcommand{\thefootnote}{\fnsymbol{footnote}}  % 符号编号
  ```

## 跨文件引用

- [document-structure.md](document-structure.md) — 文档结构
- [math-formulas.md](math-formulas.md) — 数学公式
- [wiki/font-encoding.md](wiki/font-encoding.md) — NFSS 字体坐标详情
- [wiki/ctex-guide.md](wiki/ctex-guide.md) — ctex 宏包详细选项
- [environment.md](environment.md) — fontspec 字体配置
