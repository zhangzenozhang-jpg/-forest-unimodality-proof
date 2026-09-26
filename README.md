# Forest independence polynomial unimodality — Tong Zhang

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
