from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


blueprint = Blueprint('elo', __name__)
db = SQLAlchemy()
ELO_K = 32

class MatchResult(Enum):
    WIN=1
    LOSE=0
    DRAW=0.5


class Elo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='elo')
    sport = db.relationship('Sport', backref='elo')
    score = db.Column(db.Integer, nullable=False)


@blueprint.route('/', methods=['GET'])
def hello_world():
    return 'Hello, elo!'


@blueprint.route('/<sport>/', methods=['GET'])
def hello_world(sport):
    return 'Hello, elo!'


@blueprint.route('/<sport>/<user>/', methods=['GET'])
def hello_world(sport, user):
    return 'Hello, elo!'


@blueprint.route('/<sport>/<user>/', methods=['PUT'])
def hello_world():
    return 'Hello, elo!'

def calculate_new_elo(old_elo1, old_elo2, s1):
    """ Calculates new elo for two players
    old_elo1 - elo of player 1
    old_elo2 - elo of player 2
    s1 - match result from player one's perspective
        1 = win 0.5 = draw 0 = lose
    """
    s2 = abs(1-s1)
    r1 = 10**(old_elo1/400)
    r2 = 10**(old_elo2/400)
    e1 = r1 / (r1 + r2)
    e2 = r2 / (r1 + r2)
    new_elo_1 = r1 + ELO_K*(s1 - e1)
    new_elo_2 = r2 + ELO_K*(s2 - e2)
    return new_elo_1, new_elo_2
