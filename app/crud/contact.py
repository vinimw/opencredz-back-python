from typing import List
from sqlalchemy.orm import Session
from app.models.contact import Contact

def delete_contact_by_id(db: Session, contact_id: int) -> bool:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        return False
    db.delete(contact)
    db.commit()
    return True

def get_all_contacts(db: Session) -> List[Contact]:
    return db.query(Contact).order_by(Contact.id.desc()).all()
