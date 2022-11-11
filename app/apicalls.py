from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import mysql.connector
from mysql.connector import Error

connection=None

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='cve',
                                         user='root',
                                         password='abc123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    
#from . import crud, model, schema
#from .database import SessionLocal, engine

#model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
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



