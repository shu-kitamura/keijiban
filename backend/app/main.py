from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app import engine
from app.routers import threads


@asynccontextmanager
async def lifespan(app: FastAPI):
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

@app.get("/health", tags=["Healthcheck"])
async def healthcheck():
    return {"status": "healthy"}
