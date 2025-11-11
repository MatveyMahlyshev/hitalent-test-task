from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import String, DateTime

from .base import Base


class Question(Base):
    text: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
