compile:
	./minimalsite.py -t it
	./minimalsite.py -t de

up:
	git add .
	git commit -a
	git push
