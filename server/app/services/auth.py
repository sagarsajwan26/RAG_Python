from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    hash_refresh_token,
    verify_password,
    verify_refresh_token,
    create_refresh_token_id,
)
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import RegisterRequest
from app.repositories.refresh_token import RefreshTokenRepository


class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repository = UserRepository(db)
        self.refresh_token_repository = RefreshTokenRepository(db)

    async def register(self, data: RegisterRequest) -> User:
        existing_user = await self.user_repository.get_by_email(data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="email already registerd"
            )
        user = await self.user_repository.create(
            email=data.email, password_hash=hash_password(data.password), name=data.name
        )
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def authenticate(
        self,
        email: str,
        password: str,
    ) -> User:
        user = await self.user_repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        return user

    async def login(
        self,
        email: str,
        password: str,
    ) -> tuple[str, str]:
        user = await self.authenticate(email=email, password=password)
        return await self.create_token_pair(user)

    async def create_token_pair(self, user: User) -> tuple[str, str]:
        access_token = create_access_token(user.id)
        token_id = create_refresh_token_id()
        token_secret = create_refresh_token()
        token_hash = hash_refresh_token(token_secret)
        refresh_token = f"{token_id}.{token_secret}"
        now = datetime.now(timezone.utc)

        expires_at = now + timedelta(days=settings.refresh_token_expire_days)

        await self.refresh_token_repository.create(
            user_id=user.id,
            token_id=token_id,
            token_hash=token_hash,
            expires_at=expires_at,
            created_at=now,
        )
        await self.db.commit()
        return access_token, refresh_token

    async def refresh(
        self,
        refresh_token: str,
    ) -> tuple[str, str]:
        try:
            token_id, token_secret = refresh_token.split(".", 1)

        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid refresh token"
            )
        stored_token = await self.refresh_token_repository.get_by_token_id(token_id)
        if stored_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid refresh token"
            )

        if stored_token.revoked_at is not None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="refresh token has been revoked",
            )
        now = datetime.now(timezone.utc)

        if stored_token.expires_at <= now:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="refresh token has expired",
            )
        if not verify_refresh_token(token_secret, stored_token.token_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid refresh token"
            )
        return create_access_token(stored_token.user_id)
