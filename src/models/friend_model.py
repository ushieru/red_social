from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base


class Friend(Base):
    __tablename__ = "friend"

    id = Column(String, primary_key=True, nullable=False)
    user_source_id = Column(String, ForeignKey("user.id"), nullable=False)
    user_target_id = Column(String, ForeignKey("user.id"), nullable=False)

    user_source = relationship("User", foreign_keys=[user_source_id])
    user_target = relationship("User", foreign_keys=[user_target_id])

    __table_args__ = (
        UniqueConstraint('user_source_id', 'user_target_id',
                         name='user_source_id__user_target_id'),
        UniqueConstraint('user_target_id', 'user_source_id',
                         name='user_source_id__user_target_id__reverse'),
    )

    def __repr__(self):
        return f"Friend(id={self.id!r}, user_source={self.user_source!r}, user_target={self.user_target!r})"

    def toJson(self):
        return {
            'id': self.id,
            'user_source': self.user_source.toJson(),
            'user_target': self.user_target.toJson()
        }
