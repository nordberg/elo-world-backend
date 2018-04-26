from flask import Blueprint, jsonify, request
from database import Match, Session, User, Sport


blueprint = Blueprint('matches', __name__)


@blueprint.route('/<match_id>/')
def matches(match_id):
    session = Session()
    match = session.query(Match).get(match_id)
    if request.method == 'GET' and match:
        response = jsonify({
            'id': match.id,
            'team_1': session.query(User).get(match.team_1).name,
            'team_2': session.query(User).get(match.team_2).name,
            'score_1': match.score_1,
            'score_2': match.score_2,
            'date': match.date,
            'sport': session.query(Sport).get(match.sport).name,
        })

    else:
        response = jsonify({'error': 'No match with that id'})
    return response
