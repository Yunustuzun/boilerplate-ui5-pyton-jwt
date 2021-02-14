from os import path
from pathlib import Path
from decouple import config
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))


class Config:
    load_dotenv()

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC Driver 17 for SQL Server'.format(config('DB_USER_NAME'), config('DB_PASSWORD'), config('DB_SERVER'), config('DB_PORT'), config('DB_NAME'))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')