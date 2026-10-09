.PHONY: run test lint

run:
	python3 src/main.py

test:
	python3 -m unittest discover -s tests

lint:
	python3 -m pycodestyle --max-line-length=80 src tests