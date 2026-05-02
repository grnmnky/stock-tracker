.PHONY: setup generate run compile lint test coverage verify clean

SYMBOL ?= MSFT

# Default setup: virtualenv and dependencies
setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	mkdir -p data

# Generate mock data for a symbol (e.g., make generate SYMBOL=MSFT)
generate:
	. .venv/bin/activate && python main.py --generate $(or $(filter-out $@,$(MAKECMDGOALS)),$(SYMBOL))

# Start the Flask/Web app
run:
	. .venv/bin/activate && python web/app.py

# Compile-check Python sources
compile:
	. .venv/bin/activate && python -m compileall -q .

# Lint Python code (prefer ruff, fallback to compile check)
lint:
	. .venv/bin/activate && (python -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('ruff') else 1)" && python -m ruff check . || python -m compileall -q .)

# Run tests with project-local pytest install
test:
	PYTHONPATH="$(PWD):$(PWD)/.vendor" python -m pytest -q .

# Run tests with coverage report
coverage:
	. .venv/bin/activate && PYTHONPATH="$(PWD):$(PWD)/.vendor" python -m pytest -q --cov --cov-report=term-missing .

# Run all verification steps
verify: compile lint test coverage

# Cleanup environment and data
clean:
	rm -rf .venv
	rm -rf .vendor
	rm -rf data/*.json