from sqlalchemy.orm import Session

from . import model, schema


def get_user(db: Session, cveName: str):
    return db.query(model.Cve).filter(model.cveName == cveName).first()