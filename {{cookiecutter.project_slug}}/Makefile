run:
	@gunicorn {{cookiecutter.project_slug}}:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.development

requirements-test:
	@pip install -r requirements/test.txt

requirements-dev:
	@pip install -r requirements/dev.txt

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

release-patch: ## Create patch release
	SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test bump2version patch --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version patch

release-minor: ## Create minor release
	SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test bump2version minor --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version minor

release-major: ## Create major release
	SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.test bump2version major --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 towncrier --yes --version
	git commit -am 'Update CHANGELOG'
	bump2version major
