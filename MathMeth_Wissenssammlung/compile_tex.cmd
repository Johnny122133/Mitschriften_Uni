pdflatex -draftmode main.tex
bibtex file :: or biber
:: makeindex file.idx # if needed
:: makeindex -s style.gls ...# for glossary if needed
pdflatex -draftmode main.tex
pdflatex main.tex