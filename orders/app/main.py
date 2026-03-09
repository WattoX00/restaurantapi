# start the uvicorn server in the background -> start test page for orders (waiters)

from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routers.orders_routers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8002,
        reload=True
    )
