from database import Sport, engine, Session, Base, User, Match
from sqlalchemy import create_engine
from database import Sport
from datetime import datetime
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

match = Match(team_1=user_1.id, team_2=user_2.id, score_1=2, score_2=1, date=datetime.now(), sport=table_tennis.id)

session.add(match)

session.commit()
