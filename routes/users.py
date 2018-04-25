from flask import Blueprint


blueprint = Blueprint('users', __name__)


@blueprint.route('/')
def hello_world():
    return 'Hello, users!'
