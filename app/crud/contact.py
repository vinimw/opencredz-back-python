from typing import List
from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact import ContactCreate

def delete_contact_by_id(db: Session, contact_id: int) -> bool:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        return False
    db.delete(contact)
    db.commit()
    return True

def get_all_contacts(db: Session) -> List[Contact]:
    return db.query(Contact).order_by(Contact.id.desc()).all()


def create_contact(db: Session, contact_in: ContactCreate):
    contact = Contact(**contact_in.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact