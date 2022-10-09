import os
from dotenv import load_dotenv
from flask import Flask
from src.routes import auth, users, friends, posts

load_dotenv()

app = Flask('Red Social')

app.config['JWT_SECRET'] = os.getenv('JWT_SECRET')


@app.route('/')
def index():
    return {'ok': 'ok'}


app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(friends)
app.register_blueprint(posts)
