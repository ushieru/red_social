import uuid
from typing import List
from sqlalchemy import select, and_
from src.database.database import database
from src.models import User, FriendRequest


def get_users(user: User) -> List[User]:
    statement = select(User).where(User.id.is_not(user.id))
    return database.execute(statement).scalars().all()


def get_friend_requests(user: User) -> List[FriendRequest]:
    statement = select(FriendRequest).where(
        FriendRequest.user_target_id.is_(user.id))
    return database.execute(statement).scalars().all()


def add_friend(user: User, user_id: str) -> FriendRequest:
    statement = select(FriendRequest).where(
        and_(FriendRequest.user_target_id.is_(user.id), FriendRequest.user_source_id.is_(user_id)))
    result = database.execute(statement).fetchone()
    if result:
        raise 'Add friend'
    friend_request = FriendRequest(
        id=str(uuid.uuid4()), user_source_id=user.id, user_target_id=user_id)
    database.add(friend_request)
    database.commit()
    return friend_request
