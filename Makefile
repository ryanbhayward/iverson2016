PPR = iverson2016.sol

$(PPR).ps: $(PPR).tex
	latex $(PPR)
	dvips -D 1000 $(PPR)
	ps2pdf $(PPR).ps

clean: 
	-rm $(PPR).aux
	-rm $(PPR).dvi
	-rm $(PPR).log
	-rm $(PPR).ps

cleanup: clean
	-rm $(PPR).pdf
