from operator import itemgetter
import jwt
from flask import Blueprint, request, current_app
from src.controllers.auth_controller import get_user_auth
from src.controllers.users_controller import create_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():
    json = request.get_json()
    name, email, password = itemgetter('name', 'email', 'password')(json)
    user = create_user(name, email, password)
    return user.toJson()


@auth.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    email, password = itemgetter('email', 'password')(json)
    user = get_user_auth(email, password)
    if not user:
        return {}, 400
    token = jwt.encode(
        user.toJson(), current_app.config['JWT_SECRET'], algorithm="HS256")
    return {'token': token, 'user': user.toJson()}
