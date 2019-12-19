import logging

from aiohttp import web

from {{cookiecutter.project_slug}}.contrib.exceptions import APIException
from {{cookiecutter.project_slug}}.contrib.response import JSONResponse

logger = logging.getLogger(__name__)


@web.middleware
async def exception_handler_middleware(request, handler):

    try:
        return await handler(request)

    except APIException as exc:
        return JSONResponse(data=exc.as_dict(), status=exc.status_code)

    except web.HTTPError as exc:
        logger.exception(
            f'Unknow error for request {request.url.path}. Exception: {exc}'
        )
        data = {'error_code': 'unexpected_error', 'error_message': exc.reason}
        return JSONResponse(data=data, status=exc.status_code)

    except Exception as exc:
        logger.exception(
            f'Unknow error for request {request.url.path}. Exception: {exc}'
        )
        data = {
            'error_code': 'unexpected_error',
            'error_message': 'Internal server error'
        }
        return JSONResponse(data=data, status=500)
