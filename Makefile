.PHONY: install format lint test sec

install:
	pip install -r src/requirements.txt

format:
	black src/ tests/
	black src --check

lint:
	pylint src/**.py tests/**.py

test:
	pytest
	
sec:
	bandit -r .
	pip-audit -r src/requirements.txt
