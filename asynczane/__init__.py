from io import BytesIO
from aiohttp import ClientSession
from asyncio import AbstractEventLoop, get_event_loop

from .errors import Forbidden, InternalServerError


__version__ = "0.0.1"
__author__ = "ppotatoo"

class ZaneClient():
    __slots__ = ('default_headers', 'session', 'base_url')

    def __init__(self, token, session: ClientSession=None, loop: AbstractEventLoop=None) -> None:
        self.default_headers = {
            "User-agent": "asynczane {}".format(__version__),
            "Authorization": token.strip()
        }
        self.session = session or ClientSession(headers=self.default_headers, loop=loop or get_event_loop())
        self.base_url = "https://zaneapi.com/api/"

    async def run_endpoint(self, endpoint: str, params: dict):
        async with self.session.get(self.base_url + endpoint, params=params) as resp:
            if resp.status == 403:
                raise Forbidden("Zane API returned a 403 status.")
            if resp.status == 521:
                raise InternalServerError("Zane API returned a 521 status.")
            image = await resp.read()

        return BytesIO(image)

    async def close(self):
        await self.session.close()


