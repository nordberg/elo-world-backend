from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('elo', __name__)
db = SQLAlchemy()

class Elo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='elo', nullable=False)
    sport = db.relationship('Sport', backref='elo', nullable=False)
    score = db.Column(db.Integer, nullable=False)


@blueprint.route('/')
def hello_world():
    return 'Hello, elo!'
