import asyncio

from .factory import build_app

__version__ = '0.0.0'

loop = asyncio.get_event_loop()
app = build_app(loop)
