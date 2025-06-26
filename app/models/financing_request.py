from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class FinancingRequest(Base):
    __tablename__ = "financing_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    financing_type = Column(String, nullable=False)
    vehicle_year = Column(String, nullable=False)
    vehicle_value = Column(String, nullable=False)
    down_payment = Column(String, nullable=False)
    accepted_terms = Column(Boolean, nullable=False)
