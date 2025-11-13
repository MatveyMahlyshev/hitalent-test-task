from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, DateTime
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:

    from .answer import Answer


class Question(Base):
    text: Mapped[str] = mapped_column(
        String(5),
        unique=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    answers: Mapped[list["Answer"]] = relationship(
        back_populates="question", cascade="all, delete-orphan"
    )
