from fastapi import APIRouter
from api.v1.endpoints import filter, gemini

api_router = APIRouter()
api_router.include_router(filter.router, prefix="/api/v1", tags=["Filter"])
api_router.include_router(gemini.router, prefix="/api/v1", tags=["Gemini"])