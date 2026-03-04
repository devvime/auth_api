from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from app.shared.database.session import get_db
from app.service.auth.login import LoginUseCase
from app.service.auth.refresh import RefreshTokenUseCase
from app.schema.auth.login_schema import LoginSchema
from app.schema.auth.refresh_schema import RefreshSchema
from app.shared.rate_limit import login_rate_limit

router = APIRouter(
    prefix="/auth", 
    tags=["Auth"],
    dependencies=[login_rate_limit]
)

@router.post("/login")
async def login(
    data: LoginSchema,
    session: Session = Depends(get_db)
):
    service = LoginUseCase(session)
    data = await service.execute(data.email, data.password)
    return {
        "success": True,
        "result": data,
    }


@router.post("/refresh")
async def refresh_token(
    data: RefreshSchema,
    session: Session = Depends(get_db)
):
    service = RefreshTokenUseCase(session)
    data = await service.execute(data.refresh_token)
    return {
        "success": True,
        "result": data,
    }