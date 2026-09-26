# JSP-000826 原题、文献与提交要求核查

核查日期：2026-09-26（Asia/Shanghai）。官方仓库核查版本：`1d1db84a39201357236183f0bbd620e2b220747e`，该版本提交时间 2026-09-24 02:45:02 UTC。以下是公开来源研究，不替代对用户证明的数学审计，也不是主办方的接收决定。

## 1. 正确题号与范围

对应 **JSP-000826**，原题为 **Erdős Problem 993**。不要将 JSP 编号 826 误当作 Erdős 826。官方条目问所有有限树或森林的顶点独立集计数序列是否单峰；没有 60 点或 100 点的上限。检查时条目为 `Open / Lean proof: No / Eligible to claim: No`，历史悬赏金额栏为空。[官方条目](https://github.com/TheJustinSunPrize/awards/blob/1d1db84a39201357236183f0bbd620e2b220747e/problems/catalog-0801-0900.md#JSP-000826)

原始出处是 Alavi、Malde、Schwenk、Erdős 的 *The Vertex Independence Sequence of a Graph Is Not Constrained*（1987），**Problem 3，扫描 PDF 第 7 页**。其中树与森林版本分别提出，并指出一般单峰序列的卷积未必单峰。因此不能仅凭“所有树单峰”和分量乘积公式得到森林版本。[原文扫描件](https://www.renyi.hu/~p_erdos/1987-33.pdf)

准确量词为：对每个有限森林 F，存在整数 m，使 i_0(F) ≤ … ≤ i_m(F) ≥ i_(m+1)(F) ≥ …，其中 i_k 统计 k 个顶点组成的独立集，超过独立数后补零。不是边独立集（匹配）问题，也不要求全部系数对数凹。[Erdős 993](https://www.erdosproblems.com/993)

## 2. 截至核查日的直接文献证据

2026-09-17 的 Fang–Lu–Nevo–Yao–Zheng 预印本 arXiv:2609.20961v1 的 Theorem 1.1 给出一个绝对整数 N₀，使 n ≥ N₀ 的所有森林单峰。其论证是“大阶最终成立”，没有把 N₀ 指定为 59 或 60。该结果本身不能与 n ≤ 60 直接拼接；必须另外证明 N₀ ≤ 61，或独立给出覆盖 n ≥ 59 的有效定量论证。[预印本](https://arxiv.org/abs/2609.20961v1) · [正文 Theorem 1.1](https://arxiv.org/html/2609.20961v1#S1.Thmtheorem1)

作者链接的 Lean 项目同样形式化“存在 N₀，所有 n ≥ N₀”这一命题。仓库 README 声称通过无 sorry 的构建与标准公理审计；本项研究未执行该仓库的 Lean 构建，所以不能将 README 的声明写成此次已独立验证。[作者仓库](https://github.com/junwei-lu/Erdos_993_Tree_Independent_Set_Unimodality)

原题网站目前仍显示 Open，其 proof-claims 页有 Fang 等于 2026-09-21 提交的一项 **partial proof**，内容也是充分大森林；网页列入证明主张不代表验证通过。本次原站由直接 HTTP 获取，搜索索引的旧页面仍可能显示零项，不能采用旧计数。[当前 proof-claims 页](https://www.erdosproblems.com/forum/thread/993/proof-claims)

Kadrawi–Levit 的 26 点反例针对对数凹性，不是单峰性；Ramos–Sun 的 AI 搜索也主要寻找不对数凹树。这些结果不能当作本猜想的反例。[Kadrawi–Levit](https://arxiv.org/abs/2305.01784) · [Ramos–Sun](https://arxiv.org/abs/2510.18826)

检索未发现可确认的全体森林单峰猜想完整解答或森林单峰反例。该结论仅是此次核查范围内的文献状态，不是对全球文献不存在结果的证明。用户材料的创新性与作者归属仍须对照完整引用链判断。

## 3. 当前可执行的官方提交流程

官方贡献指南要求原题的完整解答；它的关键原文是 **“Only complete solutions to the original problem are accepted”**。特例、中间引理、弱化结论和依赖未证明附加假设的结论不符合收稿条件。仓库文本应为英文；只提交目录记录与公开证据链接。证明源码、依赖、压缩包及二进制放在外部证明仓库；不要把整包提交进 awards 仓库。保留第三方署名与许可证。[贡献指南](https://github.com/TheJustinSunPrize/awards/blob/1d1db84a39201357236183f0bbd620e2b220747e/CONTRIBUTING.md)

**完整数学证明可以先按 solver-only 提交，不必先有 Lean。** 初始数学解答 PR 填 Problem、Attribution，删除 Lean 专属段落，提供公开证明、定理/页码、版本日期、作者贡献证据。若同时或后续提交 Lean，需原始证明仓库、分支、40 位 commit SHA、目标定理、陈述对应、精确环境/依赖、重现命令、公理审计。模板要求直接引用外部文件。[官方 PR 模板](https://github.com/TheJustinSunPrize/awards/blob/1d1db84a39201357236183f0bbd620e2b220747e/.github/PULL_REQUEST_TEMPLATE.md)

数学审查与 Lean 验证分别进行；Lean 是进入限时公示和奖金发放的前置条件。solver-only 材料可先审查并保留，但未完成 Lean 时不开始 14 天公示。公示自候选人实际登载并公告开始，不从开 PR 或合并时刻自动计算。获奖还需解决相关异议、本人申领、身份核验及书面确认。唯一官方联系邮箱是 `thejustinsunprize@hejustinsun.com`。私密身份、支付与寄送资料仅经官方邮件，不放公开 GitHub。[办理流程](https://github.com/TheJustinSunPrize/awards/blob/1d1db84a39201357236183f0bbd620e2b220747e/docs/award-process.md)

`lean-verify` 预审技能是推荐项，自检报告和日志链接不是强制入稿条件；完整证明与问题对应仍是硬性要求。此次若没有实际构建，不得勾选验证已通过。[验证说明](https://github.com/TheJustinSunPrize/awards/blob/1d1db84a39201357236183f0bbd620e2b220747e/docs/verification.md)

没有检得 JSP-000826 专属模板、截止日或锁定奖金数额。2026-09-16 网站规则把部分层级描述为可奖励部分进展，但现行 FAQ 和 GitHub 具体收稿流程明确排除部分解答；应按当前完整解答流程准备，不据早期笼统描述声称部分结果有资格。规则中的 2026-01-01 是历史成果金融资格追溯起点，不是提交截止日；百万美元也不是本题已承诺金额。[FAQ](https://www.hejustinsun.com/prize/faq) · [规则](https://www.hejustinsun.com/prize/rules)

## 4. 相关公开记录（用于避免重复，不构成认可）

| 记录 | 核查内容 |
| --- | --- |
| [Issue 53](https://github.com/TheJustinSunPrize/awards/issues/53) | 研究提案，正文明确没有解答、反例或完成的 Lean；没有独占权、优先权或获奖承诺。 |
| [PR 3889](https://github.com/TheJustinSunPrize/awards/pull/3889) | 只验证路径 P₄ 的 1,4,3 序列。维护者于 9 月 24 日说明部分解答不符要求。API 仍显示 open，不能把评论中的关闭意向写成已关闭。 |
| [PR 4318](https://github.com/TheJustinSunPrize/awards/pull/4318) | 自称记录“无完整形式化”；正文把 JSP-000826 错映射到 Erdős 826，其文献断言不可靠。API 显示 open。 |
| [PR 3646](https://github.com/TheJustinSunPrize/awards/pull/3646) | 早前形式化登记，9 月 23 日关闭、未合并；不代表原题已解决。 |

## 5. 本地交付与最终上传之间仍需区分的事项

本次仅生成本地材料，不创建 PR，不发布仓库，不发邮件，不提交身份或奖金申领。作者信息由用户提供：Tong Zhang；论文联系邮箱 ZhangZenoZhang@gmail.com。GitHub 用户名、对材料有发布权限的公开仓库 URL、公开版本 SHA、作者贡献证据均不得臆造。未提供时必须保留待填字段。

如果数学审计最后通过，可将同一份完整证明作为 solver-only 候选解答申请审查。若审计发现缺口，则须保留 Open，不提交“已完整解决”的 PR；研究笔记、缺口说明与复现包仍可作为私人或公开研究材料，但官方普通反馈入口不等于解答接收入口。
