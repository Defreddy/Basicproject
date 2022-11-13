from sqlalchemy.orm import Session
from . import model, schema


def get_cveid(db: Session, cveID: int):
    return db.query(model.Cve).filter(model.Cve.cveID == cveID).first()

def get_cve(db: Session, cveName: str):
    return db.query(model.Cve).filter(model.Cve.cveName == cveName).first()

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Cve).offset(skip).limit(limit).all()