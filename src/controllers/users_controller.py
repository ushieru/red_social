import uuid
from typing import List
from sqlalchemy import select, and_
from src.database.database import database
from src.models import User, FriendRequest, Friend


def get_users(user: User) -> List[User]:
    statement = select(User).where(User.id.is_not(user.id))
    return database.execute(statement).scalars().all()


def get_friend_requests(user: User) -> List[FriendRequest]:
    statement = select(FriendRequest).where(
        FriendRequest.user_target_id.is_(user.id))
    return database.execute(statement).scalars().all()


def add_friend_request(user: User, user_id: str) -> FriendRequest:
    statement = select(FriendRequest).where(
        and_(FriendRequest.user_target_id.is_(user.id), FriendRequest.user_source_id.is_(user_id)))
    result = database.execute(statement).fetchone()
    if result:
        _add_friend(user, user_id)
        return result[0]
    friend_request = FriendRequest(
        id=str(uuid.uuid4()), user_source_id=user.id, user_target_id=user_id)
    try:
        database.add(friend_request)
        database.commit()
    except:
        database.rollback()
    return friend_request


def _add_friend(user: User, user_id: str) -> Friend:
    try:
        friend = Friend(
            id=str(uuid.uuid4()), user_source_id=user.id, user_target_id=user_id)
        database.add(friend)
        database.commit()
    except:
        database.rollback()
