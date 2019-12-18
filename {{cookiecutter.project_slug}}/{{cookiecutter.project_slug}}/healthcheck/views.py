import logging

from aiocache import caches
from aiohttp import web

logger = logging.getLogger(__name__)


class HealthCheckView(web.View):
    async def get(self):
        return web.json_response(data={'status': 'OK'})


class MonitorView(web.View):
    async def get(self):
        status, msg = await self._cache_status()
        return web.json_response(
            data={'cache': msg},
            status=200 if status is True else 500
        )

    async def _cache_status(self):
        cache = caches.get('default')
        try:
            await cache.set('check', True)
            value = await cache.get('check')
        except Exception as e:
            logger.error(f'Checking cache status: {e}')
            return False, str(e)

        status = value is True
        return status, 'OK' if status else 'UNKNOW ERROR'
