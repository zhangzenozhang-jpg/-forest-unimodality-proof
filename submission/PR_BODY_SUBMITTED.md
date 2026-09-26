## Submission type

- [x] Mathematical solver information
- [ ] Lean proof or formalization author information

## Problem

- Problem ID: JSP-000826, corresponding to Erdős Problem 993.
- Original source: Alavi, Malde, Schwenk and Erdős, *The Vertex Independence Sequence of a Graph Is Not Constrained* (1987), Problem 3, PDF page 7: https://www.renyi.hu/~p_erdos/1987-33.pdf. Current problem statement: https://www.erdosproblems.com/993.
- Current catalog entry: https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0801-0900.md#JSP-000826.
- Proposed change: submit a candidate complete mathematical proof for review; if accepted, record the solver and proof reference. No Lean completion or award eligibility is claimed by this submission.
- Public manuscript: https://github.com/zhangzenozhang-jpg/-forest-unimodality-proof/blob/7cee5104a983dd1271db14be7606e96c504aa370/paper/forest_unimodality_Tong_Zhang.pdf. Title: Exact Certificates for Unimodality of Forest Independence Polynomials. Version: 2026-09-26; repository commit: 7cee5104a983dd1271db14be7606e96c504aa370.
- Exact theorem and proof locations: Theorem 1.1, p. 1; assembly on p. 2; finite-order proof in Section 2; large-order proof in Sections 3-5 with mandatory Supplements A and B.
- Mathematical scope: every finite forest, including disconnected forests and the empty forest. The proof combines the finite range of at most 60 vertices with an explicit argument for every order at least 59. The overlap covers all orders; the validity of both arguments and all inherited lemmas is part of the submitted claim.
- Supporting audit and exact computation materials: https://github.com/zhangzenozhang-jpg/-forest-unimodality-proof/blob/7cee5104a983dd1271db14be7606e96c504aa370/audit/FINAL_REVIEW_EN.md and https://github.com/zhangzenozhang-jpg/-forest-unimodality-proof/tree/7cee5104a983dd1271db14be7606e96c504aa370/verification.
- Review status: Two scoped AI-assisted mathematical reviews found no concrete gap in the checked reductions; the complete exact-arithmetic chain passed in fresh runs. The reports state their limits. This is not independent human peer review, Lean certification, or an official acceptance decision. The manuscript is a submitted proof claim; it is not represented as accepted, peer reviewed, independently human verified, or Lean verified.

## Prior and related work

Fang, Lu, Nevo, Yao and Zheng, arXiv:2609.20961v1 (2026-09-17), Theorem 1.1, prove eventual unimodality with an existential absolute threshold. Their mathematical and formalization contributions are prior work, credited separately in the manuscript. This submission claims an explicit bridge to the finite range; it does not claim authorship of their result or their Lean code.

Related records: https://github.com/TheJustinSunPrize/awards/issues/53, https://github.com/TheJustinSunPrize/awards/pull/3889, https://github.com/TheJustinSunPrize/awards/pull/4318, and https://github.com/TheJustinSunPrize/awards/pull/3646. These do not supply an accepted full solution to the forest statement in the catalog inspected on 2026-09-26. The JSP and Erdős problem numbers are different.

## Attribution

- Manuscript author and submitting mathematical contributor: Tong Zhang.
- Contribution statement: Tong Zhang submits the combined all-forest proof with its original research materials and exact certificates. AI-assisted review, reproduction, translation and manuscript preparation are disclosed; external prior work is credited separately.
- Public authorship and account linkage: https://github.com/zhangzenozhang-jpg/-forest-unimodality-proof/blob/7cee5104a983dd1271db14be7606e96c504aa370/AUTHORSHIP.md.
- Lean formalization: none submitted in this PR.
- Independent human verifier: none identified in the preparation of this package.
- AI assistance: AI tools assisted with proof auditing, exact computational reproduction, literature/rules research, and manuscript preparation. AI checks are supporting evidence, not an official review or attribution decision.
- Relevant interest: the author requests mathematical review and credit for the contribution described above; no award entitlement, exclusivity or first-solution priority is asserted by the PR opening date.

## Submission checklist

- [x] The submitted proof claim addresses the complete original statement; all dependencies and cases are included or properly cited, and its review status is stated accurately above.
- [x] This diff changes only the relevant catalog's allowed attribution, proof/publication references or status fields, with supporting public evidence.
- [x] The public URLs and version identifiers above resolve to the exact materials submitted.
- [x] I am entitled to contribute the submitted material and have retained third-party attribution and license information.
- [x] The awards PR contains no proof source files, archives, binaries, vendored dependencies, private identity information, contact details or payment information.

This is a solver-only submission. The current contribution rules do not require a Lean repository for its initial review. A verified complete Lean formalization and the subsequent official process remain necessary before public award review and payment can proceed.
