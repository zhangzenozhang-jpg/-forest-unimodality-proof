# Build the manuscripts

The English manuscript uses pdfLaTeX (TeX Live 2025 used here):

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The Chinese audit uses XeLaTeX and ctex:

    xelatex -interaction=nonstopmode -halt-on-error audit_zh.tex
    xelatex -interaction=nonstopmode -halt-on-error audit_zh.tex

Run from this directory. No shell-escape or network is required. Compile products
are main.pdf and audit_zh.pdf; the delivered PDFs have descriptive filenames.
The author is Tong Zhang; no affiliation was supplied. Email is author-provided.
