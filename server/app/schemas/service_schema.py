from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    field_validator
)

from typing import Optional
from typing import List

from uuid import UUID

import re


def sanitize_text(value: str):

    value = re.sub(r"<.*?>", "", value)
    value = value.strip()

    return value


class ServiceBase(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    slug: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    description: str = Field(
        ...,
        min_length=20,
        max_length=5000
    )

    short_description: Optional[str] = Field(
        default=None,
        max_length=500
    )

    icon: Optional[str] = None

    cover_image: Optional[HttpUrl] = None

    features: List[str]

    starting_price: Optional[str] = None

    featured: bool = False

    published: bool = True

    meta_title: Optional[str] = None

    meta_description: Optional[str] = None

    @field_validator(
        "title",
        "slug",
        "description",
        "short_description",
        "meta_title",
        "meta_description"
    )
    @classmethod
    def sanitize_fields(cls, value):

        if value:
            return sanitize_text(value)

        return value


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    pass


class ServiceResponse(ServiceBase):

    id: UUID

    class Config:
        from_attributes = True