from fastapi import FastAPI
from .routers import root


app = FastAPI()


app.include_router(root.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}