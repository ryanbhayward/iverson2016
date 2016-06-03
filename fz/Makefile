LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = forzac

full:	
	(cd pix; perl make11.pl)
	$(LATEX) $(PPR)
	$(DVIPS) -D 1000 $(PPR) -o
	ps2pdf $(PPR).ps
