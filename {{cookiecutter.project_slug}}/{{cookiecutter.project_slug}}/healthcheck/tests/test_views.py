import pytest


class TestHealthCheck:

    @pytest.fixture
    def close_redis(self, app):
        app.redis.close()

        yield

        for c in app.redis._connections:
            app.loop.run_until_complete(c._reconnect())

    async def test_healthcheck_success(self, client):
        response = await client.get('/healthcheck/')
        assert response.status == 200

        content = await response.json()
        assert content['redis'] is True

    async def test_healthcheck_fail(self, client, close_redis):
        response = await client.get('/healthcheck/')
        assert response.status == 500
