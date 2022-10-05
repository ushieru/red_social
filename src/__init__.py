from flask import Flask
from .routes.auth import auth

app = Flask('Red Social')


@app.route('/')
def index():
    return {'ok': 'ok'}


app.register_blueprint(auth)
