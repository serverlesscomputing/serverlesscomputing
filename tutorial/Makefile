all: tutorial.pdf

tutorial.pdf: *.tex
	pdflatex tutorial.tex
	pdflatex tutorial.tex
	bibtex tutorial
	bibtex tutorial
	pdflatex tutorial.tex

clean:
	-rm -f tutorial.{aux,bbl,blg,log,pdf}
	-rm -f *~
