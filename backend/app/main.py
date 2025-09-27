from fastapi import APIRouter, FastAPI
from sqlmodel import SQLModel, create_engine

from app.routers import threads, posts
import app.models


pg_url = "postgresql://user:password@localhost:5432/dev"
engine = create_engine(pg_url, echo=True, future=True)
SQLModel.metadata.create_all(engine)

app = FastAPI()

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(threads.router)
api_v1.include_router(posts.router)

app.include_router(api_v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}
