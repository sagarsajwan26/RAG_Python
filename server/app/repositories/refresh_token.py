from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.refresh_token import RefreshToken


class RefreshTokenRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        user_id: int,
        token_id: str,
        token_hash: str,
        expires_at: datetime,
        created_at: datetime,
    ) -> RefreshToken:
        refresh_token = RefreshToken(
            user_id=user_id,
            token_id=token_id,
            token_hash=token_hash,
            expires_at=expires_at,
            created_at=created_at,
        )
        self.db.add(refresh_token)

        await self.db.flush()
        return refresh_token

    async def get_by_token_id(
        self,
        token_id: str,
    ) -> RefreshToken | None:
        result = await self.db.execute(
            select(RefreshToken).where(RefreshToken.token_id == token_id)
        )
        return result.scalar_one_or_none()

    async def get_active_tokens_by_user(self, user_id: int) -> list[RefreshToken]:
        result = await self.db.execute(
            select(RefreshToken).where(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked_at.is_(None),
            )
        )
        return list(result.scalars().all())

    async def get_by_user_id(
        self,
        user_id: int,
    ) -> list[RefreshToken]:
        result = await self.db.execute(
            select(RefreshToken).where(RefreshToken.user_id == user_id)
        )

    async def revoke(
        self, refresh_token: RefreshToken, revoked_at: datetime
    ) -> RefreshToken:
        refresh_token.revoked_at = revoked_at
        await self.db.flush()
        return refresh_token
