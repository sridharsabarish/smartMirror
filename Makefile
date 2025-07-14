
run: venv test 
	 cd src && python3 app.py

.PHONY: test venv

venv:
	cd .. && source bin/activate && cd -
test: venv
	 cd test && python -m pytest -vv


