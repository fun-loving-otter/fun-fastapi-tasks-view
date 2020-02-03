import databases
from sqlalchemy import create_engine

from dbmodels import metadata

print("======================= DATABASE =======================")
DATABASE_URL = "mysql://root:root@127.0.0.1/todolistFastapi"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
metadata.create_all(engine)


def get_database() -> databases.Database:
    return database
