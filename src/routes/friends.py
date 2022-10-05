from flask import Blueprint
from src.controllers.friends_controller import get_friend_requests, get_friends, add_friend_request
from src.decorators.require_bearer_token import require_bearer_token

friends = Blueprint('friends', __name__, url_prefix='/friends')


@friends.route('/', methods=['GET'])
@require_bearer_token
def index(user):
    return [friend.toJson() for friend in get_friends(user)]


@friends.route('/requests', methods=['GET'])
@require_bearer_token
def get_requests(user):
    return [request.toJson() for request in get_friend_requests(user)]


@friends.route('/<string:user_id>', methods=['POST'])
@require_bearer_token
def add_friend(user, user_id):
    friend_request = add_friend_request(user, user_id)
    return friend_request.toJson()
