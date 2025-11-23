from faker import Faker
from pydantic import BaseModel, EmailStr, Field

fake = Faker()


class FakeUser(BaseModel):
    name: str = Field(default_factory=fake.name)
    email: EmailStr = Field(default_factory=fake.email)
    age: int = Field(default_factory=lambda: fake.random_int(min=18, max=70))


def fake_user_dict() -> dict:
    return FakeUser().model_dump()


def fake_headers() -> dict[str, str]:
    return {
        "X-Correlation-Id": fake.uuid4(),
    }



def fake_query() -> dict[str, str]:
    return {
        "search": fake.word(),
        "page": str(fake.random_int(min=1, max=10)),
    }
