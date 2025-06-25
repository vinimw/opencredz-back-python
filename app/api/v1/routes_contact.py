from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.contact import ContactCreate
from app.crud import contact as crud_contact
from app.api.deps import get_db
from app.schemas.common import ResponseMessage

router = APIRouter()

@router.post("/contact", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_contact(contact_in: ContactCreate, db: Session = Depends(get_db)):
    crud_contact.create_contact(db, contact_in)
    return {
        "success": True,
        "message": "Contact created successfully"
    }

    