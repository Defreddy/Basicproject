from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, model, schema
from .database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://api-service-defreddy.cloud.okteto.net/*",
    "https://phpmyadmin-defreddy.cloud.okteto.net/*",
    "https://api-service-defreddy.cloud.okteto.net/createcve/",
    "https://defreddy.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cve/{cveID}", response_model=schema.Cve)
def read_cve(cveID: int, db: Session = Depends(get_db)):
    db_cve = crud.get_cveid(db, cveID=cveID)
    if db_cve is None:
        raise HTTPException(status_code=404, detail="CVE not found")
    return db_cve

@app.get("/cveName/{cveName}", response_model=schema.Cve)
def read_cveName(cveName: str, db: Session = Depends(get_db)):
    db_cve = crud.get_cve(db, cveName=cveName)
    if db_cve is None:
        raise HTTPException(status_code=404, detail="CVE not found")
    return db_cve

@app.get("/product/", response_model=list[schema.Cve])
def read_users(query: str, db: Session = Depends(get_db)):
    products = crud.get_cveProducts(db, query=query)
    return products

@app.get("/allcve/", response_model=list[schema.Cve])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_all(db)
    return users

@app.post("/createcve/", response_model=schema.Cve)
async def create_cve(cve: schema.CveCreate, db: Session = Depends(get_db)):
    db_cve = crud.get_cve(db, cveName=cve.cveName)
    if db_cve:
        raise HTTPException(status_code=400, detail="CVE already registered")
    return crud.create_cve(db=db, cve=cve)
