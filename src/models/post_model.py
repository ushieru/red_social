from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(String, primary_key=True, nullable=False)
    user_id = Column(String, ForeignKey("user.id"))
    media = Column(String)
    description = Column(String)
    create_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", foreign_keys=[user_id])

    def __repr__(self):
        return f"Post(id={self.id!r}, user_id={self.user_id!r}, media={self.media!r}, description={self.description!r})"

    def toJson(self):
        return {
            'id': self.id,
            'user': self.user.toJson(),
            'media': self.media,
            'description': self.description
        }
