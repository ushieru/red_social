from . import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
database = Session()
