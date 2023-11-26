install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 metroparser

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl