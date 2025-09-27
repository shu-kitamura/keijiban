from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from sqlmodel import SQLModel

from app.routers import threads, posts
from app import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    import app.models
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(threads.router)
api_v1.include_router(posts.router)

app.include_router(api_v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}
