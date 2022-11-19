from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

username = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

print(username)
print(password)
print(host)
print(port)
print(database)

  
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            username, password, host, port, database
        )

    )
        
# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
engine = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()