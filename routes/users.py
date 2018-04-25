from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('users', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, users!'

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
