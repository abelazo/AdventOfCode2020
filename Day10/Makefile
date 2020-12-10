all: test run

run: solution.py
	python3 solution.py

init: requriements.txt
	pip3 install -r requirements.txt

test: test.py
	python3 -m unittest test.py

.PHONY: init test run
