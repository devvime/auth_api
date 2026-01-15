from fastapi import APIRouter, Depends
from app.infra.database.session import get_db
from sqlalchemy.orm import Session
from app.domain.user.schemas.create_user_schema import CreateUserSchema
from app.helper.get_current_user import get_current_user
from app.domain.user.use_cases.create_user import CreateUser

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("")
async def create_user(
    data: CreateUserSchema,
    session: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    service = CreateUser(session)
    data = await service.execute(data)
    return {
        "success": True,
        "message": "User created successfully",
        "result": data,
    }