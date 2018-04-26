import os
import database
from sqlalchemy import create_engine

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']

engine = create_engine(
    "postgresql://{}:{}@db:5432/{}".format(user, password, db_name)
)

database.Base.metadata.create_all(engine)
