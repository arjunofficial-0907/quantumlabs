import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    DateTime,
    JSON
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.database.connection import Base


class Project(Base):

    __tablename__ = "projects"

    # ======================================
    # PRIMARY KEY
    # ======================================

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    # ======================================
    # BASIC INFO
    # ======================================

    title = Column(
        String(255),
        nullable=False,
        index=True
    )

    slug = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    category = Column(
        String(100),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    short_description = Column(
        String(500),
        nullable=True
    )

    # ======================================
    # MEDIA
    # ======================================

    cover_image = Column(
        String(1000),
        nullable=True
    )

    gallery_images = Column(
        JSON,
        nullable=True,
        default=[]
    )

    # ======================================
    # LINKS
    # ======================================

    live_url = Column(
        String(1000),
        nullable=True
    )

    github_url = Column(
        String(1000),
        nullable=True
    )

    # ======================================
    # STACK
    # ======================================

    technologies = Column(
        JSON,
        nullable=False,
        default=[]
    )

    # ======================================
    # STATUS
    # ======================================

    featured = Column(
        Boolean,
        default=False
    )

    published = Column(
        Boolean,
        default=True
    )

    # ======================================
    # SEO
    # ======================================

    meta_title = Column(
        String(255),
        nullable=True
    )

    meta_description = Column(
        String(500),
        nullable=True
    )

    # ======================================
    # TIMESTAMPS
    # ======================================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now()
    )