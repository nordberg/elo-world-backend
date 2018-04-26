from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('sports', __name__)

@blueprint.route('/')
def hello_world():
    return 'Hello, sports!'
