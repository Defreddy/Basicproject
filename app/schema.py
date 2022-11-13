from datetime import date
from pydantic import BaseModel
from pydantic.schema import Optional

class CveBase(BaseModel):
    cveID: int
    cveName: str

class CveCreate(CveBase):
    pass    

class Cve(CveBase):
    vendorProject: Optional[str]
    product: Optional[str]
    vulnerabilityName: Optional[str]
    dateAdded: Optional[date]
    shortDescription: Optional[str]
    requiredAction: Optional[str]
    dueDate: Optional[date]
    notes: Optional[str]

    class Config:
        orm_mode = True

        