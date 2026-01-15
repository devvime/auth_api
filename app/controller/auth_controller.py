from fastapi import APIRouter, Depends
from app.infra.database.session import get_db
from sqlalchemy.orm import Session

from app.domain.auth.use_cases.login import LoginUseCase
from app.domain.auth.use_cases.refresh import RefreshTokenUseCase

from app.domain.auth.schemas.login_schema import LoginSchema
from app.domain.auth.schemas.refresh_schema import RefreshSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

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