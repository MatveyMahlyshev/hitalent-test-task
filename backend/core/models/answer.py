from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from typing import TYPE_CHECKING
import uuid
from datetime import datetime

from .base import Base

if TYPE_CHECKING:
    from .question import Question


class Answer(Base):
    question_id: Mapped[int] = mapped_column(
        ForeignKey(
            "questions.id",
            ondelete="CASCADE",
        )
    )
    user_id: Mapped[str] = mapped_column(
        String,
        default=uuid.uuid4(),
    )
    text: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    question: Mapped["Question"] = relationship(back_populates="answers")
