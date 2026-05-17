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


class RefreshToken(Base):

    __tablename__ = "refresh_tokens"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        String(255),
        nullable=False
    )

    token = Column(
        String(1000),
        nullable=False
    )

    revoked = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )