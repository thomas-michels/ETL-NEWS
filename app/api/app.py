from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.configs import get_environment
from app.api.routes import router
import uvicorn

_env = get_environment()

app = FastAPI(title=_env.APPLICATION_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

def run_api():
    uvicorn.run(
        app=app,
        host=_env.APPLICATION_HOST,
        port=_env.APPLICATION_PORT
    )
