from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'abc123'
host = '127.0.0.1'
port = 3306
database = 'cve'
  
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )

    )
        
# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
engine = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()