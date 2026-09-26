# 固定证书格式

`certificates_170.json.gz`包含顶层`N=170`、`MMAX=349`及558份证书。每份证书的关键字段如下。

`parent_index`对应冻结350计划的0至42行；`method`为left、central或right。`qa,qb`是Bernoulli参数q=λ/(1+λ)的有理端点，不是活动度λ。`mlo,mhi`是EM的实区间端点，不是顶点数区间。

`r,D,R,vmax`和`mgf`须由冻结来源重新推导，检查器不信任随文件填写的数值。`mgf`逐项给出t、统一正下界rate_lower和所用的异质仿射源项证书参数。

`scale`为正整数S；`coefficients`按以下顺序存储精确有理数：

```text
a_0, b_0, c_0, d, e, T_1, ..., T_s
```

对应点态下界

```text
S*f(M,j;q) >= a_0 + b_0*M + c_0*delta - d*delta^2 - e*M^2
              - sum_i T_i * (1-q+q*t_i)^M,
delta = j-q*M.
```

d、e及全部T_i必须非负，且d=0时c_0=0。所有点态端点残差还需支付完整q插值的h²Z_M/8曲率预算；不是只检查上述式子在两个q端点成立。

`candidate_margin`、`sampled_state_violation`是候选求解器的浮点日志，**接受路径不使用它们**。`certified`也不是权威判据。`replay.py`重新检查每个整数状态、无限半轴、期望端点和参数来源，再与记录`exact_check`比较。

`certificate_id`中的200、180或170搜索阶段痕迹不改变当前量词：发行中每份证书的`N`均为170。200、180阶段的矩形只需保持其记录的m范围；较低m条带由后续矩形补齐。发行包含349份200阶段矩形、79份180补充矩形、130份170补充矩形，总计558。

每个证书的scale可以不同，因此`margin_lower`是该证书Sf的保证下界。恢复原核期望的下界需除以它自己的scale。
