from flask import Blueprint


blueprint = Blueprint('sports', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, sports!'
