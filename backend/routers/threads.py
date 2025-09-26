from fastapi import APIRouter, Query

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
