# threshold59 archive audit (fresh review, 2026-09-26)

## Scope and result at this stage

The symbol n in this archive means the number of vertices. The release claims
unimodality of the independence polynomial for every finite simple forest with
n >= 59, including disconnected forests and arbitrary maximum degree. The new
certificates treat 59 <= n <= 79; n >= 80 is inherited through the frozen chain
80 -> 99 -> 130 -> 170 -> 350 -> 500 -> 900. The original release deliberately
describes this as conditional on its inherited structural lemmas. Those lemmas
are not simply absent: their mathematical proofs and finite certificates occur
inside the nested 900 input. The absence of Lean formalization or peer review is
not itself a mathematical gap.

The threshold59 archive alone does not settle the small orders n < 59. If the
separate all-forest n <= 60 proof is correct, the two order ranges overlap and
logically cover every finite forest. Overlap at 59 and 60 causes no problem. This
audit does not turn a sufficient negative numerical budget into a counterexample
or claim optimality of any threshold.

## Mathematical review actually performed

1. Read the complete new PROOF_ZH.md, the new independent integer-count checker,
   finite-kernel checker, coverage checker, source checker and replay driver.
   The leaf-weight exchange, matching lower bound, h >= ceil(n/3), complement
   independent-set bound, path coefficient lower bound, and conditional
   cancellation identity have coherent direct combinatorial proofs.
2. Checked the finite state-domain reduction. The independent checker reconstructs
   every admissible integer (n,k), every matching count envelope and every (M,j)
   state. It does not trust a claimed zero state count or a stored positive flag.
   The probability upper bound uses b^y/P_n(a), hence its direction is safe.
3. Checked the kernel signs and q-interpolation remainder: R'' is bounded above;
   paying (qb-qa)^2 Z/8 at both endpoints proves R >= 0 throughout. The payoff is
   concave in real m, so endpoint positivity suffices. The mixture weights are
   fixed for the whole distribution, nonnegative and normalized. No per-state
   kernel switching is used.
4. Reviewed the inherited head/tail proof in the 900 input
   `inputs/inherited_mean/渐近界改进证明.md`, Appendices A and B. The rooted-tree
   injection can be decoded from whether the marked vertex's grandparent is
   selected. The matching-block adjacent-layer inclusion coupling has the right
   conditional marginals and gives ratio domination of a downward-closed event.
   This is an actual proof, not an unsupported reference to small enumeration.
5. Read the complete scale-corrected mean proof and its two predecessor files:
   `森林规模修正均值不等式的证明.md`,
   `规模修正均值候选的短腿归约.md`, and
   `规模修正均值的两型末端归约.md`. The least-counterexample argument uses only
   genuinely smaller forests; the 14-vertex tip reduction excludes arbitrary leg
   lengths; root independence-number states alternate along unary chains; the
   bridge tail has an explicit positive recurrence; the 823 final branch
   combinations are derived from the preceding structural reductions. No
   unsupported extension from finitely many trees was found in these arguments.
6. Reviewed 80-package density induction, signed log variance sources, message
   flow identity and common-noise covariance integration. The degree >= 5 step
   retains a smaller nonpath tree. Scalar-source interval replacements have the
   correct signs, including response-dependent signed flow bounds. Parent-message
   feasible intervals and all spline breakpoints are checked. The log root gain
   is valid after choosing a leaf root in each component. The tilted total mean
   is not assumed monotone; whole-step and endpoint upper bounds are separated.
7. Reviewed the 99-package reuse argument. Its finite-boundary density increment
   h/129 remains valid for n <= 79. Older finite kernels have larger M domains
   and their graph-order thresholds only supplied a sufficient m lower bound.
   The 59 release excludes the N-sensitive signed log profiles introduced in the
   80 release and recomputes its own profiles at N=59.
