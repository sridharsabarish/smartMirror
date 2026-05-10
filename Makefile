

install :
	python3 -m pip install -r requirements.txt

run: install test 
	 cd src && python3 app.py

.PHONY: test venv run

venv:
	cd .. && source bin/activate && cd -
test: 
	 cd test && python3 -m pytest -vv

kill:
	 sudo pkill -f "python3 app.py"
