from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from uuid import UUID
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    description: str | None = None
    priority: Literal["high", "medium", "low"]

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    is_completed: bool
    created_at: str


'''
{
    "id": "6a89a82c197993b55a2322fc",
    "title": "Adipisicing occaecat excepteur incididunt elit.",
    "description": None,
    "is_completed": True,
    "priority": "low",
    "created_at": "Thu Apr 01 1982 15:07:58 GMT+0530 (India Standard Time)"
}
'''