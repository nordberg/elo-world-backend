from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('elo', __name__)

ELO_K = 32
WIN=1
LOSE=0
DRAW=0.5


@blueprint.route('/', methods=['GET'])
def get_all_elo():
    return 'Hello, elo!'


@blueprint.route('/<sport>/', methods=['GET'])
def get_elo_for_sport(sport):
    return 'Hello, elo!'


@blueprint.route('/<sport>/<user>/', methods=['GET'])
def get_elo_for_sport_and_user(sport, user):
    return 'Hello, elo!'


def calculate_new_elo(r1, r2, s1):
    """ Calculates new elo for two players
    r1 - elo of player 1
    r2 - elo of player 2
    s1 - match result from player one's perspective
        1 = win 0.5 = draw 0 = lose
    """
    s2 = abs(1-s1)
    R1 = 10**(r1/400)
    R2 = 10**(r2/400)
    e1 = R1 / (R1 + R2)
    e2 = R2 / (R1 + R2)
    new_elo_1 = round(r1 + ELO_K*(s1 - e1))
    new_elo_2 = round(r2 + ELO_K*(s2 - e2))
    return new_elo_1, new_elo_2
