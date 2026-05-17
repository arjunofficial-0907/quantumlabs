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


# ==========================================
# HELPERS
# ==========================================

def sanitize_text(value: str):

    value = re.sub(r"<.*?>", "", value)
    value = value.strip()

    return value


# ==========================================
# BASE
# ==========================================

class ProjectBase(BaseModel):

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

    category: str = Field(
        ...,
        min_length=2,
        max_length=100
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

    cover_image: Optional[HttpUrl] = None

    gallery_images: Optional[List[HttpUrl]] = []

    live_url: Optional[HttpUrl] = None

    github_url: Optional[HttpUrl] = None

    technologies: List[str]

    featured: bool = False

    published: bool = True

    meta_title: Optional[str] = None

    meta_description: Optional[str] = None

    # ======================================
    # SANITIZATION
    # ======================================

    @field_validator(
        "title",
        "slug",
        "category",
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


# ==========================================
# CREATE
# ==========================================

class ProjectCreate(ProjectBase):
    pass


# ==========================================
# UPDATE
# ==========================================

class ProjectUpdate(ProjectBase):
    pass


# ==========================================
# RESPONSE
# ==========================================

class ProjectResponse(ProjectBase):

    id: UUID

    class Config:
        from_attributes = True