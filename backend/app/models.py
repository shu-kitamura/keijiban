import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel


class ThreadBase(SQLModel):
    title: str
    description: str | None = None
    owner: str

class Thread(ThreadBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

class ThreadCreate(ThreadBase):
    pass

class PostBase(SQLModel):
    content: str
    author: str

class Post(PostBase, table=True):
    thread_id: uuid.UUID = Field(foreign_key="thread.id", nullable=False, index=True)
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

class PostCreate(PostBase):
    pass
