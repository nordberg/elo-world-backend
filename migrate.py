from database import Sport, engine, Session
from sqlalchemy import create_engine
from database import Sport
from sqlalchemy.orm import sessionmaker

database.Base.metadata.drop_all(engine)
database.Base.metadata.create_all(engine)

session = Session()

pingis = Sport(name='Pingis')
eight_ball = Sport(name='Biljard')

session.add(pingis)
session.add(eight_ball)

session.commit()
