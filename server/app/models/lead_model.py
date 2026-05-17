import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    Boolean
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.database.connection import Base


class Lead(Base):

    __tablename__ = "leads"

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
    # CLIENT INFO
    # ======================================

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=False,
        index=True
    )

    company = Column(
        String(255),
        nullable=True
    )

    phone = Column(
        String(50),
        nullable=True
    )

    # ======================================
    # PROJECT INFO
    # ======================================

    service = Column(
        String(255),
        nullable=False
    )

    budget = Column(
        String(100),
        nullable=True
    )

    message = Column(
        Text,
        nullable=False
    )

    # ======================================
    # TRACKING
    # ======================================

    source = Column(
        String(255),
        nullable=True
    )

    ip_address = Column(
        String(255),
        nullable=True
    )

    # ======================================
    # STATUS
    # ======================================

    contacted = Column(
        Boolean,
        default=False
    )

    archived = Column(
        Boolean,
        default=False
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