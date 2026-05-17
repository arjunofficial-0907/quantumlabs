from pydantic import (
    BaseModel,
    EmailStr,
    Field
)


class RegisterSchema(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=255
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6
    )


class LoginSchema(BaseModel):

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6
    )