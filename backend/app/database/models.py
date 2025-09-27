from datetime import datetime
import uuid

from sqlmodel import Field, SQLModel

class Thread(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(nullable=False, max_length=255)
    description: str | None = Field(default=None)
    owner: str = Field(nullable=False, max_length=100)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

class Post(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    thread_id: uuid.UUID = Field(foreign_key="thread.id", nullable=False)
    content: str = Field(nullable=False)
    author: str = Field(nullable=False, max_length=100)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
