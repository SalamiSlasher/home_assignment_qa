import pytest
import allure

from httpbin_framework.data.generators import (
    fake_headers,
    fake_query,
    fake_user_dict,
)
from httpbin_framework.models import GetArgs, PostJson, HeadersResponse


@allure.epic("httpbin.org")
@allure.feature("Request Inspection")
@allure.story("Query Parameters Echo")
@pytest.mark.asyncio
async def test_get_inspection_query(client):
    params = fake_query()

    with allure.step("Send GET /get with query params"):
        resp = await client.get("/get", params=params)

    with allure.step("Validate response"):
        assert resp.status_code == 200
        parsed = GetArgs.model_validate(resp.json())
        assert parsed.args == params


@allure.epic("httpbin.org")
@allure.feature("Request Inspection")
@allure.story("JSON Body Echo")
@pytest.mark.asyncio
async def test_post_json_echo(client):
    payload = fake_user_dict()

    with allure.step("Send POST /post with JSON body"):
        resp = await client.post("/post", json=payload)

    with allure.step("Validate JSON echo"):
        assert resp.status_code == 200
        parsed = PostJson.model_validate(resp.json())
        assert parsed.json_body == payload


@allure.epic("httpbin.org")
@allure.feature("Request Inspection")
@allure.story("Headers Echo")
@pytest.mark.asyncio
async def test_custom_headers_echo(client):
    headers = fake_headers()

    with allure.step("Send GET /headers with custom headers"):
        resp = await client.get("/headers", headers=headers)

    with allure.step("Validate echoed headers"):
        assert resp.status_code == 200
        parsed = HeadersResponse.model_validate(resp.json())

        for k, v in headers.items():
            assert parsed.headers.get(k) == v
