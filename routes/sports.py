from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('sports', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, sports!'

db = SQLAlchemy()

class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
