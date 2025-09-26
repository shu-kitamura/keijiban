from fastapi import APIRouter, Query

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
def create_post(thread_id: str, post: dict):
    return {
        "message": "Post created successfully",
        "thread_id": thread_id,
        "post": post
    }
