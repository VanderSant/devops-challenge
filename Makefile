.PHONY: install format lint test sec

install:
	pip install -r src/requirements.txt

format:
	black src

lint:
	pylint src/**.py
