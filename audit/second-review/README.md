# 第二轮审查与独立有限森林测试

`finite_review.md` 记录有限阶数学审查。`finite_exhaustive.py` 独立生成并枚举 1–10 点全部 637 个无标号森林，构造真实独立集计数，并将它们代入原始核验器的全部有效结构行域。此测试用于寻找数学约束或实现符号错误，不能代替覆盖至 60 点的精确证书证明，也不能单独证明所有阶。

要求：Python 3.10 或更新版本，只使用标准库；请勿使用 `-O`。在任意工作目录执行脚本的实际路径即可：

```text
python path/to/finite_exhaustive.py
```

默认只向标准输出打印结果，不改写随包发布的日志。脚本先检查开发目录中的 `../audit60/verify.py`；如不存在，则从脚本所在目录向上查找 `inputs/forest_n60_extension_and_n100_gap.zip`，把其中唯一的 `verify.py` 原样取到临时目录再导入。原程序的 `__file__` 保留为真实临时文件路径，数学源码没有改写，临时目录在结束后自动清理。

也可以显式指定原始核验器，以及一个自行选择的新结果文件：

```text
python path/to/finite_exhaustive.py --verifier path/to/original/verify.py
python path/to/finite_exhaustive.py --output path/to/new_results.json
```

`--output` 会明确写入（或覆盖）所指定的文件；不指定就不会保存。输出包含实际核验器的 SHA-256、每阶森林数、总森林数和结构行检查数。预期结果是 `status: PASS`、`total_forests: 637`、`row_checks: 45529`。

首次数学检查结果见 `finite_exhaustive_results.json`。修改后的可移植脚本已在隔离的模拟发布目录中使用 ZIP 回退路径再次实际运行，结果见 `finite_portability_results.json`，仍为 637 个森林、45,529 条结构行全部通过。
