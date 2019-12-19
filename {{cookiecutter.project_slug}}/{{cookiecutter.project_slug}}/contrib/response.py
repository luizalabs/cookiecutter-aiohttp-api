import json

from aiohttp import web


class JSONResponse(web.Response):

    def __init__(self, *, data=None, status=200):
        if data and not isinstance(data, str):
            data = json.dumps(data)

        super().__init__(
            text=data,
            status=status,
            content_type='application/json'
        )
