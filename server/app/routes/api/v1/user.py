from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dependencies import get_db
from app.repositories.user import UserRepository
from app.schemas.user import UserResponse
from app.services.user import UserService

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)
    return await service.get_all_users()
