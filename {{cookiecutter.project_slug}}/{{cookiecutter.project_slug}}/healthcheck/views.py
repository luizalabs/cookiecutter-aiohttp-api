from aiohttp import web


class HealthCheckView(web.View):
    async def get(self):
        redis_health = await self._check_redis()
        return web.json_response({
            'redis': redis_health
        })

    async def _check_redis(self):
        await self.request.app.redis.set('HC', '1')
        redis_health = await self.request.app.redis.get('HC')
        return redis_health == '1'
