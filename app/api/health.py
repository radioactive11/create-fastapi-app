from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}


@health_router.post("/health")
async def health_check_post():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
