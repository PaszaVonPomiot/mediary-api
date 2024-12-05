from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from mediary.app.enums import Gender


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, max_length=15)
    gender: Gender
    email: EmailStr = Field(min_length=7, max_length=100)
    is_active: bool = True
