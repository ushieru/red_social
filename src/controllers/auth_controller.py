import uuid
import hashlib
from sqlalchemy import select, and_
from src.database.database import database
from src.models.user_model import User


def create_user(name: str, email: str, password: str) -> User:
    hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User(id=str(uuid.uuid4()), name=name,
                email=email, password=hash_pass)
    database.add(user)
    database.commit()
    return user


def get_user_auth(email: str, password: str) -> User:
    hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    statement = select(User).where(
        and_(User.email.is_(email), User.password.is_(hash_pass)))
    result = database.execute(statement).fetchone()
    if not result:
        return None
    return result[0]
