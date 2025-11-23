from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class UUIDResponse(BaseModel):
    uuid: UUID


class GetArgs(BaseModel):
    args: dict[str, str] = Field(default_factory=dict)


class PostJson(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    json_body: dict | None = Field(default=None, alias="json")


class HeadersResponse(BaseModel):
    headers: dict[str, str]
