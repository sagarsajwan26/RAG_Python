from fastapi import APIRouter
from app.routes.api.v1 import auth, user, tenants, document, search

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(document.router, prefix="/document", tags=["documents"])
api_router.include_router(tenants.router, prefix="/tenant", tags=["tenants"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
