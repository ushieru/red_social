#!/usr/bin/env python3.10
import sys
import os
sys.path.append(os.getcwd())
from src.database import engine, Base
from src.models import User, FriendRequest

if __name__ == '__main__':
    Base.metadata.create_all(engine)
