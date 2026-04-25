from sqlalchemy.orm import Session
from app.infrastructure.database.models import User
from app.domain.schema.user.create_user_schema import CreateUserSchema


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, id: int):
        return self.session.query(User).filter(User.id == id).first()

    def find_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user: CreateUserSchema, hashed):
        data = User(name=user.name, email=user.email, password=hashed)
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data
