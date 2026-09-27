# Logical map of the article and fixed data

The English article is the mathematical exposition. This map locates the
computational inputs; it is not an additional proof premise. TeX labels below
are stable identifiers in the submitted source.

| Claim | English source and label | Fixed input family |
|---|---|---|
| Every forest on at most 60 vertices | `finite60.tex`, `f60:sec-main` | finite archive: `certificates.json`, `verify.py`, `verify_grid.py` |
| Integer rows and their parameter domains | `finite_rows.tex`, `f60:subsec-row-specification` | finite archive: row reconstruction and `kernel.py` |
| Initial/final monotone coefficient segments and activity window | `large59.tex`, `l59:window`, `l59:mean` | structural argument plus activity-two mean proof |
| Activity-two mean, all orders | `mean_foundations.tex`, `am:main` | stage 900: `inputs/inherited_mean/research_code/` |
| Short-leg and spider reductions | `mean_foundations.tex`, `am:short-legs`, `am:spiders` | `adjusted_mean_leg_cluster.py` and its rational data |
| Arbitrary bridge lengths and two terminal types | `mean_foundations.tex`, `am:terminal-types` | `endbranch_path_context_certificate.py`, `audit_endbranch_path_context.py` |
| All branch counts in the final mean closure | `mean_foundations.tex`, `am:final-closure` | `adjusted_mean_global_closure.py`, `audit_terminal_fan_second_stage.py` |
| Message variance, selection and heterogeneous source bounds | `analytic_foundations.tex`, `an:messages` through `an:tilting` | stages 900, 500, 350 source certificates |
| Gaussian, lattice and directional kernels; every sufficiently large real mean | `analytic_foundations.tex`, `an:fourier` through `an:unbounded` | inherited analytic data; stage-350 `fixed_plan_350.json` and `results/complete_350.json.gz` |
| Refined density/source/Laplace bounds | `finite_kernels.tex`, `fk:moments` and following subsections | stages 170, 130, 99, 80 source families, rechecked at the required order |
| Continuous activity, bounded mean, discrete support and tail join | `finite_kernels.tex`, finite-kernel subsections | exact kernel and coverage certificates at stages 170, 130, 99, 80, 59 |
| Matching-count refinement for orders 59–79 | `large59.tex`, `sec:matching59`, `sec:cert59` | stage-59 matching counts, certificates and coverage |
| Entire theorem | `main.tex`, `thm:all` | finite argument through 60 plus large-order argument from 59 |

The stage-350 large-mean inequalities remain valid for a smaller forest only
when its actual mean satisfies the stated row threshold. The finite kernels
cover the complementary mean range. Stage-80 kernels whose signed order costs
need `n >= 80` are not reused for orders 59–79.

The nested-archive paths and SHA256 identifiers of all 32 indexed historical
source documents are in `repro/source_index.json`. The extraction utility
described in `README.txt` authenticates them without running release code.
The historical documents are retained once, inside the immutable inputs.

Supplementary graph-instance diagnostics are omitted by the disclosed runtime
patches. Complete symbolic finite cases, induction bases and all-interval
certificates listed above remain essential.
