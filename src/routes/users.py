from flask import Blueprint
from src.controllers.users_controller import get_users
from src.decorators.require_bearer_token import require_bearer_token

users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/', methods=['GET'])
@require_bearer_token
def index(user):
    return [user.toJson() for user in get_users(user)]
