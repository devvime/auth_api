from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.helper.security import decode_token, create_access_token, create_refresh_token
from app.provider.user_repository import UserRepository

class RefreshTokenUseCase:
    def __init__(self, session):
        self.session = session
        self.repo = UserRepository(session)

    async def execute(self, refresh_token: str):
        try:
            payload = decode_token(refresh_token)
            user_id: str = payload.get("sub")
        except JWTError:
            raise HTTPException(401, "Invalid refresh token")
        
        try:

            user = self.repo.find_by_id(user_id)

            if not user or user.refresh_token != refresh_token:
                raise HTTPException(401, "Refresh token invalid or expired")

            new_access_token = create_access_token({"sub": str(user.id)})
            new_refresh_token = create_refresh_token({"sub": str(user.id)})
            
            user.refresh_token = new_refresh_token
            self.session.commit()
            
            return {
                "access_token": new_access_token,
                "refresh_token": new_refresh_token,
                "token_type": "bearer"
            }
            
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
