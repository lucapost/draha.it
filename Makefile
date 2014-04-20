generate: 
	./minimalsite.py -t templates/default_template.py

update:
	make
	git add .
	git commit -am fix

upload: 
	make update
	git push
	rsync -avr -e ssh ./dst/* flarevm:www/draha.it/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
