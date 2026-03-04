
from fastapi import Depends
from app.shared.database.connection import session

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()