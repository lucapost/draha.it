generate: 
	./minimalsite.py -t templates/default_template.py

github:
	make
	git add .
	git commit -am fix
	git push

flarevm: 
	rsync -avr -e ssh ./dst/* flarevm:www/draha.it/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
