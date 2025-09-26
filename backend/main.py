from fastapi import FastAPI
from routers import threads, posts

app = FastAPI()

app.include_router(
    threads.router,
    prefix="/api/v1",
)
app.include_router(
    posts.router,
    prefix="/api/v1",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
