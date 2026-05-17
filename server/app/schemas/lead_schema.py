from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator
)

from typing import Optional

from uuid import UUID

import re


def sanitize_text(value: str):

    value = re.sub(r"<.*?>", "", value)
    value = value.strip()

    return value


class LeadBase(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=255
    )

    email: EmailStr

    company: Optional[str] = Field(
        default=None,
        max_length=255
    )

    phone: Optional[str] = Field(
        default=None,
        max_length=50
    )

    service: str = Field(
        ...,
        min_length=2,
        max_length=255
    )

    budget: Optional[str] = Field(
        default=None,
        max_length=100
    )

    message: str = Field(
        ...,
        min_length=10,
        max_length=3000
    )

    source: Optional[str] = None

    @field_validator(
        "name",
        "company",
        "phone",
        "service",
        "budget",
        "message",
        "source"
    )
    @classmethod
    def sanitize_fields(cls, value):

        if value:
            return sanitize_text(value)

        return value


class LeadCreate(LeadBase):
    pass


class LeadResponse(LeadBase):

    id: UUID

    class Config:
        from_attributes = True