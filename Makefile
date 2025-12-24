.PHONY: help lint format test run

help:
	@echo "make lint   - ruff check + format check"
	@echo "make format - ruff format + fix"
	@echo "make test   - pytest"
	@echo "make run    - run app (uvicorn)"

lint:
	python -m ruff check .
	python -m ruff format --check .

format:
	python -m ruff check . --fix
	python -m ruff format .

test:
	python -m pytest -q

run:
	python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
