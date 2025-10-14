import uuid

from fastapi import APIRouter, Query
from sqlmodel import select

from app import sessionDep
from app.models import Thread, ThreadCreate
from app.routers.posts import router as posts_router

router = APIRouter(
    prefix="/threads",
)

@router.get("/search")
def search_threads(
        session: sessionDep,
        q: str = Query(
            title="Search Query",
            description="The search query for threads",
            min_length=1,
            max_length=255
        ),
    ) -> list[Thread]:

    statement = select(Thread).where(Thread.title.contains(q))
    results = session.exec(statement).all()
    return results

@router.get("/{thread_id}")
def get_thread(thread_id: uuid.UUID, session: sessionDep) -> Thread | None:
    thread = session.get(Thread, thread_id)
    return thread

@router.post("/")
def create_thread(thread: ThreadCreate, session: sessionDep) -> Thread:
    db_thread = Thread.model_validate(thread)
    session.add(db_thread)
    session.commit()
    session.refresh(db_thread)
    return db_thread

router.include_router(posts_router)
