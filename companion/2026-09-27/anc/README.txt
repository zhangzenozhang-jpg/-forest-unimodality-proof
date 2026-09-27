EXACT MATHEMATICAL CERTIFICATE REPRODUCTION

Run from any directory, using Python 3 and its standard library. The supplied
reproduction result records Python 3.12.14; other versions have not received a
complete compatibility replay:

  python -S /path/to/anc/proof_reproduce.py --work /path/to/new-empty-work

On Windows, prefer a short work path. The supplied runtime also preserves the
original long-path launcher mechanism: child Python starts in this short repro
directory and then changes directory inside Python. Keep this attachment under
a reasonably short path as well. Use --workers 1 to reduce parallel memory use;
the default is 3 workers. Allow tens of minutes and several hundred MB of disk.
Do not use -O or -OO. Existing work directories containing files are rejected.

This command checks the finite certificate and then the entire inherited chain
900 -> 500 -> 350 -> 170 -> 130 -> 99 -> 80 -> 59 in a fresh directory. It needs
no network, optional package, numerical optimizer, or forest catalogue. Success
is reported only after all five top-level subprocesses exit zero, all eight
large-order stage summaries are present, all thirteen source-omission boundaries
were authenticated, and each stage reports that diagnostics were omitted.
The result is work/proof_reproduction_summary.json, with
all_mathematical_acceptance_checks_passed = true. Logs, the full fresh stage
summary, and per-process patch records are retained in the work directory.
Failures are recorded and propagated; an old successful result is never reused.

The proof also needs the mathematical reductions in the article and appendices.
This computation is exact certificate acceptance, not proof-assistant
formalization and not an enumeration of forests to look for counterexamples.
The auxiliary verify_countermodels.py check verifies algebraic consistency of
two fixed rational points in explicitly stated real-valued relaxations. These
points are not forests, and this is neither a forest counterexample nor a
counterexample search. This auxiliary observation is not a premise of the main
unimodality theorem.

WHAT IS RETAINED

The two files under repro/inputs are byte-for-byte frozen inputs (34,702,688
bytes in total). Their SHA256 digests are fixed in proof_reproduce.py. The large
ZIP recursively contains every prior release. Each original release's integrity
checks, source reconstruction, fixed budget rows, exact kernel checks, stored
exact_check comparison, coverage verification, and unbounded-parameter bridge
are retained. The mathematical acceptance functions are not rewritten.

All complete finite proof obligations following the written structural
reduction remain, including the 378 short-leg residual records with their 756
rational endpoint checks, 295 spider bases, 180 terminal tail base indices,
1080 terminal blocks and 342 nonnegative identities, 823 final combinations,
eight rooted-type constants, and the universal tail bounds. These bounded
proof types are required by the analytic reduction. They are distinct from
checking a catalogue of arbitrary forests.

WHAT IS OMITTED, AND WHY

Original full replay scripts also call supplementary diagnostics. The new
entrypoint omits the eight diagnostic module imports/calls. It also omits four
named-host attachment cross-check blocks in inherited mean scripts (378, 16,
16, and 24 host checks) and an optional path-formula check over 1..64. The 378
named-host checks are NOT the 378 complete symbolic residual records above.
The removed host checks and finite path sampling are not used as evidence for
any universal claim; the article gives the corresponding algebraic identities
and recurrence proof. No complete structural proof case is removed.

The full patch specification is repro/patches.json; a readable unified diff is
repro/diagnostic_omissions.diff. Every modified source is locked to its original
SHA256, every replacement must match exactly once, and the resulting bytes are
also hashed. These changes are applied only in memory. Frozen ZIPs, extracted
source files and their manifests remain unchanged. The patch specification is
itself hash-locked in both entry scripts. Unknown code at a patch boundary
causes failure. The replay runtime refuses diagnostic module imports/scripts.

Inherited mean JSON comparison excludes only the explicitly omitted diagnostic
fields (path_formula_instances, actual_attachment_identities,
actual_attachment_checks, actual_attachments,
independent_vertex_deletion_attachment_checks, actual) and the two existing
timing fields. All remaining mathematical fields must still equal the frozen
reference. Legacy zero/empty/None diagnostic fields in generated mean JSON mean
not executed; the stage summaries and this entrypoint identify their omission.
This is a documented proof-only entrypoint, not a claim that the original
unmodified full entrypoint was run.

HISTORICAL SOURCE DOCUMENTS WITHOUT DUPLICATION

The frozen ZIPs contain historical source documents and diagnostic files for
hash closure. Their presence does not mean the new entrypoint executes them.
No outer duplicate manuscripts, old audits/PDFs, submission receipts or old
run logs are needed. To extract and authenticate the 32 indexed historical
proof documents without executing any release code, run:

  python -S /path/to/anc/repro/extract_sources.py --output /new/empty/docs

The index records the complete nested archive route and SHA256 for each file.
The historical finite-order Chinese proof is already inside the finite ZIP.
The English article and appendices explain the proof without requiring these
historical documents to be duplicated in the attachment.
