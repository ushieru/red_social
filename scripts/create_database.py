from src.models import User, FriendRequest
from src.database import engine, Base

Base.metadata.create_all(engine)
