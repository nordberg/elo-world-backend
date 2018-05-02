from flask import Blueprint, jsonify, request
from database import Match, Session, User, Sport, Elo
from datetime import datetime


blueprint = Blueprint('statistics', __name__)

@blueprint.route('/<player_1_id>/<player_2_id>')
def get_statistics(player_1_id, player_2_id):
    session = Session()
    player_1 = session.query(User).get(player_1_id)
    player_2 = session.query(User).get(player_2_id)
    if request.method == 'GET' and player_1 and player_2:
        statistics = {
            'matches': [],
            'elo_player_1': None,
            'elo_player_2': None,
            'leader': None,
            'wins_player_1': 0,
            'wins_player_2': 0,
        }

        db_matches = session.query(Match).filter_by(team_1=player_1.id, team_2=player_2.id)
        db_matches_2 = session.query(Match).filter_by(team_1=player_2.id, team_2=player_1.id)
        matches = []
        for db_match in db_matches:
            matches.append(str(db_match))
            if db_match.score_1 > db_match.score_2:
                statistics['wins_player_1'] += 1
        for db_match in db_matches_2:
            matches.append(str(db_match))
            if db_match.score_1 > db_match.score_2:
                statistics['wins_player_2'] += 1

        statistics['matches'] = matches
        statistics['leader'] = player_1.name if statistics['wins_player_1'] > statistics['wins_player_2'] else player_2.name

        elo_p1 = session.query(Elo).filter_by(user=player_1.id).first()
        elo_p2 = session.query(Elo).filter_by(user=player_2.id).first()

        statistics['elo_player_1'] = elo_p1.score
        statistics['elo_player_2'] = elo_p2.score

        response = jsonify(statistics)

    else:
        response = jsonify({'matches': []})
    return response
