.PHONY: setup generate run clean

# Default setup: virtualenv and dependencies
setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	mkdir -p data

# Generate mock data for a symbol (e.g., make generate SYMBOL=MSFT)
generate:
	. .venv/bin/activate && python main.py --generate $(filter-out $@,$(MAKECMDGOALS))

# Start the Flask/Web app
run:
	. .venv/bin/activate && python web/app.py

# Cleanup environment and data
clean:
	rm -rf .venv
	rm -rf data/*.json