import uuid

from sqlalchemy import (
    Column,
    String,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.database.connection import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    action = Column(
        String(255),
        nullable=False
    )

    user_email = Column(
        String(255),
        nullable=False
    )

    entity = Column(
        String(255),
        nullable=False
    )

    entity_id = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )