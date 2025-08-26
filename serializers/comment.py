# serializers/comment.py

from typing import Optional
from pydantic import BaseModel, Field

class CommentSchema(BaseModel):
  id: Optional[int] = Field(default=None)
  content: str
  tea_id: int

  class Config:
    orm_mode = True
