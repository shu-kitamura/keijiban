import uuid

from fastapi import APIRouter
from sqlmodel import select, delete

from app.models import PostCreate, Post
from app import sessionDep

router = APIRouter(
    prefix="/{thread_id}/posts",
)

@router.get("/")
def get_posts(thread_id: str, session: sessionDep) -> list[Post]:
    statement = select(Post).where(Post.thread_id == thread_id)
    posts = session.exec(statement).all()
    return posts

@router.post("/")
def create_post(thread_id: uuid.UUID, post_create: PostCreate, session: sessionDep) -> Post:
    post = Post(**post_create.model_dump(), thread_id=thread_id)
    db_post = Post.model_validate(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.delete("/{post_id}")
def delete_post(post_id: str, session: sessionDep):
    statement = delete(Post).where(Post.id == post_id)
    session.exec(statement)
    session.commit()
    return {"message": "Post deleted successfully"}
