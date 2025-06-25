from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cellphone = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    message = Column(String, nullable=False)
