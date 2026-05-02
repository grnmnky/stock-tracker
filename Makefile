.PHONY: setup generate run compile test clean

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

# Run tests with project-local pytest install
test:
	PYTHONPATH="$(PWD)/.vendor" python -m pytest -q .

# Cleanup environment and data
clean:
	rm -rf .venv
	rm -rf .vendor
	rm -rf data/*.json