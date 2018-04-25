from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('matches', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, matches!'

db = SQLAlchemy()

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_1 = db.relationship('User', backref='match', lazy=True, nullable=False)
    team_2 = db.relationship('User', backref='match', lazy=True, nullable=False)
    score_1 = db.Column(db.Integer, nullable=False)
    score_2 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    sport = db.relationship('Sport', backref='match', lazy=True, nullable=False)
