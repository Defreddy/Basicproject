from sqlalchemy.schema import Column
from sqlalchemy.types import String, Text, Date
from database import Base
class Cve(Base):
    __tablename__ = "cveDetail"
    cveName = Column(String(50), primary_key=True, index=True)
    vendorProject = Column(Text)
    product = Column(Text)
    vulnerabilityName = Column(Text)
    dateAdded = Column(Date)
    shortDescription = Column(Text)
    requiredAction = Column(Text)
    dueDate = Column(Date)
    notes = Column(Text)
