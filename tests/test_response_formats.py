import pytest
import allure
from pydantic import BaseModel, Field


class JsonSlideshow(BaseModel):
    slideshow: dict = Field(...)


@allure.epic("httpbin.org")
@allure.feature("Response Formats")
@allure.story("JSON Response")
@pytest.mark.asyncio
async def test_json_format(client):
    with allure.step("Send GET /json request"):
        resp = await client.get("/json")

    with allure.step("Validate HTTP status and Content-Type header"):
        assert resp.status_code == 200
        assert resp.headers["Content-Type"].startswith("application/json")

    with allure.step("Validate response body schema"):
        data = JsonSlideshow.model_validate(resp.json())
        assert "slideshow" in data.model_dump()


@allure.epic("httpbin.org")
@allure.feature("Response Formats")
@allure.story("HTML Response")
@pytest.mark.asyncio
async def test_html_format(client):
    with allure.step("Send GET /html request"):
        resp = await client.get("/html")

    with allure.step("Check response"):
        assert resp.status_code == 200
        content_type = resp.headers.get("Content-Type", "")
        assert "text/html" in content_type
        assert "<html>" in resp.text.lower()


@allure.epic("httpbin.org")
@allure.feature("Response Formats")
@allure.story("PNG Image Response")
@pytest.mark.asyncio
async def test_image_png(client):
    with allure.step("Send GET /image/png request"):
        resp = await client.get("/image/png")

    with allure.step("Validate byte payload and Content-Type"):
        assert resp.status_code == 200
        assert resp.headers.get("Content-Type") == "image/png"
        assert isinstance(resp.content, bytes)
        assert len(resp.content) > 0
