# Unimodality of Forest Independence Polynomials

**Computer verification and supplementary proof materials**  
Tong Zhang and Wei Li · Version 2026-09-27

This versioned supplement accompanies the mathematical proof of unimodality of the independence polynomial of every finite forest. It supplies fixed certificate data, exact acceptance programs, a reproducible entry point, and documentation of the computational part of the proof. The authors are responsible for the mathematical claims and the accompanying exposition.

## Reproduce the checks

From this version's directory, `companion/2026-09-27/`, with `anc/` present, run:

```sh
python -S anc/proof_reproduce.py --work /path/to/empty-work
```

Use a new or empty work directory outside `anc/`. The recorded complete replay used **Python 3.12.14** and only its standard library; other Python versions have not received a complete compatibility replay. Assertions must remain enabled: **do not use `-O` or `-OO`**. No network, optional package, numerical optimizer, or forest catalogue is required.

Allow tens of minutes and several hundred megabytes of disk space. Add `--workers 1` to reduce parallel memory use; the default is three workers. On Windows, use short paths for the repository and work directory. See [anc/README.txt](anc/README.txt) for the full execution instructions.

Success produces `proof_reproduction_summary.json` in the chosen work directory, including:

```json
{
  "all_mathematical_acceptance_checks_passed": true
}
```

The run also retains fresh stage summaries, subprocess return codes, logs, and omission records. A failed subprocess, missing stage, source mismatch, or incomplete omission record causes failure. An existing successful log is not accepted as a substitute for a fresh stage computation.

## What the computation establishes

The written proof reduces the problem to explicitly defined parameter domains and mathematical inequalities. The programs accept certificates for these obligations using exact arithmetic and rigorous bounds. They do not establish the theorem by enumerating forests, checking random examples, or searching for counterexamples.

| Part of the proof | Scope |
|---|---|
| Finite-order argument | Forests of order at most 60. Edgeless forests are handled directly. The remaining domain contains 17,100 scalar parameter triples, covered by direct bounds, 670 rational comparisons, and 1,907 linear certificates. |
| Large-order argument | Forests of order at least 59, using the analytic tail interface and successive exact certificate extensions. |
| Overlap | Both arguments cover orders 59 and 60, so their ranges leave no gap. |

The finite triples are parameter values supplied by the reduction, not representatives of graph isomorphism classes. Integer counting rows and rational separating identities are checked exactly, including their sign conditions and conditional assumptions. Continuous inequalities are verified on complete interval partitions by outward rational bounds or explicit polynomial identities. Discrete kernel domains are reconstructed from their integer bounds or exact combinatorial support. The written analytic arguments supply the unbounded-parameter interfaces.

The entry point checks the finite-order certificates and replays the complete inherited chain:

```text
900 → 500 → 350 → 170 → 130 → 99 → 80 → 59
```

It retains input integrity checks, source reconstruction, exact budget and kernel acceptance, comparison of mathematical fields with the frozen data, complete parameter coverage, and the analytic tail interfaces. The [proof map](anc/PROOF_MAP.md) relates the certificate families to the mathematical argument.

**The accepting programs do not formalize the written proof in a proof assistant.** Their conclusion is exact acceptance of the specified certificates. The theorem also depends on the structural reductions, analytic estimates, and domain arguments in the mathematical text.

## File map

The supplementary documents are located beside this README:

| Document | Contents |
|---|---|
| [detailed-proof-reference.pdf](detailed-proof-reference.pdf) | The longer mathematical reference, retaining the detailed certificate and reproduction material moved out of the shortened article. |
| [finite_rows.tex](finite_rows.tex) | Original integer row specifications; the notation is defined in the detailed reference. |
| [finite_data.tex](finite_data.tex) | Original finite proof-data summary and explicit affine certificate. |
| [reproducibility.tex](reproducibility.tex) | Original reproduction documentation and historical revision notes. |
| [SHA256SUMS.json](SHA256SUMS.json) | File identifiers and checksums for this version of the supplement. |

The `anc/` directory consists of the following 13 files:

```text
anc/
├── README.txt
├── proof_reproduce.py
├── REPRO_RESULT.json
├── PROOF_MAP.md
├── MATHEMATICAL_EDITS.md
└── repro/
    ├── proof_runtime.py
    ├── input_sha256.json
    ├── patches.json
    ├── diagnostic_omissions.diff
    ├── source_index.json
    ├── extract_sources.py
    └── inputs/
        ├── forest_n60_extension_and_n100_gap.zip
        └── forest_threshold_59_audited_handoff.zip
```

