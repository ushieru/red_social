from sqlalchemy import Column, String, UniqueConstraint
from src.database import Base


class FriendRequest(Base):
    __tablename__ = "friend"

    id = Column(String, primary_key=True, nullable=False)
    user_source_id = Column(String, nullable=False)
    user_target_id = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_source_id', 'user_target_id',
                         name='user_source_id__user_target_id'),
    )

    def __repr__(self):
        return f"FriendRequest(id={self.id!r}, user_source_id={self.user_source_id!r}, user_target_id={self.user_target_id!r})"

    def toJson(self):
        return {
            'id': self.id,
            'user_source_id': self.user_source_id,
            'user_target_id': self.user_target_id
        }
