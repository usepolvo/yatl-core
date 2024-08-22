# Makefile for YATL Core

# Python version
PYTHON := python3
# Virtual environment directory
VENV := venv
# Activate virtual environment
ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE := $(VENV)/Scripts/activate
else
    VENV_ACTIVATE := . $(VENV)/bin/activate
endif

# Default target
.PHONY: all
all: test

# Create virtual environment
$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV_ACTIVATE) && pip install --upgrade pip
	$(VENV_ACTIVATE) && pip install -r requirements.txt

# Run tests
.PHONY: test
test: $(VENV)/bin/activate
	$(VENV_ACTIVATE) && $(PYTHON) test-suite/runners/basic_test_runner.py

# Clean up
.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Set up development environment
.PHONY: setup
setup: $(VENV)/bin/activate

# Run linter
.PHONY: lint
lint: $(VENV)/bin/activate
	$(VENV_ACTIVATE) && pip install pylint
	$(VENV_ACTIVATE) && pylint test-suite

# Generate documentation (placeholder)
.PHONY: docs
docs:
	@echo "Generating documentation..."
	# Add commands to generate documentation here

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make test    - Run the test suite"
	@echo "  make setup   - Set up the development environment"
	@echo "  make clean   - Remove virtual environment and cache files"
	@echo "  make lint    - Run the linter"
	@echo "  make docs    - Generate documentation"
	@echo "  make help    - Show this help message"
