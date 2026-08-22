from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_access_token
from app.database.dependencies import get_db
from app.models.user import User
from app.repositories.user import UserRepository

bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: str = Depends(bearer_scheme), db: AsyncSession = Depends(get_db)
) -> User:
    token = credentials.credentials
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid or expired access token",
            headers={"www-Authenticate": "Bearer"},
        )
    repository = UserRepository(db)
    user = await repository.get_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
