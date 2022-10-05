from functools import wraps
from flask import request, current_app
import jwt


def require_bearer_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'authorization' in request.headers:
            return {'error': 'You should not be here'}, 401
        auth = request.headers['authorization']
        _, token = auth.split(' ')
        if not token:
            return {'error': 'You should not be here'}, 401
        jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=["HS256"])
        return f(*args, **kwargs)
    return decorated_function
