
import sqlalchemy as db
from decouple import config
from sqlalchemy.orm import sessionmaker


def initialize_db(app):
    engine = db.create_engine('mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC Driver 17 for SQL Server'.format(config('DB_USER_NAME'), config('DB_PASSWORD'), config('DB_SERVER'), config('DB_PORT'), config('DB_NAME')))
    connection = engine.connect()

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    metadata = db.MetaData()
    census = db.Table('Users', metadata, autoload=True, autoload_with=engine)
    print(census.columns.keys())
