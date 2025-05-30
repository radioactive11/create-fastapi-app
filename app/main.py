from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.context_hijacker import ContextHijackerMiddleware
from fastapi.middleware import Middleware

app = FastAPI()
#to add debugging friendly logging use below app definition
# app = FastAPI(middleware=[Middleware(ContextHijackerMiddleware)])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    APIRouter(),
    prefix="/api",
    tags=["api"],
)
