from sqlalchemy import Column, Integer, String
from app.db.base import Base

class HealthPlan(Base):
    __tablename__ = "health_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String, nullable=False)
    lifes = Column(String, nullable=False)
