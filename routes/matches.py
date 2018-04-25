from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('matches', __name__)

@blueprint.route('/')
def matches(id):
    match = Match.query.filter_by(id=id).first()
    if request.method == 'GET':
        response = jsonify({
            'id': match.id,
            'team_1': match.team_1,
            'team_2': match.team_2,
            'score_1': match.score_1,
            'score_2': match.score_2,
            'date': match.date,
            'sport': match.sport,
        })

        return response

db = SQLAlchemy()

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_1 = db.relationship('User', backref='match', lazy=True, nullable=False)
    team_2 = db.relationship('User', backref='match', lazy=True, nullable=False)
    score_1 = db.Column(db.Integer, nullable=False)
    score_2 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    sport = db.relationship('Sport', backref='match', lazy=True, nullable=False)

    def get_winner(self):
        if self.score_1 > self.score_2:
            return self.team_1
        elif self.score_2 > self.score_1:
            return self.team_2
        else:
            return None
