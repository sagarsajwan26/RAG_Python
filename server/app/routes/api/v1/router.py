from fastapi import APIRouter
from app.routes.api.v1 import auth, user

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(user.router, prefix="/users", tags=["Users"])
