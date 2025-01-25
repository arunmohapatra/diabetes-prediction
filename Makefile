.PHONY: install run test clean

install:
	pip install -r requirements.txt

run:
	python -m app.main

test:
	python -m unittest discover tests

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__