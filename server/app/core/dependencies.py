from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_access_token
from app.database.dependencies import get_db
from app.models.user import User
from app.repositories.user import UserRepository
from app.models.tenant_member import TenantMember

bearer_scheme = HTTPBearer()


async def get_current_user(
    access_token: str | None = Cookie(default=None), db: AsyncSession = Depends(get_db)
) -> User:
    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated"
        )

    user_id = verify_access_token(access_token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
        )
    repository = UserRepository(db)
    user = await repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )

    return user
