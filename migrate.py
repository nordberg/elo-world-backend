from database import Sport, engine, Session, Base, User, Match, Elo
from sqlalchemy import create_engine
from database import Sport
from sqlalchemy.orm import sessionmaker

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

table_tennis = Sport(name='Table Tennis')
eight_ball = Sport(name='8-ball')

session.add(table_tennis)
session.add(eight_ball)

user_1 = User(name='Marcus')
user_2 = User(name='Dexter')


session.add(user_1)
session.add(user_2)

session.commit()

elo_1 = Elo(user=user_1.id, sport=table_tennis.id, score=1000)
elo_2 = Elo(user=user_2.id, sport=table_tennis.id, score=1000)
match = Match(team_1=user_1.id, team_2=user_2.id, score_1=2, score_2=1, sport=table_tennis.id)

session.add(match)
session.add(elo_1)
session.add(elo_2)

session.commit()
