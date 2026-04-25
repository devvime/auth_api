from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from app.infrastructure.database.connection import get_db
from app.domain.service.auth.login import LoginUseCase
from app.domain.service.auth.refresh import RefreshTokenUseCase
from app.domain.schema.auth.login_schema import LoginSchema
from app.domain.schema.auth.refresh_schema import RefreshSchema
from app.api.middleware.rate_limit import login_rate_limit

router = APIRouter(prefix="/auth", tags=["Auth"], dependencies=[login_rate_limit])


@router.post("/login")
async def login(data: LoginSchema, session: Session = Depends(get_db)):
    service = LoginUseCase(session)
    data = await service.execute(data.email, data.password)
    return {
        "success": True,
        "result": data,
    }


@router.post("/refresh")
async def refresh_token(data: RefreshSchema, session: Session = Depends(get_db)):
    service = RefreshTokenUseCase(session)
    data = await service.execute(data.refresh_token)
    return {
        "success": True,
        "result": data,
    }
