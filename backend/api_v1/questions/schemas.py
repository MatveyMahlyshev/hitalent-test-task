from pydantic import BaseModel, ConfigDict
from datetime import datetime


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str


class Question(QuestionBase):
    id: int | None
    created_at: datetime | None


class QuestionCreate(QuestionBase):
    pass
