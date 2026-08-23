import enum
import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Enum, String
from sqlalchemy.orm import mapped_column, Mapped

from database import Base

class PriorityEnum(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    priority: Mapped[PriorityEnum] = mapped_column(
        Enum(PriorityEnum),
        default=PriorityEnum.LOW,
        name='priority_enum'
    )
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self) -> str:
        return f"<Task(title='{self.title}', priority='{self.priority}', completed='{self.is_completed}')"


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