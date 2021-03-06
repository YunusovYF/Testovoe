from fastapi import APIRouter

from src.routers import cities, users, picnics

router = APIRouter()

router.include_router(cities.router)
router.include_router(users.router)
router.include_router(picnics.router)

