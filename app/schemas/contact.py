from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str
    cellphone: str
    subject: str
    message: str