from fastapi import APIRouter, Depends, Response, Cookie, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dependencies import get_db
from app.services.auth import AuthService
from app.schemas.auth import LoginRequest, RegisterRequest

router = APIRouter()


@router.post("/register")
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    user = await service.register(data)

    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
    }


@router.post("/login")
async def login(
    data: LoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)
    access_token, refresh_token = await service.login(
        email=data.email,
        password=data.password,
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=30 * 60,
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=30 * 24 * 60 * 60,
    )

    return {"message": "login successful"}


@router.post("/refresh")
async def refresh(
    response: Response,
    refresh_token: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    if refresh_token is None:
        raise HTTPException(status_code=401, detail="refresh token missing")

    service = AuthService(db)
    access_token = await service.refresh(
        refresh_token=refresh_token,
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=30 * 60,
    )

    return {
        "message": "Token refreshed",
    }


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=False,
        samesite="lax",
    )
    response.delete_cookie(
        key="refresh_token",
        httponly=True,
        secure=False,
        samesite="lax",
    )
    return {"message": "logout successful"}
