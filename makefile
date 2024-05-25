.PHONY: dev activate clean install freeze

dev:
	@echo "Running development server..."
	python3 src/app.py

activate:
	@echo "Activating virtual environment..."
	source./.venv/bin/activate

clean:
	@echo "Cleaning up virtual environment..."
	rm -rf.venv

install:
	@echo "Installing dependencies..."
	pip3 install -r requirements.txt

freeze:
	@echo "Freezing installed packages..."
	pip3 freeze > requirements.txt