| File or directory | Purpose |
|---|---|
| [anc/proof_reproduce.py](anc/proof_reproduce.py) | Single entry point for fresh certificate reproduction. |
| [anc/repro/proof_runtime.py](anc/repro/proof_runtime.py) | Runtime for authenticated execution and documented diagnostic omissions. |
| [anc/repro/inputs/](anc/repro/inputs/) | Two frozen input archives; the large-order archive recursively contains the inherited releases and mean data. |
| [anc/repro/input_sha256.json](anc/repro/input_sha256.json) | Input archive identifiers. |
| [anc/REPRO_RESULT.json](anc/REPRO_RESULT.json) | Recorded complete replay, including timestamps, digests, return codes, and all eight stage summaries. |
| [anc/repro/patches.json](anc/repro/patches.json) and [diagnostic_omissions.diff](anc/repro/diagnostic_omissions.diff) | Exact authenticated omission specification and readable source differences. |
| [anc/repro/source_index.json](anc/repro/source_index.json) and [extract_sources.py](anc/repro/extract_sources.py) | Index and authenticated extraction of the 32 historical mathematical source documents. |
| [anc/PROOF_MAP.md](anc/PROOF_MAP.md) and [MATHEMATICAL_EDITS.md](anc/MATHEMATICAL_EDITS.md) | Logical map and documented mathematical/editorial clarifications. |

Executable filenames mentioned in historical documents refer to their released directories inside the frozen archives. The entry point extracts and invokes those checkers; they need not appear beside a historical readable document.

## Recorded complete replay

The following values are taken from [anc/REPRO_RESULT.json](anc/REPRO_RESULT.json). They describe the recorded run, not a new run triggered by reading this repository.

| Field | Recorded value |
|---|---|
| Start, UTC | 2026-09-27 08:52:51.432403 |
| Finish, UTC | 2026-09-27 09:28:24.652947 |
| Elapsed time | 2,133.218 seconds, approximately 35 minutes 33 seconds |
| Runtime | Python 3.12.14, 64-bit Windows |
| Mathematical acceptance | All checks passed |
| Top-level subprocesses | All five returned zero |
| Inherited chain | All eight stages replayed and passed |
| Authenticated omission boundaries | 13 |
| Supplementary graph diagnostics | Not executed |
| Original unmodified full entry point | Not used |
| Proof-assistant formalization | No |

Times recorded for individual inherited stages include their preceding chains and must not be added to obtain total elapsed time.

## Frozen input identifiers

The entry point authenticates both input archives before extraction. Their SHA-256 values are:

**`anc/repro/inputs/forest_n60_extension_and_n100_gap.zip`**

```text
3cbf5c0b32bbbce213e23db79655138aebd9ceb01fc9f55df4ac52a91ed12759
```

**`anc/repro/inputs/forest_threshold_59_audited_handoff.zip`**

```text
cbe5b28a4c0335ef099435356edaba0d440e650f7fd7398eb3dab8e11d0fa7f1
```

The original archives are preserved byte for byte. Their historical documents and diagnostic files remain present for integrity; presence in an archive does not imply execution by the supplied entry point.

## Diagnostic omissions and retained proof obligations

The supplied entry point omits supplementary graph-instance diagnostic imports and calls, four named-host attachment cross-check blocks, and optional finite path sampling. These checks are not used as evidence for the universal mathematical claims.

The complete symbolic proof domains remain active, including the 378 short-leg residual records with 756 rational endpoint checks, 295 spider bases, 180 terminal tail base indices, 1,080 terminal blocks and 342 nonnegative identities, 823 final combinations, eight rooted-type constants, and the universal tail bounds. In particular, the omitted 378 named-host checks are distinct from the retained 378 symbolic residual records.

The omission specification authenticates every affected source against its original SHA-256, requires each replacement to match exactly once, and authenticates the resulting source. All 13 source boundaries must be accounted for. Changes are applied only in memory; frozen archives, extracted source files, and their manifests are unchanged. Comparisons with historical mean summaries omit the explicitly documented diagnostic fields and existing timing fields; the mathematical fields must still match the frozen reference. The accepting mathematical functions are not rewritten.

The auxiliary `verify_countermodels.py` check verifies algebraic consistency of two fixed rational points in real-valued relaxations. These points are not forests, and this check is neither a forest counterexample search nor a premise of the main theorem.

For the precise changes and integrity conditions, consult [anc/repro/patches.json](anc/repro/patches.json), [anc/repro/diagnostic_omissions.diff](anc/repro/diagnostic_omissions.diff), and [anc/README.txt](anc/README.txt).

## Historical mathematical sources

To extract and authenticate the 32 indexed historical proof documents without executing release code, use a new or empty output directory:

```sh
python -S anc/repro/extract_sources.py --output /path/to/empty-docs
```

The [source index](anc/repro/source_index.json) records each complete nested-archive route and digest. These historical sources provide provenance. The mathematical exposition explains the active proof without requiring historical notes, diagnostic examples, or earlier thresholds to become additional hypotheses.
