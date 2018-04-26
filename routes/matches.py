from flask import Blueprint, jsonify, request
from database import Match, Session, User, Sport, Elo
from datetime import datetime
from routes.elo import calculate_new_elo, get_elo_for_sport_and_user


blueprint = Blueprint('matches', __name__)


@blueprint.route('/', methods=['GET'])
def get_all_matches():
    session = Session()
    matches = session.query(Match).all()
    response = jsonify([
        {
            'id': match.id,
            'team_1': session.query(User).get(match.team_1).name,
            'team_2': session.query(User).get(match.team_2).name,
            'score_1': match.score_1,
            'score_2': match.score_2,
            'date': match.date,
            'sport': session.query(Sport).get(match.sport).name,
        } for match in matches
    ])
    return response


@blueprint.route('/<match_id>/')
def get_match(match_id):
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
        response = jsonify({'matches': []})
    return response


@blueprint.route('/', methods=['POST', 'PUT'])
def add_match():
    session = Session()
    req = request.json
    team_1 = session.query(User).get(req['team_1'])
    team_2 = session.query(User).get(req['team_2'])
    sport = session.query(Sport).get(req['sport'])
    date = datetime.strptime(req['date'], '%Y-%m-%d').date()

    print(sport)
    match = Match(team_1=team_1.id, team_2=team_2.id, sport=sport.id, date=date, score_1=req['score_1'], score_2=req['score_2'])

    session.add(match)
    session.commit()

    team_1_result = 1 if req['score_1'] > req['score_2'] else 0
    elo_1 = session.query(Elo).filter_by(sport=sport.id, user=team_1.id).first()
    elo_2 = session.query(Elo).filter_by(sport=sport.id, user=team_2.id).first()

    if not elo_1:
        elo_1 = Elo(sport=sport.id, user=team_1.id)
        elo_1.score = 1000
    if not elo_2:
        elo_2 = Elo(sport=sport.id, user=team_2.id)
        elo_2.score = 1000

    new_elo_1, new_elo_2 = calculate_new_elo(elo_1.score, elo_2.score, team_1_result)

    elo_1.score = new_elo_1
    elo_2.score = new_elo_2

    session.add(elo_1)
    session.add(elo_2)
    session.commit()

    return jsonify({
        'id': match.id,
        'team_1': req['team_1'],
        'team_2': req['team_2'],
        'score_1': req['score_1'],
        'score_2': req['score_2'],
        'sport': req['sport'],
        'date': req['date'],
        'new_elo_1': new_elo_1,
        'new_elo_2': new_elo_2,
    })
