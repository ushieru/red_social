from flask import Blueprint
from src.controllers.users_controller import get_users, add_friend
from src.decorators.require_bearer_token import require_bearer_token

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/', methods=['GET'])
@require_bearer_token
def index(user):
    return [user.toJson() for user in get_users(user)]


@users.route('/add_friend/<string:user_id>', methods=['POST'])
@require_bearer_token
def add_friend_request(user, user_id):
    friend_request = add_friend(user, user_id)
    return friend_request.toJson()
