from flask import Blueprint, jsonify, request
from database import Match, Session, User, Sport
from datetime import datetime


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


@blueprint.route('/add_match/', methods=['POST', 'PUT'])
def add_match():
    session = Session()
    req = request.json
    print(req)
    team_1 = session.query(User).filter_by(name=req['team_1']).first()
    team_2 = session.query(User).filter_by(name=req['team_2']).first()
    sport = session.query(Sport).filter_by(name=req['sport']).first()
    date = datetime.strptime(req['date'], '%Y-%m-%d').date()

    match = Match(team_1=team_1.id, team_2=team_2.id, sport=sport.id, date=date, score_1=req['score_1'], score_2=req['score_2'])

    session.add(match)
    session.commit()

    return jsonify({
        'id': match.id,
        'team_1': req['team_1'],
        'team_2': req['team_2'],
        'score_1': req['score_1'],
        'score_2': req['score_2'],
        'sport': req['sport'],
        'date': req['date'],
    })
