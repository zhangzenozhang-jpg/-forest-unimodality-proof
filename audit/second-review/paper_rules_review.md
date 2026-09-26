# 论文、文献及投稿规则第二轮审查

审查日期：2026-09-26。审查对象：交付包中的 `paper/main.tex`、`finite60.tex`、`large59.tex`、PDF、依赖目录、PROVENANCE、审查结论及投稿生成器。此审查分工侧重论文表达、引用和规则，不冒充整个解析证明链的独立逐行重证。

## 结论

未发现论文把有限范围、松弛反例或已完成的数值复算冒充为另一个数学结论，也未发现本轮核验的文献著录错误。题目范围是所有有限简单森林；`n≤60` 与 `n≥59` 的拼接没有阶数空隙，原文明确包括孤立点、非连通森林及空森林。第 100 阶数组被正确说明为松弛系统的反例，而非森林反例。

现有稿件适合作为“主稿及必需补充材料”向数学审查提交。它不是 21 页 PDF 单独自足的证明：大阶均值、异质活动度源不等式、无界阶数和旧阶段依赖的完整论证在补充材料中。主稿已充分说明这一点。只上传 PDF、只上传复算日志、或把补充材料遗漏，将使完整投稿不成立。不能把“准备好投稿”写成“已经同行评审无误”或“保证发表”；是否最终解决原猜想仍取决于完整证明的数学有效性和审查。

本分工未找到足以单独阻止完整候选稿提交的写作、文献或规则错误。数学结论仍须与另外两个证明复核分工合并，不应仅靠本报告断言无误。

## 最新规则及编号

重新查询官方 `main`，HEAD 仍为 `1d1db84a39201357236183f0bbd620e2b220747e`，提交时间 2026-09-24T02:45:02Z。记录已保存于 `official_head_2026-09-26.json`。

