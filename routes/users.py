from flask import Blueprint, jsonify, request
from database import Session, User
from routes.exceptions import UserError


blueprint = Blueprint('users', __name__)


@blueprint.route('/', methods=['POST'])
def create_user():
    session = Session()
    req = request.json
    new_user = User(name=req["name"])
    session.add(new_user)
    session.commit()

    return jsonify({
        'id': new_user.id,
        'name': new_user.id,
    })

@blueprint.route('/', methods=['GET'])
def get_all_users():
    session = Session()
    users = session.query(User).all()
    return jsonify({
        'users': [
            {
                'id': user.id,
                'name': user.name
            }
            for user in users
        ]
    })

@blueprint.route('/<user_id>/', methods=['GET'])
def get_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    if user is None:
        raise UserError("User not found")
    return jsonify({
        'id': user.id,
        'name': user.name,
    })
