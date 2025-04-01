from api.health import health_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["health"])
