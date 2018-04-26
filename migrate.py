import os
import database
from sqlalchemy import create_engine
from database import Sport
from sqlalchemy.orm import sessionmaker

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']

engine = create_engine(
    "postgresql://{}:{}@db:5432/{}".format(user, password, db_name)
)

database.Base.metadata.drop_all(engine)
database.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

pingis = Sport(name='Pingis')
eight_ball = Sport(name='Biljard')

session.add(pingis)
session.add(eight_ball)

session.commit()
