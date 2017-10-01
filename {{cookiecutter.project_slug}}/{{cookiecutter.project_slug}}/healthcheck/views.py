from aiohttp import web


class HealthCheckView(web.View):
    async def get(self):
        {% if cookiecutter.use_redis == 'y' -%}
        redis_health = await self._check_redis()
        return web.json_response({
            'redis': redis_health
        })
        {% else -%}
        return web.json_response({'status': 'OK'})
        {%- endif %}

    {% if cookiecutter.use_redis == 'y' -%}
    async def _check_redis(self):
        await self.request.app.redis.set('HC', '1')
        redis_health = await self.request.app.redis.get('HC')
        return redis_health == '1'
    {%- endif %}
