import pytest


class TestHealthCheck:
    {% if cookiecutter.use_redis == 'y' -%}
    @pytest.fixture
    def close_redis(self, app):
        app.redis.close()

        yield

        for c in app.redis._connections:
            app.loop.run_until_complete(c._reconnect())
    {%- endif %}

    @pytest.fixture
    def route(self):
        return '/healthcheck/'

    async def test_healthcheck_success(self, client, route):
        response = await client.get(route)
        assert response.status == 200

        content = await response.json()
        {% if cookiecutter.use_redis == 'y' -%}
        assert content['redis'] is True
        {% else -%}
        assert content['status'] == 'OK'
        {%- endif %}

    {% if cookiecutter.use_redis == 'y' -%}
    async def test_healthcheck_fail(self, client, close_redis, route):
        response = await client.get(route)
        assert response.status == 500
    {%- endif %}
