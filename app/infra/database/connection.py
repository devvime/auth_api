from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()