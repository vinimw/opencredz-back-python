from pydantic import BaseModel, constr
from typing import List
from app.schemas.common import ResponseMessage

class ContactCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=3, max_length=100)
    cellphone: constr(strip_whitespace=True, min_length=10, max_length=20, pattern=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$')
    subject: constr(strip_whitespace=True, min_length=3, max_length=100)
    message: constr(strip_whitespace=True, min_length=2, max_length=1000)

class ContactOut(BaseModel):
    id: int
    name: str
    cellphone: str
    subject: str
    message: str

    class Config:
        from_attributes = True

class ContactListResponse(ResponseMessage):
    data: List[ContactOut]