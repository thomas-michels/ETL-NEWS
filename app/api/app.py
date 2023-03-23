from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.configs import get_environment

_env = get_environment()

app = FastAPI(title=_env.APPLICATION_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
