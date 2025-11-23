import httpx

from config.settings import settings
from httpbin_framework.logger import logger
from httpbin_framework.retry import retry


class HttpClient:
    def __init__(self) -> None:
        timeout = httpx.Timeout(settings.timeout)
        self._client = httpx.AsyncClient(
            base_url=settings.base_url,
            timeout=timeout,
            follow_redirects=True,
        )

    @retry(
        attempts=settings.retries,
        backoff=settings.retry_backoff,
    )
    async def get(self, url: str, **kwargs) -> httpx.Response:
        logger.info(f"GET {url} {kwargs}")
        return await self._client.get(url, **kwargs)

    @retry(
        attempts=settings.retries,
        backoff=settings.retry_backoff,
    )
    async def post(self, url: str, **kwargs) -> httpx.Response:
        logger.info(f"POST {url} {kwargs}")
        return await self._client.post(url, **kwargs)

    async def aclose(self) -> None:
        await self._client.aclose()
