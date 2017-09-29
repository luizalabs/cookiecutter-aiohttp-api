import pytest

from {{cookiecutter.project_slug}} import app as _app
from {{cookiecutter.project_slug}} import loop as _loop


@pytest.fixture(scope='session')
def loop():
    yield _loop
    _loop.close()


@pytest.fixture
def app(loop):
    return _app


@pytest.fixture(autouse=True)
def client(test_client, app):
    return app.loop.run_until_complete(test_client(app))
