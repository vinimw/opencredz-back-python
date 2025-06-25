from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact import ContactCreate

def create_contact(db: Session, contact_in: ContactCreate):
    contact = Contact(**contact_in.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact
