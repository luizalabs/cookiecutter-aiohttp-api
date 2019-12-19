import logging

from aiocache import caches
from aiohttp import web
from simple_settings import settings

logger = logging.getLogger(__name__)


class HealthCheckView(web.View):
    async def get(self):
        return web.json_response(data={'status': 'OK'})


class BaseMonitor:
    name = None

    @classmethod
    async def check(cls):
        try:
            await cls._check()
            return True
        except Exception as e:
            logger.warning(f'Error trying to validate {cls.name}! {e}')
            return False


class BaseRedisMonitor(BaseMonitor):
    key = ''
    value = True
    cache = None

    @classmethod
    async def _check(cls):
        await cls.cache.set(cls.key, cls.value, settings.SECONDS * 10)
        assert bool(await cls.cache.get(cls.key)) is True


class RedisMonitor(BaseRedisMonitor):
    name = 'redis'
    key = 'redis_monitor'
    cache = caches.get('default')


class MonitorView(web.View):

    VALIDATOR_CLASSES = [RedisMonitor]

    async def get(self):
        data = {v.name: await v.check() for v in self.VALIDATOR_CLASSES}
        status = 200 if all(data.values()) else 500

        return web.json_response(
            data=data,
            status=status
        )
