import json

import pytest
from aiohttp.web import HTTPGatewayTimeout

from {{cookiecutter.project_slug}}.contrib.exceptions import APIException
from {{cookiecutter.project_slug}}.contrib.middlewares import exception_handler_middleware
from {{cookiecutter.project_slug}}.contrib.response import JSONResponse
from {{cookiecutter.project_slug}}.version import __version__

httperror_message = 'Http error message'


async def success_handler(request):
    return JSONResponse(data={'data': 'data'}, status=200)


async def api_exception_handler(request):
    raise APIException()


async def http_error_handler(request):
    raise HTTPGatewayTimeout(reason=httperror_message)


async def unexpected_error_handler(request):
    raise Exception()


class TestVersionMiddleware:

    async def test_version_middleware(self, client):
        async with client.get('/healthcheck/') as response:
            assert response.status == 200
            assert response.headers.get('X-API-Version') == __version__


class TestResponseErrorMiddleware:

    @pytest.fixture
    def request_fixture(self, make_request):
        return make_request(
            method='get',
            url='https://www.magazineluiza.com.br/',
        )

    async def test_returns_the_response_on_success(
        self,
        request_fixture
    ):
        response = await exception_handler_middleware(
            request=request_fixture,
            handler=success_handler
        )

        assert response.status == 200

        content = json.loads(response.text)
        assert content == {'data': 'data'}

    async def test_returns_the_error_data_on_api_exception(
        self,
        request_fixture
    ):
        response = await exception_handler_middleware(
            request=request_fixture,
            handler=api_exception_handler
        )

        assert response.status == APIException.status_code

        content = json.loads(response.text)
        assert content['error_code'] == APIException.error_code
        assert content['error_message'] == APIException.error_message

    async def test_returns_the_error_data_for_httperror(self, request_fixture):
        response = await exception_handler_middleware(
            request=request_fixture,
            handler=http_error_handler
        )

        assert response.status == HTTPGatewayTimeout.status_code
        content = json.loads(response.text)
        assert content['error_code'] == 'unexpected_error'
        assert content['error_message'] == httperror_message

    async def test_supress_exception_and_returns_generic_data(
        self,
        request_fixture
    ):
        response = await exception_handler_middleware(
            request=request_fixture,
            handler=unexpected_error_handler
        )

        assert response.status == 500
        content = json.loads(response.text)
        assert content['error_code'] == 'unexpected_error'
        assert content['error_message'] == 'Internal server error'
