from sqlalchemy.schema import Column
from sqlalchemy.types import String, Text, Date, Integer

from app.database import Base

class Cve(Base):
    __tablename__ = "cveDetail"
    cveID = Column(Integer, primary_key=True, index=True)
    cveName = Column(String(50), )
    vendorProject = Column(Text)
    product = Column(Text)
    vulnerabilityName = Column(Text)
    dateAdded = Column(Date)
    shortDescription = Column(Text)
    requiredAction = Column(Text)
    dueDate = Column(Date)
    notes = Column(Text)
