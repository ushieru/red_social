from typing import List
import json
import uuid
import hashlib
from sqlalchemy import select, and_
from src.database.database import database
from src.models.user_model import User


def create_user(name: str, email: str, password: str) -> User:
    uuid_str = str(uuid.uuid4())
    hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User(id=uuid_str, name=name, email=email, password=hash_pass)
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


def get_users(user: User) -> List[User]:
    statement = select(User).where(User.id.is_not(user.id))
    return database.execute(statement).scalars().all()
