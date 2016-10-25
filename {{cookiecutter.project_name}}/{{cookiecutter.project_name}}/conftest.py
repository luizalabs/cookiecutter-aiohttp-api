import pytest

from {{cookiecutter.project_name}}.app import build_app, load_plugins


@pytest.fixture
def app(loop):
    return build_app(loop=loop)


@pytest.fixture
def client(test_client, app):
    return app.loop.run_until_complete(test_client(app))


@pytest.fixture(autouse=True)
def register_plugins(app):
    app.loop.run_until_complete(load_plugins(app))
