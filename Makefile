MANAGER     = uv
EXEC        = python3
PACKAGE     = src

install:
	${MANAGER} sync

run:
	${MANAGER} run ${EXEC} main.py