from fastapi import APIRouter

from app.api.v1.posts.controller import router as preset_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(preset_router, tags=["post"])
