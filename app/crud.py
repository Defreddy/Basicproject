from sqlalchemy.orm import Session
from app.model import Cve
from . import model, schema


def get_cveid(db: Session, cveID: int):
    return db.query(model.Cve).filter(model.Cve.cveID == cveID).first()

def get_cve(db: Session, cveName: str):
    return db.query(model.Cve).filter(model.Cve.cveName == cveName).first()

def get_cveProduct(db: Session, product: str):
    return db.query(model.Cve).filter(model.Cve.product == product).first()

def get_cveProducts(db: Session, query: str):
    products = db.query(Cve).filter(Cve.product.contains(query)).all()
    listProducts = []
    for prod in products:
        listProducts.append(prod)
    return listProducts

def get_all(db: Session, skip: int = 0):
    return db.query(model.Cve).offset(skip).all()

def create_cve(db: Session, cve: schema.CveCreate):
    db_cve = model.Cve(cveName=cve.cveName, product=cve.product,vendorProject=cve.vendorProject,dateAdded=cve.dateAdded)
    db.add(db_cve)
    db.commit()
    db.refresh(db_cve)
    return db_cve