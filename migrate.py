from database import Sport, engine, Session, Base
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

session.commit()
