from fastapi import HTTPException, status
from app.helper.security import verify_password, create_access_token, create_refresh_token
from app.provider.user_repository import UserRepository

class LoginUseCase:
    def __init__(self, session):
        self.session = session
        self.repo = UserRepository(session)

    async def execute(self, email: str, password: str):
        try:
            
            user = self.repo.find_by_email(email)
            if not user:
                raise HTTPException(400, "Invalid email or password")

            if not verify_password(password, user.password):
                raise HTTPException(400, "Invalid email or password")

            access_token = create_access_token({"sub": str(user.id)})
            refresh_token = create_refresh_token({"sub": str(user.id)})

            user.refresh_token = refresh_token
            self.session.commit()

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer",
            }
            
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