- 正确题号是 JSP-000826 / Erdős 993。官方题库仍为 Open、Lean No、Eligible No。提案可以请求维护者在审查通过后记录 Solved；不能称该状态已被官方接受。[当前题目](https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0801-0900.md#JSP-000826)
- Solver-only 完整数学解答可以先提交，不要求先具备 Lean；只在官方目录内提交英文证明链接和归属记录。证明源码、压缩包和二进制文件应在外部保存。[贡献指南](https://github.com/TheJustinSunPrize/awards/blob/main/CONTRIBUTING.md)
- 对 solver-only，官方必要证据是公开证明/发表记录、定理或页码、版本或日期、贡献者和贡献证据。**原始 Lean 仓库、分支和 40 位 SHA 是 Lean 提交的专属明确要求**，不能说所有数学提交都必须有 GitHub 仓库和 SHA。本次用户明确希望 GitHub 发布，采用公开仓库及完整 SHA 固定数学稿版本是合适的复现安排。[PR 模板](https://github.com/TheJustinSunPrize/awards/blob/main/.github/PULL_REQUEST_TEMPLATE.md)
- 初次提交只开完整数学解答 PR。不要同时开尚未满足合并条件的领奖申请，也不要把 PR 提交、合并或接受等同于得奖。[办理流程](https://github.com/TheJustinSunPrize/awards/blob/main/docs/award-process.md)

上述原始文件与上次规则快照相符；没有发现规则变化要求重做材料结构。外部数学补充材料不是 awards 仓库内文档，“awards 文档使用英文”不等于禁止外部中文数学附录。面向国际期刊的可读性仍可通过后续完整英文附录改善。

## 文献核验

| 引文 | 核验结果 |
|---|---|
| Fang, Lu, Nevo, Yao, Zheng, arXiv:2609.20961v1 | arXiv 官方页面确认 2026-09-17 18:16:42 UTC；作者是 Ethan X. Fang、Junwei Lu、Eran Nevo、Yuan Yao、Hailun Zheng；题名完全一致。原文 Theorem 1.1 仅给存在绝对阈值 N0，不给 59。论文现有写法正确，日期相对于本次 2026-09-26 不是未来日期。 |
| Andriantiana, Razanajatovo Misanantenaina, Wagner, arXiv:1807.08290 | 官方元数据与现稿一致。摘要明确平均独立集大小等于活动度 1 的对数导数，路径在树中最小；现稿没有把其擅自用于任意活动度。 |
| Kadrawi–Levit, AMC | 出版社与 Crossref 同时确认 **25(4) (2025), #P4.03**、DOI `10.26493/1855-3974.3207.2ad`。搜索曾出现第三方目录写卷 23，已用出版社主页面元数据排除；保持现稿卷 25。原始核验摘录见同目录 JSON/TXT。 |
| Ramos–Sun, arXiv:2510.18826 | 官方页面作者 Eric Ramos、Sunny Sun，题名与现稿一致；工作讨论树独立序列的对数凹性反例，现稿未误称单峰反例。 |
| Alavi–Malde–Schwenk–Erdős (1987) | 现稿题名、作者、卷 58、15–23 页与原始文献记录一致；投稿模板准确指向 Problem 3、PDF 第 7 页。 |

直接来源：

- [Fang 等 arXiv 元数据](https://arxiv.org/abs/2609.20961v1) 与 [Theorem 1.1 原文](https://arxiv.org/html/2609.20961v1)
- [平均独立集大小原文信息](https://arxiv.org/abs/1807.08290)
- [AMC 出版社文章页面](https://amc-journal.eu/index.php/amc/article/view/3207) 与 [Crossref 出版社登记元数据](https://api.crossref.org/works/10.26493/1855-3974.3207.2ad)
- [Ramos–Sun 元数据](https://arxiv.org/abs/2510.18826)
- [1987 年原始论文](https://www.renyi.hu/~p_erdos/1987-33.pdf)

## 投稿前建议修整的具体文本

这些是表达或可复现性改进，不是已发现的数学反例，也不应触发无必要的重复权限询问。

1. `main.tex` 的 `Submission and authorship status` 第一段混入制稿流程，如 “attributes the submitting author as requested” 和 “No affiliation ... is inferred from the files”。正式论文应删去这些对话式来源说明，保留在 PROVENANCE；论文中可用：

   > AI tools assisted with mathematical review, code execution, translation, organization, and manuscript preparation. Their reports are computational and editorial assistance, not independent human referee reports. No complete Lean formalization or prior journal acceptance is claimed.

   不要在未有依据时新增“作者亲自逐行验证全部数学”或“第三方许可已核实”的事实断言。用户已明确授权发布当前材料，不应仅由通用来源说明反推必须再次询问能否发布。

2. 同节的 “The proof repository and publication evidence must be public” 可精确改为：

   > A solver-only submission must provide a public proof or publication reference with its version or date and theorem locations, together with contributor and authorship evidence. This submission uses a public repository and a pinned commit to identify the complete manuscript and mandatory supplements.

   后句只在公开仓库和真实 commit 已建立后使用；尚未建立时可写 “The accompanying submission package is arranged for ...”。

3. `PROVENANCE.md`、中文提交说明、`STATUS.json` 和最终审查报告中“未提供 GitHub 用户名/仓库/commit”“本次未对外提交”等上一轮时态，发布后必须更新成实际状态。这些仅是旧包状态，不是永久限制。

4. 投稿生成器目前只给 `Current status` 和 `Publication details` 写入链接。建议在目标条目补一行 `Attribution basis`，连接仓库中的实际 `AUTHORSHIP.md`、论文和固定 commit，清楚说明 Tong Zhang 的工作与 AI 辅助；这在官方允许的字段内。作者公开记录应区分原材料、合并稿、复算/翻译等实际贡献，避免虚构发现时间、独立人类复核、独立身份验证和优先权。

5. PR 应保留数学稿完整性、适用证据和不含禁放材料的复选框，Lean-only 部分删去。把 review status 限定为实际做过的审查，避免 `final mathematical audit complete` 被理解为官方或独立同行审稿。

6. 当前整合稿 Theorem 1.1 位于 PDF 第 1 页，拼接论证在第 2 页，有限阶部分是 Section 2，大阶部分为 Sections 3–5，Section 6 是复现说明；投稿生成器的 theorem locations 与此一致。重新排版后应再次核查页码。

## 相邻提交

本轮再次检查 #53、#3889、#4318、#3646 的官方页面。#53 是研究计划；#3889 仅述 P4 的 (1,4,3) 序列，维护者评论指出只接受完整原题；#4318 混淆 JSP 与 Erdős 编号，不能当作完整解答证明；#3646 没有使当前题库成为 Solved。现稿引用这些为相关记录而未宣称自身因此具有首解优先权，处理合适。

GitHub 动态页面头部状态与缓存可能短暂不一致；正式创建 PR 前以 API 或实际登录界面的当前状态再检索同一作者及同一稿件，避免重复提交。不要靠他人未被接受推导本稿已解决，也不应把未核验的 Lean build 当作本稿证明。

## 本轮的边界

本轮没有运行外部发表或提交操作，没有修改主稿。已核对关键段落的一致性及源文献，不声称对所有基础证明逐行重证，也没有替代另两个证明审查分工。本报告仅支持“论文与必需补充材料可以作为一个完整解答候选提交审查”的表达；不支持“保证无误、保证发表、已获认可”。
