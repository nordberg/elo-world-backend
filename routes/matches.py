from flask import Blueprint


blueprint = Blueprint('matches', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, matches!'
