import pytest
import time
import allure

from httpbin_framework.models import UUIDResponse


@allure.epic("httpbin.org")
@allure.feature("Dynamic Data")
@allure.story("UUID Generation")
@pytest.mark.asyncio
async def test_uuid_changes_between_requests(client):
    with allure.step("Send first GET /uuid"):
        resp1 = await client.get("/uuid")

    with allure.step("Send second GET /uuid"):
        resp2 = await client.get("/uuid")

    uuid1 = UUIDResponse.model_validate(resp1.json()).uuid
    uuid2 = UUIDResponse.model_validate(resp2.json()).uuid

    with allure.step("Validate UUIDs are different"):
        assert uuid1 != uuid2


@allure.epic("httpbin.org")
@allure.feature("Dynamic Data")
@allure.story("Delayed Response")
@pytest.mark.asyncio
async def test_delay_endpoint(client):
    with allure.step("Measure execution time for GET /delay/2"):
        start = time.perf_counter()
        resp = await client.get("/delay/2")
        elapsed = time.perf_counter() - start

    with allure.step("Validate delay was respected"):
        assert resp.status_code == 200
        assert elapsed >= 2.0
