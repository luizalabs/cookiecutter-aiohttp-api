from {{cookiecutter.project_slug}}.version import __version__


async def version_middleware(app, handler):
    async def middleware(request):
        response = await handler(request)
        response.headers['X-API-Version'] = __version__
        return response
    return middleware
