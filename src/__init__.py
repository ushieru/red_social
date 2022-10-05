import os
from dotenv import load_dotenv
from flask import Flask
from src.routes.auth import auth
from src.decorators.require_bearer_token import require_bearer_token

load_dotenv()

app = Flask('Red Social')

app.config['JWT_SECRET'] = os.getenv('JWT_SECRET')


@app.route('/')
def index():
    return {'ok': 'ok'}


app.register_blueprint(auth)
