import time
from typing import Any, Callable, TypeVar
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routers import auth, users
from .config import settings
from .utils.logger import logger

description = f"""
This is a portfolio app for my projects
"""

app = FastAPI(
    title="My Portfolio App",
    description=description,
    version="0.1.0",
    root_path=settings.root_path
)

origins = [
    settings.client_origin,
]
# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=origins
)

# Include the routers
# app.include_router(
#     auth.router, 
#     prefix="/v1/auth",
#     tags=["Authentication"]
# )
app.include_router(
    users.router, 
    prefix="/v1/users",
    tags=["Users"]
)

F = TypeVar("F", bound=Callable[..., Any])

@app.middleware("http")
async def process_time_log_middleware(request:Request, call_next: F) -> Response:
    start_time = time.time()
    response = await call_next(request)
    process_time = str(round(time.time() - start_time, 3))
    response.headers["X-Process-Time"] = process_time

    logger.info(
        "method=%s path=%s status_code=%s process_time=%s",
        request.method,
        request.url.path,
        response.status_code,
        process_time
    )

    return response

@app.get("/", tags=["Root"], summary="Checks API status")
async def read_root():
    return JSONResponse(content={
        "status": "running!",
        "message": "Welcome to the Portfolio API"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )