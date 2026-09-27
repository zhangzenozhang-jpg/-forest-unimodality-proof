# Mathematical and editorial revisions for the English preprint

The fixed mathematical data and the two input ZIP archives have not been changed.
The article gives a consolidated English exposition of the active proof chain.

## Explicit density hypotheses

The stage-80 historical document `PROOF_ZH.md`, section 2.1, lists conditions for
the density induction. Two conditions enforced by its original
`check_density_bound.py` must also appear in that displayed mathematical list:

* `h > 0`;
* `g4 <= mu(P4) - 4*r`.

The first is used in the transfer from `r*n+h` to `(r+h/98)*n` for `n <= 98`.
The second makes the four-vertex path a valid induction base. The revised
English density appendix states both conditions. Existing certificate values
already satisfy them, so no constant or acceptance tolerance is changed.

## Location of executable files

Historical flattened readable copies were not executable release directories.
For reproduction use `python -S anc/proof_reproduce.py --work EMPTY_DIRECTORY`
from the submission root, as specified in `README.txt` and the article. Do not
look for `verify.py` beside a historical readable proof copy. The new entry point
extracts the frozen releases and calls their actual checkers.

## Consolidation

The English article contains one overall theorem and its finite/large-order
propositions, followed by the structural proof and technical appendices.
Repeated status statements, old thresholds, prize/submission history and
duplicate outer archives are not part of the preprint. The rational relaxation
obstructions at other orders are not used in the unimodality proof.

The proof-only execution omits supplementary instance diagnostics through the
fully disclosed, source-hash-locked changes in `repro/patches.json`. These are
execution changes, not edits to the archived mathematical accepting functions.
Complete finite proof obligations obtained by a mathematical reduction remain.

The English exposition and code require mathematical reading as well as exact
certificate acceptance; they are not a proof-assistant formalization.
