from typing import Union

from fastapi import APIRouter, Query
from pydantic import BaseModel

class Thread(BaseModel):
    title: str
    abstract: Union[str, None] = None
    owner: str


router = APIRouter(
    prefix="/threads",
)

@router.get("/search")
def search_threads(
        q: str = Query(
            title="Search Query",
            description="The search query for threads",
            min_length=1,
            max_length=10
        )
    ):
    return {
        "threads": [
            {"id": "thread1", "name": "Sample Thread 1"},
            {"id": "thread2", "name": "Sample Thread 2"}
        ],
        "query": q
    }

@router.post("/")
def create_thread(thread: Thread):
    return {
        "message": "Thread created successfully",
        "thread": thread
    }