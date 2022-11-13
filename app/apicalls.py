from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, model, schema
from .database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8051",
    "http://127.0.0.1:8051"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cve/{cveID}", response_model=schema.Cve)
def read_user(cveID: int, db: Session = Depends(get_db)):
    db_user = crud.get_cveid(db, cveID=cveID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/cveName/{cveName}", response_model=schema.Cve)
def read_user(cveName: str, db: Session = Depends(get_db)):
    db_user = crud.get_cve(db, cveName=cveName)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/allcve/", response_model=list[schema.Cve])
def read_users(db: Session = Depends(get_db)):
    users = db.query(model.Cve).all()
    return users


