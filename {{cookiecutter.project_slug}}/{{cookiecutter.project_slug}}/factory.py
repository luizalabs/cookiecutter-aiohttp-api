from aiohttp import web
from asyncio_redis import Pool as RedisPool
from simple_settings import settings

from .healthcheck.routes import register_routes as register_heathcheck_routes
from .middlewares.version import version_middleware


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())
    app.on_startup.append(load_plugins)
    app.on_cleanup.append(cleanup_plugins)
    register_routes(app)
    return app


def register_routes(app):
    register_heathcheck_routes(app)


def get_middlewares():
    return [version_middleware]


async def load_plugins(app):
    redis = await RedisPool.create(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        poolsize=settings.REDIS_POOLSIZE,
        loop=app.loop
    )
    app.redis = redis


async def cleanup_plugins(app):
    app.redis.close()
