from sqlalchemy import Column, Integer, String, DateTime, Boolean, text
from sqlalchemy.sql import func
from app.infra.database.connection import Base

class TimestampMixin:
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("false"))
    refresh_token = Column(String, nullable=True)
