from database import Sport, engine, Session, Base, User, Match, Elo
from sqlalchemy import create_engine
from database import Sport
from sqlalchemy.orm import sessionmaker

import random

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

POPULATE_FAKE_DATA = True

session = Session()

table_tennis = Sport(name='Table Tennis')
eight_ball = Sport(name='8-ball')

session.add(table_tennis)
session.add(eight_ball)


if POPULATE_FAKE_DATA:
    users = ['Marcus', 'Dexter', 'William', 'Aron', 'Ragnar', 'Oskar', 'André']
    db_users = []
    for i, user in enumerate(users):
        db_user = User(name=user)
        db_users.append(db_user)
        session.add(db_user)
        session.commit()
        elo = Elo(user=db_user.id, sport=table_tennis.id, score=random.randint(800,1200))
        session.add(elo)
        session.commit()

    for i in range(100):
        j = random.randint(0,len(db_users)-1)
        k = j
        while k == j:
            k = random.randint(0,len(db_users)-1)
        match = Match(team_1=db_users[j].id, team_2=db_users[k].id, score_1=2, score_2=random.randint(0,1), sport=table_tennis.id)
        session.add(match)

    session.commit()
