from fastapi import APIRouter
from pydantic import BaseModel

class Post(BaseModel):
    content: str
    author: str


router = APIRouter(
    prefix="/threads/{thread_id}",
)

@router.get("")
def get_posts(thread_id: str):
    return {
        "posts": [
            {"id": "post1", "content": "Sample Post 1"},
            {"id": "post2", "content": "Sample Post 2"}
        ],
        "thread_id": thread_id
    }

@router.post("/posts")
def create_post(thread_id: str, post: Post):
    return {
        "message": "Post created successfully",
        "thread_id": thread_id,
        "post": post
    }


@router.delete("/posts/{post_id}")
def delete_post(thread_id: str, post_id: str):
    return {
        "message": "Post deleted successfully",
    }
