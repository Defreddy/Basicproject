from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product")
async def root():
    return {"message": "This is a product"}

@app.get("/cve")
async def root():
    return {"message": "This is a cve"}

@app.get("/cve/{cveName}", response_model=schemas.Cve)
def read_user(cveName: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, cveName=cveName)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



