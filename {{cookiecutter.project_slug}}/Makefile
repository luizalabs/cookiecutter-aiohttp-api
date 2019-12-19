run:
	@gunicorn {{cookiecutter.project_slug}}:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.development

requirements-test:
	@pip install -r requirements/test.txt

test:
	@SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test py.test {{cookiecutter.project_slug}}

test-matching:
	@SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test pytest -rxs -k${Q} {{cookiecutter.project_slug}}

test-coverage:
	@SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test pytest --cov={{cookiecutter.project_slug}} {{cookiecutter.project_slug}} --cov-report term-missing

lint:
	@flake8
	@isort --check

detect-outdated-dependencies:
	@sh -c 'output=$$(pip list --outdated); echo "$$output"; test -z "$$output"'
