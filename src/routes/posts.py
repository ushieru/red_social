from operator import itemgetter
from flask import Blueprint, request
from src.controllers.posts_controller import create_post, get_posts, get_friends_posts
from src.decorators.require_bearer_token import require_bearer_token
from src.utils.b64_to_file import b64_to_file

posts = Blueprint('posts', __name__, url_prefix='/posts')


@posts.route('/', methods=['GET'])
@require_bearer_token
def index(user):
    return [post.toJson() for post in get_posts(user)]


@posts.route('/', methods=['POST'])
@require_bearer_token
def create(user):
    json = request.get_json()
    media, description = itemgetter('media', 'description')(json)
    file_name = ''
    if not media == '':
        b64, ext = itemgetter('b64', 'ext')(media)
        file_name = b64_to_file(b64, ext)
    post = create_post(user, file_name, description)
    return post.toJson()


@posts.route('/friends', methods=['GET'])
@require_bearer_token
def friends_posts(user):
    return [post.toJson() for post in get_friends_posts(user)]
