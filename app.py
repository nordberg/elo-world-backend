import os
from flask import Flask, jsonify
from routes import (
    elo,
    matches,
    sports,
    users,
    exceptions
)

app = Flask(__name__)


@app.errorhandler(exceptions.HTTPException)
def http_exception_handler(e):
    return jsonify({
        'error': e.message
    }), e.http_code


def register_blueprints(app):
    app.register_blueprint(elo.blueprint, url_prefix="/api/elo")
    app.register_blueprint(matches.blueprint, url_prefix="/api/matches")
    app.register_blueprint(sports.blueprint, url_prefix="/api/sports")
    app.register_blueprint(users.blueprint, url_prefix="/api/users")

@app.route('/')
def hello_world():
    return 'Hello, World! yo'

def run():
    register_blueprints(app)
    app.run('0.0.0.0', debug=True)

if __name__ == '__main__':
    run()
