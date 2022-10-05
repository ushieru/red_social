from sqlalchemy import Column, String
from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

    def toJson(self, insecure: bool = False):
        user = {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
        if insecure:
            user['password'] = self.password
        return user
