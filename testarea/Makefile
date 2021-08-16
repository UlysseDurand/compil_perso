compilelatex:
	@python3 ../data/main.py custom.lgi document.mdx latex

compilehtml:
	@python3 ../data/main.py custom.lgi document.mdx html

compilepdf: compilelatex
	pdflatex document.tex
	@make clean

compileall: compilehtml compilepdf 

clean:
	rm *.log
	rm *.aux