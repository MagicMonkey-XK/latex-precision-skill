---
name: math-formulas
description: "LaTeX 数学公式：行内/行间模式、数学结构、符号体系、多行公式、编号控制"
---

# 数学公式

## 数学模式

### 行内模式 vs 行间模式

| 模式 | 使用方式 | 效果 |
|------|---------|------|
| 行内 | `$...$` 或 `\(...\)` | 公式嵌入文本行中 |
| 行间 | `\[...\]` 或 `$$...$$` | 公式单独一行居中显示 |
| 行间（编号） | `\begin{equation}...\end{equation}` | 公式单独一行并自动编号 |

```latex
行内公式：$E = mc^2$
行间公式：\[ E = mc^2 \]
编号公式：
\begin{equation}
E = mc^2
\end{equation}
```

### 数学模式包（amsmath）

```latex
\usepackage{amsmath}   % 数学公式增强，必须加载
\usepackage{amssymb}   % 额外数学符号
```

## 数学结构

### 上标与下标

```latex
$x^2$          % 上标
$x_1$          % 下标
$x^{2n+1}$    % 多字符上标
$x_{ij}$      % 多字符下标
$x^{y^z}$     % 多重上标
$x_1^2$       % 同时上下标
\vec{x}       % 向量箭头
\hat{x}       % 帽子
\tilde{x}     % 波浪
\dot{x}       % 点（一阶导数）
\ddot{x}      % 两点（二阶导数）
```

### 上下画线与花括号

```latex
\overline{abc}     % 上划线
\underline{abc}    % 下划线
\overbrace{a+b+c}^{\text{三项}}  % 上花括号
\underbrace{a+b+c}_{\text{三项}}  % 下花括号
```

### 分式

```latex
\frac{分子}{分母}       % 标准分式
\tfrac{分子}{分母}       % 紧凑分式（行内用）
\dfrac{分子}{分母}       % 展示分式（行间用）
\cfrac{分子}{分母}       % 连分数
```

示例：
```latex
\[
\frac{1}{2} \qquad
\frac{x^2 + 1}{x - 1}
\]
```

### 根式

```latex
\sqrt{x}               % 平方根
\sqrt[n]{x}            % n次方根
\sqrt[3]{x + y}        % 立方根
```

### 矩阵

```latex
% 无括号矩阵
\begin{matrix}
1 & 2 \
3 & 4
\end{matrix}

% 带括号矩阵
\begin{pmatrix}   % 圆括号
\begin{bmatrix}   % 方括号
\begin{Bmatrix}   % 花括号
\begin{vmatrix}   % 竖线
\begin{Vmatrix}   % 双竖线
```

点列（省略号）：
```latex
\dots   % 横向省略号
\ddots  % 对角线省略号
\vdots  % 纵向省略号
```

## 符号体系

### 字母表与普通符号

| 输入 | 输出 | 输入 | 输出 |
|------|:----:|------|:----:|
| `\alpha` | α | `\beta` | β |
| `\gamma` | γ | `\delta` | δ |
| `\epsilon` | ε | `\varepsilon` | ε(变体) |
| `\theta` | θ | `\vartheta` | ϑ |
| `\pi` | π | `\varpi` | ϖ |
| `\mu` | µ | `\lambda` | λ |
| `\sigma` | σ | `\sum` | Σ |
| `\omega` | ω | `\Omega` | Ω |
| `\infty` | ∞ | `\partial` | ∂ |
| `\ell` | ℓ | `\nabla` | ∇ |
| `\hbar` | ℏ | `\imath` | ı |

### 数学算子（直立体）

```latex
\sin \cos \tan \cot \sec \csc    % 三角函数
\arcsin \arccos \arctan          % 反三角函数
\sinh \cosh \tanh                % 双曲函数
\exp \log \ln \lg                % 指数与对数
\lim \limsup \liminf             % 极限
\max \min \sup \inf              % 极值
\gcd \det \deg \arg              % 其他算子
```

