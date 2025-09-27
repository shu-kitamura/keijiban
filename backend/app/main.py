from fastapi import APIRouter, FastAPI
from routers import threads, posts

app = FastAPI()

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(threads.router)
api_v1.include_router(posts.router)

app.include_router(api_v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}
