from datetime import date
from pydantic import BaseModel
from pydantic.schema import Optional

class CveBase(BaseModel):
    cveID: int
    cveName: str
    vendorProject: str
    product: str
    dateAdded: date

class CveCreate(CveBase):
    pass    

class Cve(CveBase):
    vulnerabilityName: Optional[str]
    shortDescription: Optional[str]
    requiredAction: Optional[str]
    dueDate: Optional[date]
    notes: Optional[str]
    

    class Config:
        orm_mode = True

        