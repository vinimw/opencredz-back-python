from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.loan_application_pj import (
    LoanApplicationPJCreate,
    LoanApplicationPJOut,
    LoanApplicationPJListResponse
)
from app.schemas.common import ResponseMessage
from app.crud import loan_application_pj as crud

router = APIRouter()

@router.post("/loan-application-pj", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_loan_application_pj(data: LoanApplicationPJCreate, db: Session = Depends(get_db)):
    crud.create_pj_application(db, data)
    return {
        "success": True,
        "message": "Loan application PJ created successfully"
    }

@router.get("/loan-application-pj", response_model=LoanApplicationPJListResponse)
def list_loan_application_pj(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    results = crud.get_all_pj_applications(db)
    return {
        "success": True,
        "message": "List of loan applications PJ retrieved successfully",
        "data": results
    }

@router.delete("/loan-application-pj/{application_id}", response_model=ResponseMessage)
def delete_loan_application_pj(application_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    deleted = crud.delete_pj_application_by_id(db, application_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Loan application PJ not found")
    return {
        "success": True,
        "message": "Loan application PJ deleted successfully"
    }
