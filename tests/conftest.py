from typing import Any, AsyncGenerator

import pytest
import pytest_asyncio
from faker import Faker
from httpbin_framework.client import HttpClient


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[HttpClient, Any]:
    http_client = HttpClient()
    try:
        yield http_client
    finally:
        await http_client.aclose()
