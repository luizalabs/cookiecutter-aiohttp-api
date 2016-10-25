run:
	@gunicorn {{cookiecutter.project_name}}:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS={{cookiecutter.project_name}}.settings.development

requirements-test:
	@pip install -r requirements/test.txt

test:
	@SIMPLE_SETTINGS={{cookiecutter.project_name}}.settings.test py.test {{cookiecutter.project_name}}

check:
	@flake8
	@isort --check
