import os
from flask import Flask
from routes import (
    elo,
    matches,
    sports,
    users,
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def register_blueprints(app):
    app.register_blueprint(elo.blueprint, url_prefix="/elo")
    app.register_blueprint(matches.blueprint, url_prefix="/matches")
    app.register_blueprint(sports.blueprint, url_prefix="/sports")
    app.register_blueprint(users.blueprint, url_prefix="/users")

@app.route('/')
def hello_world():
    return 'Hello, World! yo'

def run():
    register_blueprints(app)
    app.run('0.0.0.0')

if __name__ == '__main__':
    run()
