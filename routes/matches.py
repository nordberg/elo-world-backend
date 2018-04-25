from flask_sqlalchemy import SQLAlchemy

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
