# Final audit conclusion — JSP-000826 / Erdős Problem 993

Date: 2026-09-26. Manuscript author: **Tong Zhang**.

## Conclusion

Revision 1.1 incorporates a second scoped review of the finite-order proof,
large-order structural chain, manuscript, sources, and current submission rules.
The three reports are in `second-review/`. No concrete blocking gap was found.
An independently generated exhaustive check of all 637 unlabelled forests of
orders 1--10 verified 45,529 structural rows. These small-graph checks seek errors;
they do not replace the universal arguments or the full exact certificates.

The supplied releases cover all finite simple forests when their complete
mathematical arguments are combined: one covers n ≤ 60, the other n ≥ 59.
The overlap is consistent. The n=100 rational array only obstructs the specified
finite-order relaxation; it is not a forest counterexample and does not refute
the independent large-order argument.

The review found **no concrete deduction error or missing order** in the key
structural reductions examined. Full exact arithmetic replay passed for the
finite part and for the entire inherited large-order chain. The resulting
manuscript is a **complete mathematical proof candidate for review**, not an
officially accepted solution, a claim of completed Lean formalization, or a
guarantee that independent referees will find no error.

## Fresh evidence

| Check | Fresh result |
|---|---|
| Finite scalar domain | all 17,100 parameter triples passed |
| Rational certificates | 670 separators + 1,907 linear certificates; 142,017 nonzero row multipliers |
| Second finite arithmetic implementation | all 1,907 linear certificates passed |
| Relaxation obstructions | all 1,198 and 8,356 rows checked exactly |
| New59 extension | all 231 certificates; 1,185,408 endpoint states; 154 strata, 43 parent intervals |
| Prior chain | 900 → 500 → 350 → 170 → 130 → 99 → 80 all passed |
| Deliberately invalid new59 inputs | all 17 rejected |
| Distribution wrapper | finite-mode extraction, SHA checks and all three finite commands passed |

The new59 and inherited80 runs were **separate invocations**. The former used
`--skip-prior`, and the latter reran its full recursive chain. The inherited80
top-level report records 1680.1 seconds, including its recursive calls.
No historical output was relabeled as a fresh check.

The ordinary Windows run first encountered WinError 267 from a long nested
child current directory. The supplied external launcher starts the Python child
at a short directory, then changes to the original directory inside Python and
executes the unchanged script. Mathematical source bytes, assertions, parameters
and certificates are unchanged. Both the initial failure and the successful
portable run are preserved.

## What was and was not audited

The detailed reports list the actual structural and implementation review.
The checked themes include maximum-independent-set counting, a sparse complement,
private-neighbor deletion constraints, actual complement edge consistency,
head/tail monotonicity, the activity-two mean reduction, maximum-weight leaf
exchange, complement matching counts, conditional cancellation, rational interval
directions, continuous q/m coverage, and safe reuse of earlier certificates.

This is not a line-by-line independent re-proof of the entire analytic history.
Arithmetic acceptance certifies the encoded inequalities. The written all-forest
reductions and infinite-domain bounds remain essential mathematical dependencies.
The complete original technical material is in the input archives; readable
source copies and exact locations are in `math-sources/DEPENDENCIES.md` and
`math-sources/SOURCE_MAP.json`.

## Files and audit identity

- `audit60/独立审查报告.md`: finite-order mathematical review and exact checks.
- `audit60/fresh_verify.log`, `fresh_verify_grid.log`, `fresh_verify_countermodels.log`.
- `audit59/AUDIT59_REPORT.md`: inherited dependency and new59 review.
- `audit59/new59_fresh_summary.json`: the fresh outer extension.
- `audit59/prior80_full_fresh_summary.json`: the full recursive inherited run.
- `audit59/prior80_full_portable_fresh.log`: fresh recursive output.
- `audit59/negative_tests_fresh.json`: rejection checks.
- `wrapper-smoke/reproduction_summary.json`: distribution wrapper check.

The original standalone Chinese finite-order Markdown is byte-identical to the
copy inside its ZIP. It is not a third independent proof. All input identities
and distribution file hashes are recorded separately.

## Submission boundary

As checked again on 2026-09-26, solver-only complete mathematical proofs may
precede Lean. The official awards PR receives catalog references to a public
proof or publication, with theorem locations, version/date, and contribution
evidence. A full 40-character commit is explicitly required for Lean submissions;
this mathematical submission also uses a pinned commit for reproducibility.
The authenticated account is `zhangzenozhang-jpg`; the author-created target
repository is `zhangzenozhang-jpg/-forest-unimodality-proof`. Publication and PR
receipts belong in the submission directory. This report itself does not assert
that an upload, PR, official acceptance, or award claim has occurred.