带上下限的算子：
```latex
\lim_{x \to 0} f(x)     % 极限
\sum_{i=1}^{n} a_i      % 求和
\prod_{i=1}^{n} a_i     % 连乘
\int_{a}^{b} f(x)\,dx   % 积分
\iint_{D} f(x,y)\,dxdy  % 二重积分
\iiint_{V}              % 三重积分
\oint                    % 围道积分
\bigcup_{i=1}^{n}       % 并集
\bigcap_{i=1}^{n}       % 交集
```

### 二元运算符与关系符

```latex
+ - \times \div \pm \mp \cdot \circ \ast

= \neq \approx \equiv \sim \simeq \cong
< > \leq \geq \ll \gg \subset \supset
\in \ni \subseteq \supseteq \subsetneq
\perp \parallel \mid \nmid
\Rightarrow \Leftarrow \Leftrightarrow
\mapsto \hookrightarrow \to \gets
```

### 括号与定界符

```latex
( ) [ ] \{ \}             % 标准括号
\langle \rangle           % 尖括号 ⟨⟩
\lvert \rvert \lVert \rVert  % 绝对值/范数
```

自动调整大小：
```latex
\left( \frac{a}{b} \right)       % 自动匹配高度的括号
\left\{ x \mid x > 0 \right\}
\right.                           % 不显示右括号（成对使用）
```

手动指定大小：
```latex
\bigl( \Bigl( \biggl( \Biggl(
\bigr) \Bigr) \biggr) \Biggr)
```

### 数学标点

```latex
$a + b = c,$  % 逗号后加小空格
$a + b = c.$  % 句号
f'(x)          % 导数撇
```

## 多行公式

### align 环境（多行对齐）

```latex
\begin{align}
y &= x^2 + 2x + 1 \
  &= (x + 1)^2
\end{align}
```

- `&` 标记对齐点
- `\` 换行
- 每行自动编号
- 用 `\nonumber` 或 `\notag` 取消某行编号

### align* 环境（不编号）

```latex
\begin{align*}
y &= mx + b \
E &= mc^2
\end{align*}
```

### gather 环境（多行居中）

```latex
\begin{gather}
a + b = c \
d + e = f
\end{gather}
```

### multline 环境（单公式多行）

```latex
\begin{multline}
a + b + c + d + e + f + g \
  + h + i + j + k + l + m + n \
  + o + p + q
\end{multline}
```

第一行左对齐，最后一行右对齐，中间行居中。

### 公式组拆分

```latex
\begin{align}
x &= a + b \nonumber \
  &= c + d + e + f \nonumber \
  &= g + h \label{eq:result}
\end{align}
```

### 花括号公式组

```latex
\begin{cases}
y = x^2 + 1 \
z = y - 1
\end{cases}
```

## 编号控制

### 取消编号

```latex
\begin{equation*}
公式不编号
\end{equation*}

\[
公式不编号
\]
```

### 交叉引用公式

```latex
\begin{equation}
E = mc^2 \label{eq:energy}
\end{equation}
公式~\eqref{eq:energy} 是质能方程。
```

## 数学间距

| 命令 | 效果 | 宽度 |
|------|:----:|:----:|
| `\,` | 小间距 | 3/18 em |
| `\:` | 中间距 | 4/18 em |
| `\;` | 大间距 | 5/18 em |
| `\!` | 负间距 | -3/18 em |
| `\quad` | 1 em | 18/18 em |
| `\qquad` | 2 em | 36/18 em |

示例：
```latex
$\int_{a}^{b} f(x)\,dx$         % 积分前小间距
$f(x) = x^2,\quad g(x) = x^3$   % 公式间分隔
```

## 跨文件引用

- [cross-refs.md](cross-refs.md) — 交叉引用与标签
- [wiki/symbols-reference.md](wiki/symbols-reference.md) — 完整符号表
