run:
	@gunicorn {{cookiecutter.project_slug}}:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.development

requirements-test:
	@pip install -r requirements/test.txt

test:
	@SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test py.test {{cookiecutter.project_slug}}

check:
	@flake8
	@isort --check
