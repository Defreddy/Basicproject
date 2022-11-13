from datetime import date
from pydantic import BaseModel

class Cve(BaseModel):
    cveID: int
    cveName: str
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

    class CveCreate(Cve):
        pass            