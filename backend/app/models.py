from datetime import datetime
import uuid

from sqlmodel import Field, SQLModel

class ThreadBase(SQLModel):
    title: str
    description: str | None = None
    owner: str

class ThreadCreate(ThreadBase):
    pass

class Thread(ThreadBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)

class PostBase(SQLModel):
    thread_id: uuid.UUID = Field(foreign_key="thread.id", nullable=False, index=True)
    content: str
    author: str

class PostCreate(PostBase):
    pass

class Post(PostBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
