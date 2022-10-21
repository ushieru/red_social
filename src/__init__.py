import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from src.routes import auth, users, friends, posts, assets

load_dotenv()

app = Flask('Red Social', static_folder='public', static_url_path='')

app.config['JWT_SECRET'] = os.getenv('JWT_SECRET')


@app.route('/')
def index():
    return {'ok': 'ok'}


@app.route('/docs')
def docs():
    return send_from_directory('public', 'index.html')


app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(friends)
app.register_blueprint(posts)
app.register_blueprint(assets)
