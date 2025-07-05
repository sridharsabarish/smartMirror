run: 
	cd src && python3 app.py

.PHONY: test

test: 
	cd test && python3 -m pytest -vv
