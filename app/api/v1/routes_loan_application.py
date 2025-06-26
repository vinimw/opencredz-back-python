from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.loan_application import (
    LoanApplicationCreate,
    LoanApplicationOut,
    LoanApplicationListResponse
)
from app.schemas.common import ResponseMessage
from app.crud import loan_application as crud

router = APIRouter()

@router.post("/loan-application", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_loan_application(data: LoanApplicationCreate, db: Session = Depends(get_db)):
    crud.create_loan_application(db, data)
    return {
        "success": True,
        "message": "Loan application created successfully"
    }

@router.get("/loan-application", response_model=LoanApplicationListResponse)
def list_loan_applications(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    results = crud.get_all_loan_applications(db)
    return {
        "success": True,
        "message": "List of loan applications retrieved successfully",
        "data": results
    }

@router.delete("/loan-application/{application_id}", response_model=ResponseMessage)
def delete_loan_application(application_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    deleted = crud.delete_loan_application_by_id(db, application_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Loan application not found")
    return {
        "success": True,
        "message": "Loan application deleted successfully"
    }
