from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from app.shared.database.session import get_db
from app.schema.user.create_user_schema import CreateUserSchema
from app.shared.helper.get_current_user import get_current_user
from app.service.user.create_user import CreateUser
from app.shared.rate_limit import global_rate_limit

router = APIRouter(
    prefix="/user", 
    tags=["Users"],
    dependencies=[global_rate_limit]
)

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