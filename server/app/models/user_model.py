import uuid

from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.database.connection import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(500),
        nullable=False
    )

    role = Column(
        String(50),
        default="admin"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )