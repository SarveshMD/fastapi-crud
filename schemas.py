from pydantic import BaseModel, ConfigDict, Field
import uuid
from datetime import datetime

from models import PriorityEnum

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = None
    priority: PriorityEnum = PriorityEnum.LOW

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    is_completed: bool
    created_at: datetime

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: PriorityEnum | None = None
    is_completed: bool | None = None

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