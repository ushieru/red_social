import uuid
import hashlib
from typing import List
from sqlalchemy import select
from src.database.database import database
from src.models import User


def create_user(name: str, email: str, password: str) -> User:
    hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User(id=str(uuid.uuid4()), name=name,
                email=email, password=hash_pass)
    database.add(user)
    database.commit()
    return user


def get_users(user: User) -> List[User]:
    statement = select(User).where(User.id.is_not(user.id))
    return database.execute(statement).scalars().all()
