.PHONY: help lint format test run

help:
	@echo "make lint   - ruff check + format check"
	@echo "make format - ruff format + fix"
	@echo "make test   - pytest"
	@echo "make run    - run app (uvicorn)"

lint:
	ruff check .
	ruff format --check .

format:
	ruff check . --fix
	ruff format .

test:
	pytest -q

run:
	python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
