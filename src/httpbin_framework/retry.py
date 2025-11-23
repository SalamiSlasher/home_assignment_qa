import asyncio
import functools
from collections.abc import Awaitable, Callable
from typing import TypeVar, ParamSpec

from httpx import HTTPError

from httpbin_framework.logger import logger

T = TypeVar("T")
P = ParamSpec("P")


def retry(
    attempts: int,
    backoff: float,
    retriable_exceptions: tuple[type[BaseException], ...] = (HTTPError,),
) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]:
    def decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            last_exc: BaseException | None = None

            for attempt in range(1, attempts + 1):
                try:
                    logger.info(
                        f"[retry] attempt={attempt}/{attempts} func={func.__name__}"
                    )
                    return await func(*args, **kwargs)

                except retriable_exceptions as exc:
                    last_exc = exc
                    logger.warning(
                        f"[retry] attempt {attempt} failed with {exc!r}, "
                        f"backoff={backoff}s"
                    )
                    if attempt == attempts:
                        logger.error("[retry] all attempts exhausted, raising last error")
                        raise
                    await asyncio.sleep(backoff)

            if last_exc:
                raise last_exc
            raise RuntimeError("retry wrapper finished without result or exception")

        return wrapper

    return decorator
