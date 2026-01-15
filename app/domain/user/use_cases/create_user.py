from sqlalchemy.orm import Session
from app.domain.user.schemas.create_user_schema import CreateUserSchema
from app.helper.security import hash_password
from app.provider.user_repository import UserRepository

class CreateUser:

    def __init__(self, session: Session):
        self.session = session

    async def execute(self, user: CreateUserSchema):
        try:
            user_repository = UserRepository(self.session)
            
            hashed = hash_password(user.password)
            
            data = user_repository.create(user, hashed)

            return {
                "id": data.id,
                "name": data.name,
                "email": data.email,
                "active": data.active,
                "super": data.super,
            }

        except Exception as e:
            self.session.rollback()
            raise e