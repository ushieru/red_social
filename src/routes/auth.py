from operator import itemgetter
import jwt
from flask import Blueprint, request
from src.controllers.users_controller import create_user, get_user_auth

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    json = request.get_json()
    name, email, password = itemgetter('name', 'email', 'password')(json)
    user = create_user(name, email, password)
    return {
        'user': user.toJson()
    }


@auth.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    email, password = itemgetter('email', 'password')(json)
    user = get_user_auth(email, password)
    if not user:
        return {}, 400
    token = jwt.encode(
        user.toJson(), "mysupersecretword", algorithm="HS256")
    return {
        'token': token
    }
