MANAGER     = uv
EXEC        = python3
PACKAGE     = src

install:
	${MANAGER} sync

run:
	${MANAGER} run ${EXEC} main.py

make lint:
	flake8 *.py
	mypy .