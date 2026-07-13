---
name: tables
description: "LaTeX 表格：tabular/array、列格式、合并、tabularx/longtable、三线表booktabs、彩色表格"
---

# 表格

## tabular 环境

```latex
\begin{tabular}{列格式}
内容
\end{tabular}
```

### 列格式参数

| 格式 | 说明 |
|:----:|------|
| `l` | 左对齐 |
| `c` | 居中对齐 |
| `r` | 右对齐 |
| `p{width}` | 固定宽度（自动换行，顶端对齐） |
| `m{width}` | 固定宽度（居中对齐，需array宏包） |
| `b{width}` | 固定宽度（底端对齐，需array宏包） |
| `|` | 竖线 |
| `@{text}` | 插入文本（替换列间距） |
| `*{n}{格式}` | 重复格式 n 次 |

### 基本示例

```latex
\begin{tabular}{|c|c|c|}
\hline
姓名 & 年龄 & 城市 \
\hline
张三 & 25 & 北京 \
李四 & 30 & 上海 \
\hline
\end{tabular}
```

## 行与列线

```latex
\hline              % 横线
\cline{i-j}         % 从第i到第j列的横线
```

## array 环境（行内数学表格）

```latex
\[
\begin{array}{ccc}
a & b & c \
d & e & f
\end{array}
\]
```

## 表格单元合并

```latex
\multicolumn{列数}{列格式}{内容}    % 跨列合并
```

需加载 multirow 宏包：

```latex
\usepackage{multirow}
\multirow{行数}{宽度}{内容}        % 跨行合并（宽度填*自动）
```

## 定宽表格（tabularx）

自动调整列宽到指定总宽：

```latex
\usepackage{tabularx}
\begin{tabularx}{\textwidth}{|X|X|X|}
\hline
左 & 中 & 右 \
\hline
\end{tabularx}
```

## 长表格（longtable）

跨页自动断开的表格，适合多行数据：

```latex
\usepackage{longtable}
\begin{longtable}{|c|c|c|}
\caption{标题}\label{tab:long}\
\hline
表头1 & 表头2 & 表头3 \
\hline
\endfirsthead
\multicolumn{3}{c}{续表}\
\hline
表头1 & 表头2 & 表头3 \
\hline
\endhead
\hline
\endfoot
数据1 & 数据2 & 数据3 \
数据4 & 数据5 & 数据6 \
\end{longtable}
```

## 三线表（booktabs）

```latex
\usepackage{booktabs}
\begin{tabular}{lccr}
\toprule
项目 & 指标1 & 指标2 & 指标3 \
\midrule
产品A & 1.2 & 3.4 & 5.6 \
产品B & 7.8 & 9.0 & 1.2 \
\bottomrule
\end{tabular}
```

## 彩色表格

```latex
\usepackage{xcolor, colortbl}
\rowcolors{2}{gray!10}{white}   % 斑马纹
```

## 浮动表格

```latex
\begin{table}[htbp]
\centering
\caption{标题}\label{tab:ex}
\begin{tabular}{lc}
\toprule
... \
\bottomrule
\end{tabular}
\end{table}
```

浮动体详细说明见 [graphics.md](graphics.md)。
