from operator import itemgetter
from flask import Blueprint, request
from src.controllers.posts_controller import create_post, get_posts, get_friends_posts
from src.decorators.require_bearer_token import require_bearer_token
from src.utils.b64_to_file import b64_to_file

posts = Blueprint('posts', __name__, url_prefix='/posts')


@posts.route('/<user_id>', methods=['POST'])
def create(user_id):
    json = request.get_json()
    media, description = itemgetter('media', 'description')(json)
    b64, ext = itemgetter('b64', 'ext')(media)
    file_name = b64_to_file(b64, ext)
    post = create_post(user_id, file_name, description)
    return post.toJson()
