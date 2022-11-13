from datetime import date
from pydantic import BaseModel

class CveBase(BaseModel):
    cveName: str
    vendorProject: str
    product: str
    vulnerabilityName: str
    dateAdded: date
    shortDescription: str
    requiredAction: str
    dueDate: date
    notes: str


class CveCreate(CveBase):
    pass

class Cve(CveBase):
    cveID: int

    class Config:
        orm_mode = True
