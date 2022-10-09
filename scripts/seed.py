#!/usr/bin/env python3.10
import sys
import os
sys.path.append(os.getcwd())
from src.controllers.users_controller import create_user
from src.controllers.friends_controller import add_friend_request
from src.controllers.posts_controller import create_post

if __name__ == '__main__':
    user1 = create_user('Feidlimid Baako Ellington',
                        'feidlimid@email.com', 'feidlimid')
    user2 = create_user('Camryn Bala Stacey', 'camryn@email.com', 'camryn')
    user3 = create_user('Praise Onyekachi Heike', 'praise@email.com', 'praise')

    create_post(user1, '30de534d-d1ea-4f3b-8f73-ba0957f96ad6.png', 'Hello dudes!')
    create_post(user1, '', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    create_post(user1, '', 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...')

    create_post(user2, '', 'Fusce nec porttitor erat.')
    create_post(user2, '', 'Nullam vitae neque ut nisi accumsan ornare quis sit amet tellus.')

    add_friend_request(user1, user2.id)
    add_friend_request(user2, user1.id)

    add_friend_request(user1, user3.id)
