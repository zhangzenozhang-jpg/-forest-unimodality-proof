# 提交到 JSP-000826 的说明

本目录供 **Tong Zhang 的完整数学解答候选稿** 使用，目标为孙宇晨奖 **JSP-000826 / Erdős 993**。完整数学解答可先按 solver-only 流程提交，现行规则不要求先有 Lean 仓库；没有完整 Lean 时不能进入限时获奖公示或领取奖金。核查日期：2026-09-26。

## 先核对本包状态

查看 `STATUS.json` 和 `audit/FINAL_REVIEW_EN.md`。本次关键结构审查未发现明确缺口，60点与新59证书、900至80完整旧链均已重跑通过；结论是可提交数学审查的完整证明候选，并非已获官方认可。60点有限结论单独不足。若后续发现实际缺口，应更新候选稿并撤回不再成立的声明。

作者为 Tong Zhang，论文联系邮箱为 ZhangZenoZhang@gmail.com；公开 PR 正文不包含此邮箱。已通过登录接口识别 GitHub 账号 zhangzenozhang-jpg，目标公开仓库为 `zhangzenozhang-jpg/-forest-unimodality-proof`，其简介与作者提供的名称一致。实际发布版本和 PR 状态见 `STATUS.json` 及发布回执；不能把准备状态当成已提交。

官方对纯数学解答要求公开证明或发表记录、版本或日期、定理位置和贡献证据，并不强制 GitHub 或40位 SHA；40位 SHA 的明确要求属于 Lean 提交。本次按作者要求使用 GitHub，并以固定 commit 精确标识完整数学材料。

## 完整证明通过审查后的操作

1. 在本人有权发布的公开 GitHub 仓库发布论文 PDF、LaTeX、复现代码及审查材料。先完成对最终文本、署名、第三方来源与发布许可的核对，再发布。纸面或本地文件路径不能替代公开链接。记录最终版本的完整 40 位 SHA。
2. 使用 `generate_submission.py` 根据真实公开仓库、SHA、论文路径、定理位置和署名证据生成 PR 正文与 catalog diff。程序只在本地生成文件，不创建 GitHub PR、不推送、不发送邮件。须显式给出 `--audit-complete`，这表示最终数学审计已经完成；不能用该参数替代审计。
3. Fork [官方仓库](https://github.com/TheJustinSunPrize/awards)，只修改 `problems/catalog-0801-0900.md` 内 JSP-000826 条目的允许字段。官方维护者负责 index、eligibility 和 candidate 状态。将本地生成的 diff 与最新条目比较，确认没有覆盖他人的变化。
4. 打开 solver-only PR，粘贴生成正文，检查公开链接和所有待核对项。此过程提交的是候选证明，请维护者审查；不是宣布已经接收或获奖。不要把整个 zip、PDF、.tex、.lean、依赖或构建产物提交进 awards 仓库。
5. 维护者审查通过并合并后，才按官方本人申领流程办理。缺少 Lean 时申请可保留，两个 claim 状态仍不可领取。今后有完整 Lean，才另交原始形式化仓库、分支、40 位 SHA、目标定理及构建/公理审计等材料。

作者已明确要求公开材料并提交数学解答。此授权不等于主办方认可证明或确认奖金资格；本次不代办身份核验、领奖或支付。

## 生成命令示意

下列尖括号全部替换为真实值，不能原样运行。脚本也允许用 `--catalog-file` 读取从官方仓库下载的最新版目录；不提供时只读获取官方 main。

```text
python generate_submission.py --repository https://github.com/<真实账号>/<真实仓库> --commit <完整40位SHA> --contribution-statement "<真实贡献说明>" --authorship-evidence-url <公开归属证据URL> --audit-complete
```

若保持本包在公开仓库根目录的结构，论文题名、路径、定理位置、审查报告和代码目录已有默认值；若移动文件，可用相应参数覆盖。

生成结果在 `generated/`：`PR_BODY.md`、`catalog.patch`、`catalog-0801-0900.proposed.md`、`submission-metadata.json`。脚本不检验数学证明本身；也不会冒充完成 Lean 验证。

## 当前官方要求与入口

- [贡献指南](https://github.com/TheJustinSunPrize/awards/blob/main/CONTRIBUTING.md)：仅收完整解答；英文目录；外部证明仓库；保留署名和许可。
- [PR 模板](https://github.com/TheJustinSunPrize/awards/blob/main/.github/PULL_REQUEST_TEMPLATE.md)：数学解答只填 Problem 与 Attribution 等适用部分。
- [参与流程](https://github.com/TheJustinSunPrize/awards/blob/main/docs/award-process.md)：完整解答与完整 Lean 分阶段；本人 claim；候选公告开始满 14 天；身份验证和确认。
- [FAQ](https://www.hejustinsun.com/prize/faq)：现行收稿范围和 Lean 要求解释。
- 官方唯一联系邮箱：`thejustinsunprize@hejustinsun.com`。私密身份材料、支付和邮寄信息仅通过官方邮箱，不公开到 GitHub。

未查到本题专属截止日或已锁定金额。不要把 2026-01-01 的追溯资格日期当作报名截止日，也不要把顶级奖的 100 万美元写成本题奖金。

如数学审查未通过，可保存研究包或通过普通反馈入口咨询，不能把反馈包装成完整解答提交。[反馈表单](https://github.com/TheJustinSunPrize/awards/issues/new?template=feedback.yml)
