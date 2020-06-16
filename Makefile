#Internal vars
VENV_DIR=venv
PROJECT_MODULE=meal_planner

ifdef OS
	RMDIR = rmdir /s/q
	PYTHON_ACTIVATE = ${VENV_DIR}\Scripts\activate
	PYTHON = py
else
	RMDIR = rm -rf
	PYTHON_ACTIVATE = . ./${VENV_DIR}/bin/activate
	PYTHON = python3
endif

#TARGETS FOR HUMAN INTERACTION
default: clean test

clean:
	@echo "Clean"
	@${RMDIR} ${VENV_DIR}
	@${RMDIR} .coverage
	@${RMDIR} ".pytest_cache"
	@${RMDIR} ".mypy_cache"

install-requirements: ${VENV_DIR}

format: install-requirements
	@echo "Formatting"
	@${PYTHON_ACTIVATE} && ${PYTHON} -m black ${PROJECT_MODULE}

lint: install-requirements
	@echo "Linting"
	@${PYTHON_ACTIVATE} && ${PYTHON} -m flake8
	@${PYTHON_ACTIVATE} && ${PYTHON} -m mypy ${PROJECT_MODULE}

test: install-requirements
	@echo "Testing"
	@${PYTHON_ACTIVATE} && ${PYTHON} -m pytest -s \
	--cov-branch \
	--cov=. \
	--cov-fail-under=70

#DIRECTORIES
${VENV_DIR}:
	@${PYTHON} -m venv venv
	@echo "Install requirements"
	@${PYTHON_ACTIVATE} \
	&& pip install -r requirements.txt

#Makefile internals
.NOTPARALLEL:

.PHONY: clean install-requirements format lint test
