from fastapi import APIRouter

from app.api.endpoints import (
    donation_router, user_router
)

main_router = APIRouter()

main_router.include_router(
    donation_router,
    prefix='/donation',
    tags=['Donations'],
)
main_router.include_router(user_router)
