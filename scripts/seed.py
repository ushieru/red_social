#!/usr/bin/env python3.10
import sys
import os
sys.path.append(os.getcwd())
from src.controllers.friends_controller import add_friend_request
from src.controllers.auth_controller import create_user

if __name__ == '__main__':
    user1 = create_user('Feidlimid Baako Ellington',
                        'feidlimid@email.com', 'feidlimid')
    user2 = create_user('Camryn Bala Stacey', 'camryn@email.com', 'camryn')
    user3 = create_user('Praise Onyekachi Heike', 'praise@email.com', 'praise')

    add_friend_request(user1, user2.id)
    add_friend_request(user2, user1.id)

    add_friend_request(user1, user3.id)
