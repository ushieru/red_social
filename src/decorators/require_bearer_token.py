from functools import wraps
from operator import itemgetter
from flask import request, current_app
import jwt
from src.models.user_model import User


def require_bearer_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'authorization' in request.headers:
            return {'error': 'You should not be here'}, 401
        auth = request.headers['authorization']
        _, token = auth.split(' ')
        if not token:
            return {'error': 'You should not be here'}, 401
        user_payload = jwt.decode(
            token, current_app.config['JWT_SECRET'], algorithms=["HS256"])
        id_, name, email = itemgetter('id', 'name', 'email')(user_payload)
        user = User(id=id_, name=name, email=email)
        return f(user, *args, **kwargs)
    return decorated_function
