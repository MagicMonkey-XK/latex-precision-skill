---
name: font-encoding
description: "LaTeX NFSS 字体坐标参数：编码、族、系列、形状的取值与含义"
---

# NFSS 字体坐标与编码

## NFSS 四维坐标

LaTeX 的 New Font Selection Scheme (NFSS) 使用四个维度确定字体：

### 1. 编码（Encoding）

| 代码 | 说明 | 适用引擎 |
|:----:|------|:--------:|
| `OT1` | 原始 TeX 编码（7-bit） | 全部 |
| `T1` | 扩展西文编码（8-bit，Cork） | 全部 |
| `T2A/B/C` | 西里尔字母编码 | pdflatex |
| `EU1` | Unicode 编码 | xelatex |
| `EU2` | Unicode 编码 | lualatex |
| `OML` | 数学字母 | 全部 |
| `OMS` | 数学符号 | 全部 |
| `OMX` | 大数学符号 | 全部 |

### 2. 族（Family）

| 声明 | 命令 | 含义 |
|:----:|:----:|------|
| `\rmfamily` | `\textrm{}` | 罗马（衬线）体 |
| `\sffamily` | `\textsf{}` | 无衬线体 |
| `\ttfamily` | `\texttt{}` | 等宽体 |

### 3. 系列（Series）

| 声明 | 命令 | 含义 |
|:----:|:----:|------|
| `\mdseries` | `\textmd{}` | 中等（常规） |
| `\bfseries` | `\textbf{}` | 粗体 |

### 4. 形状（Shape）

| 声明 | 命令 | 含义 |
|:----:|:----:|------|
| `\upshape` | `\textup{}` | 直立（常规） |
| `\itshape` | `\textit{}` | 斜体 |
| `\slshape` | `\textsl{}` | 倾斜体 |
| `\scshape` | `\textsc{}` | 小型大写 |

## 字体选择命令组合

```latex
\textit{\textbf{粗斜体}}           % 组合形状和系列
{\bfseries\itshape 粗斜体文本}     % 声明形式组合
```

## fontspec 等效命令

在 xelatex/lualatex 中，fontspec 宏包提供更直观的字体选择：

```latex
\usepackage{fontspec}
\setmainfont{Times New Roman}       % 设置罗马体
\setsansfont{Arial}                  % 设置无衬线体
\setmonofont{Courier New}            % 设置等宽体

\newfontfamily\myfont{Source Han Serif CN}  % 自定义字体命令
```

## 中文字体（ctex）

```latex
\songti     % 宋体（对应 \rmfamily）
\heiti      % 黑体（对应 \sffamily）
\fangsong   % 仿宋
\kaishu     % 楷体
```
