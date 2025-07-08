
run: test 
	 cd src && python3 app.py

.PHONY: test


test:
	 cd test && python -m pytest -vv


