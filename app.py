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
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def register_blueprints(app):
    app.register_blueprint(elo.blueprint, url_prefix="/elo")
    app.register_blueprint(matches.blueprint, url_prefix="/matches")
    app.register_blueprint(sports.blueprint, url_prefix="/sports")
    app.register_blueprint(users.blueprint, url_prefix="/users")

def run():
    register_blueprints(app)
    app.run()

if __name__ == '__main__':
    run()
