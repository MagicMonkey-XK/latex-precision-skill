---
name: graphics
description: "LaTeX 插图与浮动体：graphicx插图、浮动体控制、caption、subcaption、xcolor、TikZ简介"
---

# 插图与浮动体

## graphicx 宏包

### 加载与基本用法

```latex
\usepackage{graphicx}
\includegraphics{filename}         % 插入图片
\includegraphics[width=5cm]{fig}   % 指定宽度
\includegraphics[height=3cm]{fig}  % 指定高度
\includegraphics[scale=0.5]{fig}   % 缩放比例
```

### 可选参数

| 参数 | 示例 | 说明 |
|------|------|------|
| `width` | `width=0.5\textwidth` | 宽度（按比例缩放到此宽） |
| `height` | `height=3cm` | 高度 |
| `scale` | `scale=0.5` | 缩放比例 |
| `angle` | `angle=90` | 旋转角度 |
| `trim` | `trim=1cm 2cm 1cm 2cm` | 裁剪（左 下 右 上） |
| `clip` | `clip` | 启用裁剪（与trim配合） |
| `keepaspectratio` | `keepaspectratio` | 保持宽高比 |

```latex
% 缩放至页面宽度的80%
\includegraphics[width=0.8\textwidth]{figure.png}

% 旋转+缩放
\includegraphics[angle=90, scale=0.5]{portrait.pdf}

% 裁剪白边
\includegraphics[trim=5mm 5mm 5mm 5mm, clip]{photo.jpg}
```

### 支持的图片格式

| 引擎 | 支持格式 |
|------|---------|
| pdflatex | PDF, PNG, JPEG, GIF |
| xelatex | PDF, PNG, JPEG, EPS（需eps2pdf） |
| lualatex | PDF, PNG, JPEG, EPS |

### 图片路径设置

```latex
\graphicspath{{images/}{figures/}}   % 设置图片搜索路径
```

## 几何变换

```latex
\scalebox{2}{内容}           % 缩放内容
\reflectbox{内容}            % 水平翻转
\resizebox{5cm}{!}{内容}     % 缩放至指定宽
\rotatebox{45}{内容}         % 旋转45度
```

## 浮动体

### figure 浮动体

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figure.png}
\caption{图片标题}
\label{fig:example}
\end{figure}
```

### table 浮动体

```latex
\begin{table}[htbp]
\centering
\caption{表格标题}
\label{tab:example}
\begin{tabular}{lc}
...表格内容...
\end{tabular}
\end{table}
```

### 浮动位置参数

| 参数 | 含义 |
|:----:|------|
| `h` | here，当前位置（尽量放在代码所在处） |
| `t` | top，页面顶部 |
| `b` | bottom，页面底部 |
| `p` | page，单独浮动页 |
| `!` | 忽略内部限制（如 `[!ht]`） |
| `H` | 绝对定位（需float宏包） |

默认参数 `[tbp]`，推荐使用 `[htbp]`（LaTeX会自动选择最佳位置）。

### 浮动体控制

```latex
\usepackage{float}
\begin{figure}[H]      % H = 严格在此位置（不浮动）
\includegraphics{fig.png}
\caption{固定位置}
\end{figure}
```

### 防止浮动体越过 section

```latex
\usepackage[section]{placeins}  % float barrier
```

## 标题控制（caption 宏包）

```latex
\usepackage{caption}
\captionsetup{
  font=small,           % 标题字体大小
  labelsep=period,      % 分隔符（图1. → 图1.）
  justification=centering,  % 标题居中
  format=plain          % plain / hang
}
```

## 并排与子图表（subcaption）

```latex
\usepackage{subcaption}

\begin{figure}[htbp]
\centering
\begin{subfigure}{0.45\textwidth}
\includegraphics[width=\textwidth]{fig1.png}
\caption{子图1}
\label{fig:sub1}
\end{subfigure}
\hfill
\begin{subfigure}{0.45\textwidth}
\includegraphics[width=\textwidth]{fig2.png}
\caption{子图2}
\label{fig:sub2}
\end{subfigure}
\caption{总标题}
\label{fig:both}
\end{figure}
```

## 文字绕排

```latex
\usepackage{wrapfig}

\begin{wrapfigure}{r}{4cm}
\includegraphics[width=4cm]{fig.png}
\caption{绕排图片}
\end{wrapfigure}
```

- `r` = 右侧，`l` = 左侧
- 第二参数为图片宽度

## 彩色（xcolor 宏包）

```latex
\usepackage{xcolor}

% 颜色用法
\textcolor{red}{红色文字}          % 文字颜色
\color{blue}                        % 切换颜色
\colorbox{yellow}{黄底文字}        % 背景色
\fcolorbox{red}{yellow}{红框黄底}  % 带框背景色

% 颜色混合
red!50          % 50%红色
red!20!blue     % 20%红 + 80%蓝
```

### 预定义颜色

基本颜色：`red`、`green`、`blue`、`cyan`、`magenta`、`yellow`、`black`、`white`、`gray`

### 自定义颜色

```latex
\definecolor{mycolor}{RGB}{210, 30, 50}
\definecolor{darkgreen}{rgb}{0, 0.5, 0}
```

## TikZ 绘图简介

```latex
\usepackage{tikz}
\usetikzlibrary{shapes, arrows, positioning}
```

### 基本图形

```latex
\begin{tikzpicture}
% 画线
\draw (0,0) -- (2,0);
% 画箭头
\draw[->] (0,1) -- (2,1);
% 画矩形
\draw (0,0) rectangle (2,1);
% 画圆
\draw (1,0) circle (0.5);
% 填充
\fill[blue!20] (0,0) rectangle (2,1);
\end{tikzpicture}
```

### 节点与文字

```latex
\begin{tikzpicture}
\node[draw] at (0,0) {节点文字};
\node[draw, circle] at (2,0) {圆形};
\end{tikzpicture}
```

### 流程图示例

```latex
\begin{tikzpicture}[node distance=1.5cm]
\node[draw, rectangle] (start) {开始};
\node[draw, diamond, below of=start] (decide) {判断};
\node[draw, rectangle, below of=decide] (end) {结束};

\draw[->] (start) -- (decide);
\draw[->] (decide) -- node[right]{是} (end);
\end{tikzpicture}
```

## 跨文件引用

- [tables.md](tables.md) — 表格与浮动表格
- [environment.md](environment.md) — fontspec 等字体相关
