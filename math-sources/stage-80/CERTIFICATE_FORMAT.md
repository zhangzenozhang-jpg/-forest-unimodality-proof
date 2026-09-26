# 固定证书格式与适用范围

`certificates.json.gz`顶层为N=80、MMAX=98、新有限范围[80,98]，包含236份核证书。每份含`parent_index`、`qa,qb`、`mlo,mhi`、`method`、`scale`和`coefficients`。

q=λ/(1+λ)，不是活动度λ；m是EM的连续实数，不是顶点数。`coefficients`顺序是A,B,c,d,e,T_1,…，表示

    scale*f >= A+B*M+c*delta-d*delta^2-e*M^2
               -sum_i T_i*(1-q+q*t_i)^M.

`variance_slope`和`variance_intercept`给Var(delta)≤αm+β。`variance_type`为ratio、exact_ratio、flow_ratio、log_linear或log_integer_rank。每种来源都必须覆盖整个q、m矩形，并按N=80、有限顶点上界98重新推导。`rank_upper`只有需要整数目标秩的对数类型使用。

`variance_source`为null、`flow:文件名`或对数源项文件名。源项中a,b分别是参考/下界和上界；对数证书w=0时a只是对数参考点，w>0时还要求活动度λ≥a。所有字段都由程序重新核对，不因存在`certified:true`就接受。

`candidate_margin`、`sampled_state_violation`是浮点发现日志，不进入接受判定。`exact_check`记录有理运算结果，但重放仍重新计算。时间字段不是数学判据。

`repriced_after_source_revision`标记两份在源项修订后保持点态系数、重新计算方差费用的证书；最终期望端点已经重新精确接受。详见audit/REBUILD_NOTE.md。

65份源项分为37份普通选集方差、14份带消息相关线性响应函数的选集方差、14份对数方差。源项表中的p、r划分覆盖完整连续域，父消息集合包含全部必要端点/节点，响应覆盖整个实轴。生成器和独立检查器不同，方法名不是信任来源。

负的顶点数修正使部分对数核依赖N。下轮N降低时必须重算或替换；仅保留相同m范围不能证明这些核仍有效。
