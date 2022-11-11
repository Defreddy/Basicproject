from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_database_url="mysql+mysqlconnector://user1:abc123@localhost:3306/cve"
engine = create_engine(sql_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()