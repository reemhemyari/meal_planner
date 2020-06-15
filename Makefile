#Internal vars
VENV_DIR=venv
PROJECT_MODULE=meal_planner


#TARGETS FOR HUMAN INTERACTION
default: clean test

clean:
	@echo "Clean"
	@rm -rf ${VENV_DIR}
	@rm .coverage
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +

install-requirements: ${VENV_DIR}

format: install-requirements
	@echo "Formatting"
	@. ./${VENV_DIR}/bin/activate && python3 -m black ${PROJECT_MODULE}

lint: install-requirements
	@echo "Linting"
	@. ./${VENV_DIR}/bin/activate && python3 -m flake8
	@. ./${VENV_DIR}/bin/activate && python3 -m mypy ${PROJECT_MODULE}

test: install-requirements
	@echo "Testing"
	@. ./${VENV_DIR}/bin/activate && python3 -m pytest -s \
	--cov-branch \
	--cov=. \
	--cov-fail-under=70

#DIRECTORIES
${VENV_DIR}:
	@python3 -m venv venv
	@echo "Install requirements"
	@. ./venv/bin/activate \
	&& pip install -r requirements.txt

#Makefile internals
.NOTPARALLEL:

.PHONY: clean install-requirements format lint test
