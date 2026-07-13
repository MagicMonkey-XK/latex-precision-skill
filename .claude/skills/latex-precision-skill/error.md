---
name: latex-error
description: "LaTeX 错误排查与调试：常见错误40+、警告分析、调试技巧、最小工作示例"
---

# 错误排查与调试

## 错误信息理解

LaTeX 的错误信息格式：
```
! 错误类型
l.行号 出错行内容
                        （错误位置标记）
?
```

- 错误行以 `!` 开头
- `l.行号` 指示出错的行号
- `?` 提示等待用户输入（交互模式），可输入 `h` 查看帮助，`x` 退出

## 交互命令

| 命令 | 含义 |
|:----:|------|
| h | 显示帮助信息 |
| x | 立即退出 |
| q | 静默退出 |
| r | 跳过此错误继续 |
| s | 滚动模式（不暂停） |
| i | 插入文字后继续 |

## 常见 TeX 错误

### 1. Undefined control sequence

```
! Undefined control sequence.
l.23 \nonexistentcmd
```

**原因**：命令拼写错误或未加载对应宏包。

**解决**：
- 检查拼写是否正确
- 加载对应宏包：`tlmgr install <package>`
- 若命令在新版已改名，查询文档

### 2. Missing $ inserted

```
! Missing $ inserted.
<inserted text>
                $
l.42 文本中的 \alpha
```

**原因**：在文本模式中使用了数学命令。

**解决**：
- 将内容放入 `$...$` 或 `\[...\]`
- 或使用文本模式的等效命令（如 `\textalpha`）

### 3. Missing \begin{document}

```
! LaTeX Error: Missing \begin{document}.
```

**原因**：`\begin{document}` 之前的文本内容，或导言区中的语法错误。

**解决**：
- 检查导言区是否有未闭合的命令
- 确保 `\begin{document}` 拼写正确

### 4. Runaway argument

```
Runaway argument?
{太长且未闭合的参数...
```

**原因**：花括号未匹配，参数未正确闭合。

**解决**：
- 检查花括号配对（用编辑器的高亮功能）
- 检查是否有被注释掉的括号

### 5. Extra alignment tab

```
! Extra alignment tab has been changed to \cr.
```

**原因**：tabular 中 `&` 数量超过了列格式定义的列数。

**解决**：
- 确保每行 `&` 个数与列格式一致
- 检查 `\` 是否放对了位置

### 6. Missing number, treated as zero

```
! Missing number, treated as zero.
```

**原因**：需要数值参数的地方提供了非数值内容。

**解决**：
- 检查长度/计数器的值是否正确
- 检查参数是否为合法数字

### 7. Illegal unit of measure

```
! Illegal unit of measure (pt inserted).
```

**原因**：长度值缺少单位。

**解决**：补全单位，如 `1cm`、`10pt`、`2em`

### 8. File not found

```
! LaTeX Error: File `xxx.sty' not found.
```

**原因**：缺少宏包文件。

**解决**：
```bash
tlmgr install xxx       % TeX Live
```

或检查文件路径是否正确。

### 9. Emergency stop

```
! Emergency stop.
```

**原因**：严重错误，引擎无法继续。

**解决**：查看日志文件中此前的错误信息，先修复前面的错误。

### 10. Too deeply nested

```
! LaTeX Error: Too deeply nested.
```

**原因**：列表嵌套超过4层。

**解决**：减少嵌套层数，或使用 `list` 环境自定义。

## 常见 LaTeX 警告

### 1. Overfull \hbox

```
Overfull \hbox (12.34567pt too wide) in paragraph at lines 10--15
```

**含义**：行太宽，文字溢出页边距。

**解决**：
- 使用 `\sloppy` 或 `\emergencystretch=1em` 允许更宽松断行
- 调整页面边距
- 改写该段落（使用更短的单词/短语）
- 使用 `\hyphenation{words}` 优化断字

### 2. Underfull \hbox

```
Underfull \hbox (badness 10000) in paragraph at lines 20--25
```

**含义**：行太空（单词间距过大）。

**解决**：通常不处理（警告级别低于 Overfull），如果严重可改写段落。

### 3. Overfull \vbox / Underfull \vbox

**含义**：页面垂直方向溢出/不足，通常与分页有关。

**解决**：允许页面弹性间距，如 `\raggedbottom`。

### 4. There were undefined references

```
LaTeX Warning: There were undefined references.
```

**含义**：交叉引用未解析（通常是编译次数不够）。

**解决**：重新编译一次（或两次）。

### 5. Citation undefined

```
LaTeX Warning: Citation `key' on page 1 undefined on input line 10.
```

**含义**：参考文献引用未解析。

**解决**：运行 bibtex/biber 后重新编译两次。

### 6. Longtable column widths have changed

```
Package longtable Warning: Column widths have changed ...
```

**含义**：longtable 宽在多次编译后稳定。

**解决**：重新编译两三次即可消除。

### 7. Label multiply defined

```
LaTeX Warning: Label `sec:intro' multiply defined.
```

**含义**：标签重复定义。

**解决**：使用唯一标签名，检查是否有同名的 `\label{}` 命令。

### 8. Font shape undefined

```
LaTeX Font Warning: Font shape `...' undefined.
```

**含义**：字体形状不支持，使用替代字体。

**解决**：加载合适宏包或更改字体设置。

### 9. No file xxx.aux

```
LaTeX Warning: No file xxx.aux.
```

**含义**：第一次编译（尚不存在 `.aux` 文件），正常现象。

## 调试技巧

### 逐行检查

```latex
\errorstopmode          % 每个错误暂停（默认）
\scrollmode            % 只对致命错误暂停
\nonstopmode           % 不暂停，继续编译
\batchmode             % 完全不输出
```

### 调试命令

```latex
\show\command          % 显示命令定义
\showthe\register     % 显示寄存器值
\typeout{消息}        % 向终端输出消息
\meaning\command      % 输出命令含义
\tracingall           % 开启全部跟踪
\tracingnone          % 关闭跟踪
```

### 使用 \typeout 调试

```latex
\typeout{=== 当前计数器值：\the\value{page} ===}
```

### 使用 \tracingall

在问题区域前后添加：

```latex
\tracingall
% ... 疑似有问题的代码 ...
\tracingnone
```

输出非常详细（数千行），适用于极难定位的问题。

## 外部工具

### chktex（代码检查）

```bash
chktex file.tex                % 全面检查
chktex -n1 -n2 file.tex       % 跳过某些警告
```

检查项目：
- 括号/花括号不匹配
- 命令后缺少空格
- 错误使用 `...` vs `\dots`
- 行内公式中使用 `$$` 等

### lacheck（轻量检查）

```bash
lacheck file.tex
```

## 最小工作示例（MWE）

提问或调试时，创建最小化可重现示例：

```latex
\documentclass{article}
\begin{document}
% 仅保留出问题的最小代码
Hello, world!
\end{document}
```

MWE 原则：
1. 去掉无关宏包（保留必要的最少宏包）
2. 去掉无关内容
3. 确保他人可以编译
4. 附上完整错误信息

## 编译日志分析

### 一键扫描日志

```bash
# 查找所有错误
grep "^!" file.log

# 查找缺失字符
grep "Missing character" file.log

# 查找溢出
grep -E "(Overfull|Underfull)" file.log

# 统计警告数
grep "Warning" file.log | wc -l
```

### latexmk + 错误定位

```bash
latexmk -xelatex -silent file.tex   % 只显示错误
```

## 跨文件引用

- [compile.md](compile.md) — 编译流程与 latexmk 自动化
- [macros.md](macros.md) — 宏编写中的常见陷阱
