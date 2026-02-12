from fastapi import APIRouter

from app.api.v1 import reports

api_router = APIRouter()
api_router.include_router(reports.router, prefix="/v1", tags=["reports"])
