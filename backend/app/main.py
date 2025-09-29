from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.routers import threads, posts
from app import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    import app.models
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(threads.router)

app.include_router(api_v1)

@app.get("/")
async def root():
    return {"message": "Hello World"}
