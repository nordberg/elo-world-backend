from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Elo(Base):
    __tablename__ = 'elo'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    sport = Column(Integer, ForeignKey('sports.id'))
    score = Column(Integer, nullable=False)


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    score_1 = Column(Integer, nullable=False)
    score_2 = Column(Integer, nullable=False)
    team_1 = Column(Integer, ForeignKey('users.id'))
    team_2 = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=True)

    def __init__(self, team_1, team_2, score_1, score_2, date, sport):
        self.team_1 = team_1
        self.team_2 = team_2
        self.score_1 = score_1
        self.score_2 = score_2
        self.date = date
        self.sport = sport

    def __repr__(self):
        return '<id: {}, {}, {} {} - {} {}>'.format(self.id, self.sport, self.team_1, self.score_1, self.score_2, self.team_2)

    def get_winner(self):
        if self.score_1 > self.score_2:
            return self.team_1
        elif self.score_2 > self.score_1:
            return self.team_2
        else:
            return None


class Sport(Base):
    __tablename__ = 'sports'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)

    elo = relationship('Elo')

    def __init__(self, name):
        self.name = name


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    matches = relationship('Match', primaryjoin="or_(User.id==Match.team_1, User.id==Match.team_2)")
    elo = relationship('Elo')
