from datetime import date
from pydantic import BaseModel

class CveBase(BaseModel):
    cveID: int
    cveName: str

class CveCreate(CveBase):
    pass    

class Cve(CveBase):
    vendorProject: str
    product: str
    vulnerabilityName: str
    dateAdded: date
    shortDescription: str
    requiredAction: str
    dueDate: date
    notes: str

    class Config:
        orm_mode = True

        