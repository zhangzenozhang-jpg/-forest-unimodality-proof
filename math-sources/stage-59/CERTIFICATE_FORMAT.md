# 固定证书格式与接受边界

顶层 `release_config.json` 固定 N=59、CAP=79、previous_N=80，以及231份新证书。`certificates.json.gz`中的每一份证书只对应一个完整闭矩形 q∈[qa,qb]、m∈[mlo,mhi]。

`qa,qb`是伯努利参数q=λ/(1+λ)，不是活动度λ。`mlo,mhi`是EM的实数区间。`parent_index`对应冻结350包的43个父活动度区间之一。

`kmin`来自该q区间上的全规模均值密度、边界项和整数取整；`kmax=floor(2*qb*mhi)`。计数域按整个m矩形的上端形成，不在区间内部随意切换。`counts`保存必要(n,k)对、允许的整数j及对应的条件计数上界B_j；接受器通过另一套整数多项式递推独立重建这些数据。

`state_count`记录由组合计数非零条件得到的允许(M,j)状态数。验收不直接信任这个数，也不因某个状态产生负核而把它删去。

`kernel_weights`按左、右、中央核的顺序给出非负有理权重，满足w_L/4+w_R/4+w_C=1。它们在整个矩形内固定，不能依条件状态改变。`scale`为正整数S。

`coefficients`按以下顺序保存精确有理数：

```text
A, B, C, D_delta, D_M, T_1, ..., T_s, U_j1, ..., U_jt
```

其中j1,...,jt的顺序与`counts.j_values`一致，T的顺序与`mgf`一致。对应点态下界是

```text
S*f >= A+B*M+C*delta-D_delta*delta^2-D_M*M^2
       -sum_i T_i*(1-q+q*t_i)^M-U_j*(1-q)^M.
```

D_delta、D_M、全部T和全部U必须非负。每个q端点的残差还必须支付完整二阶导数插值费用；只检查点态公式在两个q端点非负并不充分。

`variance_slope,variance_intercept`定义该矩形上E(delta^2)≤alpha*m+beta。其来源、N相关顶点费用和整数秩端点都必须重算。`candidate_margin`只保存浮点候选日志，不参与接受。`certified`也不能代替重新计算：`replay.py`重算每个输入、状态域、端点和期望预算，再与`exact_check`比较。

`coverage.json`将所有新旧q端点共同细分。`guarantee_source`记录用于该层m保证下端的已核验整数秩密度来源，而非待证明的核结论。`witnesses`记录m并集接续所使用的矩形。它不使用80包中依赖n≥80的236份新核来证明更小n。

发行检查分为三层：`check_release.py`是哈希与固定记录检查；`smoke_test.py`是全部四份源项、三份核及连续覆盖的移址检查；`replay.py`才默认重新计算完整历史依赖与全部新证书。
