from flask import Blueprint, jsonify, request
from database import Session, Sport
from routes.exceptions import NotFound


blueprint = Blueprint('sports', __name__)

@blueprint.route('/', methods=['POST'])
def create_sport():
    session = Session()
    req = request.json
    new_sport = Sport(name=req["name"])
    session.add(new_sport)
    session.commit()

    return jsonify({
        'id': new_sport.id,
        'name': new_sport.id,
    }), 201

@blueprint.route('/', methods=['GET'])
def get_all_sports():
    session = Session()
    sports = session.query(Sport).all()
    return jsonify({
        'sports': [
            {
                'id': sport.id,
                'name': sport.name
            }
            for sport in sports
        ]
    }), 200

@blueprint.route('/<sport_id>/', methods=['GET'])
def get_sport(sport_id):
    session = Session()
    sport = session.query(Sport).get(sport_id)
    if sport is None:
        raise NotFound("Sport not found")
    return jsonify({
        'id': sport.id,
        'name': sport.name,
    }), 200