8. Reviewed the stage-350 analytic sections on negative-power Hermite bounds,
   telescoping lower-tail charges, the exact triangular variance 1/6 of the
   lattice second-difference kernel, the Gaussian variance-matching correction,
   and the monotonicity argument on the entire remaining m half-line. The
   written argument retains the changed normalization, the extra 1/96 error,
   and the original lower-tail exponent m rather than silently replacing it by
   m + 1/(6v). No omitted cost or finite-to-infinite extrapolation was identified
   in these reviewed sections.

No concrete mathematical counterexample or deduction error was found in those
reviewed portions. This is a scoped mathematical audit, not a claim that every
line of the entire large analytic chain has been independently re-proved.

## Reproduction details

All work is on `work/audit59/replay59`, a copy of the extracted source archive;
the supplied originals are not edited. Python is the bundled standard runtime.

Fresh integrity check: PASS, all 43 manifest entries and the frozen 80 input
hash agree. Log: `check_release_fresh.log`.

The fresh new59 run uses `python -S -u replay.py --skip-prior`. It is explicitly a
new59 replay and does not pretend to re-run the old chain. Its log is
`replay_new59_fresh.log`. It completed successfully in 370.547 seconds. The fresh
summary is copied to `new59_fresh_summary.json`, with detailed source and kernel
checks in `new59_fresh_source_checks.json` and `new59_fresh_kernel_checks.json`.
All 231 certificates, 1,185,408 endpoint states, 28,987 admissible (n,k) pairs,
154 q strata and 43 parent intervals passed. The four sources check 1,363
probability cells, 8,435 retention cells, 37,026 parent cases and 111,078 response
regions. The least normalized payoff remains exactly
424830401847072141613691 / 10000000000000000000000000000, at scale 23.

Fresh negative testing also passed: all 17 deliberately invalid inputs were
rejected, including corrupted counts, missing integer pairs, wrong N, false
empty regions, wrong state cap, negative mixture weights, stale variance costs,
false minorants, negative expected budgets, missing continuous coverage, a
source-domain gap, a modified frozen archive and disabled assertions. Logs and
machine-readable results: `negative_tests_fresh.log`, `negative_tests_fresh.json`.

The attempted ordinary full prior80 run hit a real Windows portability problem:
`subprocess.CreateProcess` rejects a nested child cwd above MAX_PATH (WinError
267, first observed at the 350 release path length 272). Log:
`prior80_full_fresh.log`. This is an execution-environment failure, not a failed
mathematical assertion.

An external wrapper, `windows_long_path_launcher.py`, starts each Python child in
a short cwd and then calls Python `os.chdir` to the exact original cwd before
executing the original script with runpy. It changes no release code,
certificate, assertion or arithmetic. Python subprocess flags and script
arguments are preserved. The full prior80 replay completed successfully through
this wrapper in 1680.063 seconds; log: `prior80_full_portable_fresh.log`. The full
nested summary is copied to `prior80_full_fresh_summary.json`. It freshly replays
all stages 80, 99, 130, 170, 350, 500 and 900, including all foundational finite
mean identities. The final stage-80 checks cover 236 kernels, 2,523,312 endpoint
states, 93,456 real half-line cases, 154 q strata and 43 parent intervals. Its
sources cover 28,692 probability cells, 116,974 retention cells, 403,825 parent
cases and 1,211,475 real-response regions; its 106-point density induction checks
11,130 branch classes. `combined_fresh_audit.json` records the separate new59
and prior80 calls and the per-stage results without presenting them as one
invocation. All requested arithmetic reproduction is now complete and passed.

## Submission wording implications

Do not title a submission a proof for all forest orders using this archive alone.
With a validated n <= 60 theorem, an all-order assembly is logically legitimate,
but the submission must state and prove the inherited lemmas or supply their
precise archived proof locations. Describe fresh checks separately from supplied
historical audit logs. Exact replay proves the encoded arithmetic inequalities;
the mathematical reduction of all forests to those inequalities still needs the
written proofs. Neither a positive stored flag nor lack of formalization should
be mistaken for the mathematical conclusion.
