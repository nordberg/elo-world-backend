from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('matches', __name__)

@blueprint.route('/')
def matches(id):
    match = Match.query.filter_by(id=id).first()
    if request.method == 'GET':
        response = jsonify({
            'id': match.id,
            'team_1': match.team_1,
            'team_2': match.team_2,
            'score_1': match.score_1,
            'score_2': match.score_2,
            'date': match.date,
            'sport': match.sport,
        })

        return response
