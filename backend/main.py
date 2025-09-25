from typing import Union

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    content: str
    author: Union[str, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/threads/search")
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

@app.get("/api/v1/threads/{thread_id}")
def get_posts(thread_id: str):
    return {
        "posts": [
            {"id": "post1", "content": "Sample Post 1"},
            {"id": "post2", "content": "Sample Post 2"}
        ],
        "thread_id": thread_id
    }

@app.post("/api/v1/threads/{thread_id}/posts")
def create_post(thread_id: str, post: Post):
    return {
        "message": "Post created successfully",
        "thread_id": thread_id,
        "post": post
    }
