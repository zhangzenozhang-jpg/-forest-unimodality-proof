# Current manuscript companion materials — 27 September 2026

The current manuscript is **Unimodality of Forest Independence Polynomials**,
by **Tong Zhang and Wei Li**. Its versioned computational supplement is in
[companion/2026-09-27](companion/2026-09-27/README.md): exact verification
programs, frozen certificate data, detailed proof reference, checksums,
and a complete reproduction guide. This entry point performs the proof
obligations without graph-instance enumeration. The successful complete
replay record and authenticated diagnostic omissions are documented there.

The materials below and in the other top-level directories retain the
earlier submission's provenance and instructions. Use the versioned
companion's entry point for the current manuscript.

---

# Forest independence polynomial unimodality — Tong Zhang

**Submitted for mathematical review:** [official PR #4551](https://github.com/TheJustinSunPrize/awards/pull/4551). Status at receipt: open, not accepted or merged. See `submission/PUBLICATION_STATUS.md` for the exact proof commit and receipts.

This repository-ready package is a complete mathematical proof **candidate** for
Justin Sun Prize JSP-000826 / Erdős Problem 993. It is submitted for mathematical
review, with no claim of prior acceptance or completed Lean formalization.

The two input releases cover n ≤ 60 and n ≥ 59, respectively, where n counts
vertices. Their union covers every finite simple forest. The large-order proof
includes a frozen analytic/certificate chain whose full written dependencies are
integral to the submission. An order-100 rational relaxation obstruction is not
a forest counterexample and does not obstruct this assembly.

## Read and reproduce

- `paper/forest_unimodality_Tong_Zhang.pdf`: consolidated English manuscript.
- `paper/main.tex`, `finite60.tex`, `large59.tex`: LaTeX source.
- `paper/审查与提交说明.pdf`: Chinese audit and submission report.
- `math-sources/DEPENDENCIES.md`: exact mathematical source map.
- `audit/`: fresh runs and explicit audit limitations.
- `inputs/`: unmodified original archives and their SHA-256 manifest.

Python 3.10+; no third-party mathematical packages are required by acceptance:

    python -S verification/reproduce.py --mode full --work ../forest-proof-replay

Use a new empty directory. `--mode finite` checks only the finite part.
`--mode new59` also checks the new 59 extension but does not rerun the inherited
large-order chain. The full run can take substantial time; logs are written in
the working directory. On Windows an external long-path launcher preserves all
original mathematical code and assertions. Do not use Python `-O`.

## Submission

See `submission/SUBMISSION_GUIDE_ZH.md`. The official awards PR receives only
catalog references to a public proof repository, not this ZIP or its source code.
The author-created target is https://github.com/zhangzenozhang-jpg/-forest-unimodality-proof.
Use the actual publication commit to fill the solver-only PR. Current publication
and PR receipts are recorded in the submission directory, not inferred from this README.
The second scoped review and independent small-forest structural checks are in
`audit/second-review/`. See `AUTHORSHIP.md` for account linkage and AI assistance.

Author: **Tong Zhang**. Manuscript email: ZhangZenoZhang@gmail.com.
Prepared: 26 September 2026. AI assistance and review limits are disclosed in the
manuscript. Retain attribution and original third-party license information.
