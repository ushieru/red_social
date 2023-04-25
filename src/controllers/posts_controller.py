import uuid
from typing import List
from sqlalchemy import select, or_
from src.database.database import database
from src.models.post_model import Post
from src.models.user_model import User
from src.models.friend_model import Friend


def create_post(user_id: str, file_name: str, description: str) -> Post:
    post = Post(id=str(uuid.uuid4()), user_id=user_id,
                media=file_name, description=description)
    database.add(post)
    database.commit()
    return post


def get_posts(user: User) -> List[Post]:
    statement = select(Post).where(Post.user_id.is_(
        user.id)).order_by(Post.create_at.desc())
    return database.execute(statement).scalars().all()


def get_friends_posts(user: User) -> List[Post]:
    statement = select(Post).where(
        or_(
            Post.user_id.in_(select(Friend.user_source_id).where(
                Friend.user_target_id.is_(user.id))),
            Post.user_id.in_(select(Friend.user_target_id).where(Friend.user_source_id.is_(user.id))))
    ).order_by(Post.create_at.desc())
    return database.execute(statement).scalars().all()
