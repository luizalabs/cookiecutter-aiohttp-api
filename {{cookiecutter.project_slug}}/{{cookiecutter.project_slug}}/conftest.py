import asyncio

import pytest
from aiocache import caches
from simple_settings import settings

from {{cookiecutter.project_slug}} import app as _app


@pytest.fixture(scope='session')
def loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app(loop):
    return _app


@pytest.fixture(autouse=True)
async def client(aiohttp_client, app):
    return await aiohttp_client(app)


@pytest.fixture
async def cache(loop):
    caches.set_config(settings.CACHE)
