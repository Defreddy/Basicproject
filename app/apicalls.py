from fastapi import Depends, FastAPI, HTTPException, Query, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

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
    allow_origins=["*"],
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

#@app.get("/product/{product}", response_model=list[schema.Cve])
#def read_cveName(product: str, db: Session = Depends(get_db)):
#    db_cve = crud.get_cveProducts(db, product=product)
#    if db_cve is None:
#        raise HTTPException(status_code=404, detail="CVE not found")
#    return db_cve

@app.get("/product/", response_model=schema.Cve)
def read_users(request: Request, db: Session = Depends(get_db), query: Optional[str] = None):
    products = get_cveProduct(query, db=db)
    return {"request": request, "jobs": products}

#def search(request: Request, db: Session = Depends(get_db), query: Optional[str] = None
#):
#    jobs = search_job(query, db=db)
#    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": jobs}
#    )

@app.get("/allcve/", response_model=list[schema.Cve])
def read_users(db: Session = Depends(get_db)):
    users = db.query.all()
    return users

@app.post("/createcve/", response_model=schema.Cve)
def create_cve(cve: schema.CveCreate, db: Session = Depends(get_db)):
    db_cve = crud.get_cve(db, cveName=cve.cveName)
    if db_cve:
        raise HTTPException(status_code=400, detail="CVE already registered")
    return crud.create_cve(db=db, cve=cve)
