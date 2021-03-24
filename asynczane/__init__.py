from asyncio import AbstractEventLoop, get_event_loop
from io import BytesIO

from aiohttp import ClientSession

from .errors import Forbidden, InternalServerError

__version__ = "1.0"
__author__ = "ppotatoo"


class ZaneClient:
    __slots__ = ('default_headers', 'session', 'base_url')

    def __init__(self, token, session: ClientSession = None, loop: AbstractEventLoop = None) -> None:
        self.default_headers = {
            "User-agent": "asynczane {}".format(__version__),
            "Authorization": token.strip()
        }
        self.session = session or ClientSession(headers=self.default_headers, loop=loop or get_event_loop())
        self.base_url = "https://zaneapi.com/api/"

    async def do_zane(self, endpoint: str, params: dict) -> BytesIO:
        async with self.session.get(self.base_url + endpoint, params=params) as resp:
            if resp.status == 403:
                raise Forbidden("Zane API returned a 403 status.")
            if resp.status == 521:
                raise InternalServerError("Zane API returned a 521 status.")
            image = await resp.read()

        return BytesIO(image)

    async def magic(self, url: str, magnitude: float = 0.6) -> BytesIO:
        params = {"url": url, "magnitude": magnitude}
        await self.do_zane('magic', params)

    async def floor(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('floor', params)

    async def braille(self, url: str) -> str:
        params = {"url": url}
        async with self.session.get(self.base_url + "braille", params=params) as resp:
            if resp.status == 403:
                raise Forbidden("Zane API returned a 403 status.")
            if resp.status == 521:
                raise InternalServerError("Zane API returned a 521 status.")
            data = await resp.text()

        return data

    async def deepfry(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('deepfry', params)

    async def dots(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('dots', params)

    async def jpeg(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('jpeg', params)

    async def spread(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('spread', params)

    async def cube(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('cube', params)

    async def sort(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('sort', params)

    async def palette(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('palette', params)

    async def invert(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('invert', params)

    async def posterize(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('posterize', params)

    async def grayscale(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('grayscale', params)

    async def swirl(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('swirl', params)

    async def sobel(self, url: str) -> BytesIO:
        params = {"url": url}
        return await self.do_zane('sobel', params)

    async def close(self):
        await self.session.close()
