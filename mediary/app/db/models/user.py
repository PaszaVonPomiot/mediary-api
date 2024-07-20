from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from mediary.app.enums import Gender


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str
    gender: Gender
    email: EmailStr
