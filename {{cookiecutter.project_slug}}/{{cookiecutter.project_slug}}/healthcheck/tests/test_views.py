from unittest import mock

import pytest


class TestHealthCheck:

    @pytest.fixture
    def url(self):
        return '/healthcheck/'

    async def test_should_return_status_ok(self, client, url):
        async with client.get(url) as response:
            assert response.status == 200
            content = await response.json()

        assert content == {'status': 'OK'}


class TestMonitor:

    @pytest.fixture
    def url(self):
        return '/monitor/'

    async def test_should_return_cache_ok(self, client, url):
        async with client.get(url) as response:
            assert response.status == 200
            content = await response.json()

        assert content == {'redis': True}

    async def test_should_return_cache_off_if_cache_check_fail(
        self,
        client,
        url
    ):
        cache_mock = mock.Mock()
        cache_mock.set.side_effect = ValueError('some error')

        with mock.patch(
            '{{cookiecutter.project_slug}}.healthcheck.views.RedisMonitor._check'
        ) as mock_caches:
            mock_caches.get.return_value = cache_mock
            async with client.get(url) as response:
                assert response.status == 500
                content = await response.json()

        assert content == {'redis': False}
