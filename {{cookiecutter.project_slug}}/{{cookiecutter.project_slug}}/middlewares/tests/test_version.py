from {{cookiecutter.project_slug}}.version import __version__


class TestVersion:

    async def test_version_middleware(self, app, client):
        response = await client.get('/healthcheck/')
        assert response.status == 200
        assert response.headers.get('X-API-Version') == __version__
