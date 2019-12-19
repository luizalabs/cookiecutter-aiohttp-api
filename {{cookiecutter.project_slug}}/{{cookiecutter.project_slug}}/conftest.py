import asyncio

import pytest
from aiocache import caches
from aiohttp.client_reqrep import ClientRequest
from simple_settings import settings
from yarl import URL

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


@pytest.fixture
async def make_request(loop):
    """
    Inspired on aiohttp make-request function
    https://github.com/aio-libs/aiohttp/blob/master/tests/test_client_request.py#L24
    """
    request = None

    def maker(method, url, *args, **kwargs):
        nonlocal request
        request = ClientRequest(method, URL(url), *args, loop=loop, **kwargs)
        return request

    yield maker
    if request is not None:
        await request.close()
