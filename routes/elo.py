from flask import Blueprint


blueprint = Blueprint('elo', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, elo!'
