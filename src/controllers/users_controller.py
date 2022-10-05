from typing import List
from sqlalchemy import select
from src.database.database import database
from src.models import User


def get_users(user: User) -> List[User]:
    statement = select(User).where(User.id.is_not(user.id))
    return database.execute(statement).scalars().all()
