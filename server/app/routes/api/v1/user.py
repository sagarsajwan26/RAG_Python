from fastapi import FastAPI, APIRouter, Depends
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "name": current_user.name,
    }
