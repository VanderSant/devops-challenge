.PHONY: install format lint test sec

install:
	pip install -r src/requirements.txt

format:
	black src
	black src --check

lint:
	pylint src/**.py
