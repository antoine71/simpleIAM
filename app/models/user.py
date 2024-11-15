from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import UUID, Boolean, Column, DateTime, String

from dependencies.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
        index=True,
        nullable=False,
    )
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    def __repr__(self):
        return f"<email='{self.email}', is_active={self.is_active})>"
