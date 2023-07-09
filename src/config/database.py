from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('URL_DB')
SQLALCHEMY_DATABASE_URL_CO = os.getenv('URL_CO')

def create_database():
    # Attempt to create the database if it doesn't exist
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL_CO)
        connection = engine.connect()
        connection.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
        connection.close()
    except ProgrammingError as e:
        print(f"Error creating database: {str(e)}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

