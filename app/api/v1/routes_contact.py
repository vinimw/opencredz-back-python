from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.contact import ContactCreate
from app.crud import contact as crud_contact
from app.api.deps import get_db, get_current_user
from app.schemas.common import ResponseMessage
from typing import List
from app.schemas.contact import ContactListResponse, ContactOut

router = APIRouter()

@router.post("/contact", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_contact(contact_in: ContactCreate, db: Session = Depends(get_db)):
    crud_contact.create_contact(db, contact_in)
    return {
        "success": True,
        "message": "Contact created successfully"
    }

@router.delete("/contact/{contact_id}", response_model=ResponseMessage)
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    deleted = crud_contact.delete_contact_by_id(db, contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"success": True, "message": "Contact deleted successfully"}

@router.get("/contact", response_model=ContactListResponse)
def list_contacts(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    contacts = crud_contact.get_all_contacts(db)
    return {
        "success": True,
        "message": "List of contacts retrieved successfully",
        "data": contacts
    }