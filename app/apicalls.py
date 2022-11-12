from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

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
print(get_connection())
engine = get_connection()
connection = engine.connect()

print(f"Connection to the {host} for user {user} created successfully.")


#from . import crud, model, schema
#from .database import SessionLocal, engine

#model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

@app.get("/product")
async def root():
    return {"message": "This is a product"}

@app.get("/cve")
async def root():
    return {"message": "This is a cve"}

# @app.get("/cve/{cveName}", response_model=schema.Cve)
# def read_user(cveName: str, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, cveName=cveName)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user



