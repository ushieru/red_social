from src.models.user_model import User
from src.database import engine, Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
