#Internal vars
VENV_DIR=venv
PROJECT_MODULE=meal_planner

ifdef OS
	RMDIR = rmdir /s/q
	PYTHON_ACTIVATE = ${VENV_DIR}\Scripts\activate
else
	RMDIR = rm -rf
	PYTHON_ACTIVATE = . ./${VENV_DIR}/bin/activate
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
	@${PYTHON_ACTIVATE} && python3 -m black ${PROJECT_MODULE}

lint: install-requirements
	@echo "Linting"
	@${PYTHON_ACTIVATE} && python3 -m flake8
	@${PYTHON_ACTIVATE} && python3 -m mypy ${PROJECT_MODULE}

test: install-requirements
	@echo "Testing"
	@${PYTHON_ACTIVATE} && python3 -m pytest -s \
	--cov-branch \
	--cov=. \
	--cov-fail-under=70

#DIRECTORIES
${VENV_DIR}:
	@python3 -m venv venv
	@echo "Install requirements"
	@${PYTHON_ACTIVATE} \
	&& pip install -r requirements.txt

#Makefile internals
.NOTPARALLEL:

.PHONY: clean install-requirements format lint test
