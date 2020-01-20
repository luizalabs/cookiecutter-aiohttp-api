from aiocache import caches
from aiohttp import web
from aiohttp_swagger import setup_swagger
from simple_settings import settings

from .healthcheck.routes import register_routes as register_heathcheck_routes
from .contrib.middlewares import (
    exception_handler_middleware,
    version_middleware
)


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())

    app.on_startup.append(start_plugins)
    app.on_cleanup.append(stop_plugins)

    setup_swagger(
        app,
        swagger_url='/docs',
        swagger_from_file="docs/swagger.yaml"
    )

    register_routes(app)

    return app


def register_routes(app):
    register_heathcheck_routes(app)


def get_middlewares():
    return [version_middleware, exception_handler_middleware]


async def start_plugins(app):
    caches.set_config(settings.CACHE)


async def stop_plugins(app):
    cache_config = caches.get_config()
    for cache_name in cache_config:
        await caches.get(cache_name).close()
