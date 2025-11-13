from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str = Field(min_length=5)


class Question(QuestionBase):
    id: int | None
    created_at: datetime | None


class QuestionCreate(QuestionBase):
    pass
